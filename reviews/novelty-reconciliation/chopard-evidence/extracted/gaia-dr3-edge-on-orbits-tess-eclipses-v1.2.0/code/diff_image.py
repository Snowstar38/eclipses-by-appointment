#!/usr/bin/env python3
"""Pixel-level check of the track-3 candidates: difference images (out of eclipse minus in eclipse).

For every flagged eclipse of the chosen stars, the TESS pixels of that sector are fetched (the SPOC target pixel file
when the star has 2-min data, otherwise a 15x15 TESSCut cutout of the full-frame images), and two mean images are
built: in eclipse (|t - t_ecl| < 0.4 D) and out of eclipse (the same number of hours just before and just after). Their
difference shows where the light was lost. The flux-weighted centroid of the difference image is compared with the
position of the star (Gaia coordinates through the image WCS) and with its neighbours from the TESS Input Catalog; the
uncertainty of the centroid comes from a bootstrap over the frames.
Verdict: 'on target' when the centroid of the difference is within max(3 sigma, 0.3 px) of the star, 'off target'
when it is more than 3 sigma and more than 0.5 px (about 10 arcsec) away and closer to a neighbour, 'unclear' otherwise.
Run from ~/Desktop/piste3:   python3 diff_image.py --ids 146197633037335168 1364450812894866688
   (default: every star whose flags came out 'on target' or 'check pixels' in pilot_results/artefact_vetting.csv)
Output: diff_images/<source_id>_s<sector>_<time>.png and diff_images/results.csv
"""
import argparse, os, signal, sys, warnings
import numpy as np
import pandas as pd

warnings.filterwarnings("ignore")
sys.path.insert(0, os.getcwd())
from pilot_track3 import duration

PIX_ARCSEC = 21.0
STEP_TIMEOUT = 300          # seconds after which an eclipse is abandoned (a MAST or TESSCut request that hangs)


class StepTimeout(BaseException):
    pass


def _alarm(signum, frame):
    raise StepTimeout()


def get_pixels(ra, dec, sector, prefer_spoc=True):
    """Returns (kind, time, flux cube, quality, wcs) for the sector."""
    import lightkurve as lk
    from astropy.coordinates import SkyCoord
    import astropy.units as u
    c = SkyCoord(ra * u.deg, dec * u.deg)
    if prefer_spoc:
        sr = lk.search_targetpixelfile(c, radius=10 * u.arcsec, mission="TESS", sector=int(sector), author="SPOC")
        if len(sr):
            tpf = sr[0].download(quality_bitmask="none")
            if tpf is not None:
                return "SPOC TPF", np.asarray(tpf.time.value, float), np.asarray(tpf.flux.value, float), np.asarray(tpf.quality, int), tpf.wcs
    sr = lk.search_tesscut(c, sector=int(sector))
    if len(sr):
        tpf = sr[0].download(cutout_size=15, quality_bitmask="none")
        if tpf is not None:
            return "TESSCut", np.asarray(tpf.time.value, float), np.asarray(tpf.flux.value, float), np.asarray(tpf.quality, int), tpf.wcs
    return None


def centroid(img, x0, y0, box=3):
    """Flux-weighted centroid of the positive part of img within +/- box pixels of (x0, y0)."""
    ny, nx = img.shape
    ys, xs = np.mgrid[0:ny, 0:nx]
    m = (np.abs(xs - x0) <= box) & (np.abs(ys - y0) <= box) & np.isfinite(img)
    w = np.where(m, np.clip(img, 0, None), 0.0)
    if w.sum() <= 0:
        return np.nan, np.nan
    return float((w * xs).sum() / w.sum()), float((w * ys).sum() / w.sum())


