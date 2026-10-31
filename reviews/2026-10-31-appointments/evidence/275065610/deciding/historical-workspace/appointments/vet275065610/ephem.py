"""Step 3: linear ephemeris of A eclipses, O-C, compare with Gaia P and conj; B windows from measured A + Gaia phase sep.
python -X utf8 ephem.py"""
import json, numpy as np
M = json.load(open('meas.json')); C = json.load(open('conj.json'))
keys = ['26_all', '53_q0', '79_q0', '80_q0']
t = np.array([M[k]['t0'] for k in keys]); e = np.array([M[k]['et'] for k in keys])
e = np.maximum(e, 0.002)
P0 = 28.0528; n = np.round((t - t[0]) / P0)
A = np.c_[np.ones_like(n), n]; W = 1 / e ** 2
cov = np.linalg.inv(A.T @ (A * W[:, None])); p = cov @ (A.T @ (W * t))
oc = t - A @ p; chi2 = np.sum((oc / e) ** 2); s = max(1, np.sqrt(chi2 / (len(t) - 2)))
print(f'epochs {n}; T0 = {p[0]:.5f} +- {np.sqrt(cov[0,0])*s:.5f}  P = {p[1]:.5f} +- {np.sqrt(cov[1,1])*s:.5f}  chi2 {chi2:.2f} dof {len(t)-2} (errors scaled by {s:.2f})')
for k, tt, o, ee in zip(keys, t, oc, e): print(f'  {k}: {tt:.4f}  O-C {o*1440:+.1f} min  (+-{ee*1440:.1f})')
# reference epoch near middle
nm = np.round((3100 - p[0]) / p[1]); Tm = p[0] + nm * p[1]; eTm = np.sqrt(cov[0,0] + nm**2*cov[1,1] + 2*nm*cov[0,1]) * s
print(f'  mid-epoch T0 = {Tm:.5f} +- {eTm:.5f}')
Pg, ePg = 28.052768398634207, 0.0038758127
print(f'Gaia P {Pg:.5f}+-{ePg:.5f}: dP = {p[1]-Pg:+.5f} = {(p[1]-Pg)/np.hypot(ePg, np.sqrt(cov[1,1])*s):+.2f} sigma')
for k, tt in zip(keys, t):
    c = min([c for c in C if c[0] == 'A'], key=lambda c: abs(c[2] - tt))
    print(f'  {k}: Gaia A {c[2]:.3f}+-{c[3]:.3f}  obs-pred {tt-c[2]:+.3f} d = {(tt-c[2])/c[3]:+.2f} sigma')
ph, eph = 0.5396, 0.0089
print('B windows (measured A + Gaia phase sep 0.5396+-0.0089 -> sigma 0.25 d) and Gaia-direct B:')
for kk in range(-3, 60):
    tb = p[0] + (kk + ph) * p[1]
    for lo, hi, sec in ((2010.29, 2035.12, 26), (2744.0, 2768.98, 53), (3452.54, 3479.68, 79), (3479.89, 3506.34, 80)):
        if lo - 1 < tb < hi + 1:
            g = min([c for c in C if c[0] == 'B'], key=lambda c: abs(c[2] - tb))
            print(f'  s{sec}: B(ephem) {tb:.3f} +- {np.hypot(eph*p[1], 0.003):.3f};  Gaia B {g[2]:.3f}+-{g[3]:.3f}')
nxt = [(lab, p[0] + (kk + o) * p[1]) for kk in range(int((4400 - p[0]) / p[1]), int((4700 - p[0]) / p[1]) + 1) for lab, o in (('A', 0), ('B', ph))]
print('next (BTJD 4400-4700):', ', '.join(f'{l} {x:.3f}' for l, x in nxt))
json.dump(dict(T0=p[0], P=p[1], cov=(cov * s * s).tolist()), open('ephem.json', 'w'))
