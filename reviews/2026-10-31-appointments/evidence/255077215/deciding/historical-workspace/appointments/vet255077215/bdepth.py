"""Wide look (+-2.5 d) at B events in TSPOC s12/s39 (SAP and PDCSAP), ELE s12, QLP s39/s65; box depth (|dt|<0.12 d, flat part)
vs linear baseline on 0.35<|dt|<1.0 d. -> bdepth.png, prints depths. python bdepth.py"""
import numpy as np, matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
from astropy.io import fits
D = '[local path omitted]'; V = D + 'vet255077215/'
J = [('TSPOC12 SAP', V + 'hlsp_tess-spoc_tess_phot_0000000255077215-s0012_tess_v1_lc.fits', 'SAP_FLUX', 1645.303, True),
     ('TSPOC12 PDC', V + 'hlsp_tess-spoc_tess_phot_0000000255077215-s0012_tess_v1_lc.fits', 'PDCSAP_FLUX', 1645.303, True),
     ('ELE12 RAW', V + 'hlsp_gsfc-eleanor-lite_tess_ffi_s0012-0000000255077215_tess_v1.0_lc.fits', 'RAW_FLUX', 1645.303, True),
     ('QLP12 SAP all', D + '255077215_s012.fits', 'SAP_FLUX', 1645.303, True),
     ('TSPOC39 SAP', V + 'hlsp_tess-spoc_tess_phot_0000000255077215-s0039_tess_v1_lc.fits', 'SAP_FLUX', 2380.638, False),
     ('TSPOC39 PDC', V + 'hlsp_tess-spoc_tess_phot_0000000255077215-s0039_tess_v1_lc.fits', 'PDCSAP_FLUX', 2380.638, False),
     ('QLP39 SAP', D + '255077215_s039.fits', 'SAP_FLUX', 2380.638, False),
     ('QLP65 SAP', D + '255077215_s065.fits', 'SAP_FLUX', 3089.74, False)]
fig, ax = plt.subplots(4, 2, figsize=(14, 13)); ax = ax.T.ravel()
for a, (lab, fn, col, tc, allq) in zip(ax, J):
    d = fits.open(fn)[1].data; t = np.array(d['TIME'], float); f = np.array(d[col], float); q = np.array(d['QUALITY'], int)
    ok = np.isfinite(t) & np.isfinite(f) & (np.abs(t - tc) < 2.5)
    if not allq: ok &= q == 0
    t, f, q = t[ok], f[ok] / np.nanmedian(f[ok]), q[ok]
    o = (np.abs(t - tc) > 0.35) & (np.abs(t - tc) < 1.0); c = np.polyfit(t[o] - tc, f[o], 1); r = f / np.polyval(c, t - tc) - 1
    inn = np.abs(t - tc) < 0.12
    print(f'{lab:14s} box depth {-np.median(r[inn])*100:.3f}% (n {inn.sum()}, flagged in box {(q[inn]!=0).sum()}), out rms {np.std(r[o])*1e6:.0f} ppm')
    a.plot(t, f, 'k.', ms=2); a.plot(t[q != 0], f[q != 0], 'r.', ms=2); a.axvline(tc, alpha=.3); a.set_title(lab, fontsize=9)
plt.tight_layout(); plt.savefig('bdepth.png', dpi=55)
