"""Per-pixel regression on a TESScut cutout: in +-1.3 d around an A event each pixel (own bkg = faintest-40% median subtracted)
is fitted as quadratic(t) + amp * D(t), D = trapezoid shape from the QLP fit (ecl2.json, unit depth). Prints amp/flux map
near the target, deficit centroid vs light centroid vs target position, and the Gaia G<17 neighbours' pixels.
python -X utf8 pixlite.py <cutout> <QLPkey> [hi] -> pix_<key>.png"""
import sys, json, numpy as np, matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
from astropy.io import fits
from astropy.wcs import WCS
from vetlib import trap
cut, key = sys.argv[1], sys.argv[2]; hi = float(sys.argv[3]) if len(sys.argv) > 3 else 1.3
r = {x['key']: x for x in json.load(open('ecl2.json'))}[key]; tc = r['t0']
with fits.open(cut, memmap=False) as h:
    d = h[1].data; t = np.array(d['TIME'], float); F = np.array(d['FLUX'], float); q = np.array(d['QUALITY'], int); wcs = WCS(h[2].header)
ok = np.isfinite(t) & np.all(np.isfinite(F.reshape(len(t), -1)), 1) & (q == 0) & (t > tc - 1.3) & (t < tc + hi)
t, F = t[ok], F[ok]; ny, nx = F.shape[1:]
bk = np.array([np.median(np.sort(z)[:int(0.4 * len(z))]) for z in F.reshape(len(t), -1)]); F = F - bk[:, None, None]
D = 1 - trap(t, tc, 1.0, r['T14_h'] / 24, r['T12_h'] / 24)
X = np.vstack([np.ones_like(t), t - tc, (t - tc) ** 2, -D]).T; XtXi = np.linalg.inv(X.T @ X)
amp = np.zeros((ny, nx)); ea = np.zeros((ny, nx)); med = np.median(F, 0)
for i in range(ny):
    for j in range(nx):
        b = XtXi @ X.T @ F[:, i, j]; s = np.std(F[:, i, j] - X @ b); amp[i, j] = b[3]; ea[i, j] = s * np.sqrt(XtXi[3, 3])
tx, ty = [float(v) for v in wcs.all_world2pix(313.4820379941, -36.47483670319, 0)]
yy, xx = np.mgrid[:ny, :nx]; R = np.hypot(xx - tx, yy - ty) < 3
ap = np.clip(amp, 0, None) * R; lc = np.clip(med, 0, None) * R
cdx = (ap * xx).sum() / ap.sum() - tx; cdy = (ap * yy).sum() / ap.sum() - ty
clx = (lc * xx).sum() / lc.sum() - tx; cly = (lc * yy).sum() / lc.sum() - ty
print(f'{key} tc {tc:.3f}: target pixel ({tx:.2f},{ty:.2f}); deficit centroid offset ({cdx:+.2f},{cdy:+.2f}) px; light centroid offset ({clx:+.2f},{cly:+.2f}) px')
ix, iy = int(round(tx)), int(round(ty))
print('  frac depth (amp/median, %) / S/N, 5x5 around target (rows = y):')
for i in range(iy - 2, iy + 3):
    print('   ' + '  '.join(f'{100*amp[i,j]/med[i,j]:6.2f}/{amp[i,j]/ea[i,j]:5.1f}' for j in range(ix - 2, ix + 3)))
pk = np.unravel_index(np.argmax(amp / ea * (np.hypot(xx - tx, yy - ty) < 5)), amp.shape); print(f'  peak S/N pixel (y,x) {pk}, target pixel (y,x) ({iy},{ix})')
for k in (1, 3, 5):
    m = (np.abs(xx - ix) <= k // 2) & (np.abs(yy - iy) <= k // 2); print(f'  {k}x{k} aperture depth {100*amp[m].sum()/med[m].sum():.3f}%')
G = json.load(open('gaia.json'))
for n in G['nb'][1:]:
    if float(n['phot_g_mean_mag'] or 99) < 17:
        px, py = [float(v) for v in wcs.all_world2pix(float(n['ra']), float(n['dec']), 0)]
        print(f'  neighbour G {float(n["phot_g_mean_mag"]):.2f} sep {float(n["sep"]):.1f}" at pixel ({px:.2f},{py:.2f}) offset ({px-tx:+.2f},{py-ty:+.2f})')
fig, a = plt.subplots(1, 2, figsize=(10, 5)); a[0].imshow(amp / ea, origin='lower'); a[0].plot(tx, ty, 'rx'); a[0].set_title('S/N of deficit')
a[1].imshow(np.log10(np.clip(med, 1, None)), origin='lower'); a[1].plot(tx, ty, 'rx'); plt.savefig(f'pix_{key}.png', dpi=60)
