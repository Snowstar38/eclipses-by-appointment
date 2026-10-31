"""Own per-pixel regression on TESScut: each pixel's bkg-subtracted series in +-W d of the eclipse = poly2 + amp*D(t),
D = unit-depth V trapezoid (T14, T12=T14/2) at the measured t0. Compares the eclipse-amplitude map with the PSF-like
flux maps; fits amp map as a*base_target_like... simply: reports fractional depth at target pixel and at the delta Sct pixel,
deficit centroid, and a two-source fit amp = a*PRFproxy_target + b*PRFproxy_dSct where the proxies are the out-of-eclipse
images of each star modelled as Gaussians (sigma fitted on the bright dSct star).
python mypix.py <sector> <t0> <T14_d> [W]"""
import json, sys, numpy as np, matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
from astropy.io import fits
from astropy.wcs import WCS
import vetlib as V
s, t0, T14 = int(sys.argv[1]), float(sys.argv[2]), float(sys.argv[3]); W = float(sys.argv[4]) if len(sys.argv) > 4 else 0.8
h = fits.open(f'[local path omitted]', memmap=False)
d = h[1].data; t = np.array(d['TIME'], float); F = np.array(d['FLUX'], float); q = np.array(d['QUALITY'], int); wcs = WCS(h[2].header)
ok = np.isfinite(t) & np.all(np.isfinite(F.reshape(len(t), -1)), 1) & (q == 0) & (np.abs(t - t0) < W)
t, F = t[ok], F[ok]; ny, nx = F.shape[1:]
flat = F.reshape(len(t), -1); bk = np.array([np.median(np.sort(r)[:int(0.3 * len(r))]) for r in flat]); F = F - bk[:, None, None]
D = 1 - V.trap(t, t0, 1.0, T14, T14 / 2)
x = t - t0; A = np.c_[np.ones_like(x), x, x ** 2, -D]
Y = F.reshape(len(t), -1); coef, *_ = np.linalg.lstsq(A, Y, rcond=None)
amp = coef[3].reshape(ny, nx); base = coef[0].reshape(ny, nx)
res = Y - A @ coef; sig = res.std(0).reshape(ny, nx); eamp = sig * np.sqrt(np.linalg.inv(A.T @ A)[3, 3])
G = json.load(open('gaia.json'))
stars = [(r['source_id'], float(r['ra']), float(r['dec']), float(r['phot_g_mean_mag'])) for r in G['nb'] if float(r['phot_g_mean_mag'] or 99) < 17.5]
pix = {sid: [float(v) for v in wcs.all_world2pix(ra, de, 0)] for sid, ra, de, g in stars}
T = pix['5592591338355949056']; Dsc = pix['5592591166557257984']
yy, xx = np.mgrid[:ny, :nx]
def rnd(p): return int(round(p[1])), int(round(p[0]))
print(f's{s}: N {len(t)} cad {np.median(np.diff(t))*86400:.0f}s; target pix ({T[0]:.2f},{T[1]:.2f}); dSct pix ({Dsc[0]:.2f},{Dsc[1]:.2f}) sep {np.hypot(T[0]-Dsc[0],T[1]-Dsc[1]):.2f} px')
for lab, p in (('target', T), ('dSct', Dsc)):
    iy, ix = rnd(p)
    if 0 <= ix < nx and 0 <= iy < ny: print(f'  {lab:6s} pixel ({ix},{iy}): base {base[iy,ix]:.0f} amp {amp[iy,ix]:.1f}+-{eamp[iy,ix]:.1f} e/s  frac {amp[iy,ix]/base[iy,ix]*100:.2f}+-{eamp[iy,ix]/base[iy,ix]*100:.2f}%')
# Gaussian PSF model of the out-of-eclipse image with all G<17.5 stars, fluxes free, common sigma; then fit amp map with same PSFs
def psf(p, sg): return np.exp(-((xx - p[0]) ** 2 + (yy - p[1]) ** 2) / (2 * sg ** 2))
best = None
for sg in np.arange(0.5, 1.6, 0.05):
    M = np.c_[[psf(pix[k], sg).ravel() for k in pix] + [np.ones(nx * ny)]].T
    c, *_ = np.linalg.lstsq(M, base.ravel(), rcond=None); r2 = np.sum((base.ravel() - M @ c) ** 2)
    if best is None or r2 < best[0]: best = (r2, sg, c)
_, sg, cb = best; keys = list(pix)
print(f'  PSF sigma {sg:.2f} px; base fit rms frac {np.sqrt(best[0]/base.size)/base.max():.3f}')
w = 1 / eamp.ravel() ** 2
for lab, ks in (('target only', ['5592591338355949056']), ('dSct only', ['5592591166557257984']), ('both', ['5592591338355949056', '5592591166557257984'])):
    M = np.c_[[psf(pix[k], sg).ravel() for k in ks]].T
    c, *_ = np.linalg.lstsq(M * np.sqrt(w)[:, None], amp.ravel() * np.sqrt(w), rcond=None)
    chi = np.sum(w * (amp.ravel() - M @ c) ** 2); cov = np.linalg.inv((M * w[:, None]).T @ M)
    fr = [c[i] / cb[keys.index(k)] for i, k in enumerate(ks)]
    print(f'  amp-map fit {lab:11s}: chi2 {chi:.1f} (n {amp.size})  ' + '  '.join(f'{k[-6:]}: lost {c[i]:.1f}+-{np.sqrt(cov[i,i]):.1f} e/s = {fr[i]*100:.2f}+-{np.sqrt(cov[i,i])/cb[keys.index(k)]*100:.2f}% of its flux' for i, k in enumerate(ks)))
v = np.clip(amp, 0, None) * (np.hypot(xx - T[0], yy - T[1]) < 3.5); dcx, dcy = (v * xx).sum() / v.sum(), (v * yy).sum() / v.sum()
print(f'  deficit centroid ({dcx:.2f},{dcy:.2f}): {np.hypot(dcx-T[0],dcy-T[1])*21:.1f}" from target, {np.hypot(dcx-Dsc[0],dcy-Dsc[1])*21:.1f}" from dSct')
fig, ax = plt.subplots(1, 3, figsize=(15, 5))
for a, img, ttl in zip(ax, (base, amp, amp / eamp), ('out-of-eclipse', 'eclipse amplitude e/s', 'amp / err')):
    im = a.imshow(img, origin='lower'); plt.colorbar(im, ax=a, fraction=.046); a.plot(*T, 'r+', ms=14, mew=2); a.plot(*Dsc, 'wx', ms=12, mew=2); a.set_title(ttl)
fig.suptitle(f's{s} t0 {t0}  red + target, white x dSct G9.8'); plt.tight_layout(); plt.savefig(f'w/pix_s{s:03d}.png', dpi=60)
