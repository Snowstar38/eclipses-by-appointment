"""Own two-sphere limb-darkened eclipse model (linear LD; U1 for star 1 = the star eclipsed at the deep 'P' eclipse,
U2 for star 2; no reflection/ellipsoidal; Keplerian relative orbit), fitted jointly to all QLP SAP eclipses of TIC 39013890
in s20 (1800 s, supersampled x9), s47 (600 s, x3), s60 (200 s, x1).
Free: tP (mid-time of P eclipse E=0), P, ecosw, esinw, cosi, r1=R1/a, r2=R2/a, J (central surface-brightness ratio 2/1).
Third light L3 (fraction of total) fixed by argument. w = argument of periastron of star 2 relative to star 1, so
star 2 is in front of star 1 at nu = 90 - w; with the Gaia RV primary = star 1 this w is Gaia's omega.
Data: per event, window +-0.6 d; baseline = linear fit to |dt| > 0.3 d; cadences q==0 ('q0') or all ('allq'),
then 5-sigma clipping on the residuals of a first fit.
python -X utf8 ebfit3.py <q0|allq> [L3] [esinw_fixed]  -> ebfit3_<tag>.json/.png"""
import json, os, sys, numpy as np, matplotlib
matplotlib.use('Agg'); import matplotlib.pyplot as plt
from astropy.io import fits
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from vetlib import nm
mode = sys.argv[1]; L3 = float(sys.argv[2]) if len(sys.argv) > 2 else 0.0
ESFIX = float(sys.argv[3]) if len(sys.argv) > 3 else None
U1, U2 = 0.45, 0.55
P0, T00, PH2 = 20.9235, 1859.0735, 0.4316
SS = {20: (1800, 9), 47: (600, 3), 60: (200, 1)}
T, F, K, EX = [], [], [], []
for sec in (20, 47, 60):
    d = fits.open(f'[local path omitted]')[1].data
    t = np.array(d['TIME'], float); f = np.array(d['SAP_FLUX'], float); q = np.array(d['QUALITY'], int)
    ok = np.isfinite(t) & np.isfinite(f) & (f > 0)
    if mode == 'q0': ok &= q == 0
    t, f = t[ok], f[ok]
    for kind, off in ((0, 0.0), (1, PH2)):
        for k in range(-2, 60):
            tc = T00 + (k + off) * P0
            w = np.abs(t - tc) < 0.6; o = w & (np.abs(t - tc) > 0.3)
            if (w & ~o).sum() < 5 or (o & (t < tc)).sum() < 4 or (o & (t > tc)).sum() < 4: continue
            c = np.polyfit(t[o] - tc, f[o], 1); fn_ = f[w] / np.polyval(c, t[w] - tc)
            T.append(t[w]); F.append(fn_); K.append(np.full(w.sum(), kind)); EX.append(np.full(w.sum(), sec))
            print(f's{sec} kind {kind} tc {tc:.2f} n {w.sum()} (in-ecl {(w & ~o).sum()})')
t, f, kk, ex = map(np.concatenate, (T, F, K, EX))
rg = (np.arange(200) + 0.5) / 200


def blocked(R, p, d, U):
    r = rg * R; I = 1 - U * (1 - np.sqrt(1 - rg ** 2)); dr = R / 200
    tot = np.sum(I * 2 * np.pi * r) * dr
    d = np.atleast_1d(d)[:, None]
    with np.errstate(invalid='ignore', divide='ignore'):
        c = (r ** 2 + d ** 2 - p ** 2) / (2 * r * d)
    ang = np.where(c <= -1, 2 * np.pi, np.where(c >= 1, 0.0, 2 * np.arccos(np.clip(c, -1, 1))))
    return (np.sum(I * ang * r, 1) * dr) / tot


def kepler(M, e):
    E = M.copy()
    for _ in range(25): E = E - (E - e * np.sin(E) - M) / (1 - e * np.cos(E))
    return E


