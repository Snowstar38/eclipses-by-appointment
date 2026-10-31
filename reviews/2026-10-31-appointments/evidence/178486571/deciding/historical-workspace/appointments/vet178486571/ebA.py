"""Limb-darkened two-sphere fit (functions from ebfit3.py: linear LD, Keplerian) to the three A eclipses (QLP SAP q==0;
s7 1800 s x9, s33 600 s x3, s87 200 s x1). e, w fixed at Gaia (or by argument); J fixed (only A observed).
Free: tP, P, cosi, r1, r2. Reports impact parameters at A and B and the model B eclipse for J values.
python ebA.py [ecosw esinw]  -> ebA_<tag>.json/.png"""
import json, os, sys, numpy as np, matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
from astropy.io import fits
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from vetlib import nm
U1, U2 = 0.40, 0.60
eg, wg = 0.5498732678339298, np.radians(16.980629667204354)
EC, ES = (float(sys.argv[1]), float(sys.argv[2])) if len(sys.argv) > 2 else (eg * np.cos(wg), eg * np.sin(wg))
SS = {7: (1800, 9), 33: (600, 3), 87: (200, 1)}
TC = {7: 1494.7835, 33: 2201.8761, 87: 3683.4036}
T, F, EX = [], [], []
for s in SS:
    d = fits.open(f'[local path omitted]')[1].data
    t = np.array(d['TIME'], float); f = np.array(d['SAP_FLUX'], float); q = np.array(d['QUALITY'], int)
    ok = np.isfinite(t) & np.isfinite(f) & (q == 0); t, f = t[ok], f[ok]; tc = TC[s]
    w = np.abs(t - tc) < 0.7; o = w & (np.abs(t - tc) > 0.15)
    c = np.polyfit(t[o] - tc, f[o], 2 if s == 33 else 1); T.append(t[w]); F.append(f[w] / np.polyval(c, t[w] - tc)); EX.append(np.full(w.sum(), s))
t, f, ex = map(np.concatenate, (T, F, EX))
rg = (np.arange(200) + 0.5) / 200
def blocked(R, p, d, U):
    r = rg * R; I = 1 - U * (1 - np.sqrt(1 - rg ** 2)); dr = R / 200; tot = np.sum(I * 2 * np.pi * r) * dr
    d = np.atleast_1d(d)[:, None]
    with np.errstate(invalid='ignore', divide='ignore'): c = (r ** 2 + d ** 2 - p ** 2) / (2 * r * d)
    ang = np.where(c <= -1, 2 * np.pi, np.where(c >= 1, 0.0, 2 * np.arccos(np.clip(c, -1, 1))))
    return (np.sum(I * ang * r, 1) * dr) / tot
def kepler(M, e):
    E = M.copy()
    for _ in range(25): E = E - (E - e * np.sin(E) - M) / (1 - e * np.cos(E))
    return E
def lc0(par, tt, J=0.1):
    tP, P, ci, r1, r2 = par; ec, es = EC, ES
    e = np.hypot(ec, es); w = np.arctan2(es, ec)
    nuP = np.pi / 2 - w; EP = 2 * np.arctan(np.sqrt((1 - e) / (1 + e)) * np.tan(nuP / 2)); MP = EP - e * np.sin(EP)
    E = kepler(2 * np.pi * (tt - tP) / P + MP, e)
    nu = 2 * np.arctan2(np.sqrt(1 + e) * np.sin(E / 2), np.sqrt(1 - e) * np.cos(E / 2)); r = 1 - e * np.cos(E)
    X = r * np.cos(nu + w); Y = r * np.sin(nu + w) * ci; Z = r * np.sin(nu + w); dd = np.hypot(X, Y)
    L1 = r1 ** 2 * (1 - U1 / 3); L2 = J * r2 ** 2 * (1 - U2 / 3); out = np.ones_like(tt) * (L1 + L2)
    m = (Z > 0) & (dd < r1 + r2); out[m] -= L1 * blocked(r1, r2, dd[m], U1)
    m = (Z <= 0) & (dd < r1 + r2); out[m] -= L2 * blocked(r2, r1, dd[m], U2)
    return out / (L1 + L2)
