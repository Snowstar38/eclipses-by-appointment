"""Overview of each QLP sector: raw SAP (all cadences), flagged in red, background; plus blind dip census
(running 0.25-d median vs 3-d median, q==0 only). python lcview.py"""
import glob, numpy as np, matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
from astropy.io import fits
fs = sorted(glob.glob(r'[local path omitted]'))
fig, ax = plt.subplots(len(fs)*2, 1, figsize=(16, 4*len(fs)))
for i, fn in enumerate(fs):
    with fits.open(fn) as h:
        d = h[1].data; print(fn[-10:], d.columns.names)
        t = d['TIME']; f = d['SAP_FLUX']; q = d['QUALITY']; b = d['SAP_BKG']
    ok = np.isfinite(t) & np.isfinite(f); t, f, q, b = t[ok], f[ok], q[ok], b[ok]
    f = f / np.median(f[q == 0]); g = q == 0
    dt = np.median(np.diff(t)); print(f'  N={len(t)} good={g.sum()} cad={dt*1440:.1f} min  span {t.min():.2f}-{t.max():.2f}  rms(q0)={np.std(np.diff(f[g]))/np.sqrt(2)*1e6:.0f} ppm')
    print('  flag values:', {int(v): int((q == v).sum()) for v in np.unique(q)})
    a = ax[2*i]; a.plot(t[g], f[g], 'k.', ms=1); a.plot(t[~g], f[~g], 'r.', ms=1); a.set_ylim(0.94, 1.02); a.set_title(fn[-10:])
    ax[2*i+1].plot(t, b, 'b.', ms=1)
    # blind census: 0.25 d boxes slid by 0.05 d vs local 3 d median
    tt, ff = t[g], f[g]
    hits = []
    for c in np.arange(tt.min(), tt.max(), 0.05):
        m = np.abs(tt - c) < 0.125; w = np.abs(tt - c) < 1.5
        if m.sum() < 5: continue
        dd = np.median(ff[w]) - np.median(ff[m])
        if dd > 0.0015: hits.append((c, dd))
    # merge
    groups = []
    for c, dd in hits:
        if groups and c - groups[-1][-1][0] < 0.3: groups[-1].append((c, dd))
        else: groups.append([(c, dd)])
    for gr in groups:
        c, dd = max(gr, key=lambda z: z[1]); print(f'   dip census: {c:.2f} depth {dd*1e6:.0f} ppm')
plt.tight_layout(); plt.savefig('overview.png', dpi=70)
