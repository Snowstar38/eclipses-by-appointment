"""Step 3a: geometry check of my model code on a paper star, HD 193389 (TIC 51223058; QLP from the house's read-only
P20-60 cache). Gaia SB1 P 20.79663, e 0.3555 +- 0.0044, w 77.26 +- 0.86; paper (vet8): e 0.371, w 77.6, i 35.5,
periastron shift ~ +0.28 d. Also an injection on the TARGET's own cadence + noise with known (e, w, i, S, Bm),
including the w -> w+180 branch, to show the beaming term picks the branch. Writes s3a_out.txt."""
import os
import numpy as np
from lib import *
from fitlib import *

say = say_to(open(os.path.join(OUT, "s3a_out.txt"), "w"))
C = r"[local-path-redacted]"
P = 20.79662696816996; tp = -3.118173146080107 + 389.0
T, F, S_ = [], [], []
for s in (54, 55, 81):
    t, f, q, b = load_qlp(os.path.join(C, f"51223058_s{s:03d}.fits"))
    T.append(t); F.append(f); S_.append(np.full(len(t), s))
T, F, S_ = map(np.concatenate, (T, F, S_))
B = bin_series(T, F, S_, 0.02)
for mode in ("tide", "beam"):
    M = Model(B, tp, P, mode=mode, pfree=False)
    starts = [[0.0, 0.36, np.radians(w0), np.radians(i0)] for w0 in (30, 77, 120, 257) for i0 in (35, 60)]
    r = M.fit(starts)
    o = M.summary(r.x)
    say(f"HD 193389 {mode}: e {o['e']:.4f} w {o['w']:.2f} (mod180 {o['w']%180:.2f}) i {o['i']:.1f} S {o['S']:.2e} "
        f"dtp {o['tp']-tp:+.3f} d  Bm {o.get('Bm', 0):.2e}  chi2/dof {o['chi2']/o['dof']:.2f}")
say("   Gaia e 0.3555 +- 0.0044, w 77.26 +- 0.86 ; paper: e 0.371, w 77.6, i 35.5, dtp +0.28")

# injection on the target cadence
G = gaia(); Pt = float(G["period"]); tpt = G["tp_btjd"]
d = np.load(os.path.join(OUT, "detr.npz"))
t, sec = d["t"], d["sec"]
rng = np.random.default_rng(11)
white = {s: np.std(np.diff(d["f"][sec == s])) / np.sqrt(2) for s in np.unique(sec)}
fac = beaming_factor(12000.0)
for (e0, w0, i0, S0, K) in [(0.25, 92.0, 55, 3.0e-3, 32.0), (0.25, 272.0, 55, 3.0e-3, 32.0), (0.25, 40.0, 70, 3.0e-3, 32.0)]:
    Bm0 = fac * K / C_KMS
    h = tide(t, tpt, Pt, e0, np.radians(w0), np.radians(i0), S0) + beam(t, tpt, Pt, e0, np.radians(w0), Bm0)
    noise = np.array([rng.normal(0, white[s]) for s in sec])
    y = (1 + h) * (1 + 2e-4 * np.sin((t - t.min()) / 7.0)) + noise
    Bs = bin_series(t, y, sec, 0.02)
    for mode in ("tide", "beam"):
        M = Model(Bs, tpt, Pt, mode=mode)
        starts = [[0.0, 0.3, np.radians(ww), np.radians(ii)] for ww in (60, 100, 240, 280) for ii in (45, 70)]
        o = M.summary(M.fit(starts).x)
        say(f"inject e {e0} w {w0} i {i0} S {S0:.1e} Bm {Bm0:.2e} [{mode}] -> e {o['e']:.3f} w {o['w']:.1f} (mod180 {o['w']%180:.1f}) "
            f"i {o['i']:.1f} S {o['S']:.2e} Bm {o.get('Bm', 0):.2e} dtp {o['tp']-tpt:+.4f}")
say(f"beaming factor (blackbody 12000 K, 600-1000 nm, photon-weighted) = {fac:.3f}; at 10000 K {beaming_factor(10000):.3f}; 14000 K {beaming_factor(14000):.3f}")
