"""Fit eclipses in another pipeline's light curve (TESS-SPOC SAP/PDCSAP, TASOC), compare with QLP (ecl.json).
python -X utf8 secondpipe.py <lc.fits> <fluxcol> <P> <T0> <ph2> <T14g>"""
import json, os, sys, numpy as np
from astropy.io import fits
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from vetlib import fit_trap, t0_error
fn, col, P, T0, ph2, T14g = sys.argv[1], sys.argv[2], *[float(x) for x in sys.argv[3:7]]
Q = {(r['kind'], r['E']): r for r in json.load(open(os.path.join(HERE, 'ecl.json'))) if r['status'] == 'fit'}
with fits.open(fn, memmap=False) as h:
    d = h[1].data; t = np.array(d['TIME'], float); f = np.array(d[col], float)
    qcs = [c for c in d.columns.names if c == 'QUALITY' or 'FLAG' in c.upper()]
    q = np.array(d[qcs[0]], int) if qcs else np.zeros(len(t), int); print(os.path.basename(fn), col, 'cadences', len(t))
ok = np.isfinite(t) & np.isfinite(f) & (q == 0); t, f = t[ok], f[ok]; f /= np.median(f)
for kind, off in (('P', 0), ('S', ph2)):
    for k in range(int((t.min() - T0) / P) - 1, int((t.max() - T0) / P) + 2):
        tc = T0 + (k + off) * P; w = np.abs(t - tc) < 1.0; inn = np.abs(t - tc) < T14g / 2
        if inn.sum() < 4 or (w & (t < tc - T14g / 2)).sum() < 5 or (w & (t > tc + T14g / 2)).sum() < 5: continue
        b, c2, s, tr = fit_trap(t[w], f[w], tc, 0.1 if kind == 'P' else 0.02, T14g, T14g / 4)
        e = t0_error(t[w], f[w], b, tr, s, half=0.01 if kind == 'P' else 0.02, n=201)
        qq = Q.get((kind, k))
        cmp = f"  QLP: t0 {qq['t0']:.5f} dep {qq['depth']*100:.2f}% T14 {qq['T14_h']:.2f} h -> dt {(b[0]-qq['t0'])*1440:+.1f} min" if qq else ''
        print(f'  {kind} E{k}: t0 {b[0]:.5f} +- {e*1440:.1f} min dep {b[1]*100:.2f}% T14 {b[2]*24:.2f} h T12 {b[3]*24:.2f} h{cmp}')
