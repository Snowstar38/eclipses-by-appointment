"""Common-mode check for the s006 event: for other QLP s006 stars in the shared folder, box depth in 1478.65-1479.00 against a
linear baseline fitted to 1478.40-1478.60 and 1479.05-1479.60 (q==0 raw SAP), the same as for the target. -> cm6.txt"""
import glob, os, numpy as np
from astropy.io import fits
fs = sorted(glob.glob('[local path omitted]')); res = []
for fn in fs:
    try:
        h = fits.open(fn); d = h[1].data; cam = h[0].header.get('CAMERA'); t = d['TIME']; f = d['SAP_FLUX']; q = d['QUALITY']
        m = np.isfinite(t) & np.isfinite(f) & (q == 0); t, f = t[m], f[m] / np.nanmedian(f[m])
        i = (t > 1478.65) & (t < 1479.0); o = ((t > 1478.4) & (t < 1478.6)) | ((t > 1479.05) & (t < 1479.6))
        if i.sum() < 8 or o.sum() < 15: continue
        c = np.polyfit(t[o], f[o], 1); s = np.std(f[o] - np.polyval(c, t[o])); dep = np.mean(np.polyval(c, t[i]) - f[i])
        res.append((os.path.basename(fn), cam, dep, dep / (s / np.sqrt(i.sum()))))
    except Exception as e: pass
for r in res: print(f'{r[0]:28s} cam {r[1]}  depth {r[2]*100:+.3f}%  snr {r[3]:+.1f}' + ('   <-- target' if '60583013' in r[0] else ''))
dd = np.array([r[2] for r in res if '60583013' not in r[0]]); cams = np.array([r[1] for r in res if '60583013' not in r[0]])
print(f'others: n {len(dd)}, median depth {np.median(dd)*100:+.3f}%, frac with depth > 0.15%: {np.mean(dd > 0.0015):.2f}; cam 2 only: n {np.sum(cams==2)}, median {np.median(dd[cams==2])*100 if np.any(cams==2) else np.nan:+.3f}%, >0.15%: {np.mean(dd[cams==2] > 0.0015) if np.any(cams==2) else np.nan:.2f}')
