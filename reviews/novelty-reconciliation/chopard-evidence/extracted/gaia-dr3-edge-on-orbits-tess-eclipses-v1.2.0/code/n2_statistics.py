#!/usr/bin/env python3
"""Every number quoted in the Research Note N2, recomputed from the files of the deposit, with the file it comes from.

Run from the top folder of the deposit (the same layout as the working folder of the search):
    python3 n2_statistics.py
Output: n2_numbers.txt (and the same text on screen). A missing input file only skips the numbers that depend on it.

Definitions used here (the note relies on them):
  * false-alarm rate per window, per pipeline: flags in shifted windows of the same light curves that overlap no real
    search window and contain no real flagged dip (pilot_results/false_alarms_extended.csv), with its 95 per cent upper
    bound (Clopper-Pearson); the false alarms come almost only from QLP;
  * chance that all the flags of a system are false: Poisson-binomial probability of at least k flags among its
    searched windows, each at the upper rate of its pipeline; expected number of stars with >= 2 false flags: the same
    summed over every searched star;
  * separation test: probability that two unrelated dips, each uniformly anywhere in its window (+/- half_window),
    differ by no more than the observed difference of the offsets at the two conjunctions (closest pair in time);
    two-sided;
  * calibration of the Gaia uncertainties: first eclipse at each conjunction of the accepted systems; z = offset /
    sigma_t; the windows truncate z at T = half_window / sigma_t, so the expected scatter for exact uncertainties is
    simulated from normals truncated at each T; the scale factor k of the uncertainties is fitted by maximum likelihood
    of the truncated normal, with the interval where the log-likelihood drops by 0.5;
  * self-lensing bounds: flare height 2 (R_E / R*)^2 for a Sun-like primary (1 Msun, 1 Rsun); detection probability
    interpolated from the injections (coverage included); alignment probability p_eclipse x R* / (R1 + R2) =
    p_eclipse / 1.2 (p_eclipse assumed R1 + R2 = 1.2 Rsun); per star the windows combine as 1 - prod(1 - p);
    bound = 3 / (expected detections), 95 per cent for no detection.
"""
import math, os, re, sys
import numpy as np
import pandas as pd

NAMES = {146197633037335168: "HD 284424", 1364450812894866688: "Wolf 1392", 6373132272083904896: "HD 194593",
         1726670143978052992: "BD+85 212", 6360777231720947328: "CD-81 705", 5829438581228161152: "HD 145453",
         4525943082344640256: "HD 170829", 2149342548502408320: "TYC 3908-665-1", 275228582433787904: "TOI-1656"}
WITHDRAWN = {6373132272083904896, 1726670143978052992}   # version 1.1.0: consistent with chance (two flags each, one QLP)
SEVEN = {k: v for k, v in NAMES.items() if k not in WITHDRAWN}
KNOWN = {596878550087942528: "HD 75767", 2127923409161854848: "KOI-3578"}
BOTH = [146197633037335168, 1364450812894866688, 6373132272083904896, 1726670143978052992]
DROPPED = {5299678829378060288}          # UCAC4 146-021461: pixel-level test inconclusive, not named in the note
out = []
RATE_UP = {}


def tail(ps, k):
    """Poisson-binomial probability of at least k successes."""
    dist = np.zeros(len(ps) + 1); dist[0] = 1.0
    for p in ps:
        dist[1:] = dist[1:] * (1 - p) + dist[:-1] * p; dist[0] *= 1 - p
    return float(dist[k:].sum())


def say(s=""):
    out.append(s); print(s)


def have(*paths):
    miss = [p for p in paths if not os.path.exists(p)]
    if miss:
        say(f"   [skipped: missing {', '.join(miss)}]")
    return not miss


def flagged(win):
    w = win[(win["dip_flag"] == True) & (win["dip_depth"] <= 0.5)].copy()
    w["offset"] = w["dip_t"] - w["t_pred"]
    return w


