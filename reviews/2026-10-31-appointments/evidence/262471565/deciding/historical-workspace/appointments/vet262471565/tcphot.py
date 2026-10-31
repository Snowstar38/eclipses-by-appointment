"""Independent photometry from TESScut FFI cutouts (own pipeline): per-cadence background = median of the 40% faintest
pixels; apertures 1x1, 2x2 (brightest quad incl. target pixel) and 3x3 centred on the target pixel; trapezoid x quadratic fit
(vetlib.fit_trap) of the eclipse; compare with QLP (ecl.json). python -X utf8 -P tcphot.py <cutout> <t0guess> [lo]"""
import sys, os, json, numpy as np
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from vetlib import fit_trap, t0_error, model
from astropy.io import fits
from astropy.wcs import WCS
fn, tc = sys.argv[1], float(sys.argv[2]); lo = float(sys.argv[3]) if len(sys.argv) > 3 else 1.3; hi = float(sys.argv[4]) if len(sys.argv) > 4 else 1.3
with fits.open(fn, memmap=False) as h:
    d = h[1].data; t = np.array(d['TIME'], float); F = np.array(d['FLUX'], float); q = np.array(d['QUALITY'], int); wcs = WCS(h[2].header)
    sec = h[0].header.get('SECTOR')
tx, ty = wcs.all_world2pix(313.4820379941, -36.47483670319, 0); ix, iy = int(round(float(tx))), int(round(float(ty)))
ok = np.isfinite(t) & np.all(np.isfinite(F.reshape(len(t), -1)), 1) & (q == 0) & (t > tc - lo) & (t < tc + hi)
t, F = t[ok], F[ok]; flat = F.reshape(len(t), -1)
bk = np.array([np.median(np.sort(r)[:int(0.4 * len(r))]) for r in flat]); F = F - bk[:, None, None]
sx = 1 if tx - ix > 0 else -1; sy = 1 if ty - iy > 0 else -1
Q = json.load(open(os.path.join(HERE, 'ecl2.json'))); qq = min(Q, key=lambda r: abs(r['t0'] - tc))
res = []
for lab, sl in (('1x1', [(iy, ix)]), ('2x2', [(iy, ix), (iy, ix + sx), (iy + sy, ix), (iy + sy, ix + sx)]),
                ('3x3', [(iy + a, ix + b) for a in (-1, 0, 1) for b in (-1, 0, 1)])):
    f = sum(F[:, a, b] for a, b in sl); f = f / np.median(f)
    b, c2, s, tr = fit_trap(t, f, tc, 0.005, 0.85, 0.1)
    e = t0_error(t, f, b, tr, s, half=0.15, n=301)
    res.append(dict(sec=sec, ap=lab, t0=b[0], t0_err=e, depth=b[1], T14_h=b[2] * 24, T12_h=b[3] * 24, rms_ppm=s * 1e6))
    print(f"s{sec} {lab} bk {np.median(bk):.0f}: t0 {b[0]:.5f} +- {e*1440:.1f} min  depth {b[1]*100:.2f}%  T14 {b[2]*24:.2f} h  T12 {b[3]*24:.2f} h  rms {s*1e6:.0f} ppm"
          f"   | QLP t0 {qq['t0']:.5f} (dt {(b[0]-qq['t0'])*1440:+.1f} min) depth {qq['depth']*100:.2f}% T14 {qq['T14_h']:.2f} h")
json.dump(res, open(os.path.join(HERE, f'tcphot_s{sec}.json'), 'w'), indent=1, default=float)
