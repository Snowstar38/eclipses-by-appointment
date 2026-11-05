"""Three-panel figure, paper heartbeat style. Left: flux (fitted per-segment baselines removed) folded on the
light-curve ephemeris (P 4.800079, 0.6 sigma from Gaia's), periastron and model A/B conjunctions marked, Gaia's
extrapolated periastron +-1 sigma shaded, model overlaid. Middle: every covered periastron passage (0.04-d bins),
coloured by season (one sequential hue, light = 2019 -> dark = 2025), with the model. Right: residual amplitude
spectrum in units of f_orb (all sectors), exact harmonics n = 69, 74 marked; the 4.471 c/d peak (on a G 14.25
neighbour) labelled. Writes fig_438089101.png."""
import os, json
import numpy as np
import matplotlib; matplotlib.use("Agg"); import matplotlib.pyplot as plt
from lib import *
from fitlib import *

G = gaia(); P0 = float(G["period"]); tp0 = G["tp_btjd"]
best = json.load(open(os.path.join(OUT, "s3_fit.json")))["fits"]["beam_Pfree"]
eph = json.load(open(os.path.join(OUT, "ephem.json")))
d = np.load(os.path.join(OUT, "detr.npz"))
EXP = {9: 1800 / 86400, 10: 1800 / 86400, 36: 600 / 86400, 37: 600 / 86400}
B = bin_series(d["t"], d["f"], d["sec"], 0.02, EXP)
M = Model(B, tp0, P0, mode="beam", pfree=True)
r, coef, cov, X = M.solve(np.array(best["x"]), full=True)
base = X[:, 2:] @ coef[2:]
y = B["y"] - base
P, tp, e, w, inc = best["P"], best["tp"], best["e"], np.radians(best["w"]), np.radians(best["i"])
mdl = lambda tt: tide(tt, tp, P, e, w, inc, best["S"]) + beam(tt, tp, P, e, w, best["Bm"])
off = np.median(y - X[:, :2] @ coef[:2])
y = y - off
ph = ((B["t"] - tp) / P + 0.5) % 1 - 0.5
INK, MUTED, GRID = "#222222", "#6b6b6b", "#e6e6e6"
fig, ax = plt.subplots(1, 3, figsize=(15, 4.6), gridspec_kw={"width_ratios": [1.15, 1.15, 1]})
for a in ax:
    a.grid(color=GRID, lw=0.6); a.set_axisbelow(True)
    for s in ("top", "right"): a.spines[s].set_visible(False)
# left
a = ax[0]
a.plot(ph, y * 1e3, ".", ms=1.2, color="#b8c4d6", rasterized=True)
xb, yb, eb, _ = binstat(ph, y, np.linspace(-0.5, 0.5, 101), minn=5)
a.errorbar(xb, yb * 1e3, eb * 1e3, fmt="o", ms=3, color=INK, lw=0.8)
pp = np.linspace(-0.5, 0.5, 2000)
a.plot(pp, (mdl(tp + pp * P)) * 1e3 - 0, color="#c0392b", lw=1.6, label="tide + beaming model")
Ng = eph["N_ref"]; Tg = tp0 + Ng * P0; sTg = np.hypot(float(G["t_periastron_error"]), Ng * float(G["period_error"]))
dg = (Tg - (tp + Ng * P)) / P
a.axvspan(dg - sTg / P, dg + sTg / P, color="#f0e0c0", alpha=0.6, lw=0, label=f"Gaia periastron at N={Ng}, ±1σ")
fA, fB = conj_phase(e, best["w"], "A"), conj_phase(e, best["w"], "B")
for x, lab in ((0, "periastron, A"), (fB - 1 if fB > 0.5 else fB, "B")):
    a.axvline(x, color=MUTED, ls=":", lw=1); a.text(x + 0.01, 5.3, lab, color=MUTED, fontsize=8)
a.set_xlim(-0.5, 0.5); a.set_ylim(-10, 6.5)
a.set_xlabel(f"phase from light-curve periastron (P = {P:.6f} d)"); a.set_ylabel("ΔF/F (ppt), QLP SAP")
a.legend(loc="lower left", fontsize=8, frameon=False)
a.set_title("TIC 438089101: fold, 8 sectors 2019–2025", fontsize=10, color=INK)
# middle
a = ax[1]
cyc = np.round((B["t"] - tp) / P).astype(int)
seasons = [(9, 10), (36, 37), (62, 63), (89, 90)]
shades = ["#a9c4e4", "#6f9fd6", "#3a72b8", "#163f78"]
for (s1, s2), c, yr in zip(seasons, shades, ("2019", "2021", "2023", "2025")):
    m = (B["sec"] >= s1) & (B["sec"] <= s2)
    first = True
    for cn in np.unique(cyc[m]):
        mm = m & (cyc == cn)
        dt = B["t"][mm] - (tp + cn * P)
        if mm.sum() < 0.7 * 3.0 / 0.02 or dt.min() > -1.0 or dt.max() < 1.0: continue
        xb, yb, _, _ = binstat(dt, y[mm], np.arange(-1.5, 1.5001, 0.04), minn=1)
        a.plot(xb, yb * 1e3, "-", color=c, lw=0.8, alpha=0.85, label=f"s{s1}–{s2} ({yr})" if first else None)
        first = False
tt = np.linspace(-1.5, 1.5, 600)
a.plot(tt, mdl(tp + tt) * 1e3, color="#c0392b", lw=2, label="model")
a.set_xlim(-1.5, 1.5); a.set_ylim(-10, 6.5)
a.set_xlabel("days from periastron"); a.set_ylabel("ΔF/F (ppt)")
a.legend(fontsize=8, frameon=False, loc="lower right")
a.set_title("every covered periastron passage", fontsize=10, color=INK)
# right
a = ax[2]
sp = np.load(os.path.join(OUT, "s5_spec.npz"))
forb = 1 / P
a.plot(sp["f_lo"] / forb, sp["A_all"] * 1e6, color=INK, lw=0.5)
for n, xo in ((69, 60), (74, 84)):
    a.annotate(f"n = {n}", (n, 270), (xo, 520), ha="center", fontsize=8, color="#c0392b",
               arrowprops=dict(arrowstyle="-", color="#c0392b", lw=0.8))
a.annotate("4.471 c/d: G 14.25 neighbour (30″)", (4.47108 / forb, 1200), (28, 1250), fontsize=8, color=MUTED,
           arrowprops=dict(arrowstyle="-", color=MUTED, lw=0.8))
a.text(65.3, 1120, "13.61 c/d\n(on target)", fontsize=8, color=MUTED, ha="right")
a.set_xlim(0, 115); a.set_ylim(0, 1400)
a.set_xlabel("frequency / f_orb"); a.set_ylabel("residual amplitude (ppm)")
a.set_title("residual amplitude spectrum (tide+beaming removed)", fontsize=10, color=INK)
fig.tight_layout(); fig.savefig(os.path.join(OUT, "fig_438089101.png"), dpi=130)
