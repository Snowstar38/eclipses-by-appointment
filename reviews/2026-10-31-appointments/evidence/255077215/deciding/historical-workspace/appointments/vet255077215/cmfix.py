"""s65 B (3089.745) and s39 B (2380.638): subtract the median common-mode curve of all other s065/s039 QLP stars (raw SAP q==0,
each divided by its own linear baseline on 0.4<|dt|<1.2 d, median in 1-h bins, interpolated), then refit the trapezoid.
python cmfix.py"""
import glob, os, sys, numpy as np
from astropy.io import fits
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from vetlib import fit_trap, t0_error
D = '[local path omitted]'
def rel(fn, tc):
    d = fits.open(fn, memmap=False)[1].data; t = np.array(d['TIME'], float); f = np.array(d['SAP_FLUX'], float); q = np.array(d['QUALITY'], int)
    ok = np.isfinite(t) & np.isfinite(f) & (f > 0) & (q == 0) & (np.abs(t - tc) < 1.2); t, f = t[ok], f[ok]
    out = np.abs(t - tc) > 0.4
    if out.sum() < 10 or (np.abs(t - tc) < 0.3).sum() < 5: return None
    c = np.polyfit(t[out] - tc, f[out], 1); return t, f / np.polyval(c, t - tc)
for sec, tc in ((65, 3089.745), (39, 2380.638)):
    bins = np.arange(tc - 1.2, tc + 1.2001, 1 / 24); mids = (bins[1:] + bins[:-1]) / 2; M = []
    for fn in glob.glob(D + f'*_s{sec:03d}.fits'):
        if '255077215' in fn: continue
        r = rel(fn, tc)
        if r is None: continue
        t, x = r; M.append([np.median(x[(t >= a) & (t < b)]) if np.any((t >= a) & (t < b)) else np.nan for a, b in zip(bins[:-1], bins[1:])])
    cm = np.nanmedian(np.array(M), 0); g = np.isfinite(cm)
    t, f = rel(D + f'255077215_s{sec:03d}.fits', tc)
    for lab, ff in (('raw', f), ('cm-divided', f / np.interp(t, mids[g], cm[g]))):
        w = np.abs(t - tc) < 0.8
        b, c2, s, tr = fit_trap(t[w], ff[w], tc, 0.008, 0.42, 0.08)
        e = t0_error(t[w], ff[w], b, tr, s, half=0.15, n=301)
        print(f's{sec} {lab:10s} (n stars {len(M)}): t0 {b[0]:.5f} +- {e*1440:.1f} min  depth {b[1]*100:.3f}%  T14 {b[2]*24:.2f} h  T12 {b[3]*24:.2f} h  rms {s*1e6:.0f}; cm min {np.nanmin(cm[np.abs(mids-tc)<0.3])-1:+.4f}')
