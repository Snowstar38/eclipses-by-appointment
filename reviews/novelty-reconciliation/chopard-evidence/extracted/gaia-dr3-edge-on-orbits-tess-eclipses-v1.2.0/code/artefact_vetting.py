#!/usr/bin/env python3
"""Artefact vetting of flagged eclipses and bumps, version 2 (recalibrated), after the diagnostics of the anomaly-triage
paper (P1): persistence across independent views, spacecraft events, background, photocentre, common mode.

Version 1 rejected the known eclipsing binary HD 75767 in almost every sector: its statistics compared hours of data
with the scatter of single cadences, and it read SPOC's own outlier flags on eclipse cadences as artefacts. Version 2:
  1. persistence (P1): the pilot's box statistic in every pipeline of the sector (SPOC, TESS-SPOC, QLP), with half and
     twice the flattening width, with the 'hard' quality mask, and with the cadences of spacecraft events removed
     (attitude tweak, coarse point, Argabrightening, momentum dump with 0.05 d around it, discontinuity, stray light;
     NOT impulsive outliers, which SPOC sets on deep eclipse cadences). A flag persists in a view when found within
     max(0.2 d, D) of its time, at SNR >= 5 and at least half its amplitude;
  2. spacecraft events count against a flag only if it does NOT persist once their cadences are removed;
  3. background: change of SAP_BKG during the event relative to a line fitted on the day around it, divided by the
     SAP flux: an artefact only if this change could produce at least half of the dip (or bump) by over- (under-)
     subtraction, and is significant against the correlated scatter (> 3 sigma);
  4. photocentre: change of the centroid during the event relative to a local line, in units of the scatter of
     event-length bins around it (correlated noise); above 5 sigma the flag goes to the pixel-level check (difference
     image), it is not rejected;
  5. common mode: three or more other flagged stars on the same camera within 0.1 d;
  6. crowding: CROWDSAP < 0.7 also sends the flag to the pixel-level check.
Verdicts: 'instrumental', 'check pixels', 'on target', 'not reproduced' (the flag is not found again in its own light
curve, so it cannot be vetted), 'no data'. Version 2.1 (after the calibration on 256 known eclipses): views covering
less than half of the event are not used; the background test is applied to SPOC and TESS-SPOC only; the robustness
tests apply only to a reproduced flag; the photocentre criterion is the shift per unit depth (> 0.15 px).
Calibration: run it first on known eclipses (the calibration set built from the 93 eclipsing binaries of the Gaia-TESS
survey), which should come out 'on target' or 'check pixels' in at least 95 per cent of cases:
    python3 artefact_vetting.py --windows calib_windows.csv --detail calib_detail.csv --out calib_vetting.csv
Then on the pilot:
    python3 artefact_vetting.py
"""
import argparse, os, signal, sys, warnings
import numpy as np
import pandas as pd

warnings.filterwarnings("ignore")
sys.path.insert(0, os.getcwd())
from pilot_track3 import box_extremes, duration                      # the pilot's own statistic

EVENT_BITS = {1: "attitude tweak", 4: "coarse point", 16: "Argabrightening", 32: "momentum dump", 256: "discontinuity",
              2048: "stray light", 4096: "stray light 2"}
EVENT_MASK = sum(EVENT_BITS)
FLAG_TIMEOUT = 300          # seconds after which a flag is skipped (a MAST request that hangs); a rerun retries it


class FlagTimeout(BaseException):
    pass


def _alarm(signum, frame):
    raise FlagTimeout()


def flatten_w(t, f, dur, width):
    from scipy.ndimage import median_filter
    o = np.argsort(t); t = t[o]; f = f[o]
    dt = np.median(np.diff(t)) if len(t) > 1 else 0.02
    k = max(3, int(round(width / dt)) | 1); edge = max(0.3, 1.5 * dur)
    cuts = np.where(np.diff(t) > 0.5)[0] + 1; tt, fo = [], []
    for st, sf in zip(np.split(t, cuts), np.split(f, cuts)):
        if len(st) < k or st[-1] - st[0] < 2 * edge + 4 * dur:
            continue
        fl = sf / median_filter(sf, size=min(k, len(sf) - (1 - len(sf) % 2)), mode="nearest")
        keep = (st > st[0] + edge) & (st < st[-1] - edge)
        tt.append(st[keep]); fo.append(fl[keep])
    if not tt:
        return np.array([]), np.array([]), dt
    return np.concatenate(tt), np.concatenate(fo), dt


