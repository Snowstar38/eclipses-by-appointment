"""Trapezoid fits (vetlib.fit_trap, quadratic baseline) to every A event in each pipeline, raw flux.
s007 partial: shape (depth,T14,T12) fixed at the mean of the s87/s88 QLP fits, t0 + baseline free.
python ecl.py -> ecl.json, ecl.txt (stdout), ecl_fits.png"""
import json, os, sys, glob, numpy as np, matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
from astropy.io import fits
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from vetlib import fit_trap, t0_error, model, nm
D = '[local path omitted]'; V = D + 'vet64066759/'
def F(k):
    p, s = k[:-2], int(k[-2:])
    if p == 'QLP': return D + f'64066759_s{s:03d}.fits', 'SAP_FLUX', 'QUALITY', 'SAP_BKG', 'SAP_X', 'SAP_Y'
    if p == 'TARS': return glob.glob(V + f'hlsp_tars*s{s:04d}*')[0], 'FLUX', None, None, None, None
    if p == 'TSPOC': return glob.glob(V + f'hlsp_tess-spoc*s{s:04d}*')[0], 'SAP_FLUX', 'QUALITY', 'SAP_BKG', 'MOM_CENTR1', 'MOM_CENTR2'
    if p == 'ELE': return glob.glob(V + '*eleanor*')[0], 'RAW_FLUX', 'QUALITY', 'FLUX_BKG', 'X_CENTROID', 'Y_CENTROID'
def load(key, allq):
    fn, fc, qc, bc, xc, yc = F(key)
    d = fits.open(fn)[1].data; t = np.array(d['TIME'], float); f = np.array(d[fc], float); n = len(t)
    g = lambda c: np.array(d[c], float) if c else np.full(n, np.nan)
    q = np.array(d[qc], int) if qc else np.zeros(n, int); bk, x, y = g(bc), g(xc), g(yc)
    ok = np.isfinite(t) & np.isfinite(f) & (f > 0)
    if not allq: ok &= q == 0
    return t[ok], f[ok], q[ok], bk[ok], x[ok], y[ok]
JOBS = [(3674.52, k) for k in ('QLP87', 'QLP87all', 'TARS87')] + [(3715.46, k) for k in ('QLP88', 'QLP88all', 'TARS88')]
JOBS7 = [(1504.83, k) for k in ('QLP07all', 'TSPOC07all', 'TARS07', 'ELE07all')]
out = []; fig, axs = plt.subplots(2, 5, figsize=(22, 8)); axs = axs.ravel(); i = 0
def stats(t, f, q, bk, x, y, b):
    inn = np.abs(t - b[0]) < max(b[2] / 2 - b[3], b[2] / 4); outw = (np.abs(t - b[0]) > b[2] / 2 + 0.05)
    r = {}
    for nm_, a in (('bkg', bk), ('x', x), ('y', y)):
        r['d' + nm_] = float(np.nanmedian(a[inn]) - np.nanmedian(a[outw])) if np.isfinite(a).any() else None
        r['s' + nm_] = float(np.nanstd(a[outw])) if np.isfinite(a).any() else None
    r['nflag_in'] = int((q[np.abs(t - b[0]) < b[2] / 2] != 0).sum()); r['nin'] = int((np.abs(t - b[0]) < b[2] / 2).sum())
    return r
def beta_of(res, t, s):
    dt = np.median(np.diff(t)); nb = max(1, int(round((1 / 24) / dt))); nn = len(res) // nb
    return max(1.0, np.std(res[:nn * nb].reshape(nn, nb).mean(1)) / (s / np.sqrt(nb))) if nn > 5 and nb > 1 else 1.0
