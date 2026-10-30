#!/usr/bin/env python3
"""Pilot search for eclipses (dips) and self-lensing flares (bumps) at the predicted conjunctions of
near-edge-on Gaia DR3 astrometric orbits, in TESS light curves.

Inputs, in the working folder (from the feasibility step):
  track3_astrometric_orbits_1.csv   orbital elements (period, eccentricity, t_periastron, Thiele-Innes)
  track3_detail.csv                 sigma_i, p_eclipse, conjunction-time uncertainties, TESS coverage
Run (resumable, stops cleanly after --max-hours; the most promising stars come first):
  caffeinate -i python3 pilot_track3.py --max-hours 14
  (a star whose MAST requests hang is abandoned after --star-timeout seconds; --retry-timeouts retries them)
Outputs in pilot_results/: stars.jsonl (one line per processed star), windows.csv, events.csv,
  flagged.csv, false_alarms.csv, plots/*.png and summary.txt (rewritten after every 25 stars).

Method
  * Conjunctions: an astrometric orbit gives omega only to within 180 deg, so both conjunctions are searched;
    either may be the primary eclipse or, for a dark companion, the self-lensing flare.
  * Uncertainty of a conjunction time at epoch t: linear in t through the Monte-Carlo values at BTJD 1600
    and 3100 of the feasibility step.
  * Tier A (conjunction known to better than --max-sigma days at the epoch of a sector): windows of half-width
    max(0.5 d, 2 sigma_t); in each, the deepest box dip and the highest box bump of the expected duration
    (statistic validated on the Gaia-TESS survey: running-median flattening, MAD noise), control level from
    12 random epochs of the same light curve away from every predicted window (with a smaller half-width
    when the sector is too short), and the same windows shifted by a random fraction of the period (5 draws)
    for the false-alarm rate. A bump within 1.5 durations + 1 d of a dip of at least 0.3 % and SNR 8 is not flagged
    (flattening artefact next to an eclipse). Flags: dip depth >= 0.3 %, SNR >= 8, > 2 x control; bump height
    >= 0.05 %, SNR >= 8, > 2 x control.
  * Tier B (sigma_t larger): single-event search over the sectors within 3 sigma_t of a predicted conjunction;
    every event with SNR >= 8 is listed with its offset from the prediction in units of sigma_t.
Light curves: one per sector, SPOC 2-min first, then TESS-SPOC, then QLP; only the sectors that overlap a
window (tier A) or the 3-sigma range (tier B) are downloaded.
"""
import argparse, csv, json, math, os, re, signal, sys, time, warnings
import numpy as np
import pandas as pd
from scipy.ndimage import median_filter

warnings.filterwarnings("ignore")
try:
    from astroquery.mast import conf as _mast_conf
    _mast_conf.timeout = 120          # seconds per MAST request (default 600)
except Exception:
    pass
REF_BTJD = 389.0
MJD_TO_BTJD = -56999.5
OUT = "pilot_results"
DIP_MIN, BUMP_MIN, SNR_MIN, CTRL_FACTOR, N_CTRL, N_FALSE = 0.003, 0.0005, 8.0, 2.0, 12, 5


# ------------------------------------------------------------------ orbit
def ti_to_omega(A, B, F, G):
    wpO = math.atan2(B - F, A + G); wmO = math.atan2(-B - F, A - G)
    return math.degrees(0.5 * (wpO + wmO)) % 360


def conj_times(P, e, w_deg, tp):
    out = []
    for nu0 in (90.0, 270.0):
        nu = math.radians(nu0 - w_deg)
        E = 2 * math.atan2(math.sqrt(1 - e) * math.sin(nu / 2), math.sqrt(1 + e) * math.cos(nu / 2))
        M = E - e * math.sin(E)
        out.append(tp + ((M % (2 * math.pi)) / (2 * math.pi)) * P)
    return out