def lc(par, J=0.1):
    out = np.empty_like(t)
    for s, (texp, n) in SS.items():
        m = ex == s; off = ((np.arange(n) + 0.5) / n - 0.5) * texp / 86400
        out[m] = lc0(par, (t[m][:, None] + off[None, :]).ravel(), J).reshape(-1, n).mean(1)
    return out
wt = np.ones_like(t)
KFIX = float(os.environ.get('KFIX', '0'))
def chi(p):
    tP, P, ci, r1, r2 = p
    if KFIX: p = [tP, P, ci, r1, KFIX * r1]; r2 = KFIX * r1
    if not (0 <= ci < 0.3 and 0.003 < r1 < 0.3 and 0.002 < r2 < 0.2): return 1e30
    return np.sum(((f - lc(p)) * wt) ** 2)
best = None
for ci in (0.01, 0.02, 0.03):
    for r1 in (0.025, 0.035, 0.05):
        for k in (0.2, 0.3, 0.5):
            b, c2 = nm(chi, [1494.7835, 33.67108, ci, r1, k * r1], [0.002, 0.00005, 0.003, 0.004, 0.003], it=1500)
            if best is None or c2 < best[1]: best = (b, c2)
b, c2 = best
for _ in range(3): b, c2 = nm(chi, b, [0.0005, 0.00001, 0.001, 0.001, 0.0005], it=2000)
for s, sg in ((7, 0.59e-3), (33, 0.93e-3), (87, 1.80e-3)): wt[ex == s] = 1 / sg   # per-sector rms of the free fit (fixed so chi2 compares across KFIX)
b, c2 = nm(chi, b, [0.0005, 0.00001, 0.001, 0.001, 0.0005], it=2000)
if KFIX: b = np.array(b); b[4] = KFIX * b[3]
res = f - lc(b)
e = np.hypot(EC, ES); w = np.arctan2(ES, EC)
rA = (1 - e ** 2) / (1 + e * np.cos(np.pi / 2 - w)); rB = (1 - e ** 2) / (1 + e * np.cos(1.5 * np.pi - w))
k = b[4] / b[3]; bA = rA * b[2] / b[3]; bB = rB * b[2] / b[3]
print(f'ecosw {EC:.4f} esinw {ES:.4f}: tP {b[0]:.5f} P {b[1]:.6f} cosi {b[2]:.5f} (i {np.degrees(np.arccos(b[2])):.3f}) r1 {b[3]:.5f} r2 {b[4]:.5f} k {k:.4f}  chi2 {c2:.1f} N {len(t)}')
print(f'  impact (R1 units) A {bA:.3f}, B {bB:.3f}; contact needs < 1+k = {1+k:.3f}  -> B eclipse {"YES" if bB < 1 + k else "NO (misses)"}')
for s in SS:
    m = ex == s; print(f'  s{s}: rms {np.std(res[m])*1e3:.2f} ppt')
tt = b[0] + np.linspace(-1, b[1] - 1, 400000)
for J in (0.05, 0.1, 0.15):
    m = lc0(b, tt, J); dips = m < 1 - 1e-6; ed = np.flatnonzero(np.diff(dips.astype(int)))
    for i in range(0, len(ed) - 1, 2):
        a_, z_ = tt[ed[i] + 1], tt[ed[i + 1]]; mm = (tt > a_) & (tt < z_)
        print(f'  J {J}: model eclipse at phase {((0.5*(a_+z_) - b[0]) / b[1]) % 1:.4f}  T14 {(z_-a_)*24:.2f} h  depth {(1-m[mm].min())*100:.3f}%')
json.dump(dict(par=b.tolist(), ecosw=EC, esinw=ES, k=k, bA=bA, bB=bB, chi2=c2), open(f'ebA_{EC:.3f}_{ES:.3f}_k{KFIX:g}.json', 'w'))
fig, ax = plt.subplots(1, 3, figsize=(15, 4))
for a, s in zip(ax, SS):
    m = ex == s; a.plot((t[m] - TC[s]) * 24, f[m], 'k.', ms=3); tm = np.linspace(-0.7, 0.7, 2000) + TC[s]
    a.plot((tm - TC[s]) * 24, lc0(b, tm), 'c-'); a.set_title(f's{s}')
plt.tight_layout(); plt.savefig(f'ebA_{EC:.3f}_{ES:.3f}_k{KFIX:g}.png', dpi=60)
