"""Overview of QLP raw SAP (all cadences, flagged in red) + blind dip census (box 0.2 d, sliding, vs local median).
python look.py -> overview.png, census.txt"""
import glob, numpy as np, matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
from astropy.io import fits
fs = sorted(glob.glob('[local path omitted]'))
fig, axs = plt.subplots(len(fs)*2, 1, figsize=(16, 4.5*len(fs)))
for i, fn in enumerate(fs):
    d = fits.open(fn)[1].data; c = d.columns.names
    t = np.array(d['TIME'], float); f = np.array(d['SAP_FLUX'], float); q = np.array(d['QUALITY'], int); bk = np.array(d['SAP_BKG'], float)
    ok = np.isfinite(t) & np.isfinite(f); t, f, q, bk = t[ok], f[ok], q[ok], bk[ok]; f /= np.median(f[q == 0])
    print(fn[-9:], 'cols', [x for x in c if 'CEN' in x or '_X' in x or '_Y' in x], 'n', len(t), 'q0', (q == 0).sum(), 'span', t.min(), t.max(), 'rms q0', np.std(np.diff(f[q==0]))/np.sqrt(2))
    a = axs[2*i]; a.plot(t, f, 'k.', ms=1); a.plot(t[q != 0], f[q != 0], 'r.', ms=1); a.set_ylim(0.95, 1.02); a.set_title(fn[-9:])
    axs[2*i+1].plot(t, bk, 'b.', ms=1)
    # census on q==0
    g = q == 0; tt, ff = t[g], f[g]
    for tc in np.arange(tt.min()+0.3, tt.max()-0.3, 0.05):
        inn = np.abs(tt - tc) < 0.1; out = (np.abs(tt - tc) > 0.25) & (np.abs(tt - tc) < 1.0)
        if inn.sum() < 5 or out.sum() < 20: continue
        dep = np.median(ff[out]) - np.median(ff[inn])
        if dep > 0.006: print(f'  census s{fn[-8:-5]} {tc:.2f} dip {dep*100:.2f}%  n_in {inn.sum()}')
plt.tight_layout(); plt.savefig('overview.png', dpi=60)
