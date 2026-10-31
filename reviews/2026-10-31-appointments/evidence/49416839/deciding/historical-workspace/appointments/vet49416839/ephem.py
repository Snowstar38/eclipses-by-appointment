"""Linear ephemeris of the B eclipses (QLP fit where q==0 exists, else TESS-SPOC all-q; error = hypot(fit err, pipeline scatter)),
O-C, Gaia P and conjunction comparison (conj.json from conjmc.py with this star's corr_vec). python ephem.py -> ephem.txt, ephem.json"""
import json, numpy as np
E = json.load(open('ecl.json')); C = json.load(open('conj.json'))
ev = {}
for r in E:
    if r['key'] in ('QLP36all',) or r['depth'] > 0.05: continue
    ev.setdefault(round(r['tc']), []).append(r)
T, S = [], []
for k in sorted(ev):
    rs = ev[k]; pri = [r for r in rs if r['key'] in ('QLP36', 'QLP72', 'TSPOC9all')][0]
    sc = np.std([r['t0'] for r in rs]); e = np.hypot(pri['et0'], sc); T.append(pri['t0']); S.append(e)
    print(f"B {pri['t0']:.5f} ({pri['key']}) fit err {pri['et0']*1440:.1f} min, scatter {sc*1440:.1f} min over {len(rs)} -> {e*1440:.1f} min; depths {[round(r['depth']*100,2) for r in rs]}")
T, S = np.array(T), np.array(S); n = np.round((T - T[0]) / 21.43)
A = np.vstack([np.ones_like(n), n]).T; W = np.diag(1 / S ** 2); cov = np.linalg.inv(A.T @ W @ A); p = cov @ A.T @ W @ T
oc = T - A @ p; chi2 = np.sum((oc / S) ** 2)
print(f"cycles {n}; T0 {p[0]:.5f} +- {np.sqrt(cov[0,0])*1440:.2f} min; P {p[1]:.6f} +- {np.sqrt(cov[1,1]):.6f}; chi2 {chi2:.2f}/{len(T)-2}; O-C min {np.round(oc*1440,2)}")
Pg, sPg = 21.43248856986357, 0.008339295
print(f"Gaia P {Pg:.5f} +- {sPg:.5f}: Delta {p[1]-Pg:+.5f} d = {(p[1]-Pg)/sPg:+.2f} sigma")
for t in T:
    c = min([c for c in C if c[0] == 'B'], key=lambda c: abs(c[2] - t))
    print(f"  B obs {t:.3f} vs Gaia B k={c[1]} {c[2]:.3f} +- {c[3]:.3f}: {t-c[2]:+.3f} d = {(t-c[2])/c[3]:+.2f} sigma")
json.dump(dict(T0=p[0], P=p[1], cov=cov.tolist(), T=T.tolist(), S=S.tolist(), n=n.tolist()), open('ephem.json', 'w'))
