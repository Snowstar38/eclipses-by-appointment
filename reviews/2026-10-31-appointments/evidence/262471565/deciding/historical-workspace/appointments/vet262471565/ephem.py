"""Linear ephemerides for A and B, joint fit with common P, O-C, Gaia comparison (conj.json from conjmc.py),
e cos w from phase separation, e sin w from durations. python ephem.py"""
import json, numpy as np
P0 = 23.3237
A = [(1675.73837, 1.6), (3145.08424, 0.8), (3868.09836, 1.5)]          # day, err (min): pipeline means, err=max(formal, scatter)
B = [(1663.28140, 4.0), (2036.45383, 4.0), (2059.76929, 7.0), (3132.62797, 2.5), (3878.96418, 3.0)]
def lin(ev, tref):
    t = np.array([x[0] for x in ev]); s = np.array([x[1] for x in ev]) / 1440
    n = np.round((t - tref) / P0); W = 1 / s ** 2; X = np.vstack([np.ones_like(n), n]).T
    C = np.linalg.inv(X.T @ (X * W[:, None])); p = C @ X.T @ (W * t); r = t - X @ p
    return p, np.sqrt(np.diag(C)), n, r, np.sum((r / s) ** 2), C
for lab, ev, tr in (('A', A, 1675.73837), ('B', B, 1663.28140)):
    p, e, n, r, c2, C = lin(ev, tr)
    print(f'{lab}: T0 {p[0]:.5f} +- {e[0]*1440:.1f} min  P {p[1]:.6f} +- {e[1]:.6f}  chi2 {c2:.2f} / {len(ev)-2} dof')
    for nn, rr, x in zip(n, r, ev): print(f'    E{int(nn):3d} {x[0]:.5f}  O-C {rr*1440:+6.1f} min (err {x[1]} min)')
# joint: common P, separate T0
t = np.array([x[0] for x in A + B]); s = np.array([x[1] for x in A + B]) / 1440
isB = np.r_[np.zeros(len(A)), np.ones(len(B))]
n = np.where(isB == 0, np.round((t - 1675.73837) / P0), np.round((t - 1663.2814) / P0))
X = np.vstack([1 - isB, isB, n]).T; W = 1 / s ** 2; C = np.linalg.inv(X.T @ (X * W[:, None])); p = C @ X.T @ (W * t); r = t - X @ p
e = np.sqrt(np.diag(C)); print(f'joint: T0A {p[0]:.5f} +- {e[0]*1440:.1f} min  T0B {p[1]:.5f} +- {e[1]*1440:.1f} min  P {p[2]:.6f} +- {e[2]:.6f}  chi2 {np.sum((r/s)**2):.2f}/{len(t)-3}')
P, sP = p[2], e[2]
gP, gsP = 23.323742864662634, 0.009492028
print(f'Gaia P {gP:.5f}+-{gsP:.5f}: delta {P-gP:+.5f} = {(P-gP)/np.hypot(gsP, sP):+.2f} sigma')
dph = ((p[1] - p[0]) / P) % 1; sdph = np.sqrt(C[0, 0] + C[1, 1] - 2 * C[0, 1]) / P
ecw = (dph - 0.5) * np.pi / 2
print(f'B-A phase sep {dph:.5f} +- {sdph:.5f}  -> e cos w = {ecw:.4f} +- {sdph*np.pi/2:.4f}  (first order; Gaia MC -0.0345+-0.0288, nominal -0.0411; Gaia phase sep 0.4738, MC 0.478+-0.018)')
# conjunction comparison
cj = json.load(open('conj.json'))
for lab, T0 in (('A', p[0]), ('B', p[1])):
    for c in cj:
        if c[0] != lab: continue
        k = np.round((c[2] - T0) / P); obs = T0 + k * P
        if c[2] < 1650 or c[2] > 3890 or abs(k) > 0 and not any(abs(obs - x[0]) < 0.1 for x in A + B): continue
        print(f'  {lab} pred {c[2]:.3f} +- {c[3]:.3f}  obs {obs:.4f}  O-C(Gaia) {obs-c[2]:+.3f} d = {(obs-c[2])/c[3]:+.2f} sigma')
# e sin w from T14 (pipeline means)
TA = np.array([7.66, 7.56, 7.58, 7.49, 7.42, 7.46, 7.46, 7.52, 7.27]); TB = np.array([7.88, 7.60, 8.35, 7.95])  # per-event means of unflagged B fits in ecl.txt (s13: QLP,TSPOC,TARS,ELE; s27: QLP,SPOC,TSPOC; s67: QLP,SPOC,TSPOC,TARS; s94: QLP,SPOC,TARS)
print(f'T14 A {TA.mean():.2f} +- {TA.std()/np.sqrt(len(TA)):.2f} h; B {TB.mean():.2f} +- {TB.std()/np.sqrt(len(TB)):.2f} h -> e sin w ~ (TB-TA)/(TB+TA) = {(TB.mean()-TA.mean())/(TB.mean()+TA.mean()):+.3f} +- {np.hypot(TA.std()/np.sqrt(len(TA)), TB.std()/np.sqrt(len(TB)))/(TA.mean()+TB.mean()):.3f}  (Gaia MC +0.013+-0.032)')
print('next predicted (BTJD):')
for lab, T0 in (('A', p[0]), ('B', p[1])):
    for tt in np.arange(4300, 4500):
        pass
    k0 = int(np.ceil((4400 - T0) / P))
    for k in range(k0, k0 + 4):
        tk = T0 + k * P; sk = np.sqrt(C[0 if lab == 'A' else 1, 0 if lab == 'A' else 1] + k * k * C[2, 2] + 2 * k * C[0 if lab == 'A' else 1, 2])
        print(f'  {lab} E{k}: {tk:.4f} +- {sk*1440:.1f} min')
