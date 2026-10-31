"""B-eclipse search: linear least squares of quadratic baseline + fixed-shape trapezoid (T14 W h, T12 2 h) in +-1.6 d
around each trial centre, QLP SAP q==0. Scans the Gaia/eclipse-predicted B window (A + 0.4978 P +- 3x0.76 d) and, for
the empirical noise, every other trial centre in the sector (excluding A events). python bscan.py [W_h=22]"""
import sys, numpy as np
from astropy.io import fits
from vetlib import trap
W = (float(sys.argv[1]) if len(sys.argv) > 1 else 22.0) / 24
T0, P = 1337.4273, 29.38001; sep = 0.4978 * P; sw = 0.026 * P
def load(s):
    d = fits.open(f'[local path omitted]')[1].data
    t, f, q = [np.array(d[c], float) for c in ('TIME', 'SAP_FLUX', 'QUALITY')]
    ok = np.isfinite(t) & np.isfinite(f) & (q == 0); t, f = t[ok], f[ok]; return t, f / np.median(f)
def boxfit(t, f, c):
    m = np.abs(t - c) < 1.6
    if m.sum() < 30: return np.nan, np.nan, 0
    tt, ff = t[m], f[m]; D = 1 - trap(tt, c, 1.0, W, 2 / 24)
    inn = D > 0.5
    if inn.sum() < 0.6 * W / np.median(np.diff(tt)) or (~inn).sum() < 0.4 * W / np.median(np.diff(tt)): return np.nan, np.nan, 0
    X = np.vstack([np.ones_like(tt), tt - c, (tt - c) ** 2, -D]).T
    b, *_ = np.linalg.lstsq(X, ff, rcond=None); r = ff - X @ b; s = np.std(r)
    C = np.linalg.inv(X.T @ X) * s ** 2; return b[3], np.sqrt(C[3, 3]), m.sum()
for s in (1, 27, 95):
    t, f = load(s); cs = np.arange(t.min() + 0.5, t.max() - 0.5, 0.05)
    A = T0 + np.round((cs - T0) / P) * P
    res = np.array([boxfit(t, f, c) for c in cs]); dep, err = res[:, 0], res[:, 1]
    far = (np.abs(cs - A) > 1.6) & np.isfinite(dep)
    nul = dep[far]; print(f's{s:03d}: null box depths (n={far.sum()} trial centres, not independent): median {np.median(nul)*1e6:+.0f} ppm, robust sd {1.4826*np.median(np.abs(nul-np.median(nul)))*1e6:.0f} ppm, min/max {nul.min()*1e6:+.0f}/{nul.max()*1e6:+.0f}')
    for k in range(-1, 2):
        Bc = T0 + (np.round((t.mean() - T0) / P) + k) * P + sep
        if t.min() - 1 < Bc < t.max() + 1:
            w = (np.abs(cs - Bc) < 3 * sw) & np.isfinite(dep)
            cov = np.mean([np.sum(np.abs(t - x) < W / 2) > 0.5 * W / np.median(np.diff(t)) for x in np.arange(Bc - sw, Bc + sw, 0.05)])
            print(f'   B predicted {Bc:.2f} +- {sw:.2f}: fraction of 1-sigma window with a >half-covered box {cov:.2f}; ', end='')
            if w.sum():
                print(f'{w.sum()} trial centres; depth at predicted {np.interp(Bc, cs[w], dep[w])*1e6:+.0f} +- {np.interp(Bc, cs[w], err[w])*1e6:.0f} ppm; '
                      f'max depth in +-3sig {dep[w].max()*1e6:+.0f} at {cs[w][np.argmax(dep[w])]:.2f}; mean over +-1sig {np.nanmean(dep[w & (np.abs(cs-Bc)<sw)])*1e6:+.0f} ppm')
            else: print('no usable data')
