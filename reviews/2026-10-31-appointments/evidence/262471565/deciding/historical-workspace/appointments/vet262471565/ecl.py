"""Trapezoid fits (vetlib.fit_trap, quadratic baseline) to every A and B event in every pipeline.
Raw SAP (QLP SAP_FLUX, SPOC SAP_FLUX, TARS FLUX, eleanor RAW_FLUX); q==0 unless 'all' in the job.
t0 error: profile chi2 (vetlib.t0_error) x red-noise beta (binned residual rms, 1-h bins).
Also: in-eclipse minus out-of-eclipse SAP_BKG (own units) and centroid shift. -> ecl.json, ecl.txt, ecl_*.png
python ecl.py"""
import json, os, sys, numpy as np, matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
from astropy.io import fits
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from vetlib import fit_trap, t0_error, model
D = '[local path omitted]'; V = D + 'vet469755925/'
F = {'QLP13': D + '469755925_s013.fits', 'QLP27': D + '469755925_s027.fits', 'QLP67': D + '469755925_s067.fits', 'QLP94': D + '469755925_s094.fits',
     'TSPOC13': V + 'hlsp_tess-spoc_tess_phot_0000000469755925-s0013_tess_v1_lc.fits', 'TSPOC27': V + 'hlsp_tess-spoc_tess_phot_0000000469755925-s0027_tess_v1_lc.fits',
     'TSPOC67': V + 'hlsp_tess-spoc_tess_phot_0000000469755925-s0067_tess_v1_lc.fits',
     'SPOC27': V + 'tess2020186164531-s0027-0000000469755925-0189-s_lc.fits', 'SPOC67': V + 'tess2023181235917-s0067-0000000469755925-0261-s_lc.fits',
     'SPOC94': V + 'tess2025180145000-s0094-0000000469755925-0291-s_lc.fits',
     'TARS13': V + 'hlsp_tars_tess_ffi_s0013-0000000469755925_tess_v01_lc.fits', 'TARS27': V + 'hlsp_tars_tess_ffi_s0027-0000000469755925_tess_v01_lc.fits',
     'TARS67': V + 'hlsp_tars_tess_ffi_s0067-0000000469755925_tess_v01_lc.fits', 'TARS94': V + 'hlsp_tars_tess_ffi_s0094-0000000469755925_tess_v01_lc.fits',
     'ELE13': V + 'hlsp_gsfc-eleanor-lite_tess_ffi_s0013-0000000469755925_tess_v1.0_lc.fits'}
def load(key, allq):
    with fits.open(F[key]) as h:
        d = h[1].data; c = d.columns.names
        t = np.array(d['TIME'], float)
        f = np.array(d['SAP_FLUX' if 'SAP_FLUX' in c else ('RAW_FLUX' if 'RAW_FLUX' in c else 'FLUX')], float)
        q = np.array(d['QUALITY'], int) if 'QUALITY' in c else np.zeros(len(t), int)
        bk = np.array(d['SAP_BKG' if 'SAP_BKG' in c else ('FLUX_BKG' if 'FLUX_BKG' in c else 'FLUX')], float) if any(x in c for x in ('SAP_BKG', 'FLUX_BKG')) else np.full(len(t), np.nan)
        x = np.array(d['MOM_CENTR1' if 'MOM_CENTR1' in c else ('SAP_X' if 'SAP_X' in c else 'TIME')], float)
        y = np.array(d['MOM_CENTR2' if 'MOM_CENTR2' in c else ('SAP_Y' if 'SAP_Y' in c else 'TIME')], float)
    ok = np.isfinite(t) & np.isfinite(f) & (f > 0)
    if not allq: ok &= q == 0
    return t[ok], f[ok], q[ok], bk[ok], x[ok], y[ok]
