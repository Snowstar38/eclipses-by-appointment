#!/usr/bin/env python3
"""Injection and recovery for the track-3 pilot: completeness of the eclipse search, sensitivity to self-lensing flares,
and an upper limit on compact companions.

Signals are injected into the real TESS light curves of pilot windows in which nothing was flagged, at a time drawn
from the uncertainty of the prediction (t_pred + N(0, sigma_t), kept inside the window) and with a duration of 0.7 to
1.3 times the expected one; the pilot's own detection (pilot_track3.py: flattening, box statistic, control level away
from the predicted windows, thresholds) is then run unchanged. A signal is recovered when its window is flagged with a
time within one duration of the injected one. Completeness is given among the events that fall on data surviving the
flattening (at least half of the event), and including the losses of coverage.
  dips  (eclipses):          depths 0.2, 0.3, 0.5, 1, 2, 5 per cent
  bumps (self-lensing flares): heights 0.05, 0.1, 0.2, 0.5, 1, 5 per cent
Self-lensing: a compact companion of mass Mc on the Gaia orbit magnifies a Sun-like primary (R* = 1 Rsun, M1 = 1 Msun)
by about 2 (R_E / R*)^2 at conjunction, with R_E = sqrt(4 G Mc a / c^2). For a white dwarf (0.6 Msun), a neutron star
(1.4) and a black hole (10), the expected height in each window is compared with the measured sensitivity; the sum over
windows of p_align x p_detect is the number of detections expected if every star had such a companion, and its inverse
(times 3, Poisson 95 per cent) bounds the fraction of such companions, given that no credible flare was found.
Run from ~/Desktop/piste3 after the pilot (uses the lightkurve cache; resumable):
    caffeinate -i python3 inject_recover.py            [--max-windows 300] [--seed 7]
Output: injection/results.csv, injection/summary.txt, injection/completeness.png
"""
import argparse, json, math, os, signal, sys, warnings
import numpy as np
import pandas as pd

warnings.filterwarnings("ignore")
sys.path.insert(0, os.getcwd())
import pilot_track3 as PT

DIPS = (0.002, 0.003, 0.005, 0.01, 0.02, 0.05)
BUMPS = (0.0005, 0.001, 0.002, 0.005, 0.01, 0.05)
G, C, MSUN, RSUN, DAY = 6.674e-11, 2.998e8, 1.989e30, 6.957e8, 86400.0
WINDOW_TIMEOUT = 300        # seconds after which a window is abandoned (a MAST request that hangs)


class WindowTimeout(BaseException):
    pass


def _alarm(signum, frame):
    raise WindowTimeout()


def inject(t, f, t0, dur, amp, kind):
    """Box with 10-per-cent linear ingress and egress."""
    x = np.abs(t - t0) / (dur / 2)
    shape = np.clip((1 - x) / 0.1, 0, 1)
    return f * (1 - amp * shape) if kind == "dip" else f * (1 + amp * shape)


def detect(t, f, t_pred, hw, dur, avoid, avoid_hw, rng):
    tt, ff, dt = PT.flatten(t, f, dur)
    if len(tt) < 100:
        return None
    if hw > 0.5:
        pd_, pb_, _ = PT.control_levels(tt, ff, dt, hw, dur, rng, avoid, avoid_hw)
    else:
        pd_, pb_, _ = PT.control_levels(tt, ff, dt, 0.5, dur, rng, avoid, avoid_hw)
    dip, bump = PT.box_extremes(tt, ff, dt, t_pred, hw, dur)
    if dip is None:
        return None
    cd = pd_ if np.isfinite(pd_) else 0.0; cb = pb_ if np.isfinite(pb_) else 0.0
    dflag = dip[1] >= PT.DIP_MIN and dip[2] >= PT.SNR_MIN and dip[1] > PT.CTRL_FACTOR * cd
    near_dip = dip[1] >= PT.DIP_MIN and dip[2] >= PT.SNR_MIN and abs(bump[0] - dip[0]) < 1.5 * dur + 1.0
    bflag = bump[1] >= PT.BUMP_MIN and bump[2] >= PT.SNR_MIN and bump[1] > PT.CTRL_FACTOR * cb and not near_dip
    return dict(dip_t=dip[0], dip_depth=dip[1], dip_snr=dip[2], dip_flag=bool(dflag),
                bump_t=bump[0], bump_height=bump[1], bump_snr=bump[2], bump_flag=bool(bflag))


