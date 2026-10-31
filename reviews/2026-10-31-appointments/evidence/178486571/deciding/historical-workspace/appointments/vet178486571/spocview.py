"""Overview of other-pipeline light curves (SPOC 2-min SAP/PDCSAP, TESS-SPOC, TARS, eleanor-lite). python spocview.py"""
import glob, os, numpy as np, matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
from astropy.io import fits
fs = sorted(glob.glob(r'[local path omitted]'))
fig, ax = plt.subplots(len(fs), 1, figsize=(16, 2.6*len(fs)))
for a, fn in zip(ax, fs):
    with fits.open(fn) as h:
        d = h[1].data; cols = d.columns.names
        t = np.array(d['TIME'], float)
        fc = 'SAP_FLUX' if 'SAP_FLUX' in cols else [c for c in cols if 'FLUX' in c.upper()][0]
        f = np.array(d[fc], float)
        q = np.array(d['QUALITY'], int) if 'QUALITY' in cols else np.zeros(len(t), int)
    ok = np.isfinite(t) & np.isfinite(f); t, f, q = t[ok], f[ok], q[ok]
    f /= np.nanmedian(f[q == 0]) if (q == 0).any() else np.nanmedian(f)
    g = q == 0
    a.plot(t[g], f[g], 'k.', ms=1); a.plot(t[~g], f[~g], 'r.', ms=1); a.set_ylim(0.94, 1.02)
    a.set_title(os.path.basename(fn)[:60] + ' ' + fc, fontsize=8)
    print(os.path.basename(fn)[:70], fc, f'{t.min():.3f}-{t.max():.3f}', 'cols', [c for c in cols if 'FLUX' in c.upper() or 'QUAL' in c.upper()][:8])
    for tc in (2036.45, 3127.98, 3145.08, 1675.74, 3868.1, 3879.0, 1663.27, 3132.64, 2059.77):
        w = (np.abs(t - tc) < 0.12) & g
        if w.sum(): print(f'    {tc}: min-window median flux {np.median(f[w]):.4f} (n={w.sum()})')
plt.tight_layout(); plt.savefig('spocview.png', dpi=60)
