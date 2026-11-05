"""Step 4: eclipse test, and the equilibrium-tide amplitude expectation (step 3 physics).
 (a) heartbeat (tide+beam, light-curve ephemeris) vs (b) EB alternative: trapezoid eclipse near conjunction A (and B)
     + circular-orbit harmonics cos/sin(phi), cos(2 phi) (ellipsoidal/reflection/beaming) -- dBIC.
 (c) excluded eclipse depth on top of the heartbeat: boxes of the geometric duration at A and B, 3-sigma limits with the
     error inflated by sqrt(chi2/dof) and by the red-noise box-scatter at random phases.
 (d) geometry: m2 from f(m) and i, a, separations at A/B, the inclination an eclipse needs.
Writes s4_out.txt."""
import os, json
import numpy as np
from scipy.optimize import least_squares, brentq
from lib import *
from fitlib import *

say = say_to(open(os.path.join(OUT, "s4_out.txt"), "w"))
G = gaia(); P0 = float(G["period"]); tp0 = G["tp_btjd"]; KG = float(G["semi_amplitude_primary"])
J = json.load(open(os.path.join(OUT, "s3_fit.json"))); best = J["fits"]["beam_Pfree"]; FAC = J["FAC"]
d = np.load(os.path.join(OUT, "detr.npz"))
EXP = {9: 1800 / 86400, 10: 1800 / 86400, 36: 600 / 86400, 37: 600 / 86400}
B = bin_series(d["t"], d["f"], d["sec"], 0.02, EXP)
P, tp, e, w, inc = best["P"], best["tp"], best["e"], np.radians(best["w"]), np.radians(best["i"])
n = len(B["t"])
M = Model(B, tp0, P0, mode="beam", pfree=True)
r, coef, cov, X = M.solve(np.array(best["x"]), full=True)
chi_hb = float(r @ r); k_hb = len(best["x"]) + X.shape[1]
say(f"heartbeat (tide+beam, P {P:.6f}): chi2 {chi_hb:.0f}, k {k_hb}, BIC {chi_hb + k_hb*np.log(n):.0f}")
phA, phB = conj_phase(e, np.degrees(w), "A"), conj_phase(e, np.degrees(w), "B")
tA = tp + phA * P; tB = tp + phB * P
say(f"model conjunctions: A at phase {phA:.4f} ({(phA if phA<0.5 else phA-1)*P:+.3f} d from periastron), B at {phB:.4f}")
Xb = M.Xb; wt = 1 / B["err"]

def trap(ph, ph0, depth, T14, T12):
    x = np.abs(((ph - ph0 + 0.5) % 1) - 0.5) * P           # days from centre
    y = np.zeros_like(x)
    full = x <= T14 / 2 - T12
    y[full] = 1
    ing = (x > T14 / 2 - T12) & (x < T14 / 2)
    y[ing] = (T14 / 2 - x[ing]) / max(T12, 1e-4)
    return -depth * y

def eb_resid(p, twin):
    ph = ((B["t"] - tp) / P) % 1
    cols = [np.cos(2 * np.pi * ph), np.sin(2 * np.pi * ph), np.cos(4 * np.pi * ph), np.sin(4 * np.pi * ph)]
    ecl = trap(ph, p[0], 1.0, p[1], p[2] * p[1] / 2)
    if twin: ecl = ecl + trap(ph, p[3], 1.0, p[4], p[2] * p[4] / 2) * 0 + 0
    Xs = [ecl] + ([trap(ph, p[3], 1.0, p[4], p[5] * p[4] / 2)] if twin else []) + cols
    A = np.column_stack(Xs + [Xb]) * wt[:, None]
    c, *_ = np.linalg.lstsq(A, B["y"] * wt, rcond=None)
    return B["y"] * wt - A @ c, c

best_eb = {}
for twin, Tmax in ((False, 1.6), (True, 1.6), (False, 0.5), (True, 0.5)):
    bestc = None
    say(f"[T14 bound {Tmax} d]" + ("  (0.5 d ~ the longest central eclipse an 18.8-Rsun orbit allows at A/B)" if Tmax < 1 else "  (unbounded)"))
    for ph0 in np.linspace(phA - 0.1, phA + 0.1, 9):
        for T14 in (0.3, 0.6, 0.9):
            T14 = min(T14, Tmax * 0.95)
            p0 = [ph0 % 1, T14, 0.5] + ([phB, min(0.4, Tmax*0.9), 0.5] if twin else [])
            lo = [0, 0.05, 0.02] + ([0, 0.05, 0.02] if twin else []); hi = [1, Tmax, 1.0] + ([1, Tmax, 1.0] if twin else [])
            rr = least_squares(lambda p: eb_resid(p, twin)[0], p0, bounds=(lo, hi), diff_step=1e-3)
            if bestc is None or rr.cost < bestc.cost: bestc = rr
    res, c = eb_resid(bestc.x, twin)
    chi = float(res @ res); k = len(bestc.x) + len(c)
    lab = "A+B" if twin else "A only"
    say(f"EB alternative ({lab}): trapezoid at phase {bestc.x[0]:.4f} depth {c[0]*1e3:.2f} ppt T14 {bestc.x[1]*24:.1f} h" +
        (f"; second at {bestc.x[3]:.4f} depth {c[1]*1e3:.2f} ppt T14 {bestc.x[4]*24:.1f} h" if twin else "") +
        f"; chi2 {chi:.0f}, k {k}; dBIC (EB - heartbeat) = {chi + k*np.log(n) - chi_hb - k_hb*np.log(n):+.0f}")