def lensing_height(P_days, Mc, M1=1.0, Rstar=1.0):
    a = (G * (M1 + Mc) * MSUN * (P_days * DAY) ** 2 / (4 * math.pi ** 2)) ** (1 / 3)
    RE = math.sqrt(4 * G * Mc * MSUN * a / C ** 2)
    return 2 * (RE / (Rstar * RSUN)) ** 2


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--max-windows", type=int, default=300); ap.add_argument("--seed", type=int, default=7)
    a = ap.parse_args()
    os.makedirs("injection", exist_ok=True)
    win = pd.read_csv("pilot_results/windows.csv")
    det = pd.read_csv("track3_detail.csv").drop_duplicates("source_id").set_index("source_id")
    clean = win[(win["dip_flag"] == False) & (win["bump_flag"] == False)].copy()
    rng = np.random.default_rng(a.seed)
    clean = clean.sample(frac=1.0, random_state=a.seed).head(a.max_windows)
    out_path = "injection/results.csv"
    done = set()
    if os.path.exists(out_path) and os.path.getsize(out_path) > 0:
        prev = pd.read_csv(out_path)
        done = set(zip(prev["source_id"], prev["sector"], prev["t_pred"].round(4)))
    print(f"{len(clean)} clean windows selected; {len(done)} already done", flush=True)
    cache = {}
    first = not (os.path.exists(out_path) and os.path.getsize(out_path) > 0)
    for i, w in enumerate(clean.itertuples()):
        key = (int(w.source_id), int(w.sector), round(float(w.t_pred), 4))
        if key in done:
            continue
        sid = int(w.source_id); s = det.loc[sid]; P = float(s["period"]); dur0 = PT.duration(P)
        print(f"  [{i + 1}/{len(clean)}] Gaia DR3 {sid} S{int(w.sector)}: light curve ...", end="", flush=True)
        signal.signal(signal.SIGALRM, _alarm); signal.alarm(WINDOW_TIMEOUT)
        try:
            if sid not in cache:
                cache = {sid: PT.search(float(s["ra"]), float(s["dec"]))}       # one star at a time in memory
            sr, prods = cache[sid]
            p = [x for x in prods if x["sector"] == int(w.sector)]
            data = PT.download(sr, p[0]["k"]) if p else None
        except WindowTimeout:
            print(f" abandoned after {WINDOW_TIMEOUT} s", flush=True); continue
        except Exception as exc:
            print(f" failed ({str(exc)[:50]})", flush=True); continue
        finally:
            signal.alarm(0)
        print(" injecting", flush=True)
        if data is None:
            continue
        t, f = data
        same = win[(win["source_id"] == sid) & (win["sector"] == int(w.sector))]
        avoid = same["t_pred"].tolist(); avoid_hw = float(same["half_window"].max())
        hw = float(w.half_window); sig = float(w.sigma_t)
        t_kept = PT.flatten(t, f, dur0)[0]                  # times that survive the flattening (edges and gaps removed)
        rows = []
        base = detect(t, f, float(w.t_pred), hw, dur0, avoid, avoid_hw, rng)
        if base is None or base["dip_flag"] or base["bump_flag"]:
            continue
        for kind, amps in (("dip", DIPS), ("bump", BUMPS)):
            for amp in amps:
                t_true = float(w.t_pred) + float(np.clip(rng.normal(0, sig), -0.8 * hw, 0.8 * hw))
                dur = dur0 * rng.uniform(0.7, 1.3)
                r = detect(t, inject(t, f, t_true, dur, amp, kind), float(w.t_pred), hw, dur0, avoid, avoid_hw, rng)
                if r is None:
                    continue
                n_exp = max(1, int(round(dur / np.median(np.diff(np.sort(t))))))
                covered = float(np.sum(np.abs(t_kept - t_true) < dur / 2) / n_exp)   # fraction of the event left after flattening
                flag = r["dip_flag"] if kind == "dip" else r["bump_flag"]
                t_found = r["dip_t"] if kind == "dip" else r["bump_t"]
                rec = bool(flag and abs(t_found - t_true) < max(dur, dur0, 0.1))      # found within one duration
                rows.append(dict(source_id=sid, sector=int(w.sector), author=w.author, t_pred=round(float(w.t_pred), 4), sigma_t=sig,
                                 half_window=hw, period=P, kind=kind, amp=amp, t_true=round(t_true, 4), dur=round(dur, 3),
                                 covered=round(min(covered, 1.0), 2), recovered=rec, flagged=bool(flag), t_error_h=round((t_found - t_true) * 24, 2),
                                 measured=round(r["dip_depth"] if kind == "dip" else r["bump_height"], 5),
                                 snr=round(r["dip_snr"] if kind == "dip" else r["bump_snr"], 1)))
        if rows:
            pd.DataFrame(rows).to_csv(out_path, mode="a", header=first, index=False); first = False
    summarise(out_path, det, win)


