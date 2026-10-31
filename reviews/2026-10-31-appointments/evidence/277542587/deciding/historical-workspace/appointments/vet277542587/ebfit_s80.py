"""Limb-darkened two-sphere fit (model code from ebfit3.py: lc0, linear LD U1 .45 U2 .55, L3=0) to the two s080 eclipses.
Star 1 = Gaia RV primary, eclipsed at A (nu = 90 - w, w = Gaia omega). P fixed at Gaia. Free: tP, ecosw, esinw, cosi, r1, r2, J.
Data: QLP SAP all cadences, A t>3488.35, windows +-0.8 d, linear baseline from |dt|>0.35 d. Second fit with esinw fixed at Gaia.
python -X utf8 ebfit_s80.py -> ebfit_s80.json/.png"""
import json, os, sys, numpy as np, matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
from astropy.io import fits
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__))); from vetlib import nm
U1, U2, L3 = 0.45, 0.55, 0.0
src = open('ebfit3.py').read(); exec(src[src.index("rg = (np.arange(200)"):src.index("def lc(par")])
h = fits.open('[local path omitted]'); d = h[1].data
t = np.array(d['TIME'], float); f = np.array(d['SAP_FLUX'], float); ok = np.isfinite(t) & np.isfinite(f); t, f = t[ok], f[ok]
T, F = [], []
for tc in (3488.8242, 3496.7501):
    s = (np.abs(t - tc) < 0.8) & (t > 3488.35); tt, ff = t[s], f[s]; o = np.abs(tt - tc) > 0.35
    c = np.polyfit(tt[o] - tc, ff[o], 1); T.append(tt); F.append(ff / np.polyval(c, tt - tc))
T = np.concatenate(T); F = np.concatenate(F); P = 24.326248
def chi(p, esfix=None):
    tP, ec, es, ci, r1, r2, J = p
    if esfix is not None: es = esfix
    if not (0 < r1 < .2 and 0 < r2 < .2 and 0 <= ci < 1 and 0 < J < 5 and ec * ec + es * es < .8): return 1e30
    return np.sum((F - lc0([tP, P, ec, es, ci, r1, r2, J], T)) ** 2)
best = None
for es0 in (-0.2, -0.1, 0.0):
    for ci0 in (0.03, 0.06, 0.09):
        for J0 in (0.6, 1.2):
            x0 = [3488.824, -0.272, es0, ci0, 0.06, 0.025, J0]
            x, c = nm(chi, x0, [0.005, 0.005, 0.03, 0.01, 0.01, 0.005, 0.2], it=3000)
            x, c = nm(chi, x, [0.002, 0.002, 0.01, 0.003, 0.003, 0.002, 0.05], it=3000)
            if best is None or c < best[1]: best = (x, c)
x, c = best; sig = np.sqrt(c / (len(T) - 7))
def fixfit(esf):
    bb = None
    for ci0 in (0.03, 0.06, 0.09):
        for J0 in (0.6, 1.2):
            y, cc = nm(lambda p: chi(p, esf), [x[0], x[1], esf, ci0, x[4], x[5], J0], [0.005, 0.005, 0, 0.01, 0.01, 0.005, 0.2], it=3000)
            y, cc = nm(lambda p: chi(p, esf), y, [0.002, 0.002, 0, 0.003, 0.003, 0.002, 0.05], it=3000)
            if bb is None or cc < bb[1]: bb = (y, cc)
    return bb
# profile in esinw
prof = []
for esf in np.round(np.arange(-0.26, 0.001, 0.02), 3):
    y, cc = fixfit(esf); prof.append((float(esf), float((cc - c) / sig ** 2)))
    print(f'  esinw fixed {esf:+.3f}: dchi2 {(cc - c) / sig ** 2:9.1f}  cosi {y[3]:.4f} r1 {y[4]:.4f} r2 {y[5]:.4f} J {y[6]:.3f}')
yG, cG = fixfit(-0.1961)
def desc(p):
    tP, ec, es, ci, r1, r2, J = p; e = np.hypot(ec, es); w = np.degrees(np.arctan2(es, ec)) % 360
    L2L1 = J * (r2 / r1) ** 2 * (1 - U2 / 3) / (1 - U1 / 3)
    nuA = np.pi / 2 - np.radians(w); nuB = 1.5 * np.pi - np.radians(w)
    rA = (1 - e * e) / (1 + e * np.cos(nuA)); rB = (1 - e * e) / (1 + e * np.cos(nuB))
    return dict(tP=tP, ecosw=ec, esinw=es, e=e, w=w, cosi=ci, i=np.degrees(np.arccos(ci)), r1=r1, r2=r2, k=r2 / r1, J=J, L2_over_L1=L2L1,
                L2_frac=L2L1 / (1 + L2L1), bA=rA * ci / r1, bB=rB * ci / r1, impact_A_over_sum=rA * ci / (r1 + r2), impact_B_over_sum=rB * ci / (r1 + r2))
R = dict(free=desc(x), free_rms_ppt=sig * 1e3, gaia_esinw=desc(yG), dchi2_gaia_esinw=float((cG - c) / sig ** 2), profile=prof, N=len(T))
print(json.dumps(R, indent=1, default=float)); json.dump(R, open('ebfit_s80.json', 'w'), indent=1, default=float)
fig, ax = plt.subplots(1, 2, figsize=(14, 5))
for a, tc in zip(ax, (3488.8242, 3496.7501)):
    s = np.abs(T - tc) < 0.8; tm = np.linspace(tc - 0.8, tc + 0.8, 1500)
    a.plot(T[s], F[s], 'k.', ms=2)
    a.plot(tm, lc0([x[0], P, *x[1:]], tm), 'c', label='free'); a.plot(tm, lc0([yG[0], P, yG[1], -0.1961, *yG[3:]], tm), 'm--', label='esinw=Gaia')
    a.legend()
plt.savefig('ebfit_s80.png', dpi=80)