def duration(P, e=0.0, M=1.3, R=1.2):
    a = 215.032 * (M * (P / 365.25) ** 2) ** (1 / 3)
    return min(1.5, max(0.08, P / math.pi * math.asin(min(1.0, R / a)) * math.sqrt(max(1 - e * e, 0.05))))


def sigma_at(s1600, s3100, t):
    slope = (s3100 - s1600) / 1500.0
    return max(0.05, s1600 + slope * (t - 1600.0))


def predicted(P, c, t0, t1):
    k0 = math.ceil((t0 - c) / P); k1 = math.floor((t1 - c) / P)
    return [c + k * P for k in range(k0, k1 + 1)]


# ------------------------------------------------------------------ statistics (validated on the survey)
def flatten(t, f, dur, gap=0.5):
    """Running-median flattening done segment by segment (segments split at gaps > `gap` days); the points
    within max(0.3 d, 1.5 durations) of a segment edge are dropped (edge artefacts of the filter)."""
    o = np.argsort(t); t = t[o]; f = f[o]
    dt = np.median(np.diff(t)) if len(t) > 1 else 0.02
    k = max(3, int(round(max(1.0, 4 * dur) / dt)) | 1)
    edge = max(0.3, 1.5 * dur)
    cuts = np.where(np.diff(t) > gap)[0] + 1
    tt, fo = [], []
    for seg_t, seg_f in zip(np.split(t, cuts), np.split(f, cuts)):
        if len(seg_t) < k or seg_t[-1] - seg_t[0] < 2 * edge + 4 * dur:
            continue
        fl = seg_f / median_filter(seg_f, size=min(k, len(seg_f) - (1 - len(seg_f) % 2)), mode="nearest")
        keep = (seg_t > seg_t[0] + edge) & (seg_t < seg_t[-1] - edge)
        tt.append(seg_t[keep]); fo.append(fl[keep])
    if not tt:
        return np.array([]), np.array([]), dt
    return np.concatenate(tt), np.concatenate(fo), dt


def box_extremes(t, ff, dt, tc, hw, dur):
    """Deepest dip and highest bump of width dur centred within tc +/- hw: ((t, depth, snr), (t, height, snr))."""
    lo, hi = np.searchsorted(t, [tc - hw - 1.0, tc + hw + 1.0])
    tt, fw = t[lo:hi], ff[lo:hi]
    if len(tt) < 10:
        return None, None
    sig = 1.4826 * np.median(np.abs(fw - np.median(fw)))
    if not sig > 0:
        return None, None
    cs = np.concatenate([[0.0], np.cumsum(fw)])
    centers = np.arange(tc - hw, tc + hw + 1e-9, dt / 2)
    a = np.searchsorted(tt, centers - dur / 2, side="left"); b = np.searchsorted(tt, centers + dur / 2, side="right")
    n = b - a; ok = n >= 2
    if not ok.any():
        return None, None
    mean = np.full(len(centers), np.nan); mean[ok] = (cs[b[ok]] - cs[a[ok]]) / n[ok]
    snr_unit = np.sqrt(np.maximum(n, 1)) / sig
    dep = 1.0 - mean; i = int(np.nanargmax(dep)); j = int(np.nanargmin(dep))
    return (float(centers[i]), float(dep[i]), float(dep[i] * snr_unit[i])), (float(centers[j]), float(-dep[j]), float(-dep[j] * snr_unit[j]))