JOBS = [('A', 1675.74, k) for k in ('QLP13', 'TSPOC13', 'TARS13', 'ELE13')] + \
       [('A', 3145.09, k) for k in ('QLP67', 'SPOC67', 'TSPOC67', 'TARS67')] + \
       [('A', 3868.10, k) for k in ('SPOC94', 'SPOC94all', 'QLP94all')] + \
       [('B', 1663.27, k) for k in ('QLP13', 'TSPOC13', 'TARS13', 'ELE13')] + \
       [('B', 2036.44, k) for k in ('QLP27', 'QLP27all', 'SPOC27', 'TSPOC27', 'TARS27')] + \
       [('B', 2059.77, k) for k in ('QLP27all', 'SPOC27all', 'TSPOC27all')] + \
       [('B', 3132.64, k) for k in ('QLP67', 'SPOC67', 'TSPOC67', 'TARS67')] + \
       [('B', 3878.96, k) for k in ('QLP94', 'SPOC94', 'TARS94')]
out = []; fig, axs = plt.subplots(7, 5, figsize=(22, 24)); axs = axs.ravel()
for i, (kind, tc, key) in enumerate(JOBS):
    allq = key.endswith('all'); k = key[:-3] if allq else key
    t, f, q, bk, x, y = load(k, allq)
    w = np.abs(t - tc) < 0.8
    if w.sum() < 20: print(kind, tc, key, 'no data'); continue
    t, f, q, bk, x, y = t[w], f[w], q[w], bk[w], x[w], y[w]; f = f / np.median(f)
    dep0 = 0.04 if kind == 'A' else 0.003
    b, c2, s, tr = fit_trap(t, f, tc, dep0, 0.32, 0.04)
    res = f - model(b, t, tr); dt = np.median(np.diff(t)); nb = max(1, int(round((1 / 24) / dt)))
    nn = len(res) // nb; beta = max(1.0, np.std(res[:nn * nb].reshape(nn, nb).mean(1)) / (s / np.sqrt(nb))) if nn > 5 else 1.0
    e = t0_error(t, f, b, tr, s, half=0.05 if kind == 'A' else 0.15, n=301) * beta
    inn = np.abs(t - b[0]) < b[2] / 2 - b[3]; outw = np.abs(t - b[0]) > b[2] / 2 + 0.05
    dbk = np.nanmedian(bk[inn]) - np.nanmedian(bk[outw]) if inn.sum() else np.nan
    sbk = np.nanstd(bk[outw])
    dx = (np.nanmedian(x[inn]) - np.nanmedian(x[outw])) if inn.sum() else np.nan; dy = (np.nanmedian(y[inn]) - np.nanmedian(y[outw])) if inn.sum() else np.nan
    nflag_in = int((q[np.abs(t - b[0]) < b[2] / 2] != 0).sum())
    r = dict(kind=kind, tc=tc, key=key, t0=b[0], et0=e, depth=b[1], T14_h=b[2] * 24, T12_h=b[3] * 24, flat_h=(b[2] - 2 * b[3]) * 24,
             rms=s, beta=beta, dbkg=dbk, bkg_sd=sbk, dx=dx, dy=dy, n=int(len(t)), tmin=float(t.min()), tmax=float(t.max()), nflag_in=nflag_in)
    out.append(r)
    print(f"{kind} {tc:8.2f} {key:10s} t0 {b[0]:.5f} +- {e*1440:5.1f} min  dep {b[1]*100:5.3f}%  T14 {b[2]*24:5.2f} h  T12 {b[3]*24:4.2f} h  flat {r['flat_h']:5.2f} h  rms {s*1e6:5.0f} beta {beta:.1f}  "
          f"dBKG {dbk:+.3g} (sd {sbk:.3g})  dxy {dx:+.4f},{dy:+.4f}  span {t.min():.2f}-{t.max():.2f} nflag_in {nflag_in}")
    a = axs[i]; a.plot(t, f, 'k.', ms=1.5); a.plot(t[q != 0], f[q != 0], 'r.', ms=1.5)
    tt = np.linspace(t.min(), t.max(), 1000); a.plot(tt, model(b, tt, tr), 'c-'); a.set_title(f'{kind} {key} {b[0]:.3f}', fontsize=9)
plt.tight_layout(); plt.savefig('ecl_fits.png', dpi=55)
json.dump(out, open('ecl.json', 'w'), indent=1)
