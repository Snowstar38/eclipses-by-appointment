#!/usr/bin/env python3
"""Vetting dossiers for the best candidates of the track-3 pilot.

For every candidate (by default: the stars with >= 2 flagged dips of consistent depth at the same conjunction,
dips deeper than 50 per cent being QLP artefacts and ignored), it gathers:
  1. the consistency of the eclipses: depth, offset from the prediction and its linear drift, by conjunction;
  2. one figure with every window aligned on the predicted time, from the light curves already in the
     lightkurve cache (no new download for the sectors of the pilot);
  3. the literature: every SIMBAD reference of the star, with the titles that mention eclipses or transits;
  4. the TESS Input Catalog: TESS magnitude, radius, mass and contamination ratio (light of neighbours);
  5. for a TOI, its ExoFOP disposition.
Run from ~/Desktop/piste3:   python3 vet_candidates.py          (or: --ids 146197633037335168 1364450812894866688)
Output: vetting/dossier.csv, vetting/literature.txt, vetting/<source_id>.png
"""
import argparse, io, math, os, re, sys, time, warnings
import numpy as np
import pandas as pd

warnings.filterwarnings("ignore")
OUT = "vetting"
ECL_WORDS = re.compile(r"eclips|transit|binar|light curve|photometr", re.I)


def candidates(win, ids=None):
    w = win.copy(); w["dip_off"] = w["dip_t"] - w["t_pred"]
    ok = w[(w["dip_flag"] == True) & (w["dip_depth"] <= 0.5)]
    rows = []
    for (sid, conj), g in ok.groupby(["source_id", "conj"]):
        if ids is None and len(g) < 2:
            continue
        x, y = g["t_pred"].to_numpy(), g["dip_off"].to_numpy()
        if len(g) >= 3 and np.ptp(x) > 0:
            A = np.vstack([np.ones_like(x), x]).T; c = np.linalg.lstsq(A, y, rcond=None)[0]
            rms = float(np.sqrt(np.mean((y - A @ c) ** 2))); drift = float(c[1] * 365.25)
        else:
            rms = float("nan"); drift = float((y[-1] - y[0]) / (x[-1] - x[0]) * 365.25) if len(g) > 1 and np.ptp(x) > 0 else 0.0
        ratio = float(g["dip_depth"].max() / g["dip_depth"].min())
        rows.append(dict(source_id=int(sid), conj=int(conj), n_dips=len(g), n_windows=int((w["source_id"] == sid).sum()),
                         depth_pct=round(float(g["dip_depth"].median()) * 100, 3), depth_ratio=round(ratio, 2),
                         offset_d=round(float(np.median(y)), 3), offset_rms_after_drift_d=round(rms, 3), drift_d_per_yr=round(drift, 2),
                         sectors=",".join(str(int(s)) for s in sorted(g["sector"].unique())), authors=",".join(sorted(g["author"].unique())),
                         consistent=bool(ratio < 1.5 and (len(g) == 2 or rms < 0.5))))
    c = pd.DataFrame(rows)
    if ids is not None:
        c = c[c["source_id"].isin(ids)]
    return c.sort_values(["consistent", "n_dips"], ascending=False)


def simbad_refs(ra, dec):
    from astroquery.utils.tap.core import TapPlus
    tap = TapPlus(url="https://simbad.cds.unistra.fr/simbad/sim-tap", verbose=False)
    q = f"""SELECT TOP 1 main_id, otype, oid FROM basic
            WHERE CONTAINS(POINT('ICRS', ra, dec), CIRCLE('ICRS', {ra}, {dec}, 0.0014)) = 1"""
    b = tap.launch_job(q).get_results()
    if len(b) == 0:
        return None, None, []
    oid = int(b["oid"][0])
    q2 = f"""SELECT r.bibcode, r.title, r.year FROM has_ref AS h JOIN ref AS r ON r.oidbib = h.oidbibref
             WHERE h.oidref = {oid} ORDER BY r.year"""
    refs = tap.launch_job(q2).get_results()
    return str(b["main_id"][0]), str(b["otype"][0]), [(str(r["bibcode"]), str(r["title"]), int(r["year"])) for r in refs]


