"""Per-pixel regression difference image (template: QLP trapezoid from ecl.json, not ebfit3) from a TESScut cutout: in a +-W d window around an eclipse, each pixel's
background-subtracted series is fitted as poly(t, deg 2) + amp * D(t), where D(t) = 1 - model(t) is the eclipse shape from
the joint fit (ebfit3_allq_L0.json), supersampled to the cutout cadence. amp map = flux lost at the eclipse bottom.
Reports fractional depth per pixel (amp/median flux), the deficit centroid vs the out-of-eclipse light centroid and the target,
apertures 1x1/3x3/5x5, and every Gaia G<16 neighbour's pixel.
python -X utf8 pixreg.py <cutout.fits> <label> <kind P|S> <tc> [W=0.7] [texp_s]"""
import json, os, sys, numpy as np, matplotlib
matplotlib.use('Agg'); import matplotlib.pyplot as plt
from astropy.io import fits
from astropy.wcs import WCS
HERE = os.path.dirname(os.path.abspath(__file__))
cut, lab, kind, tc = sys.argv[1], sys.argv[2], sys.argv[3], float(sys.argv[4])
W = float(sys.argv[5]) if len(sys.argv) > 5 else 0.7
sys.path.insert(0, HERE); from vetlib import trap
E = {round(r['tc']): r for r in json.load(open(os.path.join(HERE, 'ecl.json'))) if r['depth'] < 0.05 and r['key'] in ('QLP36','QLP72','TSPOC9all')}
R = min(E.values(), key=lambda r: abs(r['t0'] - tc)); mdep = R['depth']
with fits.open(cut, memmap=False) as h:
    d = h[1].data; t = np.array(d['TIME'], float); F = np.array(d['FLUX'], float); q = np.array(d['QUALITY'], int)
    wcs = WCS(h[2].header)
G = json.load(open(os.path.join(HERE, 'gaia.json')))
src_ = G['src'][0]; nb = [r for r in G['nb'][1:] if float(r['phot_g_mean_mag'] or 99) < 16]
ok = np.isfinite(t) & np.all(np.isfinite(F.reshape(len(t), -1)), 1) & (q == 0) & (np.abs(t - tc) < W)
t, F = t[ok], F[ok]
texp = np.median(np.diff(t)) * 86400; n = max(1, int(round(texp / 200)))
off = ((np.arange(n) + 0.5) / n - 0.5) * texp / 86400
Dm = (1 - trap(((t)[:, None] + off[None, :]).ravel(), tc, 1.0, R['T14_h'] / 24, R['T12_h'] / 24)).reshape(-1, n).mean(1)   # unit depth trapezoid at tc
ny, nx = F.shape[1:]
flat = F.reshape(len(t), -1); bk = np.array([np.median(np.sort(r)[:int(0.4 * len(r))]) for r in flat])
F = F - bk[:, None, None]
x = t - tc; A = np.c_[np.ones_like(x), x, x ** 2, -Dm]
coef, *_ = np.linalg.lstsq(A, F.reshape(len(t), -1), rcond=None)
amp = coef[3].reshape(ny, nx); base = coef[0].reshape(ny, nx)
res = F.reshape(len(t), -1) - A @ coef; sig = res.std(0).reshape(ny, nx)
Cinv = np.linalg.inv(A.T @ A); eamp = sig * np.sqrt(Cinv[3, 3])
print(f'{lab}: cadences {len(t)} (texp {texp:.0f} s), in-eclipse (D>0.5) {np.sum(Dm > 0.5)}')
tx, ty = [float(v) for v in wcs.all_world2pix(float(src_['ra']), float(src_['dec']), 0)]
ix, iy = int(round(tx)), int(round(ty))
yy, xx = np.mgrid[:ny, :nx]
def cen(img, r=2):
    m = (np.abs(xx - ix) <= r) & (np.abs(yy - iy) <= r); v = np.clip(img, 0, None) * m
    return (v * xx).sum() / v.sum(), (v * yy).sum() / v.sum()
dx, dy = cen(amp); ox, oy = cen(base)
pk = np.unravel_index(np.argmax(amp), amp.shape)
out = dict(label=lab, target=[tx, ty], light_cen=[ox, oy], deficit_cen=[dx, dy], peak=[int(pk[1]), int(pk[0])])
print(f'  target pixel ({tx:.2f},{ty:.2f}); light centroid ({ox:.2f},{oy:.2f}); deficit centroid ({dx:.2f},{dy:.2f}); '
      f'deficit-light offset {np.hypot(dx-ox, dy-oy)*21:.1f}"; deficit-target offset {np.hypot(dx-tx, dy-ty)*21:.1f}"; brightest deficit pixel ({pk[1]},{pk[0]})')
print(f'  target pixel: frac depth {amp[iy, ix]/base[iy, ix]*100:.2f} +- {eamp[iy, ix]/base[iy, ix]*100:.2f}%  (model {mdep*100:.2f}%)')
for r in (0, 1, 2):
    sl = (slice(iy - r, iy + r + 1), slice(ix - r, ix + r + 1)); dep = amp[sl].sum() / base[sl].sum()
    out[f'depth_ap{2*r+1}'] = float(dep); print(f'  aperture {2*r+1}x{2*r+1}: depth {dep*100:.2f}%')
for r in nb:
    px, py = [float(v) for v in wcs.all_world2pix(float(r['ra']), float(r['dec']), 0)]
    jx, jy = int(round(px)), int(round(py))
    if 0 <= jx < nx and 0 <= jy < ny:
        print(f"  neighbour G {float(r['phot_g_mean_mag']):.2f} sep {float(r['sep']):.1f}\" pixel ({px:.1f},{py:.1f}): frac depth {amp[jy, jx]/base[jy, jx]*100:+.2f} +- {eamp[jy, jx]/base[jy, jx]*100:.2f}%")
# significance map of deficit outside the 3x3 on target
m3 = (np.abs(xx - ix) <= 1) & (np.abs(yy - iy) <= 1); zz = amp / eamp
print(f'  largest |amp/err| outside the 3x3: {np.max(np.abs(zz[~m3])):.1f} at {np.unravel_index(np.argmax(np.abs(np.where(m3, 0, zz))), zz.shape)[::-1]}; inside 3x3 max {zz[m3].max():.1f}')
json.dump(out, open(os.path.join(HERE, f'pix_{lab}.json'), 'w'), indent=1)
fig, ax = plt.subplots(1, 3, figsize=(15, 5))
for a, img, ttl in zip(ax, (base, amp, amp / np.where(base > 0.02 * base.max(), base, np.nan)), ('out-of-eclipse level', 'flux lost at eclipse bottom', 'fractional depth (bright pixels)')):
    im = a.imshow(img, origin='lower'); plt.colorbar(im, ax=a, fraction=0.046); a.plot(tx, ty, 'r+', ms=14, mew=2); a.set_title(ttl)
ax[1].plot(dx, dy, 'mo', mfc='none', ms=12)
fig.suptitle(f'{lab} tc {tc}'); plt.tight_layout(); plt.savefig(os.path.join(HERE, f'pix_{lab}.png'), dpi=65)
