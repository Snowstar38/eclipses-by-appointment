"""Blind dip census (QLP SAP, q==0 and all-q): running 0.2-d box vs 1.5-d local median, every sector; plus the B-window
(s87 3677.42 +- 0.62 d from observed A ephemeris and Gaia phase sep 0.8222+-0.0184) in QLP all-q and TARS.
python census.py -> census.txt, bwin.png"""
import numpy as np, matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
from astropy.io import fits
D = '[local path omitted]'
def box(t, f, w=0.2, base=1.5):
    out = []
    for tc in np.arange(t.min(), t.max(), 0.02):
        i = np.abs(t - tc) < w / 2; o = (np.abs(t - tc) < base / 2) & ~(np.abs(t - tc) < w)
        if i.sum() < 3 or o.sum() < 6: continue
        out.append((tc, 1 - np.median(f[i]) / np.median(f[o]), i.sum()))
    return np.array(out)
for s in (15, 16, 56, 76, 83):
    d = fits.open(D + f'395790195_s{s:03d}.fits')[1].data
    for allq in (False, True):
        t = np.array(d['TIME'], float); f = np.array(d['SAP_FLUX'], float); q = np.array(d['QUALITY'], int)
        ok = np.isfinite(t) & np.isfinite(f) & (f > 0) & ((q == 0) | allq); t, f = t[ok], f[ok]
        b = box(t, f); sd = 1.4826 * np.median(np.abs(b[:, 1] - np.median(b[:, 1])))
        hits = b[b[:, 1] > max(0.003, 5 * sd)]
        groups = []
        for h in hits:
            if groups and h[0] - groups[-1][-1][0] < 0.3: groups[-1].append(h)
            else: groups.append([h])
        print(f's{s} {"allq" if allq else "q0  "} box-depth robust sd {sd*1e6:.0f} ppm; dips > max(0.3%, 5 sd):',
              [f'{max(g, key=lambda x: x[1])[0]:.2f} ({max(g, key=lambda x: x[1])[1]*100:.2f}%)' for g in groups])
