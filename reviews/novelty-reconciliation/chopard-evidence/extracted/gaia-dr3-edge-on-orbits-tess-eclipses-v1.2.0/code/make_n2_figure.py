"""Figure of the Research Note N2 (version 4): what the note claims, shown directly.
  (a), (c) the eclipses of HD 284424 and Wolf 1392 at both conjunctions, stacked by date and coloured by conjunction,
           each aligned on its own predicted time (dotted line at zero);
  (b)      O-C of HD 284424: offset of every eclipse from the Gaia prediction against the date, with the propagated
           1- and 2-sigma envelopes of the prediction: both conjunctions drift together, inside the envelope;
  (d)      every accepted system: offset in units of its propagated uncertainty against the date, with the 1- and
           2-sigma bands: the Gaia conjunction times are as accurate as their errors say;
  (e)      one eclipse of each of the other seven systems, aligned on its minimum and scaled to its depth;
  (f)      fraction of injected eclipses and flares recovered (windows with data; injection/results.csv), with the
           flare heights expected from a white dwarf, a neutron star and a black hole on these orbits.
Run from ~/Desktop/piste3 (needs pilot_results/windows.csv, track3_detail.csv, pilot_track3.py, the lightkurve cache):
    python3 make_n2_figure.py
Output: n2_figure.pdf and n2_figure.png."""
import os, sys, warnings
import numpy as np, pandas as pd
warnings.filterwarnings("ignore")
sys.path.insert(0, os.getcwd())
from pilot_track3 import flatten, duration

TOP = (146197633037335168, "HD 284424")
BOTTOM = (1364450812894866688, "Wolf 1392")
ACCEPTED = {146197633037335168: "HD 284424", 1364450812894866688: "Wolf 1392", 6360777231720947328: "CD-81 705", 5829438581228161152: "HD 145453",
            4525943082344640256: "HD 170829", 2149342548502408320: "TYC 3908-665-1", 275228582433787904: "TOI-1656",
            596878550087942528: "HD 75767 (known)", 2127923409161854848: "KOI-3578 (known)"}
C1, C2 = "#1b4f8f", "#b2182b"          # house style of the survey paper (P2)
ORANGE = "#c77c11"


def binned(t, f, width):
    edges = np.arange(t.min(), t.max() + width, width); idx = np.digitize(t, edges)
    keep = [i for i in np.unique(idx) if (idx == i).sum() >= 2]
    return np.array([t[idx == i].mean() for i in keep]), np.array([np.median(f[idx == i]) for i in keep])


def flagged(win, sid):
    g = win[(win["source_id"] == sid) & (win["dip_flag"] == True) & (win["dip_depth"] <= 0.5)].copy()
    g["offset"] = g["dip_t"] - g["t_pred"]
    return g.drop_duplicates(subset=["conj", "sector"]).sort_values("t_pred")


def lightcurves(ax, sid, name, win, det, lk, SkyCoord, u, Time):
    d = det.loc[sid]; dur = duration(float(d["period"]))
    g = flagged(win, sid)
    sr = lk.search_lightcurve(SkyCoord(d["ra"] * u.deg, d["dec"] * u.deg), radius=10 * u.arcsec, mission="TESS")
    tab = sr.table
    lo = min(g["offset"].min(), 0) - 2.0 * dur; hi = max(g["offset"].max(), 0) + 2.0 * dur
    curves = []
    for _, w in g.iterrows():
        ks = []
        if "t_min" in tab.colnames:
            ks = [k for k in range(len(sr)) if str(tab["author"][k]) == w["author"]
                  and float(tab["t_min"][k]) - 56999.5 - 1 < w["dip_t"] < float(tab["t_max"][k]) - 56999.5 + 1]
        if not ks:
            ks = [k for k in range(len(sr)) if int(tab["sequence_number"][k]) == int(w["sector"]) and str(tab["author"][k]) == w["author"]]
        if not ks:
            continue
        lc = sr[ks[0]].download(quality_bitmask="default").remove_nans().normalize()
        t, f = flatten(np.asarray(lc.time.value, float), np.asarray(lc.flux.value, float), dur)[:2]
        x = t - w["t_pred"]; m = (x > lo) & (x < hi)
        if m.sum() < 10:
            continue
        xb, fb = binned(x[m], f[m], max(dur / 15, 10 / 1440))
        curves.append((w, x[m], f[m], xb, fb, float(np.median(fb) - np.min(fb))))
    depth = max(c[5] for c in curves) if curves else 0.01
    step = 1.25 * depth
    for j, (w, x, f, xb, fb, dep) in enumerate(curves):
        col = C1 if int(w["conj"]) == 1 else C2; y0 = -j * step
        ax.plot(x, f + y0, ".", ms=0.7, color=col, alpha=0.18, rasterized=True)
        ax.plot(xb, fb + y0, "-", lw=0.9, color=col)
        date = Time(w["t_pred"] + 2457000, format="jd").datetime.strftime("%Y %b")
        ax.text(lo + 0.02 * (hi - lo), 1 + y0 + 0.12 * step, f"{date}, conj. {int(w['conj'])}", fontsize=6, color=col, va="bottom")
        near = np.abs(xb - w["offset"]) < 1.0 * dur
        xm = xb[near][np.argmin(fb[near])] if near.any() else w["offset"]          # the real minimum, not the box centre
        ax.plot([xm] * 2, [1 + y0 - 1.05 * dep, 1 + y0 - 1.25 * dep], "-", color=col, lw=0.8)
    ax.axvline(0, color="0.4", lw=0.7, ls=":")
    ax.set_xlim(lo, hi); ax.set_ylim(1 - (len(curves) - 1) * step - 1.45 * depth, 1 + 0.55 * step)
    ax.set_xlabel("time from the predicted conjunction [d]"); ax.set_ylabel("flux + offset")
    ax.set_title(name)