def main():
    say("Numbers of the Research Note N2, recomputed from the deposit\n")
    far = None
    say("== 2. The search")
    if have("track3_detail.csv"):
        d = pd.read_csv("track3_detail.csv").drop_duplicates("source_id")
        say(f"orbits selected (G < 14, best-fitting inclination within 1 deg of 90): {len(d)}   [track3_detail.csv]")
        say(f"median sigma_i: {d['sigma_i_deg'].median():.1f} deg; median sigma_t of conjunction 1 at BTJD 3100 (2023): "
            f"{d['sigma_t_c1_3100'].median():.0f} d   [track3_detail.csv]")
        say(f"sum of the eclipse probabilities: {d['p_eclipse'].sum():.0f} ({d['p_eclipse'].sum() / len(d) * 100:.1f} per cent of the sample)   [track3_detail.csv]")
    if os.path.exists("pilot_results/summary.txt"):
        s = open("pilot_results/summary.txt").read()
        m = re.search(r"stars processed: (\d+) \((\d+) with TESS data\)", s)
        if m:
            say(f"stars searched: {m.group(1)}, with TESS light curves: {m.group(2)}   [pilot_results/summary.txt]")
    if have("pilot_results/windows.csv"):
        win = pd.read_csv("pilot_results/windows.csv")
        f = flagged(win)
        say(f"search windows: {len(win)} on {win['source_id'].nunique()} stars; flagged dips: {len(f)} on {f['source_id'].nunique()} stars   [pilot_results/windows.csv]")
        from scipy.stats import beta
        if os.path.exists("pilot_results/false_alarms_extended.csv"):
            import pilot_track3 as PT
            fx = pd.read_csv("pilot_results/false_alarms_extended.csv")
            dd_ = pd.read_csv("track3_detail.csv").drop_duplicates("source_id").set_index("source_id")
            fl_ = flagged(win); keep = []
            for r in fx.itertuples():       # the no-overlap rule, also applied to trials made by version 1 of the script
                if r.source_id not in dd_.index:
                    keep.append(False); continue
                P_ = float(dd_.loc[r.source_id, "period"]); du_ = PT.duration(P_); ws_ = win[win["source_id"] == r.source_id]
                dc = np.abs(((r.t_shift - ws_["t_pred"].values) + P_ / 2) % P_ - P_ / 2)
                ok = bool(np.all(dc > r.half_window + ws_["half_window"].values + 2 * du_))
                fd = fl_[fl_["source_id"] == r.source_id]["dip_t"].values
                if ok and len(fd):
                    ok = bool(np.all(np.abs(((r.t_shift - fd) + P_ / 2) % P_ - P_ / 2) > r.half_window + 2 * du_))
                keep.append(ok)
            fx = fx[np.array(keep)]
            RATE_UP.clear()
            for au, g in fx.groupby("author"):
                k, n = int(g["dip_flag"].sum()), len(g); RATE_UP[au] = float(beta.ppf(0.95, k + 1, n - k))
                say(f"false-alarm rate, {au:9s}: {k} of {n} clean shifted windows -> {k / n * 100:.2f} per cent (95 per cent upper {RATE_UP[au] * 100:.2f})   [pilot_results/false_alarms_extended.csv]")
            far = 1.0
            ss = fx[fx["author"].isin(["SPOC", "TESS-SPOC"])]
            say(f"clean shifted windows in total: {len(fx)}; SPOC and TESS-SPOC together: {len(ss)}, with {int(ss['dip_flag'].sum())} false flags   [pilot_results/false_alarms_extended.csv]")
            exp_false = sum(RATE_UP.get(a_, max(RATE_UP.values())) for a_ in win["author"])
            say(f"expected false flags over the {len(win)} windows (upper rates): {exp_false:.0f}, against {len(f)} flags")
    if have("injection/results.csv"):
        R = pd.read_csv("injection/results.csv")
        cov = R["covered"] >= 0.5
        say(f"injected events falling on data: {cov.mean() * 100:.0f} per cent   [injection/results.csv]")
        g = R[cov & (R["kind"] == "dip")].groupby("amp")["recovered"].mean()
        deep = g[g.index >= 0.005]
        say(f"recovery of injected eclipses deeper than 0.5 per cent, windows with data: {deep.min() * 100:.0f} to {deep.max() * 100:.0f} per cent   [injection/results.csv]")
    if os.path.exists("pilot_results/windows.csv"):
        f_ = flagged(pd.read_csv("pilot_results/windows.csv")).sort_values(["source_id", "dip_t"])
        grp = (f_.groupby("source_id")["dip_t"].diff().fillna(1) >= 0.05).cumsum()
        say(f"flags: {len(f_)}; distinct dips (flags of one star within 0.05 d merged; a dip can fall in two overlapping windows): {grp.nunique()}")
    if have("pilot_results/artefact_vetting.csv"):
        v = pd.read_csv("pilot_results/artefact_vetting.csv"); vd = v[v["kind"] == "dip"].sort_values(["source_id", "t"])
        vd = vd[(vd.groupby("source_id")["t"].diff().fillna(1) >= 0.05)]          # one row per distinct dip
        c = vd["verdict"].value_counts()
        say(f"artefact vetting of the {len(vd)} distinct flagged dips: on target {c.get('on target', 0)}, check pixels {c.get('check pixels', 0)}, "
            f"instrumental {c.get('instrumental', 0)}, not reproduced {c.get('not reproduced', 0)}, no data {c.get('no data', 0)}   [pilot_results/artefact_vetting.csv]")
    if have("calib_vetting.csv"):
        cv = pd.read_csv("calib_vetting.csv")
        rem = cv[~cv["verdict"].isin(["no data", "not reproduced"])]
        ok = rem["verdict"].isin(["on target", "check pixels"]).sum()
        say(f"calibration on {len(cv)} known eclipses: {ok} of the {len(rem)} re-measured pass ({ok / len(rem) * 100:.1f} per cent)   [calib_vetting.csv]")

    say("\n== 3. Results")
    if os.path.exists("pilot_results/windows.csv"):
        f = flagged(pd.read_csv("pilot_results/windows.csv"))
        rng = np.random.default_rng(1)
        for sid in BOTH:
            g = f[f["source_id"] == sid]; c1, c2 = g[g["conj"] == 1], g[g["conj"] == 2]
            if c1.empty or c2.empty:
                continue
            pairs = [(abs(a.t_pred - b.t_pred), a, b) for a in c1.itertuples() for b in c2.itertuples()]
            _, a, b = min(pairs, key=lambda x: x[0])
            dd = abs(a.offset - b.offset)
            u1 = rng.uniform(-a.half_window, a.half_window, 400000); u2 = rng.uniform(-b.half_window, b.half_window, 400000)
            say(f"separation test {NAMES[sid]:10s}: offsets {a.offset:+.2f} / {b.offset:+.2f} d, difference {dd:.3f} d ({dd * 1440:.0f} min); "
                f"chance {np.mean(np.abs(u1 - u2) <= dd) * 100:.1f} per cent   [pilot_results/windows.csv]")
        if RATE_UP:
            win = pd.read_csv("pilot_results/windows.csv"); top = max(RATE_UP.values())
            for sid, name in NAMES.items():
                ws_ = win[win["source_id"] == sid]; k = int((f["source_id"] == sid).sum())
                ps = [RATE_UP.get(a_, top) for a_ in ws_["author"]]
                auth = f[f["source_id"] == sid]["author"].value_counts().to_dict()
                say(f"chance that all flags are false, {name:15s}: {k} of {len(ws_)} windows {auth} -> {tail(ps, k):.1e}")
            e2 = sum(tail([RATE_UP.get(a_, top) for a_ in g["author"]], 2) for _, g in win.groupby("source_id"))
            say(f"expected number of stars with >= 2 false flags over the whole search (upper rates): {e2:.1f}")
        rows = []
        for sid in list(SEVEN) + list(KNOWN):                   # version 1.1.0: the two withdrawn systems are left out
            g = f[f["source_id"] == sid]
            for conj, gc in g.groupby("conj"):
                r = gc.sort_values("t_pred").iloc[0]
                rows.append((r["offset"] / r["sigma_t"], r["half_window"] / r["sigma_t"]))
        z = np.array([x[0] for x in rows]); T = np.array([x[1] for x in rows])
        sims = []
        for _ in range(20000):
            x = []
            for t_ in T:
                while True:
                    v_ = rng.normal()
                    if abs(v_) < t_:
                        x.append(v_); break
            sims.append(np.std(x, ddof=1))
        from scipy.stats import norm
        nll = lambda k: -np.sum(norm.logpdf(z / k) - np.log(k) - np.log(2 * norm.cdf(T / k) - 1))
        ks = np.linspace(0.4, 4, 1200); L = np.array([nll(k_) for k_ in ks]); kh = ks[np.argmin(L)]; ci = ks[L <= L.min() + 0.5]
        say(f"calibration: {len(z)} conjunctions; std of offset/sigma {np.std(z, ddof=1):.2f}, expected within the windows if exact "
            f"{np.mean(sims):.2f} +/- {np.std(sims):.2f}; scale factor {kh:.2f} (68 per cent: {ci.min():.2f}-{ci.max():.2f})   [pilot_results/windows.csv]")
    if have("diff_images/results.csv"):
        di = pd.read_csv("diff_images/results.csv")
        di = di[di["source_id"].isin(SEVEN) & ~di["source_id"].isin(DROPPED)]
        test = di[di["verdict"].isin(["on target", "unclear", "off target"])]
        say(f"difference images: on target in {int((test['verdict'] == 'on target').sum())} of the {len(test)} sectors that can be tested   [diff_images/results.csv]")

    # face-on control (version 1.1.0 of the deposit): orbits that cannot eclipse, searched identically
    cw = next((f for f in ("control/control_results/windows.csv", "control_results/windows.csv") if os.path.exists(f)), None)
    if cw and os.path.exists("pilot_results/windows.csv"):
        say("\n== 3b. Face-on control (orbits over 30 deg from edge-on, searched identically)")
        from scipy.stats import beta
        C = pd.read_csv(cw); fcn = flagged(C); win = pd.read_csv("pilot_results/windows.csv"); f = flagged(win)
        say(f"control windows: {len(C)} on {C['source_id'].nunique()} stars; dip flags {len(fcn)}; bump flags {int(C['bump_flag'].sum())}   [{cw}]")
        CTRL = {}
        for au, g in C.groupby("author"):
            k, n = len(flagged(g)), len(g); CTRL[au] = (k, n)
            say(f"control false-alarm rate, {au:9s}: {k} of {n} windows -> {k / n * 100:.1f} per cent (95 per cent upper {beta.ppf(0.95, k + 1, n - k) * 100:.1f})")
        for au in ("SPOC", "TESS-SPOC", "QLP"):
            n = int((win["author"] == au).sum()); k = int((f["author"] == au).sum())
            say(f"real search, {au:9s}: {k} of {n} windows flagged ({k / max(n, 1) * 100:.1f} per cent)")
        up = lambda k, n: float(beta.ppf(0.95, k + 1, n - k))
        ctrl_only = {au: up(*CTRL[au]) for au in CTRL}
        nss = sum(n for au, (k, n) in CTRL.items() if au in ("SPOC", "TESS-SPOC")) + (754 if os.path.exists("pilot_results/false_alarms_extended.csv") else 0)
        kss = sum(k for au, (k, n) in CTRL.items() if au in ("SPOC", "TESS-SPOC"))
        combined = {"SPOC": up(kss, nss), "TESS-SPOC": up(kss, nss), "QLP": ctrl_only.get("QLP", 0.3)}
        say(f"combined SPOC and TESS-SPOC (control + shifted windows): {kss} of {nss} -> upper {combined['SPOC'] * 100:.2f} per cent")
        for lab, rt in (("control only", ctrl_only), ("combined", combined)):
            top = max(rt.values())
            for sid, name in NAMES.items():
                ws_ = win[win["source_id"] == sid]; k = int((f["source_id"] == sid).sum())
                say(f"  {lab:12s} {name:15s}: {k} of {len(ws_)} -> {tail([rt.get(a_, top) for a_ in ws_['author']], k):.1e}")
            e2 = sum(tail([rt.get(a_, top) for a_ in g["author"]], 2) for _, g in win.groupby("source_id"))
            say(f"  {lab:12s} expected false flags (upper rates) {sum(rt.get(a_, top) for a_ in win['author']):.0f} of {len(f)}; stars with >= 2 false flags expected {e2:.1f}")
        for sid in SEVEN:
            ws_ = win[(win["source_id"] == sid) & win["author"].isin(["SPOC", "TESS-SPOC"])]; k = int(len(flagged(ws_)))
            if k < int((f["source_id"] == sid).sum()):
                say(f"  {SEVEN[sid]} on SPOC and TESS-SPOC alone: {k} of {len(ws_)} -> {tail([combined['SPOC']] * len(ws_), k):.1e} (combined rate)")
        mean = {au: k / n for au, (k, n) in CTRL.items()}
        say(f"expected false flags at the control's mean rates: {sum(mean.get(a_, 0) for a_ in win['author']):.0f} of {len(f)}")
    say("\n== 4. Discussion")
    if have("injection/results.csv", "pilot_results/windows.csv", "track3_detail.csv"):
        R = pd.read_csv("injection/results.csv")
        win = pd.read_csv("pilot_results/windows.csv"); d = pd.read_csv("track3_detail.csv").drop_duplicates("source_id").set_index("source_id")
        amps = np.array(sorted(R[R["kind"] == "bump"]["amp"].unique()))
        fr = np.array([R[(R["kind"] == "bump") & (R["amp"] == a_)]["recovered"].mean() for a_ in amps])
        G, C, MS, RS, DAY = 6.674e-11, 2.998e8, 1.989e30, 6.957e8, 86400.0
        w2 = win[["source_id", "sector", "t_pred"]].drop_duplicates()
        w2 = w2[w2["source_id"].isin(d.index)]
        for label, Mc in (("white dwarf 0.6 Msun", 0.6), ("neutron star 1.4 Msun", 1.4), ("black hole 10 Msun", 10.0)):
            per = np.array([float(d.loc[s_, "period"]) for s_ in w2["source_id"]])
            a = (G * (1 + Mc) * MS * (per * DAY) ** 2 / (4 * math.pi ** 2)) ** (1 / 3)
            h = 2 * (4 * G * Mc * MS * a / C ** 2) / RS ** 2
            pdet = np.interp(np.log10(h), np.log10(amps), fr, left=0.0, right=float(fr[-1]))
            st = pd.DataFrame(dict(s=w2["source_id"].values, p=pdet)).groupby("s")["p"].apply(lambda x: 1 - np.prod(1 - x))
            palign = np.array([float(d.loc[s_, "p_eclipse"]) / 1.2 for s_ in st.index])
            n_exp = float((st.values * palign).sum())
            say(f"self-lensing, {label:22s}: expected detections if every star had one {n_exp:.1f} -> fraction below {3 / n_exp * 100:.0f} per cent (95 per cent)   [injection/results.csv]")
    if have("predictions/eclipse_predictions.csv"):
        p = pd.read_csv("predictions/eclipse_predictions.csv")
        ids = list(SEVEN) + list(KNOWN)
        nxt = p[p["source_id"].isin(ids)].sort_values("mid_utc").groupby("source_id").head(3)
        s = nxt.groupby("source_id")["sigma_min"].max()
        say(f"next eclipses predicted to better than two hours for {int((s < 120).sum())} of the {len(s)} systems   [predictions/eclipse_predictions.csv]")
        for sid, v_ in s.sort_values().items():
            say(f"   {(NAMES.get(sid) or KNOWN.get(sid)):15s} {v_:8.1f} min")
    open("n2_numbers.txt", "w").write("\n".join(out) + "\n")
    print("\n-> n2_numbers.txt")


if __name__ == "__main__":
    main()
