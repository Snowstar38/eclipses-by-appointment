"""Limb-darkened two-sphere fit (ebfit3.py machinery: linear LD U1=0.45 primary, U2=0.55) to the two A eclipses only
(TESS-SPOC SAP q0, s55 600 s x3, s82 200 s x1), P fixed 32.13919, (e cos w, e sin w) fixed at a chosen pair.
Free: tP (s55 A mid), cosi, r1=R1/a, r2=R2/a. Then: R1 from a(M1+M2), predicted B (phase, T14, depth for J). 
python -X utf8 afit.py <ecosw> <esinw>"""
import json, os, sys, numpy as np
from astropy.io import fits
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__))); from vetlib import nm
EC, ES = float(sys.argv[1]), float(sys.argv[2]); U1, U2 = 0.45, 0.55; P = 32.13919; L3 = 0.0
V = '[local path omitted]'
T, Fl, EX = [], [], []
for sec, tc in ((55, 2818.4830), (82, 3557.6843)):
    d = fits.open(V + f'hlsp_tess-spoc_tess_phot_0000000466336052-s00{sec}_tess_v1_lc.fits')[1].data
    t = np.array(d['TIME'], float); f = np.array(d['SAP_FLUX'], float); q = np.array(d['QUALITY'], int)
    ok = np.isfinite(t) & np.isfinite(f) & (q == 0); t, f = t[ok], f[ok]
    w = np.abs(t - tc) < 0.75; o = w & (np.abs(t - tc) > 0.3)
    c = np.polyfit(t[o] - tc, f[o], 2); T.append(t[w]); Fl.append(f[w] / np.polyval(c, t[w] - tc)); EX.append(np.full(w.sum(), sec))
t, f, ex = map(np.concatenate, (T, Fl, EX)); SS = {55: (600, 3), 82: (200, 1)}
rg = (np.arange(200) + 0.5) / 200
exec(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'ebfit3.py')).read().split('def blocked')[1].split('use = np.ones_like')[0].join(['def blocked', '']))
def par(p, J=0.09): return [p[0], P, EC, ES, p[1], p[2], p[3], J]
def chi(p):
    if not (0 <= p[1] < 0.1 and 0.005 < p[2] < 0.1 and 0.001 < p[3] < 0.05): return 1e30
    return np.sum((f - lc(par(p))) ** 2)
best = None
for ci in (0.0, 0.01, 0.02):
    for r1 in (0.025, 0.035):
        b, c2 = nm(chi, [2818.4830, ci, r1, r1 * 0.19], [0.002, 0.005, 0.003, 0.001], it=3000)
        b, c2 = nm(chi, b, [0.0005, 0.002, 0.001, 0.0005], it=3000)
        if best is None or c2 < best[1]: best = (b, c2)
b, c2 = best; sig = np.sqrt(c2 / (len(t) - 4)); e = np.hypot(EC, ES); w = np.arctan2(ES, EC)
rA = (1 - e * e) / (1 + e * np.sin(w)); rB = (1 - e * e) / (1 - e * np.sin(w))
bA = rA * b[1] / b[2]; bB = rB * b[1] / b[2]; k = b[3] / b[2]
print(f'ecosw {EC} esinw {ES}: tP {b[0]:.5f} cosi {b[1]:.4f} (i {np.degrees(np.arccos(b[1])):.2f}) r1 {b[2]:.5f} r2 {b[3]:.5f} k {k:.4f} bA {bA:.3f} bB {bB:.3f} rms {sig*1e6:.0f} ppm chi2/N {c2/sig**2:.0f}/{len(t)}')
for M in (1.05, 1.2, 1.35):
    m2 = 0.25 if M < 1.1 else (0.27 if M < 1.3 else 0.29)
    a = 4.2084 * (M + m2) ** (1 / 3) * P ** (2 / 3); print(f'   M1 {M} m2 {m2}: a {a:.1f} Rsun -> R1 {b[2]*a:.2f} Rsun, R2 {b[3]*a:.3f} Rsun (TIC R1 1.44)')
tt = np.arange(b[0] - P + 1, b[0] + 0.6, 0.0005)
for J in (0.05, 0.09, 0.15):
    m = lc0(par(b, J), tt); inB = m < 1 - 1e-6
    tB = tt[inB & (tt < b[0] - 0.6)]
    if len(tB): 
        ph = ((tB.mean() - (b[0] - P)) / P) % 1
        print(f'   J {J}: model B centre {tB.mean():.3f} (sep {ph:.4f}), T14 {(tB.max()-tB.min())*24:.2f} h, depth {(1-m[inB & (tt < b[0]-1)].min())*100:.3f}%')
    else: print(f'   J {J}: no B eclipse in model')
mA = lc0(par(b), tt[np.abs(tt - b[0]) < 0.5]); x = tt[np.abs(tt - b[0]) < 0.5][mA < 1]; print(f'   model A T14 {(x.max()-x.min())*24:.2f} h depth {(1-mA.min())*100:.3f}%')
json.dump(dict(ec=EC, es=ES, b=list(map(float, b)), rms=sig, bA=bA, bB=bB, k=k), open(f'afit_{EC}_{ES}.json', 'w'))
