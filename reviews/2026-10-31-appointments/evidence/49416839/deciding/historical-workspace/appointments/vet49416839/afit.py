"""Search for the A (transit) eclipse near the three covered A windows: trapezoid fit (vetlib.fit_trap) with free t0 near the
small dips at ~1565.0, ~2572.05, ~3279.30 in QLP all-q, TESS-SPOC SAP all-q, TARS; plus a joint fold on the B ephemeris.
python afit.py -> afit.txt, afit.png"""
import json, sys, os, numpy as np, matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from vetlib import fit_trap, t0_error, model
from astropy.io import fits
D = '[local path omitted]'; V = D + 'vet49416839/'
def L(src, s):
    if src == 'QLP':
        d = fits.open(D + f'49416839_s{s:03d}.fits')[1].data; t, f, q = d['TIME'], d['SAP_FLUX'], d['QUALITY']
    elif src == 'TSPOC':
        d = fits.open(V + f'hlsp_tess-spoc_tess_phot_0000000049416839-s{s:04d}_tess_v1_lc.fits')[1].data; t, f, q = d['TIME'], d['SAP_FLUX'], d['QUALITY']
    else:
        d = fits.open(V + f'hlsp_tars_tess_ffi_s{s:04d}-0000000049416839_tess_v01_lc.fits')[1].data; t, f = d['TIME'], d['FLUX']; q = np.zeros(len(t), int)
    t, f, q = np.array(t, float), np.array(f, float), np.array(q, int); ok = np.isfinite(t) & np.isfinite(f) & (f > 0)
    t, f, q = t[ok], f[ok], q[ok]; return t, f / np.median(f), q
E = json.load(open('ephem.json')); T0, P = E['T0'], E['P']
JOBS = [(9, 1565.0), (46, 2572.05), (72, 3279.30)]
fig, ax = plt.subplots(3, 3, figsize=(15, 9)); out = []
for i, (s, tc) in enumerate(JOBS):
    for j, src in enumerate(('QLP', 'TSPOC', 'TARS')):
        t, f, q = L(src, s); w = np.abs(t - tc) < 0.7
        if w.sum() < 20: continue
        t, f, q = t[w], f[w], q[w]; f = f / np.median(f)
        b, c2, sg, tr = fit_trap(t, f, tc, 0.003, 0.15, 0.05)
        e = t0_error(t, f, b, tr, sg, half=0.06, n=121)
        ph = ((b[0] - T0) / P) % 1
        print(f's{s} {src:5s} t0 {b[0]:.4f} +- {e*1440:.0f} min  depth {b[1]*100:.3f}%  T14 {b[2]*24:.2f} h  T12 {b[3]*24:.2f} h  rms {sg*1e6:.0f}  '
              f'flagged in window {int((q[np.abs(t-b[0])<b[2]/2]!=0).sum())}/{int((np.abs(t-b[0])<b[2]/2).sum())}  phase after B {ph:.4f}  data {t.min():.2f}-{t.max():.2f}')
        out.append(dict(s=s, src=src, t0=b[0], et0=e, depth=b[1], T14=b[2], T12=b[3], ph=ph))
        a = ax[i, j]; a.plot(t, f, 'k.', ms=2); a.plot(t[q != 0], f[q != 0], 'r.', ms=2)
        tt = np.linspace(t.min(), t.max(), 800); a.plot(tt, model(b, tt, tr), 'c-'); a.set_title(f's{s} {src} {b[0]:.3f}', fontsize=9); a.set_ylim(0.993, 1.004)
plt.tight_layout(); plt.savefig('afit.png', dpi=60)
json.dump(out, open('afit.json', 'w'), indent=1)
