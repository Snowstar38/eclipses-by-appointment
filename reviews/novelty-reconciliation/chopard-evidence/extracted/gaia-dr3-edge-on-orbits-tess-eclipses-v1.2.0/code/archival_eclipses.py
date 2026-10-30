#!/usr/bin/env python3
"""Retrospective test of the track-3 candidates: are their eclipses in the ground-based archives, at the predicted times?

For every candidate predicted by predict_eclipses.py (same model: the Gaia conjunction times corrected by the offset
seen in TESS), the light curves of ASAS-SN (2012 onwards, V and g) and ZTF (2018 onwards, g and r, north of -30 deg)
are folded on the predicted eclipses. Going back in time, the prediction becomes uncertain, so the search scans a shift
of the eclipses that grows linearly with the time from the TESS epoch (a correction of the period), over +/- 3 sigma of
the prediction at the archival epoch plus one duration. The statistic is the depth of the points in eclipse against the
others, in units of its error (each camera and filter normalised separately). Its significance is the fraction of null
scans (the same scan around times a random fraction of the period away from the eclipses) that reach it.
An eclipse is recovered when SNR >= 5, the null probability is below 1 per cent, and the depth is within a factor of two
of the TESS depth (bands differ). Recovered eclipses are written to predictions/archival_constraints.csv, which
predict_eclipses.py adds to its fit.
Run from ~/Desktop/piste3 after predict_eclipses.py:   python3 archival_eclipses.py     [--ids ...] [--no-ztf]
Needs:  pip3 install skypatrol   (the ASAS-SN Sky Patrol client)
Output: predictions/archival_search.csv, predictions/archival_constraints.csv, predictions/archival_plots/*.png
"""
import argparse, io, math, os, sys, warnings
import numpy as np
import pandas as pd

warnings.filterwarnings("ignore")
BTJD0 = 2457000.0
N_NULL = 60


def asassn(ra, dec):
    from pyasassn.client import SkyPatrolClient
    client = SkyPatrolClient(verbose=False)
    coll = client.cone_search(ra, dec, radius=5, units="arcsec", catalog="master_list", download=True)
    if coll is None or not hasattr(coll, "data") or len(coll.data) == 0:
        return pd.DataFrame()
    d = coll.data
    if "quality" in d.columns:
        d = d[d["quality"] == "G"]
    d = d[np.isfinite(d["flux"]) & (d["flux"] > 0)]
    out = pd.DataFrame(dict(t=d["jd"].values - BTJD0, flux=d["flux"].values, err=d["flux_err"].values,
                            group=("ASAS-SN " + d["phot_filter"].astype(str) + " " + d["camera"].astype(str)).values))
    return out


def ztf(ra, dec):
    import requests
    url = ("https://irsa.ipac.caltech.edu/cgi-bin/ZTF/nph_light_curves?POS=CIRCLE%20" + f"{ra}%20{dec}%200.0014"
           + "&BANDNAME=g,r&FORMAT=CSV")
    r = requests.get(url, timeout=120)
    if r.status_code != 200 or len(r.text) < 100:
        return pd.DataFrame()
    d = pd.read_csv(io.StringIO(r.text))
    if d.empty:
        return pd.DataFrame()
    d = d[(d["catflags"] == 0) & np.isfinite(d["mag"])]
    flux = 10 ** (-0.4 * (d["mag"].values - 20)); err = flux * d["magerr"].values * 0.921
    return pd.DataFrame(dict(t=d["hjd"].values - BTJD0, flux=flux, err=err, group=("ZTF " + d["filtercode"].astype(str) + " " + d["oid"].astype(str)).values))


def normalise(df):
    parts = []
    for g, x in df.groupby("group"):
        if len(x) < 30:
            continue
        med = np.median(x["flux"])
        y = x.copy(); y["f"] = x["flux"] / med
        mad = 1.4826 * np.median(np.abs(y["f"] - 1))
        y = y[np.abs(y["f"] - 1) < 6 * max(mad, 1e-4) + 0.5]          # remove gross outliers, keep deep eclipses
        parts.append(y)
    return pd.concat(parts) if parts else pd.DataFrame()


