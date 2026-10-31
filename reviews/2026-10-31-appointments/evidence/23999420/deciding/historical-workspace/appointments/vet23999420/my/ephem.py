"""Linear ephemerides for both eclipse kinds from my ecl.json (q==0), compare with Gaia (conj.json, conjmc full cov).
Then e cos w / e sin w from phase separation (exact Kepler solve) and duration ratio. python ephem.py"""
import json, numpy as np
E = [r for r in json.load(open('ecl.json')) if r['status'] == 'fit']
def lin(t, s, n):
    A = np.c_[np.ones_like(n), n]; W = 1 / s**2
    C = np.linalg.inv(A.T @ (A * W[:, None])); p = C @ (A.T @ (W * t)); r = t - A @ p
    chi = np.sum(r**2 * W); dof = len(t) - 2
    return p, np.sqrt(np.diag(C)), r, chi, dof
P0 = 22.1275; T0 = 2349.7517
for kind in 'PS':
    R = [r for r in E if r['kind'] == kind]
    t = np.array([r['t0'] for r in R]); s = np.array([r['t0_err'] for r in R])
    n = np.round((t - T0) / P0 - (0.4 if kind == 'S' else 0)); n = n.astype(float)
    if len(t) < 2: continue
    if len(t) == 2:
        P = (t[1] - t[0]) / (n[1] - n[0]); eP = np.hypot(*s) / (n[1] - n[0]); print(kind, 'two-point P', P, '+-', eP); continue
    p, e, r, chi, dof = lin(t, s, n); sc = max(1, np.sqrt(chi / dof))
    print(f'{kind}: T0 {p[0]:.5f} +- {e[0]*sc:.5f}  P {p[1]:.5f} +- {e[1]*sc:.5f} (chi2 {chi:.1f}/{dof}, errors x{sc:.2f})')
    for ti, si, ri in zip(t, s, r): print(f'   {ti:.4f} +- {si*1440:.1f} min  O-C {ri*1440:+.1f} min')
# Gaia comparisons
cj = json.load(open('../conj.json'))
for r in E:
    lab = 'A' if r['kind'] == 'P' else 'B'
    c = min((c for c in cj if c[0] == lab), key=lambda c: abs(c[2] - r['t0']))
    print(f"{r['kind']} {r['t0']:.3f} vs Gaia {lab} {c[2]:.3f} +- {c[3]:.3f}: {(r['t0']-c[2]):+.3f} d = {(r['t0']-c[2])/c[3]:+.2f} sigma")
