#!/usr/bin/env python3
"""False-alarm rate of the track-3 search, measured on thousands of shifted windows instead of one per star.

For every searched window of pilot_results/windows.csv, the pilot's detection (inject_recover.detect, i.e. the
pilot's flattening, box statistic, control level and thresholds) is run again at --k random times of the same light
curve, with the same window half-width. A shifted window is kept only if it overlaps none of the star's real search
windows (both conjunctions, every cycle; 2 durations of margin) and contains none of its real flagged dips, so that no
real eclipse can fall in it, and if data cover at least half of it. (Version 1 only kept the shifted centre away
from the predicted times, so that real eclipses offset from their predictions leaked into the trials.) A flag there is a false alarm. Windows as wide as their sector
cannot be shifted and give no trial.
Run from ~/Desktop/piste3 (light curves from the lightkurve cache; resumable):
    caffeinate -i python3 false_alarm_rate.py --k 10
Output: pilot_results/false_alarms_extended.csv (one row per trial) and the rate with its 95 per cent interval.
"""
import argparse, os, signal, sys, warnings
import numpy as np
import pandas as pd

warnings.filterwarnings("ignore")
sys.path.insert(0, os.getcwd())
import pilot_track3 as PT
from inject_recover import detect

TIMEOUT = 300


class Timeout(BaseException):
    pass


def _alarm(signum, frame):
    raise Timeout()


def clopper_pearson(k, n, cl=0.95):
    from scipy.stats import beta
    a = (1 - cl) / 2
    lo = 0.0 if k == 0 else beta.ppf(a, k, n - k + 1)
    hi = 1.0 if k == n else beta.ppf(1 - a, k + 1, n - k)
    return lo, hi


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--k", type=int, default=10); ap.add_argument("--seed", type=int, default=11)
    a = ap.parse_args()
    win = pd.read_csv("pilot_results/windows.csv")
    det = pd.read_csv("track3_detail.csv").drop_duplicates("source_id").set_index("source_id")
    out = "pilot_results/false_alarms_extended.csv"
    done = set()
    if os.path.exists(out) and os.path.getsize(out) > 0:
        prev = pd.read_csv(out); done = set(zip(prev["source_id"], prev["sector"], prev["t_pred"].round(4)))
    first = not (os.path.exists(out) and os.path.getsize(out) > 0)
    rng = np.random.default_rng(a.seed)
    wins = win.drop_duplicates(["source_id", "sector", "t_pred"])
    print(f"{len(wins)} windows x {a.k} shifts; {len(done)} windows already done", flush=True)
    cache = {}
    for i, w in enumerate(wins.itertuples()):
        key = (int(w.source_id), int(w.sector), round(float(w.t_pred), 4))
        if key in done:
            continue
        sid = int(w.source_id)
        if sid not in det.index:
            continue
        P = float(det.loc[sid, "period"]); dur = PT.duration(P); hw = float(w.half_window)
        ws_ = win[win["source_id"] == sid]
        conj_times = ws_["t_pred"].to_numpy(); conj_hw = ws_["half_window"].to_numpy()   # both conjunctions, any cycle (mod P)
        dips = ws_[(ws_["dip_flag"] == True) & (ws_["dip_depth"] <= 0.5)]["dip_t"].to_numpy()
        print(f"  [{i + 1}/{len(wins)}] Gaia DR3 {sid} S{int(w.sector)}: light curve ...", end="", flush=True)
        signal.signal(signal.SIGALRM, _alarm); signal.alarm(TIMEOUT)
        try:
            if sid not in cache:
                cache = {sid: PT.search(float(det.loc[sid, "ra"]), float(det.loc[sid, "dec"]))}
            sr, prods = cache[sid]
            p = [x for x in prods if x["sector"] == int(w.sector)]
            data = PT.download(sr, p[0]["k"]) if p else None
        except Timeout:
            print(" abandoned", flush=True); continue
        except Exception as exc:
            print(f" failed ({str(exc)[:40]})", flush=True); continue
        finally:
            signal.alarm(0)
        if data is None:
            print(" no data", flush=True); continue
        t, f = data
        rows = []
        tries = 0
        while len(rows) < a.k and tries < 30 * a.k:
            tries += 1
            ts = float(rng.uniform(t.min(), t.max()))                     # anywhere in the same light curve ...
            dist = np.abs(((ts - conj_times) + P / 2) % P - P / 2)
            if np.any(dist < hw + conj_hw + 2 * dur):                       # ... never overlapping a real search window
                continue
            if len(dips):
                dd = np.abs(((ts - dips) + P / 2) % P - P / 2)
                if np.any(dd < hw + 2 * dur):                               # ... nor containing a real flagged dip
                    continue
            inside = (t > ts - hw) & (t < ts + hw)
            if inside.sum() < 0.5 * min(2 * hw, t.max() - t.min()) / np.median(np.diff(t)):
                continue                                                    # and with data over most of the window
            r = detect(t, f, ts, hw, dur, list(conj_times), hw, rng)
            if r is None:
                continue
            rows.append(dict(source_id=sid, sector=int(w.sector), author=w.author, t_pred=round(float(w.t_pred), 4),
                             t_shift=round(ts, 4), half_window=hw, dip_flag=r["dip_flag"], bump_flag=r["bump_flag"],
                             dip_depth=round(r["dip_depth"], 5), dip_snr=round(r["dip_snr"], 1)))
        if rows:
            pd.DataFrame(rows).to_csv(out, mode="a", header=first, index=False); first = False
        print(f" {len(rows)} shifted windows", flush=True)
    R = pd.read_csv(out)
    for kind in ("dip", "bump"):
        k = int(R[f"{kind}_flag"].sum()); n = len(R); lo, hi = clopper_pearson(k, n)
        print(f"{kind}s: {k} false flags in {n} shifted windows -> rate {k / n * 100:.2f} per cent (95 per cent: {lo * 100:.2f}-{hi * 100:.2f})")
    print(f"-> {out}")


if __name__ == "__main__":
    main()
