"""Linear ephemeris for the A eclipses (QLP q==0 fits from ecl.json, plus a pipeline-scatter error floor), O-C,
comparison with Gaia P and the conjunction MC (conj.json, this star's corr_vec). python ephem.py -> ephem.txt"""
import json, numpy as np
E = json.load(open('ecl.json')); C = json.load(open('conj.json'))
ev = {}
for r in E:
    if r['key'].startswith('TGLCnb') or r['key'].endswith('all'): continue
    ev.setdefault(round(r['tc']), []).append(r)
T, S = [], []
for k in sorted(ev):
    rs = ev[k]; q = [r for r in rs if r['key'].startswith('QLP')][0]
    sc = np.std([r['t0'] for r in rs]); e = np.hypot(q['et0'], sc)
    T.append(q['t0']); S.append(e)
    print(f"A {q['t0']:.5f}  QLP err {q['et0']*1440:.1f} min, pipeline scatter {sc*1440:.1f} min ({len(rs)} pipelines) -> {e*1440:.1f} min")
T, S = np.array(T), np.array(S)
P0 = 33.67; n = np.round((T - T[0]) / P0)
A = np.vstack([np.ones_like(n), n]).T; W = np.diag(1 / S ** 2)
cov = np.linalg.inv(A.T @ W @ A); p = cov @ A.T @ W @ T
oc = T - A @ p; chi2 = np.sum((oc / S) ** 2)
print(f"cycles {n}  T0 {p[0]:.5f} +- {np.sqrt(cov[0,0])*1440:.2f} min  P {p[1]:.6f} +- {np.sqrt(cov[1,1]):.6f}  chi2 {chi2:.2f}/{len(T)-2}")
print('O-C (min):', np.round(oc * 1440, 2))
Pg, sPg = 33.64988642140199, 0.021282138
print(f"Gaia P {Pg:.5f} +- {sPg:.5f} -> Delta {p[1]-Pg:+.5f} d = {(p[1]-Pg)/sPg:+.2f} sigma")
for t, s in zip(T, S):
    c = min([c for c in C if c[0] == 'A'], key=lambda c: abs(c[2] - t))
    print(f"  A obs {t:.3f} vs Gaia A k={c[1]} {c[2]:.3f} +- {c[3]:.3f}: {t-c[2]:+.3f} d = {(t-c[2])/c[3]:+.2f} sigma")
json.dump(dict(T0=p[0], P=p[1], sT0=float(np.sqrt(cov[0, 0])), sP=float(np.sqrt(cov[1, 1])), cov=cov.tolist(), T=T.tolist(), S=S.tolist(), n=n.tolist()), open('ephem.json', 'w'))
