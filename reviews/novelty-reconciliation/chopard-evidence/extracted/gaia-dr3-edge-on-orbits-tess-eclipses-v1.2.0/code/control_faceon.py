#!/usr/bin/env python3
"""The face-on control: the track-3 search run on orbits that cannot eclipse (inclination far from 90 degrees), so that
every flag there is a false alarm by geometry. Compares its flag rates with the real search and with the clean shifted
windows, and recomputes the significance of the real systems with the control rates.

Run from ~/Desktop/piste3 after
    python3 feas_track3_detail.py --far-from-edge-on 30 --sample 2000 --out control_detail.csv
    caffeinate -i python3 pilot_track3.py --detail control_detail.csv --out control_results --max-hours 10
then
    python3 control_faceon.py                      # default: control_detail.csv + control_results/windows.csv
    python3 control_faceon.py --controls control_detail.csv:control_results/windows.csv control2_detail.csv:control2_results/windows.csv
Outputs: control_faceon_summary.txt
"""
import math, os
import numpy as np
import pandas as pd
from scipy.stats import beta

NAMES = {146197633037335168: "HD 284424", 1364450812894866688: "Wolf 1392", 6373132272083904896: "HD 194593",
         1726670143978052992: "BD+85 212", 6360777231720947328: "CD-81 705", 5829438581228161152: "HD 145453",
         4525943082344640256: "HD 170829", 2149342548502408320: "TYC 3908-665-1", 275228582433787904: "TOI-1656"}
L = []


def say(s=""):
    L.append(s); print(s)


def cp(k, n):
    return (0.0 if k == 0 else beta.ppf(0.025, k, n - k + 1)), (1.0 if k == n else beta.ppf(0.975, k + 1, n - k))


def tail(ps, k):
    dist = np.zeros(len(ps) + 1); dist[0] = 1.0
    for p in ps:
        dist[1:] = dist[1:] * (1 - p) + dist[:-1] * p; dist[0] *= 1 - p
    return float(dist[k:].sum())


def flagged(w):
    return w[(w["dip_flag"] == True) & (w["dip_depth"] <= 0.5)]


