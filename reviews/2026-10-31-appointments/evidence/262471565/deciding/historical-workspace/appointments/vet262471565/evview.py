"""Per-event view: QLP SAP flux (q==0 black, flagged red), SAP_BKG, SAP_X/Y around each A event. python evview.py -> evview.png"""
import numpy as np, matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
from astropy.io import fits
E = [(1, 1337.43), (27, 2042.54), (95, 3893.49)]
fig, ax = plt.subplots(4, 3, figsize=(18, 12))
for j, (s, tc) in enumerate(E):
    d = fits.open(f'[local path omitted]')[1].data
    t, f, q, b, x, y = [np.array(d[c], float) for c in ('TIME', 'SAP_FLUX', 'QUALITY', 'SAP_BKG', 'SAP_X', 'SAP_Y')]
    w = np.isfinite(t) & np.isfinite(f) & (np.abs(t - tc) < 3); t, f, q, b, x, y = t[w], f[w], q[w], b[w], x[w], y[w]
    g = q == 0; f /= np.median(f[g])
    print(s, 'raw SAP_FLUX median', np.median(np.array(d['SAP_FLUX'])[np.isfinite(d['SAP_FLUX'])]))
    for i, (v, lab) in enumerate(((f, 'SAP'), (b, 'BKG'), (x, 'X'), (y, 'Y'))):
        a = ax[i, j]; a.plot(t[g], v[g], 'k.', ms=2); a.plot(t[~g], v[~g], 'r.', ms=2); a.axvline(tc - 0.43); a.axvline(tc + 0.43); a.set_title(f's{s} {lab}')
        if lab == 'SAP': a.set_ylim(0.985, 1.008)
        if lab != 'SAP':
            lo, hi = np.nanpercentile(v[g], [1, 99]); a.set_ylim(lo - (hi - lo) * 0.3, hi + (hi - lo) * 0.3)
plt.tight_layout(); plt.savefig('evview.png', dpi=60)
