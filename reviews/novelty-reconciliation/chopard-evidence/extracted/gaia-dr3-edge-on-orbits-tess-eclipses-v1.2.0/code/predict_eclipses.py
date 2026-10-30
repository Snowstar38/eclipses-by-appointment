#!/usr/bin/env python3
"""Next eclipses of the track-3 candidates, with their uncertainties and their visibility from a ground site.

Model: the times of both conjunctions predicted by the Gaia orbit, corrected by the offset observed in TESS, which
drifts linearly with time when the Gaia period is slightly off (both eclipses shift together, as the separation test
showed). All the flagged eclipses of a star, at either conjunction, are fitted together: offset = a + b (t - t_mean); with
a single eclipse, b = 0 and its uncertainty comes from the growth of the Gaia timing uncertainty. Eclipses whose depth
differs by more than a factor of two from the median of their conjunction are left out (QLP and SPOC apertures differ,
so depths from different pipelines can differ by tens of per cent). By default every star with two or more flagged
eclipses is predicted (or --ids). Only the conjunctions at which an eclipse was seen are predicted. For each one the script
says whether it can be observed from the site: the Sun below -12 degrees and the star above --min-alt, during the
eclipse itself and during a baseline of one eclipse duration before or after it.
Flags marked 'instrumental' in artefact_vetting.csv, when that file exists, are not used.
Run from ~/Desktop/piste3:   python3 predict_eclipses.py          [--site-lat 46.77 --site-lon 23.59 --site-elev 400]
Output: predictions/eclipse_predictions.csv, predictions/observable.ics and a summary on screen.
"""
import argparse, math, os, warnings
import numpy as np
import pandas as pd

warnings.filterwarnings("ignore")
BTJD0 = 2457000.0


def eclipse_times(win, vet):
    w = win[(win["dip_flag"] == True) & (win["dip_depth"] <= 0.5)].copy()
    if vet is not None:
        bad = vet[vet["verdict"] == "instrumental"][["source_id", "t"]]
        key = set(zip(bad["source_id"].astype(int), bad["t"].round(4)))
        w = w[[(int(s), round(t, 4)) not in key for s, t in zip(w["source_id"], w["dip_t"])]]
    return w


def fit_offsets(tp, off, conj, sigma_default, drift_sigma, sig=None):
    """Offsets of the eclipses from the Gaia predictions: offset = a_c + b (t - tm), with one intercept for both
    conjunctions when their offsets agree (the Gaia separation is right), one per conjunction otherwise, and a common
    drift b; with a single epoch b = 0 and its uncertainty is the drift of the Gaia timing. Weighted by the timing
    uncertainty of each eclipse (sig; TESS eclipses: sigma_default; archival eclipses: their own, larger). Returns a
    function giving (offset, sigma) at (time, conjunction), the model used and the timing scatter."""
    tp = np.asarray(tp, float); off = np.asarray(off, float); conj = np.asarray(conj, int); tm = float(np.mean(tp))
    sig = np.full(len(tp), sigma_default) if sig is None else np.asarray(sig, float)
    cs = sorted(set(conj))
    epochs = len(np.unique(np.round(tp, 1)))
    W = 1.0 / sig ** 2

    def design(common):
        cols = [np.ones_like(tp)] if common else [(conj == c_).astype(float) for c_ in cs]
        slope = epochs >= 2 and len(tp) > len(cols) + 1          # a drift needs at least one degree of freedom left
        if slope:
            cols.append(tp - tm)
        return np.vstack(cols).T, slope

    def solve(A):
        AtWA = A.T @ (A * W[:, None])
        c_ = np.linalg.pinv(AtWA) @ (A.T @ (W * off))
        r_ = off - A @ c_
        return c_, r_, AtWA, float(np.sum(W * r_ ** 2))

    # one intercept for both conjunctions unless separate intercepts improve the fit by more than 3 sigma (chi2 > 9)
    A1, slope1 = design(True); c1, r1, M1, chi1 = solve(A1)
    common = True
    if len(cs) == 2:
        A2, slope2 = design(False)
        c2, r2, M2, chi2 = solve(A2)
        if chi1 - chi2 > 9:
            common = False
    A, with_slope = (A1, slope1) if common else design(False)
    groups = ["all"] if common else cs
    c, res, AtWA, chi = solve(A)
    dof = len(tp) - A.shape[1]
    chi2r = chi / dof if dof >= 1 else 1.0
    cov = np.linalg.pinv(AtWA) * max(1.0, chi2r)
    s = float(np.sqrt(np.sum(res ** 2) / dof)) if dof >= 1 else sigma_default
    def predict(t, cj):
        x = [1.0] if common else [1.0 if cj == gname else 0.0 for gname in groups]
        if with_slope:
            x.append(t - tm)
        x = np.array(x)
        val = float(x @ c); var = float(x @ cov @ x)
        if not with_slope:
            var += ((t - tm) * drift_sigma) ** 2
        return val, math.sqrt(max(var, 0.0))
    model = ("common offset" if common else "offset per conjunction") + (" + drift" if with_slope else ", drift from the Gaia uncertainty")
    return predict, model, s