def tic_info(ra, dec):
    from astroquery.mast import Catalogs
    t = Catalogs.query_region(f"{ra} {dec}", radius=0.003, catalog="TIC")
    if len(t) == 0:
        return {}
    t.sort("dstArcSec")
    r = t[0]
    def g(c):
        try:
            v = r[c]; return None if np.ma.is_masked(v) else float(v)
        except Exception:
            return None
    return dict(TIC=str(r["ID"]), Tmag=g("Tmag"), Teff=g("Teff"), R_star=g("rad"), M_star=g("mass"), contratio=g("contratio"),
                n_neighbours_within_60arcsec=int(len(Catalogs.query_region(f"{ra} {dec}", radius=60 / 3600, catalog="TIC")) - 1))


_TOI = None


def exofop_toi(tic):
    """TOI dispositions from the full ExoFOP TOI table (downloaded once, kept in vetting/exofop_toi.csv)."""
    global _TOI
    if _TOI is None:
        path = os.path.join(OUT, "exofop_toi.csv")
        if not os.path.exists(path):
            import requests
            r = requests.get("https://exofop.ipac.caltech.edu/tess/download_toi.php?sort=toi&output=csv", timeout=120)
            r.raise_for_status(); open(path, "w").write(r.text)
        _TOI = pd.read_csv(path)
    cols = {c.lower(): c for c in _TOI.columns}
    tic_col = cols.get("tic id") or cols.get("tic")
    if tic_col is None:
        return "TOI table without a TIC column"
    m = _TOI[_TOI[tic_col].astype(str) == str(int(float(tic)))]
    out = []
    for _, x in m.iterrows():
        out.append(f"TOI {x.get(cols.get('toi', ''), '')}: TFOPWG {x.get(cols.get('tfopwg disposition', ''), '')}, "
                   f"TESS {x.get(cols.get('tess disposition', ''), '')}, period {x.get(cols.get('period (days)', ''), '')} d, "
                   f"depth {x.get(cols.get('depth (ppm)', ''), '')} ppm; {str(x.get(cols.get('comments', ''), ''))[:150]}")
    return " | ".join(out)


