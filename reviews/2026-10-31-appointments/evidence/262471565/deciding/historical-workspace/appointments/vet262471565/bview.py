"""Look at the B windows: QLP SAP (q==0 black, flagged red), 2-h bins, and SAP_BKG, for s001 1349-1353.2 and s027 2053-2060.6,
with the candidate B at x=0.480 (2056.65 / 1351.54). python bview.py -> bview.png"""
import numpy as np, matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
from astropy.io import fits
fig, ax = plt.subplots(2, 2, figsize=(16, 8))
for j, (s, lo, hi, c) in enumerate(((1, 1346.5, 1353.2, 1351.54), (27, 2052.5, 2060.7, 2056.65))):
    d = fits.open(f'[local path omitted]')[1].data
    t, f, q, b = [np.array(d[k], float) for k in ('TIME', 'SAP_FLUX', 'QUALITY', 'SAP_BKG')]
    w = np.isfinite(f) & (t > lo) & (t < hi); t, f, q, b = t[w], f[w], q[w], b[w]; g = q == 0; f /= np.median(f[g])
    a = ax[0, j]; a.plot(t[g], f[g], 'k.', ms=2); a.plot(t[~g], f[~g], 'r.', ms=2)
    e = np.arange(lo, hi, 1 / 12); i = np.digitize(t[g], e); bm = [np.mean(f[g][i == k]) if np.sum(i == k) > 2 else np.nan for k in range(1, len(e))]
    a.plot(e[:-1] + 1 / 24, bm, 'co-', ms=4); a.set_ylim(0.994, 1.004); a.axvline(c, color='g'); a.axvspan(c - 0.5, c + 0.5, color='g', alpha=0.1); a.set_title(f's{s} B window')
    a = ax[1, j]; a.plot(t[g], b[g], 'b.', ms=2); a.plot(t[~g], b[~g], 'r.', ms=2); a.axvline(c, color='g')
plt.tight_layout(); plt.savefig('bview.png', dpi=60)