def lc0(par, tt):
    tP, P, ec, es, ci, r1, r2, J = par
    e = np.hypot(ec, es); w = np.arctan2(es, ec)
    nuP = np.pi / 2 - w; EP = 2 * np.arctan(np.sqrt((1 - e) / (1 + e)) * np.tan(nuP / 2)); MP = EP - e * np.sin(EP)
    E = kepler(2 * np.pi * (tt - tP) / P + MP, e)
    nu = 2 * np.arctan2(np.sqrt(1 + e) * np.sin(E / 2), np.sqrt(1 - e) * np.cos(E / 2)); r = 1 - e * np.cos(E)
    X = r * np.cos(nu + w); Y = r * np.sin(nu + w) * ci; Z = r * np.sin(nu + w)
    dd = np.hypot(X, Y)
    L1 = r1 ** 2 * (1 - U1 / 3); L2 = J * r2 ** 2 * (1 - U2 / 3)
    out = np.ones_like(tt) * (L1 + L2)
    m = (Z > 0) & (dd < r1 + r2); out[m] -= L1 * blocked(r1, r2, dd[m], U1)
    m = (Z <= 0) & (dd < r1 + r2); out[m] -= L2 * blocked(r2, r1, dd[m], U2)
    return (1 - L3) * out / (L1 + L2) + L3


def lc(par, tt=None, exx=None):
    tt = t if tt is None else tt; exx = ex if exx is None else exx
    out = np.empty_like(tt)
    for s, (texp, n) in SS.items():
        m = exx == s
        if not m.any(): continue
        off = ((np.arange(n) + 0.5) / n - 0.5) * texp / 86400
        out[m] = lc0(par, (tt[m][:, None] + off[None, :]).ravel()).reshape(-1, n).mean(1)
    return out


use = np.ones_like(t, bool); wt = np.ones_like(t)


def full(p):
    p = np.array(p, float)
    if ESFIX is not None: p[3] = ESFIX
    return p


def chi(p):
    p = full(p); tP, P, ec, es, ci, r1, r2, J = p
    if not (0 <= ci < 0.2 and 0.003 < r1 < 0.2 and 0.002 < r2 < 0.2 and 0.0 < J < 3 and np.hypot(ec, es) < 0.8): return 1e30
    return np.sum(((f - lc(p)) * wt)[use] ** 2)


def fit(starts):
    best = None
    for p0 in starts:
        b, c2 = nm(chi, p0, [0.003, 0.0005, 0.01, 0.03, 0.005, 0.004, 0.003, 0.05], it=2500)
        if best is None or c2 < best[1]: best = (b, c2)
    b, c2 = best
    for _ in range(3): b, c2 = nm(chi, b, [0.0005, 0.0001, 0.003, 0.01, 0.001, 0.001, 0.0005, 0.01], it=3000)
    return full(b), c2


starts = [[T00, P0, -0.10, es, ci, 0.03, 0.0105, J] for es in (0.0, 0.18) for ci in (0.005, 0.02) for J in (0.15, 0.4)]
b, c2 = fit(starts)
res_ = f - lc(b)
for s in SS:
    m = ex == s; wt[m] = 1 / (1.4826 * np.median(np.abs(res_[m] - np.median(res_[m]))))
use = np.abs(res_ * wt) < 5
print('clipped', (~use).sum(), 'of', len(t))
b, c2 = fit([b])
npar = 8 - (ESFIX is not None)
red = c2 / (use.sum() - npar)
print('chi2', c2, 'N', use.sum(), 'reduced', red)
names = ['tP', 'P', 'ecosw', 'esinw', 'cosi', 'r1', 'r2', 'J']
free = [i for i in range(8) if not (ESFIX is not None and i == 3)]
h = np.array([2e-5, 2e-6, 1e-4, 2e-3, 2e-4, 1e-4, 1e-4, 5e-3]); H = np.zeros((8, 8))
for i in free:
    for j in free:
        if j < i: continue
        v = []
        for si, sj in ((1, 1), (1, -1), (-1, 1), (-1, -1)):
            pp = b.copy(); pp[i] += si * h[i]; pp[j] += sj * h[j]; v.append(chi(pp))
        H[i, j] = H[j, i] = (v[0] - v[1] - v[2] + v[3]) / (4 * h[i] * h[j])
err = np.zeros(8); C = np.zeros((8, 8))
try:
    Cf = np.linalg.inv(H[np.ix_(free, free)] / 2) * max(1, red)
    C[np.ix_(free, free)] = Cf; err = np.sqrt(np.abs(np.diag(C)))
