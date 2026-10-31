"""Flank-referenced B depth: linear fit to q==0 flux in [c-W/2-1.0, c-W/2] U [c+W/2, c+W/2+1.0], depth = fit - mean(in |t-c|<W/2-1h).
Null: same at every 0.1-d centre in the sector away from A. python bflank.py"""
import numpy as np
from astropy.io import fits
W = 1.0
def load(s):
    d = fits.open(f'[local path omitted]')[1].data
    t, f, q = [np.array(d[c], float) for c in ('TIME', 'SAP_FLUX', 'QUALITY')]; ok = np.isfinite(f) & (q == 0); return t[ok], f[ok] / np.median(f[ok])
def dep(t, f, c):
    L = (t > c - W / 2 - 1) & (t < c - W / 2); R = (t > c + W / 2) & (t < c + W / 2 + 1); I = np.abs(t - c) < W / 2 - 1 / 24
    if L.sum() < 10 or R.sum() < 10 or I.sum() < 10: return np.nan
    m = L | R; p = np.polyfit(t[m] - c, f[m], 1); return np.polyval(p, 0) - f[I].mean()
for s in (1, 27):
    t, f = load(s); cs = np.arange(t.min() + 1.5, t.max() - 1.5, 0.1)
    A = 1337.4273 + np.round((cs - 1337.4273) / 29.38001) * 29.38001
    d = np.array([dep(t, f, c) for c in cs]); far = (np.abs(cs - A) > 1.6) & (np.abs(cs - (A + 14.6)) > 2.3) & np.isfinite(d)
    print(f's{s:03d} null: n {far.sum()} sd {np.std(d[far])*1e6:.0f} ppm, 95th pct {np.percentile(d[far],95)*1e6:+.0f}, max {d[far].max()*1e6:+.0f}')
    for x in (0.44, 0.46, 0.48, 0.4978, 0.52, 0.54):
        c = 1337.4273 + (24 if s == 27 else 0) * 29.38001 + x * 29.38001; print(f'   x {x:.4f} c {c:.2f}: depth {dep(t, f, c)*1e6:+.0f} ppm')