def oc_one(ax, sid, name, win, det, Time):
    g = flagged(win, sid); d = det.loc[sid]
    t = np.linspace(min(g["t_pred"].min(), 1300) - 50, max(g["t_pred"].max(), 3700) + 50, 300)
    for conj, col in ((1, C1), (2, C2)):
        s16, s31 = float(d[f"sigma_t_c{conj}_1600"]), float(d[f"sigma_t_c{conj}_3100"])
        sig = np.clip(s16 + (s31 - s16) * (t - 1600) / 1500, 0.02, None)
        if conj == 1:
            ax.fill_between(t, -2 * sig, 2 * sig, color="0.9", lw=0, label="Gaia prediction, 2$\\sigma$")
            ax.fill_between(t, -sig, sig, color="0.78", lw=0, label="1$\\sigma$")
    for conj, col, mk in ((1, C1, "o"), (2, C2, "s")):
        h = g[g["conj"] == conj]
        ax.plot(h["t_pred"], h["offset"], mk, color=col, ms=4.5, mec="white", mew=0.5, label=f"conjunction {conj}", zorder=3)
    if len(g) >= 2:
        c = np.polyfit(g["t_pred"], g["offset"], 1)
        ax.plot(t, np.polyval(c, t), "-", color="0.3", lw=0.6, zorder=2, label="common drift")
    ax.axhline(0, color="0.4", lw=0.7, ls=":")
    yrs = [2019, 2021, 2023, 2025]
    ax.set_xticks([Time(f"{y}-01-01").jd - 2457000 for y in yrs]); ax.set_xticklabels([str(y) for y in yrs])
    ax.set_xlim(t.min(), t.max()); ax.set_ylabel("eclipse $-$ prediction [d]")
    ax.set_title(f"{name}: offsets from the Gaia prediction")
    ax.legend(fontsize=5.5, loc="upper left", frameon=False, ncol=2)


def oc_all(ax, win, Time):
    rows = []
    for sid, name in ACCEPTED.items():
        g = flagged(win, sid)
        for _, w in g.iterrows():
            rows.append((w["t_pred"], w["offset"] / w["sigma_t"], int(w["conj"]), name, w["half_window"] / w["sigma_t"]))
    R = pd.DataFrame(rows, columns=["t", "z", "conj", "name", "T"])
    ax.axhspan(-2, 2, color="0.9", lw=0); ax.axhspan(-1, 1, color="0.78", lw=0)
    for conj, col, mk in ((1, C1, "o"), (2, C2, "s")):
        h = R[R["conj"] == conj]
        ax.plot(h["t"], h["z"], mk, color=col, ms=3.5, mec="white", mew=0.4, alpha=0.9, label=f"conjunction {conj}")
    first = R.sort_values("t").groupby(["name", "conj"]).head(1)
    # what the scatter would be if Gaia's uncertainties were exact, given that each window ends at T = hw / sigma
    rng = np.random.default_rng(1); sims = []
    for _ in range(4000):
        x = []
        for T in first["T"]:
            while True:
                v = rng.normal()
                if abs(v) < T:
                    x.append(v); break
        sims.append(np.std(x, ddof=1))
    ax.text(0.98, 0.95, f"{R['name'].nunique()} systems, {len(R)} eclipses\nfirst eclipse per conjunction: std {first['z'].std(ddof=1):.2f}\n"
            f"expected within the windows if exact: {np.mean(sims):.2f} $\\pm$ {np.std(sims):.2f}",
            transform=ax.transAxes, ha="right", va="top", fontsize=6)
    yrs = [2019, 2021, 2023, 2025]
    ax.set_xticks([Time(f"{y}-01-01").jd - 2457000 for y in yrs]); ax.set_xticklabels([str(y) for y in yrs])
    ax.axhline(0, color="0.4", lw=0.7, ls=":"); ax.set_ylim(-3.5, 3.5)
    ax.set_ylabel("(eclipse $-$ prediction) / $\\sigma_{\\rm Gaia}$"); ax.set_title("All systems")
    ax.legend(fontsize=5.5, loc="lower left", frameon=False)


