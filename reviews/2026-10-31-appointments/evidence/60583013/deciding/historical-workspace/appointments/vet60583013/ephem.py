"""Ephemeris from the three events, Gaia comparison, e cos w / e sin w, physics, next eclipses. -> ephem.txt"""
import json, numpy as np
from vetlib import fit_trap, model, trap, nm
from astropy.io import fits
import glob
E = json.load(open('ecl.json')); g = lambda kind, key: [r for r in E if r['kind'] == kind and r['key'] == key][0]
# event times: QLP value, error = max(formal, half pipeline spread)
def ev(kind, keys):
    ts = np.array([g(kind, k)['t0'] for k in keys]); e = max(g(kind, keys[0])['et0'], (ts.max() - ts.min()) / 2); return g(kind, keys[0])['t0'], e
A33 = ev('A', ['QLP33', 'TSPOC33', 'TARS33']); B33 = ev('B', ['QLP33', 'TSPOC33', 'TARS33']); B6 = ev('B?', ['QLP6', 'TSPOC6', 'TARS6'])
print('A s033', A33, '\nB s033', B33, '\nB s006', B6)
Gp, Gpe = 26.656871295616213, 0.0094707655
for n in (27, 28, 29):
    P = (B33[0] - B6[0]) / n; eP = np.hypot(B33[1], B6[1]) / n; print(f'  B cycles {n}: P {P:.5f} +- {eP:.5f}  vs Gaia {Gp:.5f}+-{Gpe:.5f}: {(P-Gp)/Gpe:+.1f} sigma')
n = 28; P = (B33[0] - B6[0]) / n; eP = np.hypot(B33[1], B6[1]) / n
print(f'ADOPTED P = {P:.5f} +- {eP:.5f} d (two B events, 28 cycles; one A, so A ephemeris assumes same P); O-C = 0 by construction (2 points)')
ph = (B33[0] - A33[0]) / P; eph = np.hypot(B33[1], A33[1]) / P
print(f'B-A phase {ph:.5f} +- {eph:.5f}; Gaia 0.5468 +- 0.0151 (conjmc) -> {(ph-0.5468)/0.0151:+.1f} sigma')
# e cos w (exact relation solved numerically for small e sin w)
def dphi(ec, es):
    e = np.hypot(ec, es); w = np.arctan2(es, ec)
    nuA, nuB = np.pi/2 - w, 3*np.pi/2 - w
    M = lambda nu: (lambda E_: E_ - e*np.sin(E_))(2*np.arctan2(np.sqrt(1-e)*np.sin(nu/2), np.sqrt(1+e)*np.cos(nu/2)))
    return ((M(nuB) - M(nuA)) / (2*np.pi)) % 1
ecs = np.linspace(-0.2, 0.2, 40001); ec = ecs[np.argmin(np.abs([dphi(x, 0.02) - ph for x in ecs]))]
print(f'e cos w = {ec:.4f} (+- {np.pi/2*eph:.4f} from timing); Gaia 0.0736 +- 0.0238 -> {(ec-0.0736)/0.0238:+.1f} sigma')
# secondary duration with ingress fixed to primary's (same b at both conjunctions to first order), TSPOC+QLP s033 and s006
TA = g('A', 'TSPOC33')['T14_h'] / 24; T12A = g('A', 'TSPOC33')['T12_h'] / 24
for key, kind, fn in (('TSPOC33', 'B', '*tess-spoc*s0033*'), ('TSPOC6', 'B?', '*tess-spoc*s0006*')):
    d = fits.getdata(glob.glob('[local path omitted]' + fn)[0], 1); t = d['TIME']; f = d['SAP_FLUX']; q = d['QUALITY']
    t0 = g(kind, key)['t0']; m = np.isfinite(t) & np.isfinite(f) & (q == 0) & (np.abs(t - t0) < 0.7); t, f = t[m], f[m] / np.median(f[m])
    def chi(p):
        if p[1] < 0 or p[2] < 2 * T12A: return 1e30
        return np.sum((f - trap(t, p[0], p[1], p[2], T12A) * (p[3] + p[4]*(t-t0) + p[5]*(t-t0)**2)) ** 2)
    b, c = nm(chi, [t0, 0.003, 0.38, 1, 0, 0], [0.01, 0.001, 0.03, 0.001, 0.001, 0.001])
    s = np.sqrt(c / len(t)); grid = np.linspace(0.25, 0.55, 121); prof = []
    for T in grid:
        bb, cc = nm(lambda p: chi([p[0], p[1], T, p[2], p[3], p[4]]), [b[0], b[1], b[3], b[4], b[5]], [0.005, 0.0005, 0.001, 0.001, 0.001]); prof.append(cc / s**2)
    prof = np.array(prof) - min(prof); okT = grid[prof <= 1]
    print(f'{key} B with T12 fixed {T12A*24:.2f} h: t0 {b[0]:.4f} depth {b[1]*100:.3f}% T14 {b[2]*24:.2f} h (1-sigma {okT.min()*24:.2f}-{okT.max()*24:.2f} h); primary T14 {TA*24:.2f} h')
    r = b[2] / TA; print(f'   T_B/T_A = {r:.3f} -> e sin w ~ (r-1)/(r+1) = {(r-1)/(r+1):+.3f} (range {(okT.min()/TA-1)/(okT.min()/TA+1):+.3f} .. {(okT.max()/TA-1)/(okT.max()/TA+1):+.3f}); Gaia 0.0205 +- 0.0225')