def control_levels(t, ff, dt, hw, dur, rng, avoid=(), avoid_hw=0.0):
    """95th percentiles of the deepest dip and highest bump at N_CTRL random epochs of the light curve, away
    from every predicted window (avoid: predicted times; avoid_hw: their half-width). If windows of half-width
    hw do not fit, the largest half-width that does (>= 0.5 d) is used. Returns (p95_dip, p95_bump, hw_used)."""
    avoid = np.asarray(list(avoid), float)
    for hwc in (hw, hw / 2, hw / 4, 0.5):
        hwc = max(0.5, hwc)
        lo, hi = t[0] + hwc, t[-1] - hwc
        if hi <= lo:
            continue
        d, b, tries = [], [], 0
        while len(d) < N_CTRL and tries < 60 * N_CTRL:
            tries += 1
            c = rng.uniform(lo, hi)
            if avoid.size and np.min(np.abs(avoid - c)) < avoid_hw + hwc + dur:
                continue
            x, y = box_extremes(t, ff, dt, c, hwc, dur)
            if x is not None:
                d.append(x[1]); b.append(y[1])
        if len(d) >= 5:
            return float(np.percentile(d, 95)), float(np.percentile(b, 95)), hwc
        if hwc == 0.5:
            break
    return float("nan"), float("nan"), float("nan")


def single_events(t, ff, dt, dur, kind):
    """Box events over a whole light curve, |SNR| >= 8, at least 2 durations apart."""
    sig = 1.4826 * np.median(np.abs(ff - np.median(ff)))
    if not sig > 0 or len(t) < 50:
        return []
    cs = np.concatenate([[0.0], np.cumsum(ff)])
    centers = np.arange(t[0] + dur, t[-1] - dur, dt)
    a = np.searchsorted(t, centers - dur / 2, side="left"); b = np.searchsorted(t, centers + dur / 2, side="right")
    n = b - a; ok = n >= 3
    if not ok.any():
        return []
    centers, a, b, n = centers[ok], a[ok], b[ok], n[ok]
    amp = 1.0 - (cs[b] - cs[a]) / n if kind == "dip" else (cs[b] - cs[a]) / n - 1.0
    snr = amp * np.sqrt(n) / sig
    order = np.argsort(-snr); events = []
    for i in order:
        if snr[i] < SNR_MIN or amp[i] < (DIP_MIN if kind == "dip" else BUMP_MIN):
            break
        if all(abs(centers[i] - e[0]) > 2 * dur for e in events):
            events.append((float(centers[i]), float(amp[i]), float(snr[i])))
        if len(events) >= 5:
            break
    return events


# ------------------------------------------------------------------ TESS light curves
PREF = {"SPOC": 0, "TESS-SPOC": 1, "QLP": 2}


def search(ra, dec):
    import lightkurve as lk
    from astropy.coordinates import SkyCoord
    import astropy.units as u
    sr = lk.search_lightcurve(SkyCoord(ra * u.deg, dec * u.deg), radius=10 * u.arcsec, mission="TESS")
    if len(sr) == 0:
        return sr, []
    tab = sr.table; rows = []
    for k in range(len(sr)):
        auth = str(tab["author"][k])
        if auth not in PREF:
            continue
        sector = int(tab["sequence_number"][k]) if "sequence_number" in tab.colnames else int(re.findall(r"\d+", str(tab["mission"][k]))[-1])
        t0 = float(tab["t_min"][k]) + MJD_TO_BTJD if "t_min" in tab.colnames else float("nan")
        t1 = float(tab["t_max"][k]) + MJD_TO_BTJD if "t_max" in tab.colnames else t0 + 27.5
        exptime = float(tab["exptime"][k]) if "exptime" in tab.colnames else 0.0
        rows.append(dict(k=k, sector=sector, author=auth, t0=t0, t1=t1, exptime=exptime, dist=float(tab["distance"][k])))
    best = {}
    for r in rows:   # one light curve per sector: SPOC first, then the shortest cadence, then the closest
        key = (PREF[r["author"]], r["exptime"] if r["exptime"] > 0 else 1e9, r["dist"])
        if r["sector"] not in best or key < best[r["sector"]][0]:
            best[r["sector"]] = (key, r)
    return sr, [v[1] for v in sorted(best.values(), key=lambda x: x[1]["sector"])]


def download(sr, k):
    lc = sr[k].download(quality_bitmask="default")
    if lc is None:
        return None
    lc = lc.remove_nans().normalize()
    t = np.asarray(lc.time.value, float); f = np.asarray(lc.flux.value, float)
    m = np.isfinite(t) & np.isfinite(f)
    return t[m], f[m]


