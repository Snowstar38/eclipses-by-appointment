"""Second pipeline: TASOC s26 (raw FLUX_RAW if present, else FLUX) trapezoid fit of the A eclipse. python -X utf8 tasoc.py <fits>"""
import sys, numpy as np
from astropy.io import fits
sys.path.insert(0, '.'); import vetlib as v
with fits.open(sys.argv[1], memmap=False) as h:
    d = h[1].data; print('cols', d.columns.names)
    t = np.array(d['TIME'], float); col = 'FLUX_RAW' if 'FLUX_RAW' in d.columns.names else 'FLUX'
    f = np.array(d[col], float); q = np.array(d['QUALITY'], int) if 'QUALITY' in d.columns.names else np.zeros(len(t), int)
ok = np.isfinite(t) & np.isfinite(f); t, f, q = t[ok], f[ok], q[ok]; f = f / np.median(f)
m = np.abs(t - 2023.87) < 0.8
print(col, 'n in window', m.sum(), 'flags', dict(zip(*np.unique(q[m], return_counts=True))))
for lab, sel in (('all', m), ('q0', m & (q == 0))):
    if sel.sum() < 20: print(lab, 'too few'); continue
    b, c2, sig, tr = v.fit_trap(t[sel], f[sel], 2023.87, 0.05, 0.28, 0.1)
    et = v.t0_error(t[sel], f[sel], b, tr, sig)
    print(f'{lab}: n {sel.sum()} t0 {b[0]:.4f}+-{et:.4f} depth {b[1]*1e6:.0f} ppm T14 {b[2]*24:.2f} h T12 {b[3]*24:.2f} h rms {sig*1e6:.0f}')