# physics
K, e, Pd = 19.564073993036963, 0.08009, Gp
fm = 1.0361e-7 * K**3 * Pd * (1 - e**2)**1.5; print(f'mass function f(m) = {fm:.4f} Msun')
for M1 in (1.0, 1.14, 1.3):
    m2 = 0.1
    for _ in range(100): m2 = (fm * (M1 + m2)**2) ** (1/3)
    a = ((M1 + m2) * (Pd / 365.25)**2) ** (1/3) * 215.03
    R1, R2 = 1.853, m2 * 1.0
    for lab, s in (('A', +1), ('B', -1)):
        r = a * (1 - e**2) / (1 + s * e * np.sin(np.radians(16.47)))
        T = Pd / np.pi * np.sqrt(1 - e**2) / (1 + s * e * np.sin(np.radians(16.47))) * np.arcsin((R1 + R2) / a) * 24
        if lab == 'A': TAc = T
    print(f'  M1 {M1}: m2(i=90) {m2:.3f} Msun, a {a:.1f} Rsun ({a/R1:.1f} R1), central T14 at A {TAc:.2f} h, at B {T:.2f} h (R1 1.853, R2~{R2:.2f})')
k = np.sqrt(g('A', 'TSPOC33')['depth']); T14 = g('A', 'TSPOC33')['T14_h']; T23 = T14 - 2 * g('A', 'TSPOC33')['T12_h']; x = (T23 / T14)**2
b2 = ((1 - k)**2 - x * (1 + k)**2) / (1 - x); aR = 2 * Pd / np.pi * k**0.5 / np.sqrt((T14/24)**2 - (T23/24)**2)
print(f'primary shape (no LD): k ~ {k:.3f} (R2 ~ {k*1.853:.2f} Rsun if R1 1.853), b ~ {np.sqrt(max(b2,0)):.2f}, a/R1 ~ {aR:.1f} (circular; x(1+e sin w) ~ {aR*1.0:.1f})')
dB = g('B', 'TSPOC33')['depth']; print(f'secondary/primary depth {dB/g("A","TSPOC33")["depth"]:.3f} -> TESS surface-brightness ratio ~ {dB/k**2:.3f}')
h, c_, kb, lam = 6.626e-34, 3e8, 1.381e-23, 0.8e-6
for T2 in (3200, 3400, 3600):
    bb = lambda T: 1 / (np.exp(h*c_/(lam*kb*T)) - 1); print(f'  blackbody 800 nm ratio T2 {T2} / 6076 K: {bb(T2)/bb(6076):.3f} -> occultation depth {k**2*bb(T2)/bb(6076)*100:.3f}%')
# next eclipses
TA0 = A33[0]; print(f'Ephemeris A: BTJD {TA0:.4f} + n x {P:.5f};  B: BTJD {B33[0]:.4f} + n x {P:.5f}')
for lab, T0 in (('A', TA0), ('B', B33[0])):
    n0 = int(np.ceil((4336 - T0) / P)); print(lab, 'next:', ', '.join(f'{T0 + n*P:.3f}+-{abs(n)*eP + (A33[1] if lab=="A" else B33[1]):.3f}' for n in range(n0, n0 + 6)))