GALLERY = [(2149342548502408320, "TYC 3908-665-1"), (6360777231720947328, "CD$-$81 705"), (4525943082344640256, "HD 170829"), (5829438581228161152, "HD 145453"),
           (275228582433787904, "TOI-1656")]


def gallery(ax, win, det, lk, SkyCoord, u):
    import matplotlib
    """One eclipse per system: the best-covered one (at least 80 per cent of the eclipse and a baseline on both sides),
    with the fastest cadence, not merely the most significant."""
    for j, (sid, name) in enumerate(GALLERY):
        g = flagged(win, sid)
        if g.empty:
            continue
        d = det.loc[sid]; P = float(d["period"]); dur = duration(P)
        try:
            sr = lk.search_lightcurve(SkyCoord(d["ra"] * u.deg, d["dec"] * u.deg), radius=10 * u.arcsec, mission="TESS")
            tab = sr.table
        except Exception:
            continue
        best = None
        for _, w in g.iterrows():
            ks = [k for k in range(len(sr)) if str(tab["author"][k]) == w["author"]
                  and float(tab["t_min"][k]) - 56999.5 - 1 < w["dip_t"] < float(tab["t_max"][k]) - 56999.5 + 1] if "t_min" in tab.colnames else []
            if not ks:
                ks = [k for k in range(len(sr)) if int(tab["sequence_number"][k]) == int(w["sector"]) and str(tab["author"][k]) == w["author"]]
            if not ks:
                continue
            try:
                lc = sr[ks[0]].download(quality_bitmask="default").remove_nans().normalize()
            except Exception:
                continue
            t, f = flatten(np.asarray(lc.time.value, float), np.asarray(lc.flux.value, float), dur)[:2]
            if len(t) < 20:
                continue
            cad = float(np.median(np.diff(np.sort(t))))
            inn = np.abs(t - w["dip_t"]) < dur / 2
            cover = inn.sum() / max(dur / cad, 1)
            left = ((t - w["dip_t"] < -0.8 * dur) & (t - w["dip_t"] > -2.5 * dur)).sum() * cad
            right = ((t - w["dip_t"] > 0.8 * dur) & (t - w["dip_t"] < 2.5 * dur)).sum() * cad
            ok = cover >= 0.8 and left >= 0.5 * dur and right >= 0.5 * dur
            score = (ok, -cad, float(w["dip_snr"]))
            if best is None or score > best[0]:
                best = (score, t, f, w, cad)
        if best is None:
            continue
        _, t, f, w, cad = best
        m = np.abs(t - w["dip_t"]) < 2.5 * dur
        xb, fb = binned(t[m], f[m], max(dur / 15, 1.6 * cad, 10 / 1440))
        if len(fb) < 5:
            continue
        near = np.abs(xb - w["dip_t"]) < dur
        tmin = xb[near][np.argmin(fb[near])] if near.any() else w["dip_t"]
        side = np.abs(xb - tmin) > 0.8 * dur
        base = np.median(fb[side]) if side.any() else 1.0
        depth = base - fb[near].min() if near.any() else base - fb.min()
        if depth <= 0:
            continue
        x = (t[m] - tmin) * 24; y = (f[m] - base) / depth
        y0 = -1.6 * j
        ax.plot(x, y + y0, ".", ms=0.6, color="0.55", alpha=0.25, rasterized=True)
        ax.plot((xb - tmin) * 24, (fb - base) / depth + y0, "-", lw=0.9, color=C1 if int(w["conj"]) == 1 else C2)
        ax.text(29, y0 + 0.12, f"{name}, {P:.1f} d, {depth * 100:.2f}%", ha="right", va="bottom", fontsize=5.5)
    ax.set_xlim(-30, 30); ax.set_ylim(-1.6 * (len(GALLERY) - 1) - 1.4, 0.75)
    ax.set_yticks([]); ax.yaxis.set_minor_locator(matplotlib.ticker.NullLocator())
    ax.set_xlabel("hours from the eclipse minimum"); ax.set_ylabel("flux, scaled to each depth")
    ax.set_title("The other systems: one eclipse each")