# ------------------------------------------------------------------ one star
def process(star, rng, max_sigma, plots):
    sid = int(star["source_id"]); P = float(star["period"]); e = float(np.nan_to_num(star["eccentricity"], nan=0.0))
    w = ti_to_omega(star["a_thiele_innes"], star["b_thiele_innes"], star["f_thiele_innes"], star["g_thiele_innes"])
    tp = REF_BTJD + float(star["t_periastron"]); cs = conj_times(P, min(e, 0.95), w, tp)
    sig = {0: (star["sigma_t_c1_1600"], star["sigma_t_c1_3100"]), 1: (star["sigma_t_c2_1600"], star["sigma_t_c2_3100"])}
    dur = duration(P, e)
    sr, prods = search(star["ra"], star["dec"])
    res = dict(source_id=sid, type=star["type"], g=float(star["g"]), period=P, p_eclipse=float(star["p_eclipse"]),
               duration=dur, n_products=len(prods), windows=[], events=[], false=[], status="ok")
    if not prods:
        res["status"] = "no TESS light curve"; return res
    chosen = []
    for p in prods:
        need = False
        for ci, c in enumerate(cs):
            for tc in predicted(P, c, p["t0"] - 60, p["t1"] + 60):
                s = sigma_at(*sig[ci], tc)
                reach = (max(0.5, 2 * s) if s < max_sigma else 3 * s) + 1.0
                if tc + reach > p["t0"] and tc - reach < p["t1"]:
                    need = True
        if need or not np.isfinite(p["t0"]):
            chosen.append(p)
    res["n_downloaded"] = len(chosen)
    for p in chosen:
        try:
            data = download(sr, p["k"])
        except Exception as exc:
            res["windows"].append(dict(sector=p["sector"], error=str(exc)[:80])); continue
        if data is None or len(data[0]) < 100:
            continue
        t, ff, dt = flatten(*data, dur)
        if len(t) < 100:
            continue
        avoid, avoid_hw = [], 0.0
        for ci, c in enumerate(cs):
            for tc in predicted(P, c, t[0] - 3 * max_sigma, t[-1] + 3 * max_sigma):
                s_ = sigma_at(*sig[ci], tc)
                if s_ < max_sigma:
                    avoid.append(tc); avoid_hw = max(avoid_hw, max(0.5, 2 * s_))
        p95_d, p95_b, _ = control_levels(t, ff, dt, 0.5, dur, rng, avoid, avoid_hw)
        for ci, c in enumerate(cs):
            for tc in predicted(P, c, t[0] - 3 * max_sigma, t[-1] + 3 * max_sigma):
                s = sigma_at(*sig[ci], tc)
                if s < max_sigma:   # tier A window
                    hw = max(0.5, 2 * s)
                    if tc + hw < t[0] or tc - hw > t[-1]:
                        continue
                    if hw > 0.5:
                        pd_, pb_, hw_ctrl = control_levels(t, ff, dt, hw, dur, rng, avoid, avoid_hw)
                    else:
                        pd_, pb_, hw_ctrl = p95_d, p95_b, 0.5
                    dip, bump = box_extremes(t, ff, dt, tc, hw, dur)
                    if dip is None:
                        continue
                    wrow = dict(sector=p["sector"], author=p["author"], conj=ci + 1, t_pred=round(tc, 4), sigma_t=round(s, 3), half_window=round(hw, 3),
                                dip_t=round(dip[0], 4), dip_depth=dip[1], dip_snr=dip[2], dip_ctrl=pd_,
                                bump_t=round(bump[0], 4), bump_height=bump[1], bump_snr=bump[2], bump_ctrl=pb_)
                    cd = pd_ if np.isfinite(pd_) else 0.0; cb = pb_ if np.isfinite(pb_) else 0.0
                    wrow["control_half_window"] = hw_ctrl
                    wrow["dip_flag"] = bool(dip[1] >= DIP_MIN and dip[2] >= SNR_MIN and dip[1] > CTRL_FACTOR * cd)
                    near_dip = dip[1] >= DIP_MIN and dip[2] >= SNR_MIN and abs(bump[0] - dip[0]) < 1.5 * dur + 1.0
                    wrow["bump_flag"] = bool(bump[1] >= BUMP_MIN and bump[2] >= SNR_MIN and bump[1] > CTRL_FACTOR * cb and not near_dip)
                    res["windows"].append(wrow)
                    if (wrow["dip_flag"] or wrow["bump_flag"]) and plots:
                        plot_window(sid, p, t, ff, tc, hw, dur, wrow)
                    for _ in range(N_FALSE):   # shifted windows: false-alarm rate
                        tf = tc + rng.uniform(0.0, 1.0) * P
                        # the shifted window must not overlap any true window of either conjunction
                        if min(abs(((tf - c_) + P / 2) % P - P / 2) for c_ in cs) < 2 * hw + dur:
                            continue
                        fd, fb = box_extremes(t, ff, dt, tf, hw, dur)
                        if fd is None:
                            continue
                        fnear = fd[1] >= DIP_MIN and fd[2] >= SNR_MIN and abs(fb[0] - fd[0]) < 1.5 * dur + 1.0
                        res["false"].append(dict(dip_flag=bool(fd[1] >= DIP_MIN and fd[2] >= SNR_MIN and fd[1] > CTRL_FACTOR * cd),
                                                 bump_flag=bool(fb[1] >= BUMP_MIN and fb[2] >= SNR_MIN and fb[1] > CTRL_FACTOR * cb and not fnear)))
        # tier B: single events over the sector, with their offset from the nearest prediction
        if all(sigma_at(*sig[ci], 0.5 * (t[0] + t[-1])) >= max_sigma for ci in (0, 1)):
            for kind in ("dip", "bump"):
                for te, amp, snr in single_events(t, ff, dt, dur, kind):
                    best = None
                    for ci, c in enumerate(cs):
                        for tc in predicted(P, c, te - P, te + P):
                            s = sigma_at(*sig[ci], tc); z = abs(te - tc) / s
                            if best is None or z < best[0]:
                                best = (z, ci + 1, tc, s)
                    res["events"].append(dict(sector=p["sector"], author=p["author"], kind=kind, t=round(te, 4), amplitude=amp, snr=snr,
                                              conj=best[1], t_pred=round(best[2], 3), sigma_t=round(best[3], 2), offset_sigma=round(best[0], 2)))
    return res