def analyse(t, cube, q, t_ecl, dur, x_star, y_star, rng, n_boot=200):
    good = (q == 0) & np.all(np.isfinite(cube.reshape(len(t), -1)), axis=1)
    inn = good & (np.abs(t - t_ecl) < 0.4 * dur)
    out = good & (np.abs(t - t_ecl) > 0.6 * dur) & (np.abs(t - t_ecl) < 0.6 * dur + 0.8 * dur)
    if inn.sum() < 3 or out.sum() < 6:
        return None
    img_in, img_out = np.nanmean(cube[inn], axis=0), np.nanmean(cube[out], axis=0)
    diff = img_out - img_in
    cx, cy = centroid(diff, x_star, y_star)
    ox, oy = centroid(img_out, x_star, y_star)
    ii, oo = np.where(inn)[0], np.where(out)[0]
    bx, by = [], []
    for _ in range(n_boot):
        d = np.nanmean(cube[rng.choice(oo, len(oo))], axis=0) - np.nanmean(cube[rng.choice(ii, len(ii))], axis=0)
        x_, y_ = centroid(d, x_star, y_star)
        if np.isfinite(x_):
            bx.append(x_); by.append(y_)
    sig = float(np.hypot(np.std(bx), np.std(by))) if len(bx) > 10 else np.nan
    depth_pix = float(np.nansum(diff) / np.nansum(img_out)) if np.nansum(img_out) > 0 else np.nan
    return dict(diff=diff, img_out=img_out, cx=cx, cy=cy, ox=ox, oy=oy, sigma_px=sig, n_in=int(inn.sum()), n_out=int(out.sum()),
                depth_in_cutout=depth_pix)