def to_site_utc(btjd, coord, site):
    """BJD_TDB (as BTJD) -> UTC time at the site (light travel time removed, one iteration)."""
    from astropy.time import Time
    t = Time(btjd + BTJD0, format="jd", scale="tdb", location=site)
    ltt = t.light_travel_time(coord, kind="barycentric")
    t2 = Time(t.jd - ltt.jd, format="jd", scale="tdb", location=site)
    ltt2 = t2.light_travel_time(coord, kind="barycentric")
    return Time(t.jd - ltt2.jd, format="jd", scale="tdb", location=site).utc


def visibility(t_mid_utc, dur, coord, site, min_alt):
    """Fraction of the eclipse observable at night, and whether a baseline before or after it is observable too."""
    from astropy.coordinates import AltAz, get_sun
    from astropy.time import TimeDelta
    import astropy.units as u
    grid = t_mid_utc + TimeDelta(np.linspace(-1.5 * dur, 1.5 * dur, 121), format="jd")
    frame = AltAz(obstime=grid, location=site)
    alt = coord.transform_to(frame).alt.deg
    sun = get_sun(grid).transform_to(frame).alt.deg
    ok = (alt > min_alt) & (sun < -12)
    x = np.linspace(-1.5, 1.5, 121)
    inside = np.abs(x) <= 0.5
    frac = float(ok[inside].mean())
    before = bool(ok[(x >= -1.5) & (x < -0.5)].mean() > 0.5); after = bool(ok[(x > 0.5) & (x <= 1.5)].mean() > 0.5)
    ing = bool(ok[np.abs(x + 0.5) < 0.05].all()); egr = bool(ok[np.abs(x - 0.5) < 0.05].all())
    if frac > 0.95 and (before or after):
        label = "full eclipse with baseline"
    elif ing and before:
        label = "ingress with baseline"
    elif egr and after:
        label = "egress with baseline"
    elif frac > 0.3:
        label = "part of the eclipse, no baseline"
    else:
        label = "not observable"
    best_alt = float(np.max(np.where(ok, alt, -90)))
    return label, round(frac, 2), round(best_alt, 1)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--ids", nargs="*", type=int, default=None)
    ap.add_argument("--site-lat", type=float, default=46.77); ap.add_argument("--site-lon", type=float, default=23.59)
    ap.add_argument("--site-elev", type=float, default=400.0); ap.add_argument("--min-alt", type=float, default=25.0)
    ap.add_argument("--until", default="2028-06-30"); ap.add_argument("--sigma-ecl", type=float, default=0.01, help="days")
    a = ap.parse_args()
    from astropy.coordinates import SkyCoord, EarthLocation
    from astropy.time import Time
    import astropy.units as u
    import sys
    sys.path.insert(0, os.getcwd())
    from pilot_track3 import duration
    win = pd.read_csv("pilot_results/windows.csv")
    vet = None
    if os.path.exists("pilot_results/artefact_vetting.csv"):
        v = pd.read_csv("pilot_results/artefact_vetting.csv")
        if "reasons_instrumental" in v.columns:          # written by artefact_vetting.py version 2
            vet = v
            print(f"artefact vetting (version 2) applied: {int((v['verdict'] == 'instrumental').sum())} instrumental flags left out")
        else:
            print("pilot_results/artefact_vetting.csv comes from version 1 of the vetting (miscalibrated): ignored")
    det = pd.read_csv("track3_detail.csv").drop_duplicates("source_id").set_index("source_id")
    names = {}
    if os.path.exists("pilot_results/known_check.csv"):
        k = pd.read_csv("pilot_results/known_check.csv")
        names = {int(r.source_id): str(r.SIMBAD).split(" [")[0] for r in k.itertuples() if isinstance(r.SIMBAD, str) and r.SIMBAD}
    ecl = eclipse_times(win, vet)
    ecl["sigma"] = a.sigma_ecl
    if os.path.exists("predictions/archival_constraints.csv") and os.path.getsize("predictions/archival_constraints.csv") > 0:
        try:
            arc = pd.read_csv("predictions/archival_constraints.csv")
        except pd.errors.EmptyDataError:
            arc = pd.DataFrame()
        if len(arc):
            ecl = pd.concat([ecl, arc], ignore_index=True)
            print(f"{len(arc)} archival eclipses added to the fit (predictions/archival_constraints.csv)")
    orb = pd.read_csv("track3_astrometric_orbits_1.csv").drop_duplicates("source_id").set_index("source_id")
    from pilot_track3 import ti_to_omega, conj_times, predicted
    site = EarthLocation(lat=a.site_lat * u.deg, lon=a.site_lon * u.deg, height=a.site_elev * u.m)
    now = Time.now(); end = Time(a.until)
    rows = []
    for sid, g in ecl.groupby("source_id"):
        sid = int(sid)
        keep = []
        for conj, gc in g.groupby("conj"):
            med = gc["dip_depth"].median()
            keep.append(gc[(gc["dip_depth"] >= 0.5 * med) & (gc["dip_depth"] <= 2 * med)])
        g = pd.concat(keep)
        if a.ids and sid not in a.ids:
            continue
        if not a.ids and len(g) < 2:
            continue
        if sid not in orb.index or sid not in det.index:
            continue
        s, o = det.loc[sid], orb.loc[sid]
        P = float(o["period"]); e = min(float(np.nan_to_num(o["eccentricity"], nan=0.0)), 0.95)
        w = ti_to_omega(o["a_thiele_innes"], o["b_thiele_innes"], o["f_thiele_innes"], o["g_thiele_innes"])
        cs = conj_times(P, e, w, 389.0 + float(o["t_periastron"]))
        drift = max(abs(float(s["sigma_t_c1_3100"]) - float(s["sigma_t_c1_1600"])) / 1500.0, 1e-4)   # days per day
        pred_off, model, sig_e = fit_offsets(g["t_pred"].values, (g["dip_t"] - g["t_pred"]).values, g["conj"].values, a.sigma_ecl, drift,
                                             sig=g["sigma"].fillna(a.sigma_ecl).values)
        coord = SkyCoord(float(s["ra"]) * u.deg, float(s["dec"]) * u.deg)
        dur = duration(P)
        for conj, gc in g.groupby("conj"):
            for tg in predicted(P, cs[int(conj) - 1], now.jd - BTJD0, end.jd - BTJD0):
                o_, sig = pred_off(tg, int(conj))
                tb = tg + o_
                tu = to_site_utc(tb, coord, site)
                label, frac, alt = visibility(tu, dur, coord, site, a.min_alt)
                rows.append(dict(source_id=sid, name=names.get(sid, ""), conj=int(conj), G=round(float(s["g"]), 2), period_d=round(P, 4),
                                 depth_pct=round(float(gc["dip_depth"].median()) * 100, 2), duration_h=round(dur * 24, 1),
                                 mid_utc=tu.iso[:16], sigma_min=round(sig * 1440, 1), n_tess_eclipses=int((g["sector"] >= 0).sum()),
                                 n_archival=int((g["sector"] < 0).sum()),
                                 offset_d=round(o_, 3), model=model, visibility=label,
                                 fraction_observable=frac, best_altitude=alt))
    os.makedirs("predictions", exist_ok=True)
    df = pd.DataFrame(rows)
    if df.empty:
        print("no candidate with two or more consistent eclipses"); return
    df.sort_values("mid_utc").to_csv("predictions/eclipse_predictions.csv", index=False)
    obs = df[df["visibility"] != "not observable"].sort_values("mid_utc")
    ics = ["BEGIN:VCALENDAR", "VERSION:2.0", "PRODID:-//track3//eclipse predictions//EN"]
    for r in obs.itertuples():
        t = Time(r.mid_utc); half = r.duration_h / 48
        st = (t - half * u.day).datetime.strftime("%Y%m%dT%H%M%SZ"); en = (t + half * u.day).datetime.strftime("%Y%m%dT%H%M%SZ")
        ics += ["BEGIN:VEVENT", f"UID:{r.source_id}-{r.conj}-{st}@track3", f"DTSTART:{st}", f"DTEND:{en}",
                f"SUMMARY:Eclipse {r.name or r.source_id} ({r.depth_pct}%, {r.visibility})",
                f"DESCRIPTION:Gaia DR3 {r.source_id}, conjunction {r.conj}, mid-eclipse {r.mid_utc} UTC +/- {r.sigma_min} min, "
                f"duration {r.duration_h} h, depth {r.depth_pct}%, G = {r.G}, best altitude {r.best_altitude} deg", "END:VEVENT"]
    ics.append("END:VCALENDAR")
    open("predictions/observable.ics", "w").write("\n".join(ics) + "\n")
    df["name"] = df["name"].fillna("").astype(str)
    print(f"{df['source_id'].nunique()} candidates, {len(df)} predicted eclipses until {a.until}; observable from the site: {len(obs)}")
    for r in obs.head(25).itertuples():
        print(f"  {r.mid_utc} UTC +/- {r.sigma_min:>5} min  {(r.name or str(r.source_id)):22s} {r.depth_pct:5.2f}%  {r.duration_h:4.1f} h  G={r.G:5.2f}  {r.visibility}")
    print("-> predictions/eclipse_predictions.csv, predictions/observable.ics")


if __name__ == "__main__":
    main()