def figure(sid, win, detail, path):
    """All windows of the star aligned on the predicted time (light curves from the lightkurve cache)."""
    import matplotlib; matplotlib.use("Agg"); import matplotlib.pyplot as plt
    import lightkurve as lk
    from astropy.coordinates import SkyCoord
    import astropy.units as u
    sys.path.insert(0, os.getcwd())
    from pilot_track3 import flatten
    d = detail.loc[sid]; g = win[win["source_id"] == sid].sort_values("t_pred")
    sr = lk.search_lightcurve(SkyCoord(d["ra"] * u.deg, d["dec"] * u.deg), radius=10 * u.arcsec, mission="TESS")
    if len(sr) == 0:
        return False
    tab = sr.table
    sector_of = {k: int(tab["sequence_number"][k]) for k in range(len(sr))}
    rows = g.to_dict("records"); n = len(rows)
    fig, axes = plt.subplots(n, 1, figsize=(7, 1.3 * n + 0.6), sharex=True, squeeze=False)
    cache = {}
    for i, w in enumerate(rows):
        ax = axes[i][0]
        ks = [k for k, s in sector_of.items() if s == w["sector"] and str(tab["author"][k]) == w["author"]]
        if not ks:
            ax.text(0.5, 0.5, f"sector {w['sector']} not found", transform=ax.transAxes, ha="center", fontsize=6); continue
        key = (w["sector"], w["author"])
        if key not in cache:
            lc = sr[ks[0]].download(quality_bitmask="default").remove_nans().normalize()
            t, f = np.asarray(lc.time.value, float), np.asarray(lc.flux.value, float)
            cache[key] = flatten(t, f, 0.3)[:2]
        t, ff = cache[key]
        m = np.abs(t - w["t_pred"]) < w["half_window"] + 1.5
        ax.plot(t[m] - w["t_pred"], ff[m], ".", ms=1.5, color="0.35")
        ax.axvspan(-w["half_window"], w["half_window"], color="tab:blue", alpha=0.07)
        if w["dip_flag"]:
            ax.axvline(w["dip_t"] - w["t_pred"], color="tab:red", lw=0.8, ls="--")
        ax.text(0.01, 0.82, f"S{w['sector']} {w['author']} conj {w['conj']}  dip {w['dip_depth'] * 100:.2f}% (SNR {w['dip_snr']:.0f})"
                + ("  FLAG" if w["dip_flag"] else ""), transform=ax.transAxes, fontsize=6)
    axes[-1][0].set_xlabel("time from the predicted conjunction [d]")
    fig.suptitle(f"Gaia DR3 {sid}  P = {d['period']:.2f} d", fontsize=8)
    fig.tight_layout(); fig.savefig(path, dpi=120); plt.close(fig)
    return True


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--ids", nargs="*", type=int, default=None)
    ap.add_argument("--no-figures", action="store_true")
    a = ap.parse_args()
    os.makedirs(OUT, exist_ok=True)
    win = pd.read_csv("pilot_results/windows.csv")
    detail = pd.read_csv("track3_detail.csv").drop_duplicates("source_id").set_index("source_id")
    cand = candidates(win, a.ids)
    stars = list(dict.fromkeys(cand["source_id"].tolist()))
    print(f"{len(stars)} candidate stars ({int(cand['consistent'].sum())} conjunction(s) with consistent repeated dips)", flush=True)
    dossiers, lit = [], []
    for sid in stars:
        d = detail.loc[sid]; ra, dec = float(d["ra"]), float(d["dec"])
        rec = dict(source_id=sid, type=d["type"], G=round(float(d["g"]), 2), period=round(float(d["period"]), 3))
        cs = cand[cand["source_id"] == sid]
        rec["eclipses"] = " ; ".join(f"conj {r.conj}: {r.n_dips}/{r.n_windows} windows, {r.depth_pct}% (x{r.depth_ratio}), offset {r.offset_d:+.2f} d"
                                     f"{'' if r.offset_rms_after_drift_d != r.offset_rms_after_drift_d else f', rms {r.offset_rms_after_drift_d} d'}"
                                     f", {r.authors}" for r in cs.itertuples())
        rec["consistent"] = bool(cs["consistent"].any())
        try:
            name, otype, refs = simbad_refs(ra, dec)
        except Exception as exc:
            name, otype, refs = None, None, []; print(f"  SIMBAD failed for {sid}: {str(exc)[:60]}")
        hits = [r for r in refs if ECL_WORDS.search(r[1] or "")]
        rec.update(simbad=name, otype=otype, n_refs=len(refs), n_refs_eclipse_words=len(hits))
        lit.append(f"== Gaia DR3 {sid} = {name} [{otype}], {len(refs)} references")
        for b, title, y in refs:
            lit.append(f"   {'*' if ECL_WORDS.search(title or '') else ' '} {y} {b}  {title}")
        try:
            rec.update(tic_info(ra, dec))
        except Exception as exc:
            print(f"  TIC failed for {sid}: {str(exc)[:60]}")
        if rec.get("TIC"):
            try:
                rec["exofop_toi"] = exofop_toi(rec["TIC"])
            except Exception:
                rec["exofop_toi"] = "query failed"
        if not a.no_figures:
            try:
                rec["figure"] = f"{sid}.png" if figure(sid, win, detail, os.path.join(OUT, f"{sid}.png")) else ""
            except Exception as exc:
                rec["figure"] = f"failed: {str(exc)[:50]}"
        dossiers.append(rec)
        print(f"  Gaia DR3 {sid} = {name} [{otype}]: {rec['eclipses']} | refs {len(refs)} ({len(hits)} with eclipse/transit words)"
              f" | contamination {rec.get('contratio')} | {rec.get('exofop_toi', '')[:80]}", flush=True)
        pd.DataFrame(dossiers).to_csv(os.path.join(OUT, "dossier.csv"), index=False)
        open(os.path.join(OUT, "literature.txt"), "w").write("\n".join(lit) + "\n")
        time.sleep(0.5)
    print(f"-> {OUT}/dossier.csv, {OUT}/literature.txt, {OUT}/*.png")


if __name__ == "__main__":
    main()