# ---- (d) geometry ----
M1s = (2.5, 3.2, 3.8); R1s = (2.6, 3.25, 3.9)
fm = float(G["fm"])
for M1 in M1s:
    si = np.sin(inc)
    m2 = brentq(lambda m: (m * si) ** 3 / (M1 + m) ** 2 - fm, 1e-3, 20)
    a = 4.2084 * ((M1 + m2) * P ** 2) ** (1 / 3)              # Rsun
    R2 = m2 ** 0.8 if m2 < 1.5 else m2 ** 0.57
    for kind, nuw in (("A", 90.0), ("B", 270.0)):
        nu = np.radians(nuw) - w; r_ = a * (1 - e * e) / (1 + e * np.cos(nu))
        for R1 in R1s:
            ineed = np.degrees(np.arccos(min(1, (R1 + R2) / r_)))
            b = r_ * np.cos(inc) / R1
            if R1 == 3.25:
                say(f"M1 {M1} -> m2 {m2:.2f} (q {m2/M1:.3f}) a {a:.1f} Rsun; conj {kind}: r {r_:.1f} Rsun, eclipse needs i > {ineed:.1f} deg "
                    f"(R1 {R1}, R2 {R2:.2f}); at fitted i {np.degrees(inc):.1f}: b = {b:.2f} R1")
    # equilibrium-tide expectation: ellipsoidal semi-amplitude ~ alpha q (R1/a)^3 sin^2 i; Kumar S = A_ell / (1.5 sin^2 i)
    for R1 in R1s:
        u, beta = 0.30, 0.25
        tau = 0.25  # gravity-darkening coefficient for a radiative B star in a red band (~ beta * x / (1-e^-x) ~ 0.3)
        alpha = 0.15 * (15 + u) * (1 + tau) / (3 - u)
        S_exp = alpha * (m2 / M1) * (R1 / a) ** 3 / 1.5
        if M1 == 3.2:
            say(f"   R1 {R1}: expected undiluted S = {S_exp:.2e} (alpha_ell {alpha:.2f}); diluted by contratio 0.369 -> {S_exp/1.369:.2e}; fitted S {best['S']:.2e}")
    Bexp = FAC * KG / C_KMS
    if M1 == 3.2:
        say(f"   expected beaming Bm (Gaia K1, 12000 K, diluted /1.369) {Bexp/1.369:.2e}; fitted {best['Bm']:.2e} -> diluted-corrected K1-eq {best['Bm']*1.369*C_KMS/FAC:.0f} km/s")

# ---- (c) box limits on top of the heartbeat ----
infl = np.sqrt(chi_hb / (n - k_hb))
resid = r / wt     # unweighted residual flux
ph = ((B["t"] - tp) / P) % 1
rng = np.random.default_rng(5)
for kind, phc, dur in (("A", phA, 0.42), ("B", phB, 0.45)):
    half = dur / 2 / P
    def box(pc):
        m = np.abs(((ph - pc + 0.5) % 1) - 0.5) < half
        side = (np.abs(((ph - pc + 0.5) % 1) - 0.5) > half) & (np.abs(((ph - pc + 0.5) % 1) - 0.5) < 3 * half)
        return np.average(resid[side], weights=wt[side] ** 2) - np.average(resid[m], weights=wt[m] ** 2), \
               1 / np.sqrt(np.sum(wt[m] ** 2))
    dep, sd = box(phc % 1)
    rnd = np.array([box(x)[0] for x in rng.uniform(0, 1, 300)])
    sred = 1.4826 * np.median(np.abs(rnd - np.median(rnd)))
    say(f"box at {kind} (duration {dur*24:.0f} h): residual depth {dep*1e6:+.0f} ppm; white err x infl {sd*infl*1e6:.0f}, red (random-phase MAD) {sred*1e6:.0f} ppm "
        f"-> 3-sigma limit {(max(dep,0) + 3*max(sd*infl, sred))*1e6:.0f} ppm")
