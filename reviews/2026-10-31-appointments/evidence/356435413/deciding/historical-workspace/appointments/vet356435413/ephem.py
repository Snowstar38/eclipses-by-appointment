"""B linear ephemeris from ecl.json (per-event mean over pipelines; QLP25 uses flagged cadences), O-C, Gaia P and
conjunction comparison (conj.json from conjmc.py, this star's corr_vec), A-window prediction = B ephemeris + Gaia
phase separation. -> ephem.txt"""
import json, numpy as np
E = json.load(open('ecl.json')); P0 = 27.4788
ev = {}
for r in E:
    s = r['key'].rstrip('al'); s = r['key'][:-3] if r['key'].endswith('all') else r['key']
    if r['key'].endswith('all') and not r['key'].startswith('QLP25') and not r['key'].startswith('TSPOC52'): continue
    ev.setdefault(r['tc'], []).append((r['t0'], r['et0'], r['depth'], r['T14_h'], r['T12_h'], r['key']))
T = []
for tc, L in sorted(ev.items()):
    t = np.array([x[0] for x in L]); e = np.array([x[1] for x in L])
    m = np.sum(t / e**2) / np.sum(1 / e**2); err = max(np.sqrt(1 / np.sum(1 / e**2)), np.std(t) / np.sqrt(len(t)) if len(t) > 1 else 0, 1/1440)
    T.append((m, err)); print(f"B {tc}: mean t0 {m:.5f} +- {err*1440:.1f} min over {[x[5] for x in L]}  spread {np.ptp(t)*1440:.1f} min  depth {np.mean([x[2] for x in L])*100:.2f}%  T14 {np.mean([x[3] for x in L]):.2f} h  T12 {np.mean([x[4] for x in L]):.2f} h")
t = np.array([x[0] for x in T]); s = np.array([x[1] for x in T]); n = np.round((t - t[0]) / P0)
X = np.vstack([np.ones_like(n), n]).T; W = 1 / s**2; C = np.linalg.inv(X.T @ (X * W[:, None])); p = C @ X.T @ (W * t); r = t - X @ p
print(f"B: T0 {p[0]:.5f} +- {np.sqrt(C[0,0])*1440:.1f} min  P {p[1]:.6f} +- {np.sqrt(C[1,1]):.6f}  chi2 {np.sum((r/s)**2):.2f}/{len(t)-2}")
for nn, rr, ss in zip(n, r, s): print(f"   E{int(nn):3d}  O-C {rr*1440:+6.2f} min  (err {ss*1440:.1f})")
gP, gsP = 27.4787767793643, 0.008121668
print(f"Gaia P {gP:.5f} +- {gsP:.5f}: delta {p[1]-gP:+.5f} d = {(p[1]-gP)/np.hypot(gsP, np.sqrt(C[1,1])):+.2f} sigma")
cj = json.load(open('conj.json'))
for c in cj:
    if c[0] == 'B' and any(abs(c[2] - x) < 3 for x in t):
        k = np.round((c[2] - p[0]) / p[1]); o = p[0] + k * p[1]; print(f"  B pred {c[2]:.3f} +- {c[3]:.3f}  obs {o:.4f}  O-C {o-c[2]:+.3f} d = {(o-c[2])/c[3]:+.2f} sigma")
json.dump(dict(T0=p[0], P=p[1], C=C.tolist()), open('ephemB.json', 'w'))
ph, sph = 0.7014, 0.0096   # Gaia MC B-A phase separation (conjmc.txt): A = B - 0.7014 P = B + 0.2986 P
print('A windows from B ephemeris + Gaia phase separation (A = B + (1-0.7014)P, sigma 0.0096 P = %.2f d):' % (sph * p[1]))
for k in range(-1, 60):
    tA = p[0] + (k + 1 - ph) * p[1]
    if 1983 < tA < 3480: print(f"   A {tA:.3f} +- {sph*p[1]:.2f}")
print('next predicted (BTJD), B with linear-ephemeris error; A with phase-separation error:')
for k in range(int(np.ceil((4300 - p[0]) / p[1])), int(np.ceil((4300 - p[0]) / p[1])) + 8):
    sk = np.sqrt(C[0,0] + k*k*C[1,1] + 2*k*C[0,1]); tA = p[0] + (k + 1 - ph) * p[1]
    print(f"   B E{k}: {p[0]+k*p[1]:.4f} +- {sk*1440:.1f} min      A(no eclipse expected): {tA:.2f} +- {sph*p[1]:.2f}")
