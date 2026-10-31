"""Linear ephemeris of the A eclipses (QLP SAP q==0 times from ecl2.json; errors = max(formal, pipeline scatter)),
O-C, Gaia comparison with conj.json (conjmc.py, this star's own corr_vec). python ephem2.py"""
import json, numpy as np
E = {r['key']: r for r in json.load(open('ecl2.json'))}
t = np.array([E['QLP1']['t0'], E['QLP27']['t0'], E['QLP95']['t0']])
# pipeline scatter at s1 (QLP, eleanor, TASOC, TGLCap, TGLCpsf, own TESScut 3x3) -> per-event floor
s1 = np.array([1337.4310, 1337.4341, 1337.4702, 1337.4422, 1337.4453, 1337.44169]); fl = np.std(s1, ddof=1)
own = np.array([1337.44169, 2042.54908, 3893.49056])
e = np.sqrt(np.array([E[k]['et0'] for k in ('QLP1', 'QLP27', 'QLP95')]) ** 2 + fl ** 2)
print(f'pipeline scatter at s1: {fl*1440:.1f} min; per-event errors (min): {np.round(e*1440,1)}')
for lab, tt in (('QLP', t), ('own TESScut 3x3', own)):
    n = np.round((tt - tt[0]) / 29.386).astype(int); A = np.vstack([np.ones(3), n]).T; W = np.diag(1 / e ** 2)
    C = np.linalg.inv(A.T @ W @ A); p = C @ A.T @ W @ tt; oc = tt - A @ p; chi = np.sum((oc / e) ** 2)
    print(f'{lab}: epochs {n}  T0 {p[0]:.4f} +- {np.sqrt(C[0,0])*1440:.1f} min  P {p[1]:.5f} +- {np.sqrt(C[1,1]):.5f}  O-C (min) {np.round(oc*1440,1)}  chi2 {chi:.2f}/1')
    gP, gsP = 29.385742080749214, 0.013426122
    print(f'   vs Gaia P {gP:.5f}+-{gsP:.5f}: diff {p[1]-gP:+.5f} = {(p[1]-gP)/np.hypot(gsP, np.sqrt(C[1,1])):+.2f} sigma')
# aliases: other cycle counts
for N in (23, 24, 25):
    print(f'   alias N={N} between s1 and s27: P {(t[1]-t[0])/N:.4f}  -> ({(t[1]-t[0])/N-29.3857:+.3f} d vs Gaia = {((t[1]-t[0])/N-29.3857)/0.0134:+.0f} sigma)')
cj = json.load(open('conj.json')); 
for tt in t:
    c = min([r for r in cj if r[0] == 'A'], key=lambda r: abs(r[2] - tt))
    print(f'A obs {tt:.3f} vs Gaia A k={c[1]} {c[2]:.3f} +- {c[3]:.3f}: {tt-c[2]:+.3f} d = {(tt-c[2])/c[3]:+.2f} sigma')