def measure(t, f, dur, t_event, tol, width, kind):
    tt, ff, dt = flatten_w(t, f, dur, width)
    if len(tt) < 50 or np.min(np.abs(tt - t_event)) > dur:
        return None
    d, b = box_extremes(tt, ff, dt, t_event, tol, dur)
    if d is None:
        return None
    return d if kind == "dip" else b


def load_products(ra, dec, sector):
    import lightkurve as lk
    from astropy.coordinates import SkyCoord
    import astropy.units as u
    sr = lk.search_lightcurve(SkyCoord(ra * u.deg, dec * u.deg), radius=10 * u.arcsec, mission="TESS", sector=int(sector))
    out = {}
    if len(sr) == 0:
        return out
    tab = sr.table
    order = sorted(range(len(sr)), key=lambda k: (float(tab["exptime"][k]) != 120.0, float(tab["distance"][k])))
    for k in order:
        auth = str(tab["author"][k])
        if auth not in ("SPOC", "TESS-SPOC", "QLP") or auth in out:
            continue
        try:
            lc = sr[k].download(quality_bitmask="none")
        except Exception:
            continue
        if lc is not None:
            out[auth] = lc
    return out


def col(lc, name):
    try:
        if name in getattr(lc, "colnames", []):
            v = lc[name]; return np.asarray(v.value if hasattr(v, "value") else v, float)
    except Exception:
        pass
    return None


def arrays(lc, mode):
    """mode 'default' or 'hard' (lightkurve masks) or 'no events' (default mask minus the spacecraft-event cadences)."""
    from lightkurve.utils import TessQualityFlags
    q = np.asarray(lc.quality.value if hasattr(lc.quality, "value") else lc.quality, int)
    t_all = np.asarray(lc.time.value, float); f_all = np.asarray(lc.flux.value, float)
    # impulsive-outlier flags (512) are ignored: SPOC sets them on deep eclipse cadences, and a single-cadence outlier
    # cannot by itself make a box dip lasting hours
    good = TessQualityFlags.create_quality_mask(q & ~512, bitmask="hard" if mode == "hard" else "default")
    if mode == "no events":
        good &= (q & EVENT_MASK) == 0
        for td in t_all[(q & 32) != 0]:
            good &= np.abs(t_all - td) > 0.05
    m = good & np.isfinite(t_all) & np.isfinite(f_all)
    med = np.nanmedian(f_all[m]) if m.any() else np.nan
    return t_all[m], f_all[m] / med, q, t_all


def events_in(q, t_all, t_event, half):
    m = np.abs(t_all - t_event) < half
    bits = int(np.bitwise_or.reduce(q[m])) if m.any() else 0
    return [n for b, n in sorted(EVENT_BITS.items()) if bits & b]