def neighbours(ra, dec, wcs, radius_arcsec=63):
    from astroquery.mast import Catalogs
    t = Catalogs.query_region(f"{ra} {dec}", radius=radius_arcsec / 3600, catalog="TIC").to_pandas()
    if t.empty:
        return t
    px = wcs.all_world2pix(np.vstack([t["ra"], t["dec"]]).T, 0)
    t["x"], t["y"] = px[:, 0], px[:, 1]
    return t[["ID", "Tmag", "ra", "dec", "x", "y", "dstArcSec"]]


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--ids", nargs="*", type=int, default=None); ap.add_argument("--max-per-star", type=int, default=3)
    a = ap.parse_args()
    win = pd.read_csv("pilot_results/windows.csv")
    det = pd.read_csv("track3_detail.csv").drop_duplicates("source_id").set_index("source_id")
    flags = win[(win["dip_flag"] == True) & (win["dip_depth"] <= 0.5)].copy()
    if os.path.exists("pilot_results/artefact_vetting.csv"):
        v = pd.read_csv("pilot_results/artefact_vetting.csv")
        if "reasons_instrumental" in v.columns:
            ok = v[v["verdict"].isin(["on target", "check pixels"]) & (v["kind"] == "dip")]
            keys = set(zip(ok["source_id"].astype(int), ok["t"].round(3)))
            flags = flags[[(int(s), round(t, 3)) in keys for s, t in zip(flags["source_id"], flags["dip_t"])]]
    if a.ids:
        flags = flags[flags["source_id"].isin(a.ids)]
    flags = flags.sort_values("dip_snr", ascending=False).groupby("source_id").head(a.max_per_star)
    os.makedirs("diff_images", exist_ok=True)
    rng = np.random.default_rng(20261012)
    rows = []
    print(f"{len(flags)} eclipses of {flags['source_id'].nunique()} stars", flush=True)
    for r in flags.itertuples():
        sid = int(r.source_id); s = det.loc[sid]; ra, dec = float(s["ra"]), float(s["dec"]); dur = duration(float(s["period"]))
        rec = dict(source_id=sid, sector=int(r.sector), t_ecl=round(float(r.dip_t), 4), depth_lc_pct=round(float(r.dip_depth) * 100, 2))
        print(f"  ... Gaia DR3 {sid} S{r.sector}: fetching the pixels", flush=True)
        signal.signal(signal.SIGALRM, _alarm); signal.alarm(STEP_TIMEOUT)
        try:
            got = get_pixels(ra, dec, r.sector)
        except StepTimeout:
            got = None; rec["note"] = f"abandoned after {STEP_TIMEOUT} s (server not answering)"
            print(f"  ... Gaia DR3 {sid} S{r.sector}: abandoned after {STEP_TIMEOUT} s", flush=True)
        except Exception as exc:
            got = None; rec["note"] = f"pixels failed: {str(exc)[:60]}"
        finally:
            signal.alarm(0)
        if got is None:
            rec.setdefault("note", "no pixel data"); rows.append(rec); continue
        kind, t, cube, q, wcs = got
        xs, ys = wcs.all_world2pix([[ra, dec]], 0)[0]
        res = analyse(t, cube, q, float(r.dip_t), dur, xs, ys, rng)
        if res is None:
            rec.update(pixels=kind, note="too few frames in or out of eclipse"); rows.append(rec); continue
        off = float(np.hypot(res["cx"] - xs, res["cy"] - ys))
        signal.signal(signal.SIGALRM, _alarm); signal.alarm(120)
        try:
            nb = neighbours(ra, dec, wcs)
        except (Exception, StepTimeout):
            nb = pd.DataFrame()
        finally:
            signal.alarm(0)
        closest = None
        if len(nb):
            nb["d_diff"] = np.hypot(nb["x"] - res["cx"], nb["y"] - res["cy"])
            closest = nb.sort_values("d_diff").iloc[0]
        sig = res["sigma_px"]
        if off <= max(3 * (sig if np.isfinite(sig) else 0.3), 0.3):
            verdict = "on target"
        elif off > 0.5 and (not np.isfinite(sig) or off > 3 * sig) and closest is not None and closest["dstArcSec"] > 2:
            verdict = "off target"
        else:
            verdict = "unclear"
        rec.update(pixels=kind, offset_px=round(off, 3), offset_arcsec=round(off * PIX_ARCSEC, 1), sigma_px=round(sig, 3) if np.isfinite(sig) else None,
                   n_in=res["n_in"], n_out=res["n_out"], depth_in_cutout_pct=round(res["depth_in_cutout"] * 100, 3),
                   closest_source=None if closest is None else f"TIC {int(closest['ID'])} (T={closest['Tmag']:.1f}, {closest['dstArcSec']:.0f}\" from the star)",
                   n_neighbours_within_3px=int((nb["dstArcSec"] < 63).sum() - 1) if len(nb) else None, verdict=verdict)
        rows.append(rec)
        try:
            import matplotlib; matplotlib.use("Agg"); import matplotlib.pyplot as plt
            fig, axes = plt.subplots(1, 2, figsize=(7.4, 3.4))
            for ax, img, title in ((axes[0], res["img_out"], "out of eclipse"), (axes[1], res["diff"], "difference (out - in)")):
                ax.imshow(img, origin="lower", cmap="viridis"); ax.set_title(title, fontsize=8)
                ax.plot(xs, ys, "x", color="red", ms=8, mew=1.5, label="target")
                if len(nb):
                    m = (nb["dstArcSec"] > 2) & (nb["x"].between(-0.5, img.shape[1] - 0.5)) & (nb["y"].between(-0.5, img.shape[0] - 0.5))
                    ax.plot(nb[m]["x"], nb[m]["y"], "o", mfc="none", mec="white", ms=5, mew=0.8, label="TIC neighbours")
            axes[1].plot(res["cx"], res["cy"], "+", color="orange", ms=12, mew=2, label="centroid of the difference")
            axes[1].legend(fontsize=6, loc="upper right")
            fig.suptitle(f"Gaia DR3 {sid}  S{r.sector} ({kind})  t = {float(r.dip_t):.3f}: offset {off:.2f} px ({off*PIX_ARCSEC:.0f}\") -> {verdict}", fontsize=8)
            fig.tight_layout(); fig.savefig(f"diff_images/{sid}_s{int(r.sector)}_{int(float(r.dip_t))}.png", dpi=120); plt.close(fig)
        except Exception:
            pass
        print(f"  Gaia DR3 {sid} S{r.sector} ({kind}): offset {off:.2f} px = {off*PIX_ARCSEC:.0f}\" (sigma {sig:.2f} px) -> {verdict}", flush=True)
    pd.DataFrame(rows).to_csv("diff_images/results.csv", index=False)
    print("-> diff_images/results.csv and diff_images/*.png")


if __name__ == "__main__":
    main()
