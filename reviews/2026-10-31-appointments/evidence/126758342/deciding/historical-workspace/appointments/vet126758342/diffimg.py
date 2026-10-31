"""Difference image from a TESScut cutout.
python -X utf8 diffimg.py <cutout.fits> <gaia.json> <label> <in_lo> <in_hi> <out_lo1> <out_hi1> [<out_lo2> <out_hi2>]
In-eclipse: cadences in [in_lo, in_hi]; out: cadences in the out windows. Per-cadence background = median of the
40% faintest pixels. Prints the diff-image centroid vs the target and Gaia neighbours (G<16), per-pixel fractional
depths, and depths in 1/3x3/5x5 apertures centred on the target pixel. Saves diff_<label>.png and diff_<label>.json."""
import json, os, sys
import numpy as np, matplotlib
matplotlib.use('Agg'); import matplotlib.pyplot as plt
from astropy.io import fits
from astropy.wcs import WCS
cut, gj, lab = sys.argv[1], sys.argv[2], sys.argv[3]
w = [float(x) for x in sys.argv[4:]]
inw = (w[0], w[1]); outs = [(w[i], w[i + 1]) for i in range(2, len(w), 2)]
HERE = os.path.dirname(os.path.abspath(__file__))
with fits.open(cut, memmap=False) as h:
    d = h[1].data; t = np.array(d['TIME'], float); F = np.array(d['FLUX'], float); q = np.array(d['QUALITY'], int)
    wcs = WCS(h[2].header)
G = json.load(open(gj))
src = G['src'][0]; nb = [r for r in G['nb'][1:] if float(r['phot_g_mean_mag'] or 99) < 16 and float(r['sep']) < 90]
ok = np.isfinite(t) & np.all(np.isfinite(F.reshape(len(t), -1)), 1)
t, F, q = t[ok], F[ok], q[ok]
ny, nx = F.shape[1:]
flat = F.reshape(len(t), -1); bk = np.array([np.median(np.sort(r)[:int(0.4 * len(r))]) for r in flat])
F = F - bk[:, None, None]
mi = (t >= inw[0]) & (t <= inw[1]); mo = np.zeros_like(mi)
for a, b in outs: mo |= (t >= a) & (t <= b)
print(f'{lab}: in cadences {mi.sum()} (flagged {(q[mi]!=0).sum()}), out cadences {mo.sum()} (flagged {(q[mo]!=0).sum()})')
Iin = np.median(F[mi], 0); Iout = np.median(F[mo], 0); D = Iout - Iin
tx, ty = wcs.all_world2pix(float(src['ra']), float(src['dec']), 0)
nbp = [(r, *wcs.all_world2pix(float(r['ra']), float(r['dec']), 0)) for r in nb]
ix, iy = int(round(float(tx))), int(round(float(ty)))
# centroid of the deficit in a 5x5 box around the brightest deficit pixel and around the target
yy, xx = np.mgrid[:ny, :nx]
def cen(img, cx, cy, r=2):
    m = (np.abs(xx - cx) <= r) & (np.abs(yy - cy) <= r); v = np.clip(img, 0, None) * m
    return (v * xx).sum() / v.sum(), (v * yy).sum() / v.sum()
dx, dy = cen(D, ix, iy); ox, oy = cen(Iout, ix, iy)
print(f'  target at pixel ({float(tx):.2f}, {float(ty):.2f}); out-of-eclipse light centroid ({ox:.2f}, {oy:.2f}); '
      f'deficit centroid ({dx:.2f}, {dy:.2f}); offset deficit-vs-light {np.hypot(dx-ox, dy-oy)*21:.1f}"')
pk = np.unravel_index(np.argmax(D), D.shape)
print(f'  brightest deficit pixel (x,y)=({pk[1]},{pk[0]}); target pixel ({ix},{iy})')
res = dict(label=lab, target=[float(tx), float(ty)], light_cen=[ox, oy], deficit_cen=[dx, dy], peak=[int(pk[1]), int(pk[0])])
for r, px, py in nbp:
    jx, jy = int(round(float(px))), int(round(float(py)))
    if 0 <= jx < nx and 0 <= jy < ny:
        print(f"  neighbour G {float(r['phot_g_mean_mag']):.2f} sep {float(r['sep']):.1f}\" at pixel ({float(px):.1f},{float(py):.1f}): "
              f"frac depth at its pixel {D[jy, jx]/Iout[jy, jx]*100:+.1f}%  (target pixel {D[iy, ix]/Iout[iy, ix]*100:+.1f}%)")
for r in (0, 1, 2):
    sl = (slice(iy - r, iy + r + 1), slice(ix - r, ix + r + 1))
    dep = D[sl].sum() / Iout[sl].sum(); res[f'depth_ap{2*r+1}'] = dep
    print(f'  aperture {2*r+1}x{2*r+1} on target: depth {dep*100:.1f}%')
# fraction of the total deficit (positive, within 3 px) that sits within 1 px of the target
m3 = (np.abs(xx - ix) <= 3) & (np.abs(yy - iy) <= 3); m1 = (np.abs(xx - ix) <= 1) & (np.abs(yy - iy) <= 1)
fr = np.clip(D, 0, None)[m1].sum() / np.clip(D, 0, None)[m3].sum()
fo = Iout[m1].sum() / Iout[m3].sum()
print(f'  share of the 7x7 deficit inside the 3x3 on target: {fr:.2f} (share of the out-of-eclipse light: {fo:.2f})')
res['share_def_3x3'] = fr; res['share_light_3x3'] = fo
json.dump(res, open(os.path.join(HERE, f'diff_{lab}.json'), 'w'), indent=1)
fig, ax = plt.subplots(1, 3, figsize=(15, 5))
for a, img, ttl in zip(ax, (Iout, D, D / np.where(Iout > 0.02 * Iout.max(), Iout, np.nan)),
                       ('out of eclipse', 'out - in (flux lost)', 'fractional depth (bright pixels)')):
    im = a.imshow(img, origin='lower', cmap='viridis'); plt.colorbar(im, ax=a, fraction=0.046)
    a.plot(float(tx), float(ty), 'r+', ms=14, mew=2)
    for r, px, py in nbp:
        a.plot(float(px), float(py), 'wx', ms=8); a.text(float(px) + 0.3, float(py) + 0.3, f"{float(r['phot_g_mean_mag']):.1f}", color='w', fontsize=7)
    a.set_title(ttl)
ax[1].plot(dx, dy, 'mo', mfc='none', ms=12)
fig.suptitle(f'{lab}: in {inw}, out {outs}')
plt.tight_layout(); plt.savefig(os.path.join(HERE, f'diff_{lab}.png'), dpi=70)