def plot_window(sid, p, t, ff, tc, hw, dur, w):
    try:
        import matplotlib; matplotlib.use("Agg"); import matplotlib.pyplot as plt
        os.makedirs(os.path.join(OUT, "plots"), exist_ok=True)
        m = np.abs(t - tc) < hw + 1.5
        fig, ax = plt.subplots(figsize=(7, 3))
        ax.plot(t[m], ff[m], ".", ms=2, color="0.4")
        ax.axvspan(tc - hw, tc + hw, color="tab:blue", alpha=0.08); ax.axvline(tc, color="tab:blue", lw=1)
        if w["dip_flag"]:
            ax.axvline(w["dip_t"], color="tab:red", lw=1, ls="--")
        if w["bump_flag"]:
            ax.axvline(w["bump_t"], color="tab:green", lw=1, ls="--")
        ax.set_title(f"Gaia DR3 {sid}  sector {p['sector']} {p['author']}  conj {w['conj']}  "
                     f"dip {w['dip_depth']*100:.2f}% SNR {w['dip_snr']:.0f}  bump {w['bump_height']*100:.2f}% SNR {w['bump_snr']:.0f}", fontsize=7)
        ax.set_xlabel("BTJD"); ax.set_ylabel("flattened flux")
        fig.tight_layout(); fig.savefig(os.path.join(OUT, "plots", f"{sid}_s{p['sector']}_c{w['conj']}_{int(tc)}.png"), dpi=110); plt.close(fig)
    except Exception:
        pass


