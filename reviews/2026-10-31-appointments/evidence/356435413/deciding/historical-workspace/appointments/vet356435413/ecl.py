"""Trapezoid fits (exposure-supersampled, quadratic baseline) to every B event (and A windows) in every pipeline.
Raw SAP (QLP SAP_FLUX, SPOC/TESS-SPOC SAP_FLUX, TARS FLUX, TASOC FLUX_RAW); q==0 unless key ends in 'all'.
t0 error: profile chi2 x red-noise beta. Also in-minus-out SAP_BKG (own units) and centroid shift. -> ecl.json, ecl.txt, ecl_fits.png"""
import json, os, sys, numpy as np, matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
from astropy.io import fits
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from vetlib import nm, trap
D = '[local path omitted]'; V = D + 'vet356435413/'
F = {f'QLP{s}': D + f'356435413_s0{s}.fits' for s in (25, 26, 52, 53, 79)}
F.update({f'TSPOC{s}': V + f'hlsp_tess-spoc_tess_phot_0000000356435413-s00{s}_tess_v1_lc.fits' for s in (25, 26, 52, 53, 79)})
F.update({f'TARS{s}': V + f'hlsp_tars_tess_ffi_s00{s}-0000000356435413_tess_v01_lc.fits' for s in (25, 26, 52, 53, 79)})
F['SPOC79'] = V + 'tess2024142205832-s0079-0000000356435413-0274-s_lc.fits'
F['TASOC26'] = V + 'hlsp_tasoc_tess_ffi_tic00356435413-s0026-cam1-ccd3-c1800_tess_v06_ens-lc.fits'
EXP = {25: 1800, 26: 1800, 52: 600, 53: 600, 79: 200}
def load(key, allq):
    with fits.open(F[key]) as h:
        d = h[1].data; c = d.columns.names
        t = np.array(d['TIME'], float)
        f = np.array(d['SAP_FLUX' if 'SAP_FLUX' in c else ('FLUX_RAW' if 'FLUX_RAW' in c else 'FLUX')], float)
        q = np.array(d['QUALITY'], int) if 'QUALITY' in c else np.zeros(len(t), int)
        bk = np.array(d['SAP_BKG' if 'SAP_BKG' in c else 'FLUX_BKG'], float) if any(x in c for x in ('SAP_BKG', 'FLUX_BKG')) else np.full(len(t), np.nan)
        x = np.array(d['MOM_CENTR1'] if 'MOM_CENTR1' in c else (d['SAP_X'] if 'SAP_X' in c else np.full(len(t), np.nan)), float)
        y = np.array(d['MOM_CENTR2'] if 'MOM_CENTR2' in c else (d['SAP_Y'] if 'SAP_Y' in c else np.full(len(t), np.nan)), float)
    ok = np.isfinite(t) & np.isfinite(f) & (f > 0)
    if not allq: ok &= q == 0
    return t[ok], f[ok], q[ok], bk[ok], x[ok], y[ok]
def mdl(p, t, tref, texp):
    ns = max(1, int(round(texp / 120))); off = (np.arange(ns) + 0.5) / ns - 0.5
    tt = (t[:, None] + off[None, :] * texp / 86400).ravel()
    m = trap(tt, p[0], p[1], p[2], p[3]).reshape(len(t), ns).mean(1)
    return m * (p[4] + p[5] * (t - tref) + p[6] * (t - tref) ** 2)
def fit(t, f, tc, texp):
    def chi(p):
        if p[1] < 0 or p[2] <= 0.02 or p[3] <= 0.002 or p[3] > p[2] / 2: return 1e30
        return np.sum((f - mdl(p, t, tc, texp)) ** 2)
    best = None
    for T14 in (0.08, 0.12, 0.16):
        p0 = [tc, 0.018, T14, T14 / 3, 1.0, 0, 0]; st = [0.01, 0.005, 0.02, 0.01, 0.001, 0.001, 0.001]
        b, c2 = nm(chi, p0, st)
        for _ in range(3): b, c2 = nm(chi, b, [s / 3 for s in st])
        if best is None or c2 < best[1]: best = (b, c2)
    return best[0], best[1], np.std(f - mdl(best[0], t, tc, texp))
