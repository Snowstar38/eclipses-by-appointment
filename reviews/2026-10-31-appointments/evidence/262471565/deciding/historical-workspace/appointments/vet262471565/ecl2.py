"""Trapezoid fits (vetlib.fit_trap, quadratic baseline) to each A eclipse in QLP SAP (q==0 and all cadences) and the s001
second pipelines (eleanor-lite RAW, TASOC FLUX_RAW, TGLC aperture/psf, T16 IFL2). Also BKG/centroid through each.
python -X utf8 ecl2.py -> ecl2.txt (stdout), ecl2.json, ecl2_fits.png"""
import json, numpy as np, matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
from astropy.io import fits
from vetlib import fit_trap, model, t0_error
D = '[local path omitted]'; V = D + 'vet262471565/'
def L(key):
    if key.startswith('QLP'):
        d = fits.open(D + f'262471565_s{int(key[3:]):03d}.fits')[1].data
        return d['TIME'], d['SAP_FLUX'], d['QUALITY'], d['SAP_BKG'], d['SAP_X'], d['SAP_Y']
    if key == 'ELE1':
        d = fits.open(V + 'hlsp_gsfc-eleanor-lite_tess_ffi_s0001-0000000262471565_tess_v1.0_lc.fits')[1].data
        return d['TIME'], d['RAW_FLUX'], d['QUALITY'], d['FLUX_BKG'], d['X_CENTROID'], d['Y_CENTROID']
    if key == 'TASOC1':
        d = fits.open(V + 'hlsp_tasoc_tess_ffi_tic00262471565-s0001-cam1-ccd1-c1800_tess_v05_ens-lc.fits')[1].data
        return d['TIME'], d['FLUX_RAW'], d['QUALITY'], d['FLUX_BKG'], d['MOM_CENTR1'], d['MOM_CENTR2']
    if key.startswith('TGLC'):
        d = fits.open(V + 'hlsp_tglc_tess_ffi_gaiaid-6778562032182247424-s0001-cam1-ccd1_tess_v1_llc.fits')[1].data
        c = 'aperture_flux' if key == 'TGLC1ap' else 'psf_flux'
        return d['time'], d[c], d['TESS_flags'] | d['TGLC_flags'], d['background'], d['time'] * np.nan, d['time'] * np.nan
    if key == 'T16_1':
        d = fits.open(V + 'hlsp_t16_tess_ffi_s0001-cam1-ccd1-06778562032182247424_tess_v01_llc.fits')[1].data
        f = np.array(d['IFL2'], float)
        return d['TMID_BJD'] - 2457000, f, np.zeros(len(f), int), d['BGV'], d['XPOS'], d['YPOS']
JOBS = [(1337.45, k) for k in ('QLP1', 'QLP1all', 'ELE1', 'TASOC1', 'TGLC1ap', 'TGLC1psf')] + \
       [(2042.55, k) for k in ('QLP27', 'QLP27all')] + [(3893.55, k) for k in ('QLP95', 'QLP95all')]
out = []; fig, axs = plt.subplots(3, 4, figsize=(20, 12)); axs = axs.ravel()
for i, (tc, key) in enumerate(JOBS):
    allq = key.endswith('all'); k = key[:-3] if allq else key
    t, f, q, bk, x, y = [np.array(a, float) for a in L(k)]; q = np.nan_to_num(q).astype(int); o = np.argsort(np.nan_to_num(t)); t, f, q, bk, x, y = t[o], f[o], q[o], bk[o], x[o], y[o]
    ok = np.isfinite(t) & np.isfinite(f) & (f > 0)
    if not allq: ok &= q == 0
    w = ok & (np.abs(t - tc) < 1.3)
    w &= np.abs(f / np.nanmedian(f[w]) - 1) < 0.05
    t, f, q, bk, x, y = t[w], f[w], q[w], bk[w], x[w], y[w]; f = f / np.median(f)
    b, c2, s, tr = fit_trap(t, f, tc, 0.005, 0.72, 0.08)
    res = f - model(b, t, tr); dt = np.median(np.diff(t)); nb = max(1, int(round((1 / 24) / dt)))
    nn = len(res) // nb; beta = max(1.0, np.std(res[:nn * nb].reshape(nn, nb).mean(1)) / (s / np.sqrt(nb))) if nn > 5 else 1.0
    e = t0_error(t, f, b, tr, s, half=0.15, n=301) * beta
    inn = np.abs(t - b[0]) < b[2] / 2 - b[3]; outw = np.abs(t - b[0]) > b[2] / 2 + 0.05
    dbk = np.nanmedian(bk[inn]) - np.nanmedian(bk[outw]); sbk = np.nanstd(bk[outw])
    dx = np.nanmedian(x[inn]) - np.nanmedian(x[outw]); dy = np.nanmedian(y[inn]) - np.nanmedian(y[outw])
    sx = np.nanstd(x[outw]); nfl = int((q[np.abs(t - b[0]) < b[2] / 2] != 0).sum())
    r = dict(key=key, t0=b[0], et0=e, depth=b[1], T14_h=b[2] * 24, T12_h=b[3] * 24, flat_h=(b[2] - 2 * b[3]) * 24, rms=s, beta=beta,
             dbkg=dbk, bkg_sd=sbk, dx=dx, dy=dy, sx=sx, span=[float(t.min()), float(t.max())], nflag_in=nfl)
    out.append(r)
    print(f"{key:9s} t0 {b[0]:.4f} +- {e*24:4.2f} h  dep {b[1]*100:5.3f}%  T14 {b[2]*24:5.2f} h  T12 {b[3]*24:4.2f} h  flat {r['flat_h']:5.2f} h  rms {s*1e6:4.0f} beta {beta:.1f}  "
          f"dBKG {dbk:+.3g} (sd {sbk:.3g})  dxy {dx:+.4f},{dy:+.4f} (sd {sx:.4f})  span {t.min():.2f}-{t.max():.2f} nflag_in {nfl}")
    a = axs[i]; a.plot(t, f, 'k.', ms=2); a.plot(t[q != 0], f[q != 0], 'r.', ms=2)
    tt = np.linspace(t.min(), t.max(), 1000); a.plot(tt, model(b, tt, tr), 'c-'); a.set_title(f'{key} {b[0]:.3f}', fontsize=9); a.set_ylim(0.985, 1.008)
plt.tight_layout(); plt.savefig('ecl2_fits.png', dpi=60)
json.dump(out, open('ecl2.json', 'w'), indent=1)
