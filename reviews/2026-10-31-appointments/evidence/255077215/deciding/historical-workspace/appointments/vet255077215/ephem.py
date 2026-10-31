"""Linear ephemerides (A, B, joint common P), O-C, Gaia P and conjunction comparison (conj.json from conjmc.py with this
star's corr_vec), e cos w / e sin w from phase separation and durations (exact Kepler solve), next eclipses. python ephem.py"""
import json, numpy as np
P0 = 26.262
# event times: means over pipelines in ecl.txt; error = max(formal, pipeline scatter), s65 B inflated for common mode
A = [(1637.3433, 2.5), (2372.6850, 1.0), (3081.7607, 1.5), (4158.5019, 1.5)]
B = [(1645.3026, 6.0), (2380.6383, 4.0), (3089.7447, 15.0)]
def fit(ev, isB):
    t = np.array([x[0] for x in ev]); s = np.array([x[1] for x in ev]) / 1440
    ref = np.where(isB, 1645.3026, 1637.3433); n = np.round((t - ref) / P0)
    cols = [1 - isB, isB, n] if isB.any() and (~isB.astype(bool)).any() else [np.ones_like(n), n]
    X = np.vstack(cols).T; W = 1 / s ** 2; C = np.linalg.inv(X.T @ (X * W[:, None])); p = C @ X.T @ (W * t); r = t - X @ p
    return p, C, n, r, s
for lab, ev in (('A', A), ('B', B)):
    p, C, n, r, s = fit(ev, np.zeros(len(ev)) if lab == 'A' else np.ones(len(ev)))
    e = np.sqrt(np.diag(C)); print(f'{lab}: T0 {p[0]:.5f} +- {e[0]*1440:.1f} min  P {p[1]:.6f} +- {e[1]:.6f}  chi2 {np.sum((r/s)**2):.2f}/{len(ev)-2}')
    for nn, rr, x in zip(n, r, ev): print(f'   E{int(nn):3d} {x[0]:.4f} O-C {rr*1440:+6.1f} min (err {x[1]})')
isB = np.r_[np.zeros(len(A)), np.ones(len(B))]
p, C, n, r, s = fit(A + B, isB); e = np.sqrt(np.diag(C))
print(f'joint: T0A {p[0]:.5f} +- {e[0]*1440:.1f} min  T0B {p[1]:.5f} +- {e[1]*1440:.1f} min  P {p[2]:.6f} +- {e[2]:.6f}  chi2 {np.sum((r/s)**2):.2f}/{len(s)-3}')
for x, nn, rr in zip(A + B, n, r): print(f'   {x[0]:.4f} E{int(nn)} O-C {rr*1440:+.1f} min')
P, sP = p[2], e[2]; gP, gsP = 26.27034069020509, 0.064040445
print(f'Gaia P {gP:.4f} +- {gsP:.4f}: delta {P-gP:+.4f} d = {(P-gP)/np.hypot(gsP, sP):+.2f} sigma')
dph = ((p[1] - p[0]) / P) % 1; sdph = np.sqrt(C[0, 0] + C[1, 1] - 2 * C[0, 1]) / P
print(f'B-A phase separation {dph:.5f} +- {sdph:.5f}; first-order e cos w = {(dph-0.5)*np.pi/2:.4f}')
cj = json.load(open('conj.json'))
for lab, T0 in (('A', p[0]), ('B', p[1])):
    for c in cj:
        if c[0] != lab: continue
        k = np.round((c[2] - T0) / P); obs = T0 + k * P
        if any(abs(obs - x[0]) < 0.1 for x in A + B):
            print(f'  {lab} Gaia pred {c[2]:.3f} +- {c[3]:.3f}  obs {obs:.4f}  O-C {obs-c[2]:+.3f} d = {(obs-c[2])/c[3]:+.2f} sigma')
# exact solve: phase separation and duration ratio (equal chords, b effects ignored) -> e, w
TA, TB = 12.79, 10.0   # mean T14 (h): A from QLP39/TSPOC39/QLP65/QLP103/TSPOC12; B from TSPOC12/ELE12/QLP39/TSPOC39
def tconj(nu, e):
    E = 2 * np.arctan2(np.sqrt(1 - e) * np.sin(nu / 2), np.sqrt(1 + e) * np.cos(nu / 2)); return (E - e * np.sin(E)) / (2 * np.pi)
best = None
for ec in np.linspace(-0.6, 0.0, 601):
    for es in np.linspace(-0.4, 0.2, 601):
        ee = np.hypot(ec, es); w = np.arctan2(es, ec)
        if ee >= 0.9: continue
        ph = (tconj(1.5 * np.pi - w, ee) - tconj(np.pi / 2 - w, ee)) % 1
        rat = (1 + es) / (1 - es)   # T_B / T_A for equal chords (v_t ratio)
        c2 = ((ph - dph) / 0.0003) ** 2 + ((rat - TB / TA) / 0.03) ** 2
        if best is None or c2 < best[0]: best = (c2, ec, es, ee, np.degrees(w) % 360, ph, rat)
print(f'exact solve (equal impact chords): e cos w {best[1]:.4f}  e sin w {best[2]:.4f}  e {best[3]:.3f}  w {best[4]:.1f} deg  (phase {best[5]:.5f}, TB/TA {best[6]:.3f} vs {TB/TA:.3f})')
print('Gaia: e 0.341+-0.143, w 191.5+-24.6; MC e cos w -0.31+-0.14, e sin w -0.05+-0.14')
print('next predicted eclipses (BTJD):')
for lab, i in (('A', 0), ('B', 1)):
    T0 = p[i]; k0 = int(np.ceil((4400 - T0) / P))
    for k in range(k0, k0 + 5):
        sk = np.sqrt(C[i, i] + k * k * C[2, 2] + 2 * k * C[i, 2]); print(f'  {lab} E{k}: {T0 + k*P:.4f} +- {sk*1440:.1f} min')
