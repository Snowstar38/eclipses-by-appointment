"""Per-pixel regression on a TESScut cutout: each pixel (bkg-subtracted by the cutout's faint-pixel median) in +-W d of the event
= quadratic(t) + amp * D(t), D = unit-depth trapezoid from ecl.json (key). Prints target-pixel/aperture depths, deficit centroid vs
light centroid, every Gaia G<19 neighbour's pixel, and the largest significance outside the 3x3. -> pix_<lab>.json/.png
python -X utf8 pixtrap.py <cutout> <lab> <ecl.json key> <kind> [W]"""
import json, sys, numpy as np, matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
from astropy.io import fits
from astropy.wcs import WCS
from vetlib import trap
cut, lab, key, kind = sys.argv[1:5]; W = float(sys.argv[5]) if len(sys.argv) > 5 else 0.8
E = [r for r in json.load(open('ecl.json')) if r['key'] == key and r['kind'] == kind][0]
t0, T14, T12 = E['t0'], E['T14_h'] / 24, E['T12_h'] / 24
with fits.open(cut) as h:
    d = h[1].data; t = np.array(d['TIME'], float); F = np.array(d['FLUX'], float); q = np.array(d['QUALITY'], int); wcs = WCS(h[2].header)
ok = np.isfinite(t) & np.all(np.isfinite(F.reshape(len(t), -1)), 1) & (np.abs(t - t0) < W) & ((q & ~4096) == 0)
t, F = t[ok], F[ok]; ny, nx = F.shape[1:]
fl = F.reshape(len(t), -1); bk = np.array([np.median(np.sort(r)[:int(0.4 * len(r))]) for r in fl]); F = F - bk[:, None, None]
Dm = 1 - trap(t, t0, 1.0, T14, T12); x = t - t0
A = np.c_[np.ones_like(x), x, x ** 2, -Dm]; coef, *_ = np.linalg.lstsq(A, F.reshape(len(t), -1), rcond=None)
amp = coef[3].reshape(ny, nx); base = coef[0].reshape(ny, nx)
res = F.reshape(len(t), -1) - A @ coef; sig = res.std(0).reshape(ny, nx); eamp = sig * np.sqrt(np.linalg.inv(A.T @ A)[3, 3])
G = json.load(open('gaia.json')); s0 = G['src'][0]
tx, ty = [float(v) for v in wcs.all_world2pix(float(s0['ra']), float(s0['dec']), 0)]; ix, iy = int(round(tx)), int(round(ty))
yy, xx = np.mgrid[:ny, :nx]
def cen(img, r=2):
    m = (np.abs(xx - ix) <= r) & (np.abs(yy - iy) <= r); v = np.clip(img, 0, None) * m; return (v * xx).sum() / v.sum(), (v * yy).sum() / v.sum()
dx, dy = cen(amp); ox, oy = cen(base)
print(f'{lab} ({key} {kind} t0 {t0:.4f}): {len(t)} cadences; target pixel ({tx:.2f},{ty:.2f}); light cen ({ox:.2f},{oy:.2f}); deficit cen ({dx:.2f},{dy:.2f}); '
      f'deficit-light {np.hypot(dx-ox,dy-oy)*21:.1f}"  deficit-target {np.hypot(dx-tx,dy-ty)*21:.1f}"')
print(f'  target pixel depth {amp[iy,ix]/base[iy,ix]*100:.3f} +- {eamp[iy,ix]/base[iy,ix]*100:.3f}%  (light-curve fit {E["depth"]*100:.3f}%)')
out = dict(label=lab, t0=t0, target=[tx, ty], light=[ox, oy], deficit=[dx, dy])
for r in (0, 1, 2):
    sl = (slice(iy - r, iy + r + 1), slice(ix - r, ix + r + 1)); out[f'ap{2*r+1}'] = float(amp[sl].sum() / base[sl].sum()); print(f'  aperture {2*r+1}x{2*r+1}: {out[f"ap{2*r+1}"]*100:.3f}%')
for r in G['nb'][1:]:
    g = float(r['phot_g_mean_mag'] or 99)
    if g > 19 or float(r['sep']) > 80: continue
    px, py = [float(v) for v in wcs.all_world2pix(float(r['ra']), float(r['dec']), 0)]; jx, jy = int(round(px)), int(round(py))
    if 0 <= jx < nx and 0 <= jy < ny:
        print(f'  nb G {g:.2f} sep {float(r["sep"]):5.1f}" pix ({jx},{jy}): amp/err {amp[jy,jx]/eamp[jy,jx]:+.1f}, frac {amp[jy,jx]/base[jy,jx]*100:+.2f}%, '
              f'flux lost there / flux lost on target pixel {amp[jy,jx]/amp[iy,ix]:+.3f}')
m3 = (np.abs(xx - ix) <= 1) & (np.abs(yy - iy) <= 1); z = amp / eamp; zo = np.where(m3, 0, z)
print(f'  max |amp/err| outside 3x3: {np.abs(zo).max():.1f} at {np.unravel_index(np.argmax(np.abs(zo)), z.shape)[::-1]}; target pixel amp/err {z[iy,ix]:.1f}; inside-3x3 max {z[m3].max():.1f}')
json.dump(out, open(f'pix_{lab}.json', 'w'), indent=1)
fig, ax = plt.subplots(1, 3, figsize=(15, 5))
for a, img, tt in zip(ax, (base, amp, z), ('out-of-eclipse', 'flux lost', 'amp/err')):
    im = a.imshow(img, origin='lower'); plt.colorbar(im, ax=a, fraction=.046); a.plot(tx, ty, 'r+', ms=14, mew=2); a.set_title(tt)
ax[1].plot(dx, dy, 'mo', mfc='none', ms=12); fig.suptitle(lab); plt.tight_layout(); plt.savefig(f'pix_{lab}.png', dpi=60)