def local_change(t_all, x, t_event, half):
    """Change of x during the event relative to a line fitted on +/- (half + 1 d) outside it, and its significance in
    units of the scatter of event-length bins of the residuals (correlated noise). Returns (change, z)."""
    ok = np.isfinite(x) & np.isfinite(t_all)
    t, y = t_all[ok], x[ok]
    near = np.abs(t - t_event) < half + 1.0
    inn = np.abs(t - t_event) < half
    out = near & (np.abs(t - t_event) > half + 0.1)
    if inn.sum() < 3 or out.sum() < 20:
        return None, None
    c = np.polyfit(t[out] - t_event, y[out], 1)
    res = y - np.polyval(c, t - t_event)
    delta = float(np.median(res[inn]))
    edges = np.arange(t[out].min(), t[out].max() + 2 * half, 2 * half)
    idx = np.digitize(t[out], edges)
    bins = [res[out][idx == i].mean() for i in np.unique(idx) if (idx == i).sum() >= 3]
    if len(bins) < 3:
        return delta, None
    s = float(np.std(bins, ddof=1))
    return delta, (float(delta / s) if s > 0 else None)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--windows", default="pilot_results/windows.csv"); ap.add_argument("--detail", default="track3_detail.csv")
    ap.add_argument("--out", default="pilot_results/artefact_vetting.csv")
    ap.add_argument("--ids", nargs="*", type=int, default=None); ap.add_argument("--kind", default="both", choices=["both", "dip", "bump"])
    a = ap.parse_args()
    win = pd.read_csv(a.windows)
    det = pd.read_csv(a.detail).drop_duplicates("source_id").set_index("source_id")
    flags = []
    if a.kind in ("both", "dip"):
        flags += [dict(source_id=int(r.source_id), kind="dip", sector=int(r.sector), author=r.author, t=float(r.dip_t), amp=float(r.dip_depth), snr=float(r.dip_snr))
                  for r in win[(win["dip_flag"] == True) & (win["dip_depth"] <= 0.5)].itertuples()]
    if a.kind in ("both", "bump") and "bump_flag" in win.columns:
        flags += [dict(source_id=int(r.source_id), kind="bump", sector=int(r.sector), author=r.author, t=float(r.bump_t), amp=float(r.bump_height), snr=float(r.bump_snr))
                  for r in win[win["bump_flag"] == True].itertuples()]
    if a.ids:
        flags = [x for x in flags if x["source_id"] in set(a.ids)]
    work = a.out.replace(".csv", "_work.csv")
    done = {}
    if os.path.exists(work):
        for _, x in pd.read_csv(work).iterrows():
            done[(int(x["source_id"]), x["kind"], round(float(x["t"]), 4))] = x.to_dict()
    print(f"{len(flags)} flags to vet; {len(done)} already done", flush=True)
    cache = {}
    for i, x in enumerate(flags):
        key = (x["source_id"], x["kind"], round(x["t"], 4))
        if key in done:
            continue
        s = det.loc[x["source_id"]]; P = float(s["period"]); dur = duration(P)
        base = max(1.0, 4 * dur); tol = max(0.2, dur); half = max(dur / 2, 0.1)
        rec = dict(x, period=P, duration=round(dur, 3), camera=None, ccd=None, crowdsap=None, events_in_window="",
                   bkg_change_rel=None, bkg_z=None, centroid_shift_px=None, centroid_z=None, note="")
        ck = (x["source_id"], x["sector"])
        if ck not in cache:
            signal.signal(signal.SIGALRM, _alarm); signal.alarm(FLAG_TIMEOUT)
            try:
                cache[ck] = load_products(float(s["ra"]), float(s["dec"]), x["sector"])
            except FlagTimeout:
                print(f"  [{i + 1}/{len(flags)}] Gaia DR3 {x['source_id']} S{x['sector']}: skipped after {FLAG_TIMEOUT} s "
                      "(server not answering); rerun to retry it", flush=True)
                continue
            except Exception as exc:
                cache[ck] = {}; rec["note"] = f"download failed: {str(exc)[:50]}"
            finally:
                signal.alarm(0)
        views = []
        ref_cov = {}
        def add(label, t, f, width):
            n_in = int(np.sum(np.abs(t - x["t"]) < half))
            auth = label.split("/")[0]
            if label.endswith("/default"):
                ref_cov[auth] = n_in
            if ref_cov.get(auth) and n_in < 0.5 * ref_cov[auth]:
                views.append((label, None, np.nan, np.nan)); return          # too few cadences left in the event
            m = measure(t, f, dur, x["t"], tol, width, x["kind"])
            if m is not None:
                views.append((label, bool(m[2] >= 5 and m[1] >= 0.5 * x["amp"]), m[1], m[2]))
        for auth, lc in cache[ck].items():
            t, f, q, t_all = arrays(lc, "default")
            add(f"{auth}/default", t, f, base)
            if auth != x["author"]:
                continue
            add(f"{auth}/half width", t, f, max(0.5, base / 2)); add(f"{auth}/double width", t, f, 2 * base)
            th, fh, _, _ = arrays(lc, "hard"); add(f"{auth}/hard mask", th, fh, base)
            tn, fn, _, _ = arrays(lc, "no events"); add(f"{auth}/no events", tn, fn, base)
            rec["events_in_window"] = ";".join(events_in(q, t_all, x["t"], half + 0.05))
            meta = getattr(lc, "meta", {}) or {}
            rec["camera"], rec["ccd"], rec["crowdsap"] = meta.get("CAMERA"), meta.get("CCD"), meta.get("CROWDSAP")
            bkg, sap = col(lc, "sap_bkg"), col(lc, "sap_flux")
            if auth in ("SPOC", "TESS-SPOC") and bkg is not None and sap is not None:   # QLP columns are not comparable
                dbkg, zb = local_change(t_all, bkg, x["t"], half)
                fsap = np.nanmedian(sap[np.abs(t_all - x["t"]) < half + 1.0])
                if dbkg is not None and np.isfinite(fsap) and fsap > 0:
                    rec["bkg_change_rel"] = round(dbkg / fsap, 5); rec["bkg_z"] = None if zb is None else round(zb, 1)
            try:
                cx = np.asarray(lc.centroid_col.value, float); cy = np.asarray(lc.centroid_row.value, float)
                dx, zx = local_change(t_all, cx, x["t"], half); dy, zy = local_change(t_all, cy, x["t"], half)
                if zx is not None and zy is not None:
                    rec["centroid_shift_px"] = round(float(np.hypot(dx, dy)), 4); rec["centroid_z"] = round(float(np.hypot(zx, zy)), 1)
            except Exception:
                pass
        rec["views"] = " | ".join(f"{l}:" + ("coverage<50%" if ok is None else f"{'Y' if ok else 'n'}({amp*100:.2f}%,{snr:.0f})") for l, ok, amp, snr in views)
        used = [v for v in views if v[1] is not None]
        rec["n_views"] = len(used); rec["persistence"] = round(float(np.mean([v[1] for v in used])), 2) if used else None
        own = {l.split("/")[1]: ok for l, ok, _, _ in used if l.startswith(x["author"] + "/")}
        seen = {l.split("/")[0]: ok for l, ok, _, _ in used if l.endswith("/default")}
        precise = [p for p in ("SPOC", "TESS-SPOC") if p in seen]
        rec["reproduced"] = own.get("default")          # the flag is found again in its own light curve
        ri, rp = [], []
        if rec["reproduced"] and rec["events_in_window"] and own.get("no events") is False:
            ri.append(f"vanishes without the {rec['events_in_window']} cadences")
        if x["author"] == "QLP" and precise and not any(seen[p] for p in precise):
            ri.append("absent from the SPOC/TESS-SPOC light curve")
        robust = [own.get(k) for k in ("half width", "double width", "hard mask") if own.get(k) is not None]
        if rec["reproduced"] and len(robust) >= 2 and np.mean(robust) < 0.5:
            ri.append("not robust to the flattening or the quality mask")
        br = rec["bkg_change_rel"]
        if br is not None:
            explains = (br if x["kind"] == "dip" else -br) >= 0.5 * x["amp"]
            if explains and (rec["bkg_z"] is None or abs(rec["bkg_z"]) > 3):
                ri.append(f"background change of {br*100:+.2f}% of the flux explains it")
        # an eclipse on the target moves the photocentre in proportion to its depth (calibration: <= 0.11 px per unit
        # depth for 95 per cent of the known eclipses); an eclipse on a neighbour 1 pixel away gives of order 1 px per unit
        if rec["centroid_z"] is not None and rec["centroid_z"] > 5 and rec["centroid_shift_px"] / max(x["amp"], 1e-4) > 0.15:
            rp.append(f"centroid moves by {rec['centroid_shift_px']:.3f} px, {rec['centroid_shift_px'] / x['amp']:.2f} px per unit depth ({rec['centroid_z']:.0f} sigma)")
        if rec["crowdsap"] is not None and float(rec["crowdsap"]) < 0.7:
            rp.append(f"CROWDSAP {float(rec['crowdsap']):.2f}")
        rec["reasons_instrumental"], rec["reasons_pixels"] = "; ".join(ri), "; ".join(rp)
        done[key] = rec
        pd.DataFrame(list(done.values())).to_csv(work, index=False)
        print(f"  [{i + 1}/{len(flags)}] Gaia DR3 {x['source_id']} {x['kind']} S{x['sector']} {x['author']} {x['amp']*100:.2f}%: persistence "
              f"{rec['persistence']} over {rec['n_views']} views" + (f"; {rec['reasons_instrumental']}" if ri else "") + (f"; {rec['reasons_pixels']}" if rp else ""), flush=True)
    df = pd.DataFrame(list(done.values()))
    if not len(df):
        print("nothing vetted"); return
    cm = []
    for _, r in df.iterrows():
        if pd.isna(r["camera"]):
            cm.append(0); continue
        same = df[(df["sector"] == r["sector"]) & (df["camera"] == r["camera"]) & (df["source_id"] != r["source_id"]) & (np.abs(df["t"] - r["t"]) < 0.1)]
        cm.append(int(same["source_id"].nunique()))
    df["common_mode"] = cm
    verdicts, reasons = [], []
    for _, r in df.iterrows():
        ri = [s_ for s_ in str(r["reasons_instrumental"]).split("; ") if s_ and s_ != "nan"]
        rp = [s_ for s_ in str(r["reasons_pixels"]).split("; ") if s_ and s_ != "nan"]
        if r["common_mode"] >= 3:
            ri.append(f"{r['common_mode']} other stars on the same camera at the same time")
        if not r["n_views"]:
            verdicts.append("no data")
        elif r.get("reproduced") is False or str(r.get("reproduced")) == "False":
            verdicts.append("not reproduced")          # cannot be vetted: the flag is not found again in its own light curve
        else:
            verdicts.append("instrumental" if ri else "check pixels" if rp else "on target")
        reasons.append("; ".join(ri + rp))
    df["verdict"] = verdicts; df["reasons"] = reasons
    df.to_csv(a.out, index=False)
    print("\nverdicts:", df.groupby(["kind", "verdict"]).size().to_dict())
    print(f"-> {a.out}")


if __name__ == "__main__":
    main()