def completeness(ax):
    import math
    if not os.path.exists("injection/results.csv"):
        ax.text(0.5, 0.5, "injection/results.csv missing", transform=ax.transAxes, ha="center"); return
    R = pd.read_csv("injection/results.csv"); R = R[R["covered"] >= 0.5]
    for kind, col, lab in (("dip", C1, "eclipses"), ("bump", ORANGE, "self-lensing flares")):
        g = R[R["kind"] == kind].groupby("amp")["recovered"].agg(["mean", "size"]).reset_index()
        err = np.sqrt(g["mean"] * (1 - g["mean"]) / g["size"])
        ax.errorbar(g["amp"] * 100, g["mean"], yerr=err, fmt="o-", ms=3, lw=0.9, color=col, capsize=1.5, label=lab)
    G_, C_, MS, RS, DAY = 6.674e-11, 2.998e8, 1.989e30, 6.957e8, 86400.0
    for Mc, lab in ((0.6, "WD"), (1.4, "NS"), (10.0, "BH")):
        P = 90.0; a = (G_ * (1 + Mc) * MS * (P * DAY) ** 2 / (4 * math.pi ** 2)) ** (1 / 3)
        h = 2 * (4 * G_ * Mc * MS * a / C_ ** 2) / RS ** 2 * 100
        ax.axvline(h, color="0.6", lw=0.6, ls="--"); ax.text(h, 1.03, lab, fontsize=5.5, color="0.4", ha="center", va="bottom")
    ax.set_xscale("log"); ax.set_ylim(-0.03, 1.1); ax.set_xlabel("injected depth or height [%]")
    ax.set_ylabel("fraction recovered"); ax.legend(fontsize=5.5, loc="lower right", frameon=False)
    ax.set_title("Recovery of injected signals (windows with data)")


def main():
    import matplotlib; matplotlib.use("Agg"); import matplotlib.pyplot as plt
    import lightkurve as lk
    from astropy.coordinates import SkyCoord
    from astropy.time import Time
    import astropy.units as u
    plt.rcParams.update({   # house style of the survey paper (P2): serif STIX, thin lines, ticks inside on four sides
        "font.family": "serif", "font.serif": ["STIXGeneral", "DejaVu Serif", "Times New Roman"], "mathtext.fontset": "stix",
        "font.size": 7.5, "axes.labelsize": 7.5, "axes.titlesize": 7.5, "legend.fontsize": 6.3, "xtick.labelsize": 6.8,
        "ytick.labelsize": 6.8, "axes.linewidth": 0.5, "lines.linewidth": 0.8, "lines.markersize": 3.0, "patch.linewidth": 0.5,
        "xtick.direction": "in", "ytick.direction": "in", "xtick.top": True, "ytick.right": True,
        "xtick.minor.visible": True, "ytick.minor.visible": True, "xtick.major.size": 3.0, "xtick.minor.size": 1.6,
        "ytick.major.size": 3.0, "ytick.minor.size": 1.6, "xtick.major.width": 0.5, "xtick.minor.width": 0.35,
        "ytick.major.width": 0.5, "ytick.minor.width": 0.35, "legend.frameon": False, "legend.handlelength": 1.6,
        "pdf.fonttype": 42, "savefig.dpi": 300, "axes.formatter.use_mathtext": True, "errorbar.capsize": 0})
    win = pd.read_csv("pilot_results/windows.csv")
    det = pd.read_csv("track3_detail.csv").drop_duplicates("source_id").set_index("source_id")
    fig, ax = plt.subplots(3, 2, figsize=(7.09, 7.4), gridspec_kw=dict(width_ratios=[1, 1.15]))
    lightcurves(ax[0][0], TOP[0], TOP[1], win, det, lk, SkyCoord, u, Time)
    oc_one(ax[0][1], TOP[0], TOP[1], win, det, Time)
    lightcurves(ax[1][0], BOTTOM[0], BOTTOM[1], win, det, lk, SkyCoord, u, Time)
    oc_all(ax[1][1], win, Time)
    gallery(ax[2][0], win, det, lk, SkyCoord, u)
    completeness(ax[2][1])
    for a_, lab in zip(ax.flat, "abcdef"):
        a_.text(-0.12, 1.04, f"({lab})", transform=a_.transAxes, fontsize=7.5, fontweight="bold")
    fig.tight_layout(); fig.savefig("n2_figure.pdf"); fig.savefig("n2_figure.png", dpi=300)
    print("-> n2_figure.pdf, n2_figure.png")


if __name__ == "__main__":
    main()
