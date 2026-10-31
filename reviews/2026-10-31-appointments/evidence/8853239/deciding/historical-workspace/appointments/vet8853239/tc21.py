"""Own TESScut photometry (bkg = median of 40% faintest pixels; 2x2 and 3x3 apertures on target), full sector; dip census
and fit of the A eclipse. python tc21.py <sector> <tguess>  -> tc_s<sec>.txt/png"""
import sys, os, numpy as np, matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from vetlib import fit_trap, t0_error, model
from astropy.io import fits
from astropy.wcs import WCS
sec, tg = int(sys.argv[1]), float(sys.argv[2])
fn = f'[local path omitted]'
with fits.open(fn, memmap=False) as h:
    d = h[1].data; t = np.array(d['TIME'], float); F = np.array(d['FLUX'], float); q = np.array(d['QUALITY'], int); wcs = WCS(h[2].header)
tx, ty = wcs.all_world2pix(142.36889102532, 31.28236052452, 0); ix, iy = int(round(float(tx))), int(round(float(ty)))
ok = np.isfinite(t) & np.all(np.isfinite(F.reshape(len(t), -1)), 1)
t, F, q = t[ok], F[ok], q[ok]
bk = np.array([np.median(np.sort(r.ravel())[:int(0.4 * r.size)]) for r in F]); F = F - bk[:, None, None]
f = sum(F[:, iy + a, ix + b] for a in (-1, 0, 1) for b in (-1, 0, 1)); f = f / np.median(f[q == 0])
print('sector', sec, 'N', len(t), 'range', t.min(), t.max(), 'q!=0', (q != 0).sum(), 'cad', np.median(np.diff(t)) * 1440)
print('gaps', [(round(t[i], 2), round(t[i + 1], 2)) for i in np.where(np.diff(t) > 0.1)[0]])
for x in np.arange(t.min(), t.max(), 0.1):
    inn = np.abs(t - x) < 0.1; base = (np.abs(t - x) < 0.8) & ~(np.abs(t - x) < 0.35)
    if inn.sum() < 3 or base.sum() < 8: continue
    dep = np.median(f[base]) - np.median(f[inn])
    if dep > 0.01: print(f'  dip {x:.2f} depth {dep*100:.2f}%  nflag_in {(q[inn]!=0).sum()}/{inn.sum()}  bkg {np.median(bk[inn]):.0f} vs {np.median(bk[base]):.0f}')
w = (np.abs(t - tg) < 0.8) & (q == 0)
if w.sum() > 20:
    b, c2, s, tr = fit_trap(t[w], f[w], tg, 0.06, 0.28, 0.06)
    e = t0_error(t[w], f[w], b, tr, s, half=0.05, n=201)
    print(f'A fit: t0 {b[0]:.5f} +- {e*1440:.1f} min depth {b[1]*100:.2f}% T14 {b[2]*24:.2f} h T12 {b[3]*24:.2f} h flat {(b[2]-2*b[3])*24:.2f} h rms {s*1e6:.0f}')
fig, ax = plt.subplots(2, 1, figsize=(16, 7)); ax[0].plot(t[q == 0], f[q == 0], 'k.', ms=2); ax[0].plot(t[q != 0], f[q != 0], 'r.', ms=2)
ax[1].plot(t, bk, 'b.', ms=2); ax[0].axvline(tg, color='orange'); plt.savefig(f'tc_s{sec}.png', dpi=70)
