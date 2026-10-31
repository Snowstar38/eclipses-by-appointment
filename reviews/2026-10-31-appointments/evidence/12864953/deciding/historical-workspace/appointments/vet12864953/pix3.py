W = float(__import__("sys").argv[1])
# pix3.py: as pix.py but cubic trend and half-window W (argv[1]); s69 only. python pix3.py W
"""TESScut per-pixel regression (poly2 trend + amp x trapezoid template from the SPOC fit) for each s69 eclipse, and own
aperture photometry of s29 and s69 from the cutouts (bkg already subtracted by TESScut; 3x3 and 1x1 on the target pixel).
python pix.py  -> pix.txt (stdout), pix_*.png, tc_s29.npz"""
import sys, os, numpy as np, matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
from astropy.io import fits; from astropy.wcs import WCS
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__))); from vetlib import trap
V = '[local path omitted]'; RA, DE = 4.33833807641, -17.68085326713
def load(s):
    h = fits.open(V + f'tesscut_s{s:03d}.fits'); d = h[1].data; w = WCS(h[2].header)
    x, y = w.all_world2pix(RA, DE, 0); t = np.array(d['TIME'], float); F = np.array(d['FLUX'], float); q = np.array(d['QUALITY'], int)
    return t, F, q, float(x), float(y)
EV = {'B': (3196.0987, 0.01080, 6.37 / 24, 2.32 / 24), 'A': (3204.1016, 0.01725, 5.93 / 24, 2.62 / 24)}
t, F, q, x0, y0 = load(69); ix, iy = int(round(x0)), int(round(y0)); print('s69 target pixel (col,row)', x0, y0)
for k, (tc, dep, T14, T12) in EV.items():
    ok = np.isfinite(t) & (q == 0) & (np.abs(t - tc) < W) & np.all(np.isfinite(F), axis=(1, 2))
    tt = t[ok]; D = 1 - trap(tt, tc, 1.0, T14, T12)
    X = np.vstack([np.ones_like(tt), tt - tc, (tt - tc) ** 2, (tt - tc) ** 3, D]).T
    amp = np.zeros(F.shape[1:]); ae = np.zeros_like(amp); med = np.median(F[ok], axis=0)
    for j in range(F.shape[1]):
        for i in range(F.shape[2]):
            c, *_ = np.linalg.lstsq(X, F[ok, j, i], rcond=None); r = F[ok, j, i] - X @ c
            cov = np.linalg.inv(X.T @ X) * r.var(); amp[j, i] = -c[4]; ae[j, i] = np.sqrt(cov[4, 4])
    jj, ii = np.mgrid[:amp.shape[0], :amp.shape[1]]
    sel = amp / ae > 3; a = np.clip(amp, 0, None) * sel
    cx, cy = (a * ii).sum() / a.sum(), (a * jj).sum() / a.sum()
    m = np.clip(med, 0, None); lx, ly = (m * ii).sum() / m.sum(), (m * jj).sum() / m.sum()
    jm, im = np.unravel_index(np.argmax(amp / ae), amp.shape)
    print(f'{k} tc={tc}: max-S/N deficit pixel (col,row)=({im},{jm}) S/N={(amp/ae)[jm,im]:.1f}; deficit centroid ({cx:.2f},{cy:.2f}) vs light centroid ({lx:.2f},{ly:.2f}) vs target ({x0:.2f},{y0:.2f})')
    for n in (0, 1, 2):
        s = (slice(iy - n, iy + n + 1), slice(ix - n, ix + n + 1)); print(f'   {2*n+1}x{2*n+1} frac depth {amp[s].sum()/med[s].sum()*100:.3f}%')
    print('   frac depth per pixel (%) 5x5 around target (rows bottom->top):')
    for j in range(iy - 2, iy + 3): print('   ' + ' '.join(f'{amp[j,i]/med[j,i]*100:6.2f}' for i in range(ix - 2, ix + 3)))
    fig, ax = plt.subplots(1, 2, figsize=(10, 4.5)); im0 = ax[0].imshow(amp, origin='lower'); ax[0].plot(x0, y0, 'r+'); plt.colorbar(im0, ax=ax[0]); ax[0].set_title(f'{k} flux lost')
    im1 = ax[1].imshow(amp / ae, origin='lower'); ax[1].plot(x0, y0, 'r+'); plt.colorbar(im1, ax=ax[1]); ax[1].set_title('S/N'); plt.savefig(f'pix3_{k}_W{W}.png', dpi=80); plt.close()
raise SystemExit
fig, axs = plt.subplots(2, 1, figsize=(16, 8))
for a_, s in zip(axs, (29, 69)):
    t, F, q, x0, y0 = load(s); ix, iy = int(round(x0)), int(round(y0))
    f3 = F[:, iy - 1:iy + 2, ix - 1:ix + 2].sum(axis=(1, 2)); ok = np.isfinite(t) & np.isfinite(f3)
    print(f's{s}: n={len(t)} finite={ok.sum()} q0={(ok&(q==0)).sum()} quality values', dict(zip(*np.unique(q[ok], return_counts=True))))
    f3 = f3 / np.nanmedian(f3[ok & (q == 0)]) if (ok & (q == 0)).sum() else f3 / np.nanmedian(f3[ok])
    a_.plot(t[ok], f3[ok], 'r.', ms=1); g = ok & (q == 0); a_.plot(t[g], f3[g], 'k.', ms=1); a_.set_ylim(0.95, 1.03); a_.set_title(f's{s} TESScut 3x3')
    np.savez(f'tc_s{s:02d}.npz', t=t, f=f3, q=q)
plt.savefig('tc_overview.png', dpi=80)