# ------------------------------------------------------------------ summary
def summarise(done):
    win = [dict(source_id=r["source_id"], type=r["type"], **w) for r in done for w in r["windows"] if "error" not in w]
    ev = [dict(source_id=r["source_id"], type=r["type"], **e) for r in done for e in r["events"]]
    fa = [f for r in done for f in r["false"]]
    pd.DataFrame(win).to_csv(os.path.join(OUT, "windows.csv"), index=False)
    pd.DataFrame(ev).to_csv(os.path.join(OUT, "events.csv"), index=False)
    flagged = [w for w in win if w["dip_flag"] or w["bump_flag"]]
    pd.DataFrame(flagged).to_csv(os.path.join(OUT, "flagged.csv"), index=False)
    n_fa = len(fa); fd = sum(f["dip_flag"] for f in fa); fb = sum(f["bump_flag"] for f in fa)
    pd.DataFrame([dict(false_windows=n_fa, false_dip_flags=fd, false_bump_flags=fb)]).to_csv(os.path.join(OUT, "false_alarms.csv"), index=False)
    stars_dip = {w["source_id"] for w in win if w["dip_flag"]}; stars_bump = {w["source_id"] for w in win if w["bump_flag"]}
    rate_d = fd / n_fa if n_fa else float("nan"); rate_b = fb / n_fa if n_fa else float("nan")
    near = [e for e in ev if e["offset_sigma"] < 2]
    lines = [f"stars processed: {len(done)} ({sum(r['status'] == 'ok' for r in done)} with TESS data); p_eclipse summed over them: {sum(r['p_eclipse'] for r in done):.1f}",
             f"tier A windows examined: {len(win)}; flagged dips: {sum(w['dip_flag'] for w in win)} on {len(stars_dip)} stars; flagged bumps: {sum(w['bump_flag'] for w in win)} on {len(stars_bump)} stars",
             f"false-alarm rate per window (shifted windows, {n_fa}): dips {rate_d:.3f}, bumps {rate_b:.3f} -> expected false flags among the real windows: dips {rate_d * len(win):.1f}, bumps {rate_b * len(win):.1f}",
             f"tier B single events: {len(ev)} ({sum(e['kind'] == 'dip' for e in ev)} dips, {sum(e['kind'] == 'bump' for e in ev)} bumps); within 2 sigma of a predicted conjunction: {len(near)}",
             "flagged stars (tier A), most significant first:"]
    for w in sorted(flagged, key=lambda x: -max(x["dip_snr"] if x["dip_flag"] else 0, x["bump_snr"] if x["bump_flag"] else 0))[:40]:
        kind = "DIP " if w["dip_flag"] else "BUMP"
        amp = w["dip_depth"] if w["dip_flag"] else w["bump_height"]; snr = w["dip_snr"] if w["dip_flag"] else w["bump_snr"]
        lines.append(f"  {kind} Gaia DR3 {w['source_id']} ({w['type']}) sector {w['sector']} conj {w['conj']}: {amp*100:.2f}% SNR {snr:.0f}, offset {w[('dip_t' if w['dip_flag'] else 'bump_t')] - w['t_pred']:+.2f} d (sigma_t {w['sigma_t']} d)")
    open(os.path.join(OUT, "summary.txt"), "w").write("\n".join(lines) + "\n")
    return lines


class StarTimeout(BaseException):
    """Raised by the watchdog; a BaseException so that the per-sector `except Exception` does not swallow it."""
    pass


