"""Step 5: mass function, m2, a; limb-darkened sphere fit of the 4 A eclipses with Gaia e,w fixed (and varied), giving
a/R1, k=R2/R1, b_A; then the B-conjunction impact parameter and whether a B eclipse can happen. python -X utf8 physics.py"""
import sys, json, numpy as np
sys.path.insert(0, '.'); import vetlib as v
P = 28.04921; e0, w0 = 0.5113, np.radians(83.98); K = 39.92
G = 6.674e-11; Ms = 1.989e30; Rs = 6.957e8
f = (P * 86400) * (K * 1e3) ** 3 * (1 - e0 ** 2) ** 1.5 / (2 * np.pi * G) / Ms
print(f'mass function f(M) = {f:.4f} Msun')
for M1 in (1.2, 1.4, 1.6):
    m2 = 0.1
    for _ in range(200): m2 = (f * (M1 + m2) ** 2) ** (1 / 3)
    a = ((G * (M1 + m2) * Ms * (P * 86400) ** 2) / (4 * np.pi ** 2)) ** (1 / 3) / Rs
    print(f'  M1 {M1}: m2(i=90) {m2:.3f} Msun; a {a:.1f} Rsun; r_A {a*(1-e0**2)/(1+e0*np.sin(w0)):.1f}, r_B {a*(1-e0**2)/(1-e0*np.sin(w0)):.1f} Rsun')
u1, u2 = 0.32, 0.27
rg = (np.arange(400) + 0.5) / 400; I = 1 - u1 * (1 - np.sqrt(1 - rg ** 2)) - u2 * (1 - np.sqrt(1 - rg ** 2)) ** 2
Ftot = np.sum(I * 2 * np.pi * rg) / 400
def occ(z, k):
    z = np.atleast_1d(z)[:, None]; r = rg[None, :]
    c = np.clip((r ** 2 + z ** 2 - k ** 2) / (2 * r * np.maximum(z, 1e-9)), -1, 1); th = np.arccos(c)
    th = np.where(z + r <= k, np.pi, th); th = np.where(r - z >= k, 0, th)
    return 1 - np.sum(I * 2 * r * th, 1) / 400 / Ftot
def kep(M, e):
    E = M.copy()
    for _ in range(30): E = E - (E - e * np.sin(E) - M) / (1 - e * np.cos(E))
    return 2 * np.arctan2(np.sqrt(1 + e) * np.sin(E / 2), np.sqrt(1 - e) * np.cos(E / 2))
def zsep(t, tA, aR, cosi, e, w):
    nuA = np.pi / 2 - w; EA = 2 * np.arctan(np.sqrt((1 - e) / (1 + e)) * np.tan(nuA / 2)); MA = EA - e * np.sin(EA)
    M = MA + 2 * np.pi * (t - tA) / P; nu = kep(M, e); r = aR * (1 - e ** 2) / (1 + e * np.cos(nu))
    return r * np.sqrt(1 - np.sin(nu + w) ** 2 * (1 - cosi ** 2))
M = json.load(open('meas.json')); E = json.load(open('ephem.json'))
segs = []
for s, key, texp in ((26, '26_all', 1800), (53, '53_q0', 600), (79, '79_q0', 200), (80, '80_q0', 200)):
    d = [v.load_qlp(fn) for fn in v.qlp_files(275065610) if f'_s0{s}' in fn][0]
    use = np.ones_like(d['q'], bool) if key.endswith('all') else d['q'] == 0
    m = use & (np.abs(d['t'] - M[key]['t0']) < 0.7); n = max(1, int(round(texp / 200)))
    segs.append((d['t'][m], d['f'][m], M[key]['t0'], ((np.arange(n) + .5) / n - .5) * texp / 86400, M[key]['rms']))
def lc(t, tc, aR, k, cosi, e, w, off):
    tt = (t[:, None] + off[None, :]).ravel()
    return occ(zsep(tt, tc, aR, cosi, e, w), k).reshape(len(t), -1).mean(1)
