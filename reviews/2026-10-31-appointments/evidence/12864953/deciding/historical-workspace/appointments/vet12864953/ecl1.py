"""Trapezoid fits (vetlib.fit_trap, quadratic baseline, +-1.0 d) to the two s69 events, raw SAP, q==0 and all-q,
for every available pipeline file passed. t0 error = profile chi2 x red-noise beta. Background and centroid excursions.
python ecl1.py <label> <file> <fluxcol>"""
import sys, os, json, numpy as np
from astropy.io import fits
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from vetlib import fit_trap, t0_error, model
lab, fn, col = sys.argv[1], sys.argv[2], sys.argv[3]
d = fits.open(fn)[1].data; c = d.columns.names
t = np.array(d['TIME'], float); f = np.array(d[col], float)
q = np.array(d['QUALITY'], int) if 'QUALITY' in c else np.zeros(len(t), int)
bk = np.array(d['SAP_BKG'], float) if 'SAP_BKG' in c else None
cx = [k for k in ('SAP_X', 'MOM_CENTR1') if k in c]; cy = [k for k in ('SAP_Y', 'MOM_CENTR2') if k in c]
out = {}
for kind, tc in (('B', 3196.10), ('A', 3204.10)):
    for qs in ('q0', 'allq'):
        ok = np.isfinite(t) & np.isfinite(f) & (np.abs(t - tc) < 1.0)
        if qs == 'q0': ok &= (q == 0)
        tt, ff = t[ok], f[ok] / np.nanmedian(f[ok])
        if len(tt) < 50: print(lab, kind, qs, 'too few', len(tt)); continue
        best, sig = fit_trap(tt, ff, tc, 0.015, 0.22, 0.05)[:2]
        try: e0 = t0_error(tt, ff, best, tc, sig)
        except Exception as ex: e0 = float('nan')
        e0 = e0[0] if isinstance(e0, tuple) else e0
        inn = np.abs(tt - best[0]) < best[2] / 2 * 0.8; oo = (np.abs(tt - best[0]) > best[2] / 2 + 0.1)
        s = dict(t0=best[0], t0err_d=float(e0), dep=best[1], T14_h=best[2] * 24, T12_h=best[3] * 24, flat_h=(best[2] - 2 * best[3]) * 24,
                 rms=float(sig), n=int(len(tt)), nflag_in=int(((q[np.isfinite(t) & (np.abs(t - best[0]) < best[2] / 2)]) != 0).sum()))
        if bk is not None:
            b = bk[ok]; s['bkg_in_minus_out'] = float(np.nanmedian(b[inn]) - np.nanmedian(b[oo])); s['bkg_out_sd'] = float(np.nanstd(b[oo]))
        for k in cx + cy:
            v = np.array(d[k], float)[ok]; s[k + '_shift'] = float(np.nanmedian(v[inn]) - np.nanmedian(v[oo])); s[k + '_sd'] = float(np.nanstd(v[oo]) / np.sqrt(max(inn.sum(), 1)))
        out[kind + '_' + qs] = s
        print(lab, kind, qs, ' '.join((f'{k}={v:.5f}' if k=='t0' else f'{k}={v:.5g}') if isinstance(v, float) else f'{k}={v}' for k, v in s.items()))
json.dump(out, open(f'ecl_{lab}.json', 'w'), indent=0)