def main():
    import argparse
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--controls", nargs="+", default=["control_detail.csv:control_results/windows.csv"],
                    help="detail:windows pairs of one or more control runs (merged; a star counts once)")
    a = ap.parse_args()
    Cs, cds = [], []
    for pair in a.controls:
        d_, w_ = pair.split(":")
        Cs.append(pd.read_csv(w_)); cds.append(pd.read_csv(d_).drop_duplicates("source_id"))
    C = pd.concat(Cs, ignore_index=True).drop_duplicates(["source_id", "sector", "author", "conj", "t_pred"])
    cd = pd.concat(cds, ignore_index=True).drop_duplicates("source_id").set_index("source_id")
    R = pd.read_csv("pilot_results/windows.csv")
    # a control star must be unable to eclipse: drop the few whose Monte-Carlo leaves a non-negligible eclipse probability
    bad = set(cd.index[cd["p_eclipse"] > 1e-3]); n_bad = int(C["source_id"].isin(bad).sum())
    C = C[~C["source_id"].isin(bad)].reset_index(drop=True)
    C["hw_bin"] = pd.cut(C["half_window"], [0, 1, 3, 6, 30], labels=["<1 d", "1-3 d", "3-6 d", ">6 d"])
    R["hw_bin"] = pd.cut(R["half_window"], [0, 1, 3, 6, 30], labels=["<1 d", "1-3 d", "3-6 d", ">6 d"])
    say("Face-on control: the track-3 search on orbits that cannot eclipse\n")
    say(f"control: {len(C)} windows on {C['source_id'].nunique()} stars (sample of {len(cd)} orbits far from edge-on; "
        f"{n_bad} windows of stars with p_eclipse > 1e-3 dropped); real search: {len(R)} windows on {R['source_id'].nunique()} stars")
    fc = flagged(C); fr = flagged(R)
    say(f"dip flags: control {len(fc)} ({len(fc) / len(C) * 100:.1f} per cent of windows), real {len(fr)} ({len(fr) / len(R) * 100:.1f} per cent)")
    say(f"bump flags: control {int(C['bump_flag'].sum())} ({C['bump_flag'].mean() * 100:.1f} per cent), real {int(R['bump_flag'].sum())} ({R['bump_flag'].mean() * 100:.1f} per cent)")
    say("\nfalse-alarm rate per window from the control, by pipeline (95 per cent interval):")
    RATE = {}
    for au, g in C.groupby("author"):
        k = len(flagged(g)); n = len(g); lo, hi = cp(k, n); RATE[au] = (k / n, hi)
        say(f"  {au:9s}: {k:3d} of {n:4d} -> {k / n * 100:5.2f} per cent ({lo * 100:.2f}-{hi * 100:.2f})")
    say("by window half-width (all pipelines):")
    for b, g in C.groupby("hw_bin", observed=True):
        k = len(flagged(g)); n = len(g); lo, hi = cp(k, n) if n else (0, 1)
        say(f"  {str(b):6s}: {k:3d} of {n:4d} -> {k / max(n, 1) * 100:5.2f} per cent ({lo * 100:.2f}-{hi * 100:.2f})")
    # concentration on a few stars, and stars with repeated false flags (the look-elsewhere quantity, measured)
    per = flagged(C).groupby("source_id").size().reindex(C["source_id"].unique(), fill_value=0)
    nwin = C.groupby("source_id").size()
    say(f"\nstars with >= 1 false dip flag: {int((per >= 1).sum())} of {len(per)}; with >= 2: {int((per >= 2).sum())}; with >= 3: {int((per >= 3).sum())}")
    multi = nwin[nwin >= 2]
    say(f"among the {len(multi)} control stars with >= 2 windows, {int((per[multi.index] >= 2).sum())} have >= 2 false flags "
        f"(real search: {int((R.groupby('source_id').size() >= 2).sum())} stars with >= 2 windows)")
    if per.sum():
        top = per.sort_values(ascending=False); n10 = max(1, int(np.ceil(0.1 * len(top))))
        say(f"the 10 per cent noisiest control stars give {top.head(n10).sum() / per.sum() * 100:.0f} per cent of the false flags")
    # expected false flags in the real search, using the control rate of each pipeline
    top_rate = max(v[1] for v in RATE.values()) if RATE else 0.1
    exp_mean = sum(RATE.get(a_, (top_rate, top_rate))[0] for a_ in R["author"])
    exp_hi = sum(RATE.get(a_, (top_rate, top_rate))[1] for a_ in R["author"])
    say(f"\nexpected false dip flags in the real search: {exp_mean:.1f} (at the upper rates {exp_hi:.1f}), against {len(fr)} flags: "
        f"excess {len(fr) - exp_mean:.0f}")
    say("\nsignificance of the real systems with the control's rates (Poisson-binomial over their windows): mean rate, upper rate")
    for sid, name in NAMES.items():
        ws = R[R["source_id"] == sid]; k = len(flagged(ws))
        pm = [RATE.get(a_, (top_rate, top_rate))[0] for a_ in ws["author"]]; ph = [RATE.get(a_, (top_rate, top_rate))[1] for a_ in ws["author"]]
        say(f"  {name:15s}: {k} of {len(ws)} windows -> {tail(pm, k):.1e}, {tail(ph, k):.1e}")
    e2 = sum(tail([RATE.get(a_, (top_rate, top_rate))[1] for a_ in g["author"]], 2) for _, g in R.groupby("source_id"))
    say(f"expected number of real-search stars with >= 2 false flags (control rates): {e2:.1f}")
    if os.path.exists("pilot_results/false_alarms_extended.csv"):
        say("\n(for comparison, the clean shifted windows of N2 gave 0 of 754 for SPOC and TESS-SPOC, 3 of 322 for QLP)")
    # depth distribution of the false flags: what a false alarm looks like
    if len(fc):
        q = fc["dip_depth"].quantile([0.5, 0.9]).values * 100
        say(f"\nfalse dips in the control: median depth {q[0]:.2f} per cent, 90th percentile {q[1]:.2f} per cent; "
            f"real flagged dips: median {fr['dip_depth'].median() * 100:.2f} per cent")
    # sample-size rule: which claim does the control support for each system (rule of three with zero flags)
    say("\nsample-size check: control windows needed per pipeline to support a claim, versus windows available")
    avail = {au: int((C["author"] == au).sum()) for au in ("SPOC", "TESS-SPOC", "QLP")}
    say(f"  available: {avail}  (the rule applies to pipelines with no false flag; where the rate is measured, the significance above uses it)")
    for alpha in (1e-3, 1e-5):
        say(f"  claim 'chance below {alpha:.0e}':")
        for sid, name in NAMES.items():
            ws = R[R["source_id"] == sid]; k = len(flagged(ws)); n = len(ws)
            if k == 0:
                continue
            p_req = (alpha / math.comb(n, k)) ** (1.0 / k)
            n_req = math.ceil(3.0 / p_req)
            pipes = sorted(set(flagged(ws)["author"]))
            zero = [a_ for a_ in pipes if len(flagged(C[C["author"] == a_])) == 0]       # pipelines with no false flag in the control
            ok = all(avail.get(a_, 0) >= n_req for a_ in zero) and len(zero) == len(pipes)
            say(f"    {name:15s}: {k} of {n} flags ({', '.join(pipes)}) -> rate must be < {p_req * 100:.2f} per cent -> {n_req} zero-flag windows per pipeline: {'supported' if ok else 'NOT supported'}")
    open("control_faceon_summary.txt", "w").write("\n".join(L) + "\n"); print("\n-> control_faceon_summary.txt")


if __name__ == "__main__":
    main()
