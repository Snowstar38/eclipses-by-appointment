"""Physics: mass function, m2(i) for plausible M1, a, a/R1; e sin w implied by the A-eclipse chord speed (ebfit v) for a range of
stellar R1, M1; B-conjunction geometry (b_B, T14_B, occulted fraction of the companion) and expected secondary depth vs e sin w,
with a blackbody TESS-band surface-brightness ratio. python -X utf8 physics.py"""
import json, numpy as np
G = 6.674e-11; Ms = 1.989e30; Rs = 6.957e8; day = 86400.
P = 39.542578; K = 11.9025; eK = 0.7652; e = 0.1384; ee = 0.0381
fit = json.load(open('ebfit.json')); k, b, v = fit['k'], fit['b'], fit['v']; ek, eb, ev = fit['ek'], fit['eb'], fit['ev']
fm = (1 - e ** 2) ** 1.5 * (K * 1e3) ** 3 * P * day / (2 * np.pi * G) / Ms
print(f"f(m) = {fm:.5f} Msun  (K {K:.2f}+-{eK:.2f}, e {e:.3f})")
def m2_of(M1, fm, sini=1.0):
    m = 0.1
    for _ in range(200): m = (fm * (M1 + m) ** 2) ** (1 / 3) / sini
    return m
for M1 in (1.0, 1.07, 1.14, 1.2):
    m2 = m2_of(M1, fm); m2lo = m2_of(M1, fm * ((K - eK) / K) ** 3); m2hi = m2_of(M1, fm * ((K + eK) / K) ** 3)
    a = (G * (M1 + m2) * Ms * (P * day) ** 2 / (4 * np.pi ** 2)) ** (1 / 3) / Rs
    print(f"M1 {M1:.2f}: m2(i=90) = {m2:.3f} ({m2lo:.3f}-{m2hi:.3f}) Msun; a = {a:.2f} Rsun = {a/215.03:.4f} AU")
# e sin w from chord speed: v_A [R1/d] = 2 pi a / (P R1) * (1 + e sin w) / sqrt(1 - e^2)
print("\nImplied (1 + e sin w)/sqrt(1-e^2) from v_A = %.2f +- %.2f R1/d:" % (v, ev))
for M1, R1 in ((1.14, 1.053), (1.14, 0.95), (1.14, 1.15), (1.05, 1.0), (1.2, 1.2)):
    m2 = m2_of(M1, fm); a = (G * (M1 + m2) * Ms * (P * day) ** 2 / (4 * np.pi ** 2)) ** (1 / 3) / Rs
    q = v * P * R1 / (2 * np.pi * a); esw = q * np.sqrt(1 - e ** 2) - 1
    print(f"  M1 {M1:.2f} R1 {R1:.3f}: a/R1 {a/R1:.1f}; ratio {q:.3f} -> e sin w = {esw:+.3f} (for e=0.138; d(esw)/dR1 = {q*np.sqrt(1-e**2)/R1:.2f} per Rsun); R2 = k R1 = {k*R1:.3f} Rsun")
# central durations
M1, R1 = 1.14, 1.053; m2 = m2_of(M1, fm); a = (G * (M1 + m2) * Ms * (P * day) ** 2 / (4 * np.pi ** 2)) ** (1 / 3) / Rs
for esw in (0.0, 0.12):
    vA = 2 * np.pi * a / R1 / P * (1 + esw) / np.sqrt(1 - e ** 2); vB = 2 * np.pi * a / R1 / P * (1 - esw) / np.sqrt(1 - e ** 2)
    print(f"e sin w {esw:.2f}: central (b=0) T14 at A = {2*(1+k)/vA*24:.2f} h, at B = {2*(1+k)/vB*24:.2f} h")
# blackbody TESS-band (600-1000 nm, flat) surface brightness ratio
lam = np.linspace(600e-9, 1000e-9, 400); h, c, kb = 6.626e-34, 2.998e8, 1.381e-23
Bl = lambda T: 1 / lam ** 5 / (np.exp(h * c / (lam * kb * T)) - 1)
T1 = 6091.
print()
for T2 in (3100, 3250, 3400):
    sb = np.trapezoid(Bl(T2) * lam, lam) / np.trapezoid(Bl(T1) * lam, lam)
    L2 = k ** 2 * sb; print(f"T2 {T2} K: TESS-band surface brightness ratio {sb:.4f}; L2/L1 = {L2:.5f}; full-occultation secondary depth {L2/(1+L2)*1e3:.2f} ppt")
# B geometry vs e sin w: occulted fraction of the companion's (uniform) disc by the primary (radius 1) at separation b_B
def overlap(R, r, d):
    if d >= R + r: return 0.0
    if d <= R - r: return np.pi * r ** 2
    a1 = r ** 2 * np.arccos((d ** 2 + r ** 2 - R ** 2) / (2 * d * r)); a2 = R ** 2 * np.arccos((d ** 2 + R ** 2 - r ** 2) / (2 * d * R))
    return a1 + a2 - 0.5 * np.sqrt((-d + r + R) * (d + r - R) * (d - r + R) * (d + r + R))
sb = np.trapezoid(Bl(3250) * lam, lam) / np.trapezoid(Bl(T1) * lam, lam); L2 = k ** 2 * sb
print("\ne sin w | b_B | occulted frac of companion | secondary depth (ppt, T2 3250 K BB) | T14_B (h)")
rows = []
for esw in np.arange(-0.05, 0.3001, 0.025):
    bB = b * (1 + esw) / (1 - esw); fr = overlap(1, k, bB) / (np.pi * k ** 2)
    vB = v * (1 - esw) / (1 + esw); T14B = 2 * np.sqrt(max((1 + k) ** 2 - bB ** 2, 0)) / vB * 24
    rows.append((esw, bB, fr, fr * L2 / (1 + L2) * 1e3, T14B)); print(f"  {esw:+.3f} | {bB:.3f} | {fr:.3f} | {fr*L2/(1+L2)*1e3:.2f} | {T14B:.2f}")
json.dump(dict(fm=fm, rows=rows, L2=L2), open('physics.json', 'w'), indent=1)
