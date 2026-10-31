"""Linear ephemeris for the A eclipses (QLP q0 times for s87/s88; s007 = mean of 4 pipelines, error = max(pipeline spread, 3 min)
for the fixed-shape partial fit). Compares with Gaia P and conjmc predictions. python ephem.py -> ephem.txt"""
import json, numpy as np
E = {r['key']: r for r in json.load(open('ecl.json'))}
s7 = [E[k]['t0'] for k in ('QLP07all', 'TSPOC07all', 'TARS07', 'ELE07all')]
t = np.array([np.mean(s7), E['QLP87']['t0'], E['QLP88']['t0']]); e = np.array([max(np.std(s7), 3 / 1440), E['QLP87']['et0'], E['QLP88']['et0']])
print('s007 pipelines', ['%.5f' % x for x in s7], 'sd %.1f min' % (np.std(s7) * 1440))
P0 = t[2] - t[1]; n = np.round((t - t[1]) / P0).astype(int); print('epochs', n, 'P from s87/88 alone %.4f +- %.4f' % (P0, np.hypot(e[1], e[2])))
A = np.vstack([np.ones(3), n]).T; W = np.diag(1 / e ** 2); C = np.linalg.inv(A.T @ W @ A); p = C @ A.T @ W @ t
oc = t - A @ p; chi2 = np.sum((oc / e) ** 2)
print(f'T0(E=0, s87) {p[0]:.5f} +- {np.sqrt(C[0,0])*1440:.1f} min  P {p[1]:.5f} +- {np.sqrt(C[1,1]):.5f} d  chi2 {chi2:.2f}/1')
print('O-C min', np.round(oc * 1440, 2))
Pg, sPg = 40.92664903, 0.016201613
print(f'Gaia P {Pg:.5f}+-{sPg:.5f}: delta {p[1]-Pg:+.4f} d = {(p[1]-Pg)/sPg:+.2f} sigma')
pred = {1504.655: 0.345, 3673.769: 1.200, 3714.696: 1.217}
for (pt, ps), ob in zip(pred.items(), t): print(f'  obs {ob:.4f} vs Gaia A {pt:.3f}+-{ps:.3f}: {ob-pt:+.3f} d = {(ob-pt)/ps:+.2f} sigma')
T0, P = p[0], p[1]; sT, sP = np.sqrt(C[0, 0]), np.sqrt(C[1, 1])
print('Next A (BTJD):', ', '.join(f'{T0 + k*P:.3f}+-{np.sqrt(sT**2 + (k*sP)**2 + 2*k*C[0,1])*1440:.0f}min' for k in range(17, 22)))
json.dump(dict(T0=T0, P=P, sT0=sT, sP=sP, cov=C.tolist()), open('ephem.json', 'w'))