def summarise(out_path, det, win):
    if not os.path.exists(out_path) or os.path.getsize(out_path) == 0:
        print("no injection done"); return
    R = pd.read_csv(out_path)
    lines = [f"{R[['source_id', 'sector', 't_pred']].drop_duplicates().shape[0]} windows, {len(R)} injections; "
             f"{(R['covered'] >= 0.5).mean() * 100:.0f} per cent of the injected events fall on data (at least half of the event covered)"]
    Rc = R[R["covered"] >= 0.5]
    comp = {}
    for kind, amps in (("dip", DIPS), ("bump", BUMPS)):
        lines.append(f"\n{kind}s: fraction recovered among events covered by data (all | SPOC | TESS-SPOC | QLP), and including coverage losses")
        for amp in amps:
            g = Rc[(Rc["kind"] == kind) & (Rc["amp"] == amp)]
            ga = R[(R["kind"] == kind) & (R["amp"] == amp)]
            if g.empty:
                continue
            fr = [g["recovered"].mean()] + [g[g["author"] == au]["recovered"].mean() if (g["author"] == au).any() else np.nan for au in ("SPOC", "TESS-SPOC", "QLP")]
            comp[(kind, amp)] = float(ga["recovered"].mean())          # the detection probability used below includes coverage
            lines.append(f"  {amp * 100:5.2f} %: " + " | ".join("  -  " if not np.isfinite(x) else f"{x:5.2f}" for x in fr)
                         + f"   (n = {len(g)}) | with coverage: {ga['recovered'].mean():.2f}")
    d = R[(R["kind"] == "dip") & R["recovered"]]
    if len(d):
        lines.append(f"\ntiming of the recovered eclipses: median |error| {d['t_error_h'].abs().median():.2f} h, 90th percentile {d['t_error_h'].abs().quantile(0.9):.2f} h")
    # self-lensing: expected flare heights, detection probability, upper limits
    wins = win[["source_id", "sector", "t_pred"]].drop_duplicates().copy()          # every window the pilot searched
    wins = wins[wins["source_id"].isin(det.index)]
    wins["period"] = [float(det.loc[s_, "period"]) for s_ in wins["source_id"]]
    amps = np.array(BUMPS); fr_all = np.array([comp.get(("bump", x), np.nan) for x in amps])
    lines.append("\nself-lensing (R* = 1 Rsun, M1 = 1 Msun): expected height and detection probability per window")
    tot = {}
    for label, Mc in (("white dwarf 0.6 Msun", 0.6), ("neutron star 1.4 Msun", 1.4), ("black hole 10 Msun", 10.0)):
        hts = np.array([lensing_height(P, Mc) for P in wins["period"]])
        pdet = np.interp(np.log10(hts), np.log10(amps), np.nan_to_num(fr_all), left=0.0, right=float(np.nan_to_num(fr_all[-1])))
        palign = np.array([float(det.loc[s_, "p_eclipse"]) if s_ in det.index else 0.0 for s_ in wins["source_id"]])
        # the same companion is seen at most once per star: combine its windows
        stars = pd.DataFrame(dict(source_id=wins["source_id"].values, pdet=pdet, palign=palign)).groupby("source_id").agg(
            pdet=("pdet", lambda x: 1 - np.prod(1 - x)), palign=("palign", "first"))
        n_exp = float((stars["pdet"] * stars["palign"]).sum())
        tot[label] = n_exp
        lines.append(f"  {label:24s}: median height {np.median(hts) * 100:.3f} %, median detection probability {np.median(pdet):.2f}; "
                     f"detections expected if every star had one: {n_exp:.2f}" + (f" -> fraction < {3 / n_exp:.2f} (95 %)" if n_exp > 0 else ""))
    lines.append(f"  (over the {len(wins)} windows of {wins['source_id'].nunique()} stars searched by the pilot; detection probability"
                 " from the injections, coverage included; alignment probability p_eclipse from the feasibility step)")
    open("injection/summary.txt", "w").write("\n".join(lines) + "\n")
    print("\n".join(lines))
    try:
        import matplotlib; matplotlib.use("Agg"); import matplotlib.pyplot as plt
        fig, axes = plt.subplots(1, 2, figsize=(7, 2.8))
        for ax, kind, amps_ in ((axes[0], "dip", DIPS), (axes[1], "bump", BUMPS)):
            for au, col in (("SPOC", "tab:blue"), ("TESS-SPOC", "tab:green"), ("QLP", "tab:orange")):
                y = [Rc[(Rc["kind"] == kind) & (Rc["amp"] == x) & (Rc["author"] == au)]["recovered"].mean() for x in amps_]
                ax.plot(np.array(amps_) * 100, y, "o-", color=col, ms=3, label=au)
            ax.set_xscale("log"); ax.set_ylim(-0.03, 1.03); ax.set_xlabel(("eclipse depth" if kind == "dip" else "flare height") + " [%]")
            ax.set_ylabel("fraction recovered"); ax.legend(fontsize=6)
        fig.tight_layout(); fig.savefig("injection/completeness.png", dpi=130); plt.close(fig)
    except Exception:
        pass


if __name__ == "__main__":
    main()