def chi(p, e=e0, w=w0, ret=False):
    aR, k, b, dt = p
    if aR < 3 or k <= 0.02 or k > 0.8 or b < 0 or b > 1 + k: return 1e30
    rA = aR * (1 - e ** 2) / (1 + e * np.sin(w)); cosi = b / rA
    c2 = 0; out = []
    for t, fl, t0, off, rms in segs:
        mm = lc(t, t0 + dt, aR, k, cosi, e, w, off); x = t - t0
        A = mm[:, None] * np.c_[np.ones_like(x), x, x * x]; c, *_ = np.linalg.lstsq(A, fl, rcond=None)
        r = fl - A @ c; c2 += np.sum(r ** 2) / rms ** 2; out.append(np.std(r))
    return (c2, out) if ret else c2
best = None
for aR0 in (6, 10, 15, 22):
    for b0 in (0.3, 0.6, 0.85):
        p, c = v.nm(chi, [aR0, 0.25, b0, 0.0], [2, .05, .1, .002], it=1500)
        if best is None or c < best[1]: best = (p, c)
p, c2 = best
for _ in range(2): p, c2 = v.nm(chi, p, [.5, .02, .03, .001], it=1500)
aR, k, b, dt = p; rA = aR * (1 - e0 ** 2) / (1 + e0 * np.sin(w0)); rB = aR * (1 - e0 ** 2) / (1 - e0 * np.sin(w0))
cosi = b / rA; bB = rB * cosi
print(f'best: a/R1 {aR:.2f}, k {k:.3f}, b_A {b:.3f} (R1 units), i {np.degrees(np.arccos(cosi)):.2f} deg, dt {dt*1440:+.1f} min, chi2 {c2:.0f} (N {sum(len(s[0]) for s in segs)})')
print(f'  -> b_B = {bB:.2f} R1 vs contact limit 1+k = {1+k:.2f}: B eclipse {"possible" if bB < 1 + k else "IMPOSSIBLE"}')
rho = 3 * np.pi * aR ** 3 / (6.674e-8 * (P * 86400) ** 2)
print(f'  stellar density from a/R1 (q->0): {rho:.3f} g/cc = {rho/1.41:.3f} rho_sun; for M1+m2 ~ 2.1 Msun R1 ~ {(( (6.674e-11*2.1*1.989e30*(P*86400)**2)/(4*np.pi**2))**(1/3)/6.957e8)/aR:.2f} Rsun')
# profile: smallest b_A grid, minimum chi2 and B feasibility
print('profile over b_A (refit aR,k,dt):')
for bf in (0.0, 0.2, 0.4, 0.6, 0.8, 0.9, 1.0):
    q, cc = v.nm(lambda z: chi([z[0], z[1], bf, z[2]]), [aR, k, p[3]], [1, .03, .002], it=1500)
    rA_ = q[0] * (1 - e0 ** 2) / (1 + e0 * np.sin(w0)); bB_ = bf / rA_ * q[0] * (1 - e0 ** 2) / (1 - e0 * np.sin(w0))
    print(f'  b_A {bf:.1f}: dchi2 {cc-c2:+8.1f}  a/R1 {q[0]:6.2f} k {q[1]:.3f}  b_B {bB_:.2f} (1+k {1+q[1]:.2f})')
# B eclipse with Gaia e,w varied: what e sin w would let B happen?
print('B feasibility vs e sin w (b_B/b_A = (1+esw)/(1-esw)); need b_B < 1+k:', f'requires (1+esw)/(1-esw) < {(1+k)/b:.2f} -> esw < {((1+k)/b-1)/((1+k)/b+1):.3f}; Gaia esw 0.508+-0.008')
json.dump(dict(aR=aR, k=k, bA=b, bB=bB, cosi=cosi, dt=dt), open('physics.json', 'w'))
