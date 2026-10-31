"""Trapezoid fits (vetlib.fit_trap, quadratic baseline) to every A event in every pipeline; raw SAP (QLP SAP_FLUX,
TESS-SPOC SAP_FLUX, TARS FLUX, eleanor RAW_FLUX, TGLC cal_aper/cal_psf). 'all' = keep flagged cadences.
t0 error: profile chi2 x red-noise beta. Also in-minus-out background (own units) and centroid shift. python ecl.py"""
import json, os, sys, numpy as np, matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
from astropy.io import fits
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from vetlib import fit_trap, t0_error, model
D = '[local path omitted]'; V = D + 'vet178486571/'
F = {'QLP7': D + '178486571_s007.fits', 'QLP33': D + '178486571_s033.fits', 'QLP87': D + '178486571_s087.fits',
     'TSPOC7': V + 'hlsp_tess-spoc_tess_phot_0000000178486571-s0007_tess_v1_lc.fits', 'TSPOC33': V + 'hlsp_tess-spoc_tess_phot_0000000178486571-s0033_tess_v1_lc.fits',
     'TARS7': V + 'hlsp_tars_tess_ffi_s0007-0000000178486571_tess_v01_lc.fits', 'TARS33': V + 'hlsp_tars_tess_ffi_s0033-0000000178486571_tess_v01_lc.fits',
     'TARS87': V + 'hlsp_tars_tess_ffi_s0087-0000000178486571_tess_v01_lc.fits', 'ELE7': V + 'hlsp_gsfc-eleanor-lite_tess_ffi_s0007-0000000178486571_tess_v1.0_lc.fits',
     'TGLCa7': V + 'hlsp_tglc_tess_ffi_gaiaid-3045462460926732032-s0007-cam2-ccd4_tess_v1_llc.fits',
     'TGLCp7': V + 'hlsp_tglc_tess_ffi_gaiaid-3045462460926732032-s0007-cam2-ccd4_tess_v1_llc.fits',
     'TGLCnb7': V + 'hlsp_tglc_tess_ffi_gaiaid-3045462460927705472-s0007-cam2-ccd4_tess_v1_llc.fits'}
def load(key, allq):
    with fits.open(F[key]) as h:
        d = h[1].data; c = d.columns.names
        if key.startswith('TGLC'):
            t = np.array(d['time'], float); f = np.array(d['cal_aper_flux' if key.startswith('TGLCa') else 'cal_psf_flux'], float)
            q = np.array(d['TESS_flags'], int) | np.array(d['TGLC_flags'], int); bk = np.array(d['background'], float); x = y = np.full(len(t), np.nan)
        else:
            t = np.array(d['TIME'], float)
            f = np.array(d['SAP_FLUX' if 'SAP_FLUX' in c else ('RAW_FLUX' if 'RAW_FLUX' in c else 'FLUX')], float)
            q = np.array(d['QUALITY'], int) if 'QUALITY' in c else np.zeros(len(t), int)
            bk = np.array(d['SAP_BKG' if 'SAP_BKG' in c else 'FLUX_BKG'], float) if any(z in c for z in ('SAP_BKG', 'FLUX_BKG')) else np.full(len(t), np.nan)
            x = np.array(d['MOM_CENTR1' if 'MOM_CENTR1' in c else ('SAP_X' if 'SAP_X' in c else ('X_CENTROID' if 'X_CENTROID' in c else 'TIME'))], float)
            y = np.array(d['MOM_CENTR2' if 'MOM_CENTR2' in c else ('SAP_Y' if 'SAP_Y' in c else ('Y_CENTROID' if 'Y_CENTROID' in c else 'TIME'))], float)
    ok = np.isfinite(t) & np.isfinite(f) & (f > 0)
    if not allq: ok &= q == 0
    return t[ok], f[ok], q[ok], bk[ok], x[ok], y[ok]
JOBS = [('A', 1494.80, k) for k in ('QLP7', 'TSPOC7', 'TARS7', 'ELE7', 'TGLCa7', 'TGLCp7', 'TGLCnb7')] + \
       [('A', 2201.88, k) for k in ('QLP33', 'QLP33all', 'TSPOC33', 'TSPOC33all', 'TARS33')] + \
       [('A', 3683.40, k) for k in ('QLP87', 'QLP87all', 'TARS87')]
out = []; fig, axs = plt.subplots(3, 5, figsize=(22, 11)); axs = axs.ravel()
for i, (kind, tc, key) in enumerate(JOBS):
    allq = key.endswith('all'); k = key[:-3] if allq else key
    t, f, q, bk, x, y = load(k, allq)
    w = np.abs(t - tc) < 0.8
    if w.sum() < 10: print(kind, tc, key, 'no data'); continue
    t, f, q, bk, x, y = t[w], f[w], q[w], bk[w], x[w], y[w]; f = f / np.median(f)
    b, c2, s, tr = fit_trap(t, f, tc, 0.055, 0.15, 0.06)
    res = f - model(b, t, tr); dt = np.median(np.diff(t)); nb = max(1, int(round((1 / 24) / dt)))
    nn = len(res) // nb; beta = max(1.0, np.std(res[:nn * nb].reshape(nn, nb).mean(1)) / (s / np.sqrt(nb))) if nn > 5 and nb > 1 else 1.0
    e = t0_error(t, f, b, tr, s, half=0.03, n=301) * beta
    inn = np.abs(t - b[0]) < b[2] / 2; outw = np.abs(t - b[0]) > b[2] / 2 + 0.05
    dbk = np.nanmedian(bk[inn]) - np.nanmedian(bk[outw]) if inn.sum() else np.nan; sbk = np.nanstd(bk[outw])
    dx = (np.nanmedian(x[inn]) - np.nanmedian(x[outw])) if inn.sum() else np.nan; dy = (np.nanmedian(y[inn]) - np.nanmedian(y[outw])) if inn.sum() else np.nan
    nflag_in = int((q[inn] != 0).sum()); nin = int(inn.sum())
    r = dict(kind=kind, tc=tc, key=key, t0=b[0], et0=e, depth=b[1], T14_h=b[2] * 24, T12_h=b[3] * 24, flat_h=(b[2] - 2 * b[3]) * 24,
             rms=s, beta=beta, dbkg=dbk, bkg_sd=sbk, dx=dx, dy=dy, n=int(len(t)), nin=nin, tmin=float(t.min()), tmax=float(t.max()), nflag_in=nflag_in)
    out.append(r)
    print(f"{kind} {key:10s} t0 {b[0]:.5f} +- {e*1440:5.1f} min  dep {b[1]*100:5.2f}%  T14 {b[2]*24:5.2f} h  T12 {b[3]*24:4.2f} h  flat {r['flat_h']:5.2f} h  rms {s*1e6:5.0f} beta {beta:.1f} "
          f"dBKG {dbk:+.3g} (sd {sbk:.3g})  dxy {dx:+.4f},{dy:+.4f}  span {t.min():.2f}-{t.max():.2f} nin {nin} nflag_in {nflag_in}")
    a = axs[i]; a.plot(t, f, 'k.', ms=2); a.plot(t[q != 0], f[q != 0], 'r.', ms=2)
    tt = np.linspace(t.min(), t.max(), 1000); a.plot(tt, model(b, tt, tr), 'c-'); a.set_title(f'{kind} {key} {b[0]:.3f}', fontsize=9)
plt.tight_layout(); plt.savefig('ecl_fits.png', dpi=55)
json.dump(out, open('ecl.json', 'w'), indent=1)
