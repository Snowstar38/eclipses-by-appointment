"""Per-pixel regression on a TESScut cutout: each pixel's bkg-subtracted series in +-W d of the eclipse = poly2(t) + amp*D(t),
D = unit-depth trapezoid from meas.json (this star's own fit). Reports fractional depth at target and neighbour pixels,
deficit centroid vs target & neighbour. python -X utf8 pixreg.py <cutout> <label> <meas key> [W=0.8] [qmode all|q0]"""
import sys, json, numpy as np, matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
from astropy.io import fits; from astropy.wcs import WCS
sys.path.insert(0, '.'); import vetlib as v
cut, lab, key = sys.argv[1:4]; W = float(sys.argv[4]) if len(sys.argv) > 4 else 0.8; qm = sys.argv[5] if len(sys.argv) > 5 else 'q0'
M = json.load(open('meas.json'))[key]
with fits.open(cut, memmap=False) as h:
    d = h[1].data; t = np.array(d['TIME'], float); F = np.array(d['FLUX'], float); q = np.array(d['QUALITY'], int); wcs = WCS(h[2].header)
ok = np.isfinite(t) & np.all(np.isfinite(F.reshape(len(t), -1)), 1) & (np.abs(t - M['t0']) < W)
if qm == 'q0': ok &= (q == 0)
t, F = t[ok], F[ok]; ny, nx = F.shape[1:]
flat = F.reshape(len(t), -1); bk = np.array([np.median(np.sort(r)[:int(0.3 * len(r))]) for r in flat]); F = F - bk[:, None, None]
D = 1 - v.trap(t, M['t0'], 1.0, M['T14'], M['T12'])
x = t - M['t0']; A = np.c_[np.ones_like(x), x, x ** 2, -D]
coef, *_ = np.linalg.lstsq(A, F.reshape(len(t), -1), rcond=None)
amp = coef[3].reshape(ny, nx); base = coef[0].reshape(ny, nx)
res = F.reshape(len(t), -1) - A @ coef; eamp = (res.std(0) * np.sqrt(np.linalg.inv(A.T @ A)[3, 3])).reshape(ny, nx)
G = json.load(open('gaia.json')); T = G['src'][0]
tx, ty = [float(z) for z in wcs.all_world2pix(float(T['ra']), float(T['dec']), 0)]
nbs = [r for r in G['nb'][1:] if float(r['phot_g_mean_mag']) < 16]
yy, xx = np.mgrid[:ny, :nx]; ix, iy = int(round(tx)), int(round(ty))
def cen(img, r=2):
    m = (np.abs(xx - ix) <= r) & (np.abs(yy - iy) <= r); w = np.clip(img, 0, None) * m
    return (w * xx).sum() / w.sum(), (w * yy).sum() / w.sum()
dx, dy = cen(amp); ox, oy = cen(base)
print(f'{lab}: n={len(t)} in-ecl={np.sum(D>0.5)}  target px ({tx:.2f},{ty:.2f}) light cen ({ox:.2f},{oy:.2f}) deficit cen ({dx:.2f},{dy:.2f}) '
      f'deficit-target {np.hypot(dx-tx,dy-ty)*21:.1f}"  deficit-light {np.hypot(dx-ox,dy-oy)*21:.1f}"')
print(f'  target pixel frac depth {amp[iy,ix]/base[iy,ix]*100:.2f} +- {eamp[iy,ix]/base[iy,ix]*100:.2f}%   (LC depth {M["dep"]*100:.2f}%)')
for r in (0, 1, 2):
    sl = (slice(iy - r, iy + r + 1), slice(ix - r, ix + r + 1)); print(f'  ap {2*r+1}x{2*r+1}: {amp[sl].sum()/base[sl].sum()*100:.2f}%')
for r in nbs:
    px, py = [float(z) for z in wcs.all_world2pix(float(r['ra']), float(r['dec']), 0)]; jx, jy = int(round(px)), int(round(py))
    if 0 <= jx < nx and 0 <= jy < ny:
        print(f"  nb G {float(r['phot_g_mean_mag']):.2f} sep {float(r['sep']):.1f}\" px ({px:.1f},{py:.1f}): frac depth {amp[jy,jx]/base[jy,jx]*100:+.2f} +- {eamp[jy,jx]/base[jy,jx]*100:.2f}%  amp/err {amp[jy,jx]/eamp[jy,jx]:.1f}")
# line profile along target->45" neighbour
r45 = [r for r in nbs if abs(float(r['sep']) - 45.2) < 1][0]
px, py = [float(z) for z in wcs.all_world2pix(float(r45['ra']), float(r45['dec']), 0)]
print('  pixel row along target->nb45 (frac depth %, base):')
for f_ in np.linspace(-0.5, 1.5, 9):
    a, b = int(round(tx + f_ * (px - tx))), int(round(ty + f_ * (py - ty)))
    if 0 <= a < nx and 0 <= b < ny: print(f'     frac {f_:+.2f} pix ({a},{b}) depth {amp[b,a]/base[b,a]*100:6.2f} +- {eamp[b,a]/base[b,a]*100:.2f}  base {base[b,a]:.0f}  amp {amp[b,a]:.0f}')
fig, ax = plt.subplots(1, 3, figsize=(15, 5))
for a, img, ttl in zip(ax, (base, amp, np.where(base > 0.03 * base.max(), amp / base, np.nan)), ('out-of-eclipse', 'flux lost', 'fractional depth')):
    im = a.imshow(img, origin='lower'); plt.colorbar(im, ax=a, fraction=.046); a.plot(tx, ty, 'r+', ms=14, mew=2); a.plot(px, py, 'wx', ms=12, mew=2); a.set_title(ttl)
ax[1].plot(dx, dy, 'mo', mfc='none', ms=12); fig.suptitle(f'{lab} red+ target, white x G12.1 nb 45"'); plt.tight_layout(); plt.savefig(f'pix_{lab}.png', dpi=65)
