"""Common-mode test: in every other star's QLP file of the same sector, depth of a box at our eclipse vs local baseline.
python commonmode.py -> commonmode.txt"""
import glob, os, numpy as np
from astropy.io import fits
D = '[local path omitted]'
TESTS = [(87, (3683.35, 3683.47), [(3683.0, 3683.25), (3683.70, 3683.95)]),
         (33, (2201.83, 2201.92), [(2202.10, 2202.40)]),
         (7, (1494.74, 1494.83), [(1494.3, 1494.6), (1495.0, 1495.3)])]
me = None
for s, box, base in TESTS:
    fs = sorted(glob.glob(D + f'*_s{s:03d}.fits')); res = []
    for fn in fs:
        try:
            with fits.open(fn, memmap=False) as h:
                d = h[1].data; t = np.array(d['TIME'], float); f = np.array(d['SAP_FLUX'], float); q = np.array(d['QUALITY'], int)
                cam, ccd = h[0].header.get('CAMERA'), h[0].header.get('CCD')
        except Exception: continue
        ok = np.isfinite(t) & np.isfinite(f) & (q == 0); t, f = t[ok], f[ok]
        ib = (t > box[0]) & (t < box[1]); ob = np.zeros_like(ib)
        for a, b in base: ob |= (t > a) & (t < b)
        if ib.sum() < 3 or ob.sum() < 5: continue
        sd = np.std(f[ob]) / np.median(f[ob])
        dep = 1 - np.median(f[ib]) / np.median(f[ob])
        res.append((os.path.basename(fn), cam, ccd, dep, sd))
    tic_me = [r for r in res if r[0].startswith('178486571')]
    me = tic_me[0] if tic_me else None
    deps = np.array([r[3] for r in res if not r[0].startswith('178486571')])
    same = [r for r in res if me and r[1] == me[1] and r[2] == me[2] and not r[0].startswith('178486571')]
    print(f's{s} box {box}: N={len(deps)} other stars; median dip {np.median(deps)*100:+.3f}%  frac>1% {np.mean(deps>0.01):.3f}  frac>3% {np.mean(deps>0.03):.3f}')
    if me: print(f'   target: cam {me[1]} ccd {me[2]} dip {me[3]*100:.2f}%')
    sd_ = np.array([r[3] for r in same])
    if len(sd_): print(f'   same cam/ccd: N={len(sd_)} median {np.median(sd_)*100:+.3f}%  max {sd_.max()*100:.2f}%  frac>1% {np.mean(sd_>0.01):.3f}')
    for r in sorted(res, key=lambda r: -r[3])[:5]: print('   top', r[0], r[1], r[2], f'{r[3]*100:.2f}%  sd {r[4]*100:.2f}%')