def t0err(t, f, b, tc, texp, sig):
    ts = b[0] + np.linspace(-0.03, 0.03, 241); c2 = []
    for x in ts:
        p = b.copy(); p[0] = x; m = mdl(p, t, tc, texp); a = np.sum(f * m) / np.sum(m * m); c2.append(np.sum((f - a * m) ** 2) / sig ** 2)
    c2 = np.array(c2) - min(c2); ok = ts[c2 <= 1]; return (ok.max() - ok.min()) / 2 if len(ok) > 1 else ts[1] - ts[0]
B = {25: 1984.2, 26: 2011.73, 52: 2726.13, 53: 2753.60, 79: 3468.01}
JOBS = []
for s, tc in B.items():
    for p in ('QLP', 'TSPOC', 'TARS') + (('SPOC',) if s == 79 else ()) + (('TASOC',) if s == 26 else ()):
        JOBS.append(('B', tc, f'{p}{s}')); JOBS.append(('B', tc, f'{p}{s}all')) if p in ('QLP', 'TSPOC', 'SPOC', 'TASOC') else None
if __name__ != "__main__": JOBS = []
out = []; fig, axs = plt.subplots(6, 6, figsize=(26, 22)); axs = axs.ravel(); i = 0
for kind, tc, key in JOBS:  # empty on import
    allq = key.endswith('all'); k = key[:-3] if allq else key; s = int(''.join(ch for ch in k if ch.isdigit()))
    texp = 120 if k.startswith('SPOC') else EXP[s]
    t, f, q, bk, x, y = load(k, allq)
    w = np.abs(t - tc) < 0.6
    if w.sum() < 15 or (np.abs(t[w] - tc) < 0.06).sum() < 2: print(kind, tc, key, 'no/insufficient data', w.sum()); continue
    t, f, q, bk, x, y = t[w], f[w], q[w], bk[w], x[w], y[w]; f = f / np.median(f)
    b, c2, sg = fit(t, f, tc, texp)
    res = f - mdl(b, t, tc, texp); dt = np.median(np.diff(t)); nb = max(1, int(round((1 / 24) / dt)))
    nn = len(res) // nb; beta = max(1.0, np.std(res[:nn * nb].reshape(nn, nb).mean(1)) / (sg / np.sqrt(nb))) if (nn > 5 and nb > 1) else 1.0
    e = t0err(t, f, b, tc, texp, sg) * beta
    inn = np.abs(t - b[0]) < max(b[2] / 2 - b[3], 0.02); outw = np.abs(t - b[0]) > b[2] / 2 + 0.05
    dbk = np.nanmedian(bk[inn]) - np.nanmedian(bk[outw]); sbk = np.nanstd(bk[outw])
    dx = np.nanmedian(x[inn]) - np.nanmedian(x[outw]); dy = np.nanmedian(y[inn]) - np.nanmedian(y[outw])
    nfl = int((q[np.abs(t - b[0]) < b[2] / 2] != 0).sum()); nin = int((np.abs(t - b[0]) < b[2] / 2).sum())
    r = dict(kind=kind, tc=tc, key=key, t0=b[0], et0=e, depth=b[1], T14_h=b[2] * 24, T12_h=b[3] * 24, flat_h=(b[2] - 2 * b[3]) * 24, rms=sg, beta=beta,
             dbkg=dbk, bkg_sd=sbk, dx=dx, dy=dy, nin=nin, nflag_in=nfl)
    out.append(r)
    print(f"{kind} {key:9s} t0 {b[0]:.5f} +- {e*1440:5.1f} min  dep {b[1]*100:5.3f}%  T14 {b[2]*24:5.2f} h  T12 {b[3]*24:4.2f} h  flat {r['flat_h']:5.2f} h  rms {sg*1e6:5.0f} b{beta:.1f}  "
          f"dBKG {dbk:+.3g} (sd {sbk:.3g})  dxy {dx:+.4f},{dy:+.4f}  n_in {nin} flag_in {nfl}")
    a = axs[i]; i += 1; a.plot(t, f, 'k.', ms=2); a.plot(t[q != 0], f[q != 0], 'r.', ms=2)
    tt = np.linspace(t.min(), t.max(), 1500); a.plot(tt, mdl(b, tt, tc, 1), 'c-'); a.set_title(f'{key} {b[0]:.4f} d{b[1]*100:.2f}%', fontsize=9)
if __name__ == '__main__':
    plt.tight_layout(); plt.savefig('ecl_fits.png', dpi=50)
    json.dump(out, open('ecl.json', 'w'), indent=1)