def scan(t, f, eclipse_time, P, dur, tm, t_a, smax, step):
    """Best (snr, depth, shift, n_in) of the box at the predicted eclipses, shifted by s (t - tm)/(t_a - tm)."""
    best = None
    sig = 1.4826 * np.median(np.abs(f - np.median(f)))
    if not sig > 0:
        return None
    for s in np.arange(-smax, smax + 1e-9, step):
        shift = s * (t - tm) / (t_a - tm)
        tt = t - shift
        k = np.round((tt - eclipse_time) / P)
        d = tt - (eclipse_time + k * P)
        inn = np.abs(d) < dur / 2
        n = int(inn.sum())
        if n < 3:
            continue
        depth = float(np.median(f[~inn]) - np.mean(f[inn]))
        snr = depth / (sig / math.sqrt(n))
        if best is None or snr > best[0]:
            best = (snr, depth, float(s), n)
    return best


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--ids", nargs="*", type=int, default=None); ap.add_argument("--no-ztf", action="store_true")
    a = ap.parse_args()
    sys.path.insert(0, os.getcwd())
    import predict_eclipses as PE
    from pilot_track3 import ti_to_omega, conj_times, duration
    pred = pd.read_csv("predictions/eclipse_predictions.csv")
    win = pd.read_csv("pilot_results/windows.csv")
    det = pd.read_csv("track3_detail.csv").drop_duplicates("source_id").set_index("source_id")
    orb = pd.read_csv("track3_astrometric_orbits_1.csv").drop_duplicates("source_id").set_index("source_id")
    vet = None
    if os.path.exists("pilot_results/artefact_vetting.csv"):
        v = pd.read_csv("pilot_results/artefact_vetting.csv")
        vet = v if "reasons_instrumental" in v.columns else None
    ecl = PE.eclipse_times(win, vet)
    stars = sorted(set(pred["source_id"]))
    if a.ids:
        stars = [s for s in stars if s in set(a.ids)]
    os.makedirs("predictions/archival_plots", exist_ok=True)
    rows, cons = [], []
    rng = np.random.default_rng(20261012)
    for sid in stars:
        g = ecl[ecl["source_id"] == sid]
        keep = []
        for conj, gc in g.groupby("conj"):
            med = gc["dip_depth"].median(); keep.append(gc[(gc["dip_depth"] >= 0.5 * med) & (gc["dip_depth"] <= 2 * med)])
        if not keep:
            continue
        g = pd.concat(keep)
        s, o = det.loc[sid], orb.loc[sid]
        P = float(o["period"]); e = min(float(np.nan_to_num(o["eccentricity"], nan=0.0)), 0.95)
        w = ti_to_omega(o["a_thiele_innes"], o["b_thiele_innes"], o["f_thiele_innes"], o["g_thiele_innes"])
        cs = conj_times(P, e, w, 389.0 + float(o["t_periastron"]))
        drift = max(abs(float(s["sigma_t_c1_3100"]) - float(s["sigma_t_c1_1600"])) / 1500.0, 1e-4)
        pred_off, model, _ = PE.fit_offsets(g["t_pred"].values, (g["dip_t"] - g["t_pred"]).values, g["conj"].values, 0.01, drift)
        tm = float(np.mean(g["t_pred"]))
        dur = duration(P)
        ra, dec = float(s["ra"]), float(s["dec"])
        name = str(pred[pred["source_id"] == sid]["name"].fillna("").iloc[0]) or str(sid)
        data = []
        try:
            data.append(asassn(ra, dec))
        except Exception as exc:
            print(f"  {name}: ASAS-SN failed ({str(exc)[:60]})")
        if not a.no_ztf and dec > -31:
            try:
                data.append(ztf(ra, dec))
            except Exception as exc:
                print(f"  {name}: ZTF failed ({str(exc)[:60]})")
        data = [d for d in data if len(d)]
        if not data:
            rows.append(dict(source_id=sid, name=name, survey="none", note="no archival data")); continue
        for d in data:
            survey = d["group"].iloc[0].split()[0]
            d = normalise(d)
            if d.empty:
                continue
            t, f = d["t"].values, d["f"].values
            t_a = float(np.median(t))
            for conj, gc in g.groupby("conj"):
                depth_tess = float(gc["dip_depth"].median())
                c0 = cs[int(conj) - 1]
                off_a, sig_a = pred_off(t_a, int(conj))
                ecl0 = c0 + off_a                 # reference eclipse time with the offset at the archival epoch
                smax = 3 * sig_a + dur; step = max(dur / 6, 0.005)
                if abs(t_a - tm) < 1:
                    continue
                best = scan(t, f, ecl0, P, dur, tm, t_a, smax, step)
                if best is None:
                    continue
                null = []
                for _ in range(N_NULL):
                    frac = rng.uniform(0.15, 0.85)
                    b0 = scan(t, f, ecl0 + frac * P, P, dur, tm, t_a, smax, step)
                    if b0 is not None:
                        null.append(b0[0])
                p_null = float(np.mean(np.array(null) >= best[0])) if null else float("nan")
                ok = best[0] >= 5 and p_null < 0.01 and 0.5 * depth_tess <= best[1] <= 2 * depth_tess
                rows.append(dict(source_id=sid, name=name, survey=survey, conj=int(conj), n_points=len(t), years=round((t.max() - t.min()) / 365.25, 1),
                                 depth_tess_pct=round(depth_tess * 100, 2), depth_archive_pct=round(best[1] * 100, 2), snr=round(best[0], 1),
                                 n_in_eclipse=best[3], shift_at_archive_d=round(best[2], 3), sigma_pred_at_archive_d=round(sig_a, 3),
                                 p_null=round(p_null, 3), recovered=ok))
                print(f"  {name} conj {conj} {survey}: {len(t)} points over {(t.max() - t.min()) / 365.25:.1f} yr; depth {best[1]*100:.2f}% "
                      f"(TESS {depth_tess*100:.2f}%), SNR {best[0]:.1f}, {best[3]} points in eclipse, null p {p_null:.3f}"
                      + ("  -> RECOVERED" if ok else ""), flush=True)
                if ok:
                    k = round((t_a - ecl0) / P)
                    tg = c0 + k * P
                    cons.append(dict(source_id=sid, conj=int(conj), t_pred=tg, dip_t=tg + off_a + best[2], dip_depth=best[1],
                                     dip_flag=True, author=f"archive {survey}", sector=-1, dip_snr=best[0], sigma=max(step, dur / 4)))
                    try:
                        import matplotlib; matplotlib.use("Agg"); import matplotlib.pyplot as plt
                        shift = best[2] * (t - tm) / (t_a - tm); tt = t - shift
                        kk = np.round((tt - ecl0) / P); dd = tt - (ecl0 + kk * P)
                        m = np.abs(dd) < 3 * dur
                        fig, ax = plt.subplots(figsize=(6, 2.6))
                        ax.plot(dd[m] * 24, f[m], ".", ms=2, color="0.4"); ax.axvspan(-dur * 12, dur * 12, color="tab:blue", alpha=0.08)
                        ax.set_xlabel("hours from the eclipse"); ax.set_ylabel("normalised flux")
                        ax.set_title(f"{name} conj {conj}, {survey}: {best[1]*100:.2f}% (TESS {depth_tess*100:.2f}%), SNR {best[0]:.0f}", fontsize=8)
                        fig.tight_layout(); fig.savefig(f"predictions/archival_plots/{sid}_c{conj}_{survey}.png", dpi=120); plt.close(fig)
                    except Exception:
                        pass
    pd.DataFrame(rows).to_csv("predictions/archival_search.csv", index=False)
    cols = ["source_id", "conj", "t_pred", "dip_t", "dip_depth", "dip_flag", "author", "sector", "dip_snr", "sigma"]
    pd.DataFrame(cons, columns=cols).to_csv("predictions/archival_constraints.csv", index=False)   # header even when empty
    rec = sum(1 for r in rows if r.get("recovered"))
    print(f"\n{rec} archival eclipses recovered -> predictions/archival_search.csv, predictions/archival_constraints.csv")
    print("Rerun predict_eclipses.py: it adds the recovered archival eclipses to its fit.")


if __name__ == "__main__":
    main()
