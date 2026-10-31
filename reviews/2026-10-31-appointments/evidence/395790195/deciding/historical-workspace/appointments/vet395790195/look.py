"""Overview: raw SAP_FLUX all sectors (q==0 black, flagged red), SAP_BKG, Gaia conjunctions (conj.json). python look.py"""
import json, numpy as np, matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
from astropy.io import fits
D = '[local path omitted]'; S = (15, 16, 56, 76, 83); cj = json.load(open('conj.json'))
fig, ax = plt.subplots(len(S), 1, figsize=(16, 3.2 * len(S)))
for a, s in zip(ax, S):
    d = fits.open(D + f'395790195_s{s:03d}.fits')[1].data; t = np.array(d['TIME'], float); f = np.array(d['SAP_FLUX'], float); q = np.array(d['QUALITY'], int)
    ok = np.isfinite(t) & np.isfinite(f); g = ok & (q == 0); f = f / np.nanmedian(f[g])
    a.plot(t[ok & (q != 0)], f[ok & (q != 0)], 'r.', ms=1.5); a.plot(t[g], f[g], 'k.', ms=1.5); a.set_ylim(0.82, 1.06)
    b = np.array(d['SAP_BKG'], float); a2 = a.twinx(); a2.plot(t[ok], b[ok], 'g-', lw=0.4, alpha=0.5)
    for lab, k, m, sd, h in cj:
        if t[ok].min() - 3 < m < t[ok].max() + 3: a.axvspan(m - sd, m + sd, color='gold' if lab == 'A' else 'skyblue', alpha=0.3); a.axvline(m, color='orange' if lab == 'A' else 'b')
    a.set_xlim(t[ok].min() - 3, t[ok].max() + 3); a.set_title(f's{s}')
    u = np.unique(q[ok]); print(s, 'flags', {int(x): int((q[ok] == x).sum()) for x in u})
plt.tight_layout(); plt.savefig('overview.png', dpi=60)