for tc, key in JOBS:
    allq = key.endswith('all'); k = key[:-3] if allq else key
    t, f, q, bk, x, y = load(k, allq); w = np.abs(t - tc) < 0.8
    t, f, q, bk, x, y = t[w], f[w], q[w], bk[w], x[w], y[w]; f = f / np.median(f)
    b, c2, s, tr = fit_trap(t, f, tc, 0.023, 0.14, 0.05)
    res = f - model(b, t, tr); beta = beta_of(res, t, s)
    e = t0_error(t, f, b, tr, s, half=0.03, n=301) * beta
    r = dict(kind='A', key=key, t0=b[0], et0=e, depth=b[1], T14_h=b[2] * 24, T12_h=b[3] * 24, flat_h=(b[2] - 2 * b[3]) * 24, rms=s, beta=beta, **stats(t, f, q, bk, x, y, b))
    out.append(r); print(' '.join(f'{kk}={vv:.6g}' if isinstance(vv, float) else f'{kk}={vv}' for kk, vv in r.items()))
    a = axs[i]; i += 1; a.plot(t, f, 'k.', ms=2); a.plot(t[q != 0], f[q != 0], 'r.', ms=2)
    tt = np.linspace(t.min(), t.max(), 1000); a.plot(tt, model(b, tt, tr), 'c-'); a.set_title(f'{key} {b[0]:.4f}', fontsize=9)
q0 = [r for r in out if r['key'] in ('QLP87', 'QLP88')]
dep, T14, T12 = [np.mean([r[k] for r in q0]) for k in ('depth', 'T14_h', 'T12_h')]; T14 /= 24; T12 /= 24
print(f'template from QLP87/88 q0: depth {dep*100:.3f}% T14 {T14*24:.2f} h T12 {T12*24:.2f} h')
for tc, key in JOBS7:
    allq = key.endswith('all'); k = key[:-3] if allq else key
    t, f, q, bk, x, y = load(k, allq); w = np.abs(t - tc) < 1.0
    t, f, q, bk, x, y = t[w], f[w], q[w], bk[w], x[w], y[w]; f = f / np.median(f)
    def chi(p, scale=1.0):
        return np.sum((f - model([p[0], dep * p[3] * scale, T14, T12, p[1], p[2], 0.0], t, tc)) ** 2)
    def chi_fixdep(p): return np.sum((f - model([p[0], dep, T14, T12, p[1], p[2], 0.0], t, tc)) ** 2)
    best, c2 = nm(chi_fixdep, [tc, 1.0, 0.0], [0.02, 0.002, 0.001]); best, c2 = nm(chi_fixdep, best, [0.005, 0.001, 0.0005])
    bf = [best[0], dep, T14, T12, best[1], best[2], 0.0]; res = f - model(bf, t, tc); s = np.std(res)
    ts = best[0] + np.linspace(-0.05, 0.05, 401); cc = []
    for tt_ in ts:
        bb, c = nm(lambda p: chi_fixdep([tt_, p[0], p[1]]), best[1:], [0.001, 0.0005]); cc.append(c / s ** 2)
    cc = np.array(cc) - min(cc); ok = ts[cc <= 1]; e = (ok.max() - ok.min()) / 2
    # free-depth variant
    b2, c22 = nm(lambda p: np.sum((f - model([p[0], p[3], T14, T12, p[1], p[2], 0.0], t, tc)) ** 2), [best[0], best[1], best[2], dep], [0.01, 0.001, 0.0005, 0.003])
    r = dict(kind='A', key=key, t0=best[0], et0=e, depth=dep, T14_h=T14 * 24, T12_h=T12 * 24, rms=s, n_in=int((np.abs(t - best[0]) < T14 / 2).sum()),
             nflag_in=int((q[np.abs(t - best[0]) < T14 / 2] != 0).sum()), t0_freedepth=b2[0], depth_free=b2[3], first_t=float(t[t > 1504.5].min()))
    out.append(r); print(' '.join(f'{kk}={vv:.6g}' if isinstance(vv, float) else f'{kk}={vv}' for kk, vv in r.items()))
    a = axs[i]; i += 1; a.plot(t, f, 'k.', ms=3); a.plot(t[q != 0], f[q != 0], 'r.', ms=3)
    tt = np.linspace(t.min(), t.max(), 1000); a.plot(tt, model(bf, tt, tc), 'c-'); a.set_xlim(1504.5, 1505.2); a.set_title(f'{key} {best[0]:.4f}', fontsize=9)
plt.tight_layout(); plt.savefig('ecl_fits.png', dpi=55)
json.dump(out, open('ecl.json', 'w'), indent=1)