except Exception as ex_: print('Hessian failed', ex_)
for n, v, s in zip(names, b, err): print(f'  {n:6s} {v:.6f} +- {s:.6f}')
e = np.hypot(b[2], b[3]); w = np.degrees(np.arctan2(b[3], b[2])) % 360; inc = np.degrees(np.arccos(b[4]))
L2L1 = b[7] * (b[6] / b[5]) ** 2 * (1 - U2 / 3) / (1 - U1 / 3)
nuA = np.pi / 2 - np.radians(w); nuB = 1.5 * np.pi - np.radians(w)
rA = (1 - e ** 2) / (1 + e * np.cos(nuA)); rB = (1 - e ** 2) / (1 + e * np.cos(nuB))
bA = rA * b[4] / b[5]; bB = rB * b[4] / b[5]
print(f'  e {e:.4f} w {w:.2f} deg i {inc:.3f} k=r2/r1 {b[6]/b[5]:.4f} L2/L1(TESS) {L2L1:.4f}; impact in R1 at A {bA:.3f}, at B {bB:.3f}; 1+k = {1+b[6]/b[5]:.3f}; 1-k = {1-b[6]/b[5]:.3f}')
out = dict(zip(names, b.tolist()), err=err.tolist(), cov=C.tolist(), e=e, w=w, inc=inc, k=b[6] / b[5], L2L1=L2L1, bA=bA, bB=bB,
           chi2=c2, N=int(use.sum()), red=red, L3=L3, mode=mode, esfix=ESFIX)
tt = np.linspace(b[0] - 1, b[0] + b[1] - 1, 600000); m = lc0(b, tt); dips = m < 1 - 1e-6
edges = np.flatnonzero(np.diff(dips.astype(int))); seg = [(tt[edges[i] + 1], tt[edges[i + 1]]) for i in range(0, len(edges) - 1, 2)]
out['model_eclipses'] = []
for a_, z_ in seg:
    mm = (tt > a_) & (tt < z_); mid = 0.5 * (a_ + z_)
    dep = 1 - m[mm].min(); fl = (m[mm] < m[mm].min() + 0.002 * dep).sum() * (tt[1] - tt[0]) * 24
    out['model_eclipses'].append(dict(phase=float(((mid - b[0]) / b[1]) % 1), T14_h=float((z_ - a_) * 24), depth=float(dep), flat_h=float(fl)))
    print(f'  model eclipse: phase {((mid - b[0]) / b[1]) % 1:.5f} T14 {(z_ - a_)*24:.3f} h depth {dep*100:.3f}% near-flat (within 0.2% of depth) {fl:.2f} h')
# per-sector residual rms in eclipse
for s in SS:
    for kind in (0, 1):
        m_ = use & (ex == s) & (kk == kind) & (lc(b) < 1 - 1e-4)
        if m_.any(): print(f'  s{s} kind {kind}: in-eclipse residual mean {np.mean((f - lc(b))[m_])*1e3:+.2f} ppt rms {np.std((f - lc(b))[m_])*1e3:.2f} ppt (n {m_.sum()})')
tag = f'{mode}_L{L3:g}' + (f'_es{ESFIX:g}' if ESFIX is not None else '')
json.dump(out, open(os.path.join(HERE, f'ebfit3_{tag}.json'), 'w'), indent=1)
fig, ax = plt.subplots(2, 2, figsize=(13, 8), sharex='col', gridspec_kw=dict(height_ratios=[3, 1]))
ph2m = out['model_eclipses'][1]['phase'] if len(out['model_eclipses']) > 1 else PH2
for j, (kind, off) in enumerate(((0, 0.0), (1, ph2m))):
    for s, c in ((20, 'C0'), (47, 'C1'), (60, 'C2')):
        m_ = (kk == kind) & (ex == s) & use; ph = ((t[m_] - b[0]) / b[1] - off + 0.5) % 1 - 0.5
        ax[0, j].plot(ph * b[1] * 24, f[m_], '.', ms=3, color=c, label=f's{s}')
        ax[1, j].plot(ph * b[1] * 24, (f - lc(b))[m_], '.', ms=3, color=c)
    tm = b[0] + off * b[1] + np.linspace(-0.6, 0.6, 3000)
    ax[0, j].plot((tm - b[0] - off * b[1]) * 24, lc0(b, tm), 'k-', lw=1)
    ax[1, j].set_xlabel('hours'); ax[0, j].set_title(['P (A)', 'S (B)'][kind] + f' {tag}'); ax[0, j].legend()
plt.tight_layout(); plt.savefig(os.path.join(HERE, f'ebfit3_{tag}.png'), dpi=70)