def _alarm(signum, frame):
    raise StarTimeout()


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--orbits", default="track3_astrometric_orbits_1.csv"); ap.add_argument("--detail", default="track3_detail.csv")
    ap.add_argument("--max-hours", type=float, default=14.0); ap.add_argument("--max-sigma", type=float, default=10.0)
    ap.add_argument("--max-stars", type=int, default=0); ap.add_argument("--no-plots", action="store_true")
    ap.add_argument("--seed", type=int, default=20261011)
    ap.add_argument("--out", default="pilot_results", help="output folder (default pilot_results)")
    ap.add_argument("--star-timeout", type=int, default=600, help="seconds after which a star is abandoned (default 600)")
    ap.add_argument("--retry-timeouts", action="store_true", help="retry the stars abandoned in a previous run")
    a = ap.parse_args()
    global OUT
    OUT = a.out
    os.makedirs(OUT, exist_ok=True)
    orb = pd.read_csv(a.orbits).drop_duplicates("source_id").set_index("source_id")
    det = pd.read_csv(a.detail)
    det = det[det["n_lightcurves"] > 0].copy()
    for c in ("period", "eccentricity", "t_periastron", "a_thiele_innes", "b_thiele_innes", "f_thiele_innes", "g_thiele_innes"):
        det[c if c != "period" else "period_orb"] = det["source_id"].map(orb[c])
    det = det[det["t_periastron"].notna() & det["a_thiele_innes"].notna()]
    det["sig_best"] = det[["sigma_t_c1_3100", "sigma_t_c2_3100"]].min(axis=1)
    tierA = det[det["sig_best"] < a.max_sigma].sort_values("p_eclipse", ascending=False)
    tierB = det[det["sig_best"] >= a.max_sigma].sort_values("exp_detectable", ascending=False)
    order = pd.concat([tierA, tierB])
    if a.max_stars:
        order = order.head(a.max_stars)
    done_ids = set(); done = []
    path = os.path.join(OUT, "stars.jsonl")
    if os.path.exists(path):
        for line in open(path):
            r = json.loads(line)
            if a.retry_timeouts and str(r.get("status", "")).startswith("timeout"):
                continue
            done.append(r); done_ids.add(r["source_id"])
    print(f"{len(order)} stars to search ({len(tierA)} tier A, {len(tierB)} tier B); {len(done_ids)} already done", flush=True)
    rng = np.random.default_rng(a.seed); t_start = time.time()
    with open(path, "a") as fh:
        for k, (_, star) in enumerate(order.iterrows()):
            if int(star["source_id"]) in done_ids:
                continue
            if (time.time() - t_start) / 3600 > a.max_hours:
                print("time limit reached: stopping cleanly (rerun to continue)", flush=True); break
            signal.signal(signal.SIGALRM, _alarm); signal.alarm(a.star_timeout)
            try:
                r = process(star, rng, a.max_sigma, not a.no_plots)
            except StarTimeout:
                r = dict(source_id=int(star["source_id"]), type=star["type"], g=float(star["g"]), period=float(star["period"]),
                         p_eclipse=float(star["p_eclipse"]), windows=[], events=[], false=[], status=f"timeout after {a.star_timeout} s")
            except Exception as exc:
                r = dict(source_id=int(star["source_id"]), type=star["type"], g=float(star["g"]), period=float(star["period"]),
                         p_eclipse=float(star["p_eclipse"]), windows=[], events=[], false=[], status="error: " + str(exc)[:100])
            finally:
                signal.alarm(0)
            fh.write(json.dumps(r) + "\n"); fh.flush(); done.append(r); done_ids.add(r["source_id"])
            nd = sum(w.get("dip_flag", False) for w in r["windows"]); nb = sum(w.get("bump_flag", False) for w in r["windows"])
            el = (time.time() - t_start) / 60
            print(f"[{len(done_ids)}/{len(order)}] Gaia DR3 {r['source_id']} ({r['type']}, P = {r['period']:.0f} d, p_ecl {r['p_eclipse']:.2f}): "
                  f"{r.get('n_downloaded', 0)} sectors, {len(r['windows'])} windows, {nd} dip / {nb} bump flags, {len(r['events'])} events  [{el:.0f} min]", flush=True)
            if len(done_ids) % 25 == 0:
                summarise(done)
    print("\n".join(summarise(done)))


if __name__ == "__main__":
    main()
