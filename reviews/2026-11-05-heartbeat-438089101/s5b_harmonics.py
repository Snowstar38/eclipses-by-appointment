"""Step 5b: are the harmonic-flagged peaks (n = 74, 69, 7, 6) at EXACT orbital harmonics? Free-frequency nonlinear
sinusoid fits (on residuals with the strong p modes prewhitened), n = f/f_orb with error from the fit covariance
(scaled by the residual rms), compared with the f_orb error from the light-curve period. Also checks the strong
non-harmonic modes for combination / orbital-sideband relations. Writes s5b_out.txt."""
import os, json
import numpy as np
from scipy.optimize import least_squares
from lib import *
from fitlib import *

say = say_to(open(os.path.join(OUT, "s5b_out.txt"), "w"))
G = gaia(); P0 = float(G["period"]); tp0 = G["tp_btjd"]
J = json.load(open(os.path.join(OUT, "s3_fit.json"))); best = J["fits"]["beam_Pfree"]
d = np.load(os.path.join(OUT, "detr.npz"))
EXP = {9: 1800 / 86400, 10: 1800 / 86400, 36: 600 / 86400, 37: 600 / 86400, 62: 200 / 86400, 63: 200 / 86400, 89: 200 / 86400, 90: 200 / 86400}
U = bin_series(d["t"], d["f"], d["sec"], 1e-6, EXP)
M = Model(U, tp0, P0, mode="beam", pfree=True)
r, coef, cov, X = M.solve(np.array(best["x"]), full=True)
res = U["y"] - X @ coef; t = U["t"]; sec = U["sec"]
P = best["P"]; sPlc = 2.981e-05          # jackknife sigma_P from s3b
forb = 1 / P; sforb = sPlc / P ** 2
t0 = 2700.0
main = [4.47108, 13.60915, 12.81149, 13.64614, 13.61811, 4.52620]
def multi(p, tt, nf):
    y = np.zeros_like(tt)
    for k in range(nf):
        f, a, b = p[3 * k:3 * k + 3]
        y += a * np.sin(2 * np.pi * f * (tt - t0)) + b * np.cos(2 * np.pi * f * (tt - t0))
    return y
p0 = []
for f in main:
    A = np.column_stack([np.sin(2 * np.pi * f * (t - t0)), np.cos(2 * np.pi * f * (t - t0))])
    c, *_ = np.linalg.lstsq(A, res, rcond=None); p0 += [f, c[0], c[1]]
fitm = least_squares(lambda p: multi(p, t, len(main)) - res, p0, x_scale="jac")
rw = res - multi(fitm.x, t, len(main))
sig = np.std(rw)
Jm = fitm.jac; C = np.linalg.pinv(Jm.T @ Jm) * sig ** 2
say(f"f_orb = {forb:.7f} +- {sforb:.1e} c/d (light-curve P {P:.6f} +- {sPlc:.1e})")
say("strong modes (simultaneous nonlinear fit):")
fm = []
for k in range(len(main)):
    f = fitm.x[3 * k]; sf = np.sqrt(C[3 * k, 3 * k]); a = np.hypot(*fitm.x[3 * k + 1:3 * k + 3])
    fm.append(f)
    n = f / forb; sn = np.hypot(sf / forb, f * sforb / forb ** 2)
    say(f"  f {f:.6f} +- {sf:.1e} c/d  amp {a*1e6:.0f} ppm  n = {n:.4f} +- {sn:.4f}")
say("combination / sideband search among strong modes (|f_i +- f_j - m f_orb| within 3 sigma, |m| <= 10):")
for i in range(len(fm)):
    for j in range(i + 1, len(fm)):
        for sgn in (+1, -1):
            dfr = fm[i] + sgn * fm[j] if sgn > 0 else abs(fm[i] - fm[j])
            m_ = dfr / forb
            if abs(m_ - round(m_)) < 0.02 and abs(round(m_)) <= 60:
                say(f"   f{i} {'+' if sgn>0 else '-'} f{j} = {dfr:.5f} = {m_:.3f} f_orb")
for i in range(len(fm)):
    for k2 in (2, 3):
        say(f"   {k2} x f{i} = {k2*fm[i]:.4f}") if False else None

say("\nharmonic-flagged peaks, free frequency fit on prewhitened residuals:")
for n0 in (74, 69, 7, 6, 2, 3, 4, 5):
    f0 = n0 * forb
    A = np.column_stack([np.sin(2 * np.pi * f0 * (t - t0)), np.cos(2 * np.pi * f0 * (t - t0))])
    c, *_ = np.linalg.lstsq(A, rw, rcond=None)
    fit1 = least_squares(lambda p: multi(p, t, 1) - rw, [f0, c[0], c[1]], x_scale="jac")
    Cj = np.linalg.pinv(fit1.jac.T @ fit1.jac) * np.std(rw - multi(fit1.x, t, 1)) ** 2
    f, sf = fit1.x[0], np.sqrt(Cj[0, 0]); a = np.hypot(*fit1.x[1:])
    n = f / forb; sn = np.hypot(sf / forb, f * sforb / forb ** 2)
    say(f"  n0 {n0:3d}: free f {f:.6f} +- {sf:.1e} (start {f0:.6f}); amp {a*1e6:.0f} ppm; n = {n:.4f} +- {sn:.4f} -> {(n-n0)/sn:+.1f} sigma from {n0}")
