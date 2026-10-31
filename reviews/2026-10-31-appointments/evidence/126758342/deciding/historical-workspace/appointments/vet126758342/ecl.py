"""Trapezoid fits (vetlib.fit_trap, quadratic baseline) to every event, raw SAP in each pipeline.
t0 error: profile chi2 x red-noise beta. Also dBKG (own units), centroid shift, flagged count. python ecl.py -> ecl.json, ecl.txt, ecl_fits.png"""
import json, os, sys, numpy as np, matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
from astropy.io import fits
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from vetlib import fit_trap, t0_error, model
D = '[local path omitted]'; V = D + 'vet126758342/'
F = {'QLP15': D + '126758342_s015.fits', 'QLP41': D + '126758342_s041.fits', 'QLP55': D + '126758342_s055.fits',
     'TSPOC15': V + 'hlsp_tess-spoc_tess_phot_0000000126758342-s0015_tess_v1_lc.fits', 'TSPOC41': V + 'hlsp_tess-spoc_tess_phot_0000000126758342-s0041_tess_v1_lc.fits',
     'TSPOC55': V + 'hlsp_tess-spoc_tess_phot_0000000126758342-s0055_tess_v1_lc.fits',
     'TASOC15': V + 'hlsp_tasoc_tess_ffi_tic00126758342-s0015-cam1-ccd3-c1800_tess_v06_ens-lc.fits'}
def load(key, allq):
    with fits.open(F[key]) as h:
        d = h[1].data; c = d.columns.names
        t = np.array(d['TIME'], float)
        f = np.array(d['SAP_FLUX' if 'SAP_FLUX' in c else 'FLUX_RAW'], float)
        q = np.array(d['QUALITY'], int)
        bk = np.array(d['SAP_BKG' if 'SAP_BKG' in c else 'FLUX_BKG'], float)
        x = np.array(d['MOM_CENTR1' if 'MOM_CENTR1' in c else 'SAP_X'], float)
        y = np.array(d['MOM_CENTR2' if 'MOM_CENTR2' in c else 'SAP_Y'], float)
    ok = np.isfinite(t) & np.isfinite(f) & (f > 0)
    if not allq: ok &= q == 0
    return t[ok], f[ok], q[ok], bk[ok], x[ok], y[ok]
JOBS = [('B', 1729.54, k) for k in ('QLP15', 'QLP15all', 'TSPOC15', 'TASOC15')] + \
       [('B', 2438.51, k) for k in ('QLP41', 'QLP41all', 'TSPOC41')] + \
       [('B', 2804.44, k) for k in ('QLP55', 'QLP55all', 'TSPOC55')]
out = []; fig, axs = plt.subplots(2, 5, figsize=(22, 8)); axs = axs.ravel()
for i, (kind, tc, key) in enumerate(JOBS):
    allq = key.endswith('all'); k = key[:-3] if allq else key
    t, f, q, bk, x, y = load(k, allq)
    w = np.abs(t - tc) < 0.8
    if w.sum() < 20: print(kind, tc, key, 'no data'); continue
    t, f, q, bk, x, y = t[w], f[w], q[w], bk[w], x[w], y[w]; f = f / np.median(f)
    b, c2, s, tr = fit_trap(t, f, tc, 0.022, 0.2, 0.08)
    res = f - model(b, t, tr); dt = np.median(np.diff(t)); nb = max(1, int(round((1 / 24) / dt)))
    nn = len(res) // nb; beta = max(1.0, np.std(res[:nn * nb].reshape(nn, nb).mean(1)) / (s / np.sqrt(nb))) if nn > 5 and nb > 1 else 1.0
    e = t0_error(t, f, b, tr, s, half=0.05, n=301) * beta
    inn = np.abs(t - b[0]) < max(b[2] / 2 - b[3], b[2] / 4); outw = np.abs(t - b[0]) > b[2] / 2 + 0.05
    dbk = np.nanmedian(bk[inn]) - np.nanmedian(bk[outw]); sbk = np.nanstd(bk[outw])
    dx = np.nanmedian(x[inn]) - np.nanmedian(x[outw]); dy = np.nanmedian(y[inn]) - np.nanmedian(y[outw])
    sx = np.nanstd(x[outw]); sy = np.nanstd(y[outw])
    nflag_in = int((q[np.abs(t - b[0]) < b[2] / 2] != 0).sum()); nin = int((np.abs(t - b[0]) < b[2] / 2).sum())
    r = dict(kind=kind, tc=tc, key=key, t0=b[0], et0=e, depth=b[1], T14_h=b[2] * 24, T12_h=b[3] * 24, flat_h=(b[2] - 2 * b[3]) * 24,
             rms=s, beta=beta, dbkg=dbk, bkg_sd=sbk, dx=dx, dy=dy, sx=sx, sy=sy, n=int(len(t)), nin=nin, nflag_in=nflag_in)
    out.append(r)
    print(f"{kind} {key:9s} t0 {b[0]:.5f} +- {e*1440:5.1f} min  dep {b[1]*100:5.3f}%  T14 {b[2]*24:5.2f} h  T12 {b[3]*24:4.2f} h  flat {r['flat_h']:5.2f} h  rms {s*1e6:5.0f} beta {beta:.1f}  "
          f"dBKG {dbk:+.3g} (sd {sbk:.3g})  dxy {dx:+.4f},{dy:+.4f} (sd {sx:.4f},{sy:.4f})  n_in {nin} nflag_in {nflag_in}")
    a = axs[i]; a.plot(t, f, 'k.', ms=2); a.plot(t[q != 0], f[q != 0], 'r.', ms=2)
    tt = np.linspace(t.min(), t.max(), 1000); a.plot(tt, model(b, tt, tr), 'c-'); a.set_title(f'{kind} {key} {b[0]:.3f}', fontsize=9)
plt.tight_layout(); plt.savefig('ecl_fits.png', dpi=55)
json.dump(out, open('ecl.json', 'w'), indent=1)
