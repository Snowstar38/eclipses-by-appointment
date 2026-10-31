"""Blind dip census (QLP SAP q0 and all-q, TESS-SPOC SAP all-q, TARS): 0.25-d box vs 1.5-d local median, every sector;
then every A window (B + 0.3386 P +- Gaia phase-sep sd 0.0121 P = 0.26 d, from conjmc.py) and every B / half-period alias time covered,
with coverage counts and 1-h binned limits. python windows.py -> windows.txt, windows.png"""
import json, numpy as np, matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
from astropy.io import fits
D = '[local path omitted]'; V = D + 'vet49416839/'
E = json.load(open('ephem.json')); T0, P = E['T0'], E['P']
def L(src, s):
    if src == 'QLP':
        d = fits.open(D + f'49416839_s{s:03d}.fits')[1].data; t, f, q = d['TIME'], d['SAP_FLUX'], d['QUALITY']
    elif src == 'TSPOC':
        d = fits.open(V + f'hlsp_tess-spoc_tess_phot_0000000049416839-s{s:04d}_tess_v1_lc.fits')[1].data; t, f, q = d['TIME'], d['SAP_FLUX'], d['QUALITY']
    else:
        d = fits.open(V + f'hlsp_tars_tess_ffi_s{s:04d}-0000000049416839_tess_v01_lc.fits')[1].data; t, f = d['TIME'], d['FLUX']; q = np.zeros(len(t), int)
    t, f, q = np.array(t, float), np.array(f, float), np.array(q, int); ok = np.isfinite(t) & np.isfinite(f) & (f > 0)
    t, f, q = t[ok], f[ok], q[ok]; return t, f / np.median(f), q
def box(t, f, w=0.25, base=1.5):
    out = []
    for tc in np.arange(t.min(), t.max(), 0.02):
        i = np.abs(t - tc) < w / 2; o = (np.abs(t - tc) < base / 2) & ~(np.abs(t - tc) < w)
        if i.sum() < 3 or o.sum() < 6: continue
        out.append((tc, 1 - np.median(f[i]) / np.median(f[o])))
    return np.array(out)
print(f'ephemeris B: T0 {T0:.5f} P {P:.6f}')
for s in (9, 36, 46, 72):
    for src, allq in (('QLP', False), ('QLP', True), ('TSPOC', True), ('TARS', True)):
        t, f, q = L(src, s); m = (q == 0) | allq; b = box(t[m], f[m])
        sd = 1.4826 * np.median(np.abs(b[:, 1] - np.median(b[:, 1]))); hits = b[b[:, 1] > max(0.003, 5 * sd)]
        g = []
        for h in hits:
            if g and h[0] - g[-1][-1][0] < 0.3: g[-1].append(h)
            else: g.append([h])
        print(f's{s} {src}{" allq" if allq else " q0"}: box sd {sd*1e6:.0f} ppm; dips > max(0.3%, 5sd):',
              [f'{max(x, key=lambda z: z[1])[0]:.2f} ({max(x, key=lambda z: z[1])[1]*100:.2f}%)' for x in g])
# windows
W = []
for n in range(-1, 82):
    tb = T0 + n * P
    W += [('A', tb + 0.3386 * P, 0.26), ('B', tb, 0.003), ('B+P/2 alias', tb + P / 2, 0.003)]
span = {s: L('TSPOC', s)[0] for s in (9, 36, 46, 72)}
rows = []
for lab, tc, sg in W:
    for s, tt in span.items():
        if tt.min() - 0.5 < tc < tt.max() + 0.5: rows.append((lab, tc, sg, s))
fig, ax = plt.subplots(len(rows), 1, figsize=(12, 2.6 * len(rows)))
for a, (lab, tc, sg, s) in zip(ax, rows):
    print(f'{lab} {tc:.3f} +- {sg:.2f} (s{s}):')
    for k, (src, c) in enumerate((('QLP', 'k'), ('TSPOC', 'b'), ('TARS', 'g'))):
        t, f, q = L(src, s); w = np.abs(t - tc) < 1.5
        win = np.abs(t - tc) < sg + 0.12; n0 = int((win & (q == 0)).sum()); na = int(win.sum())
        lim = ''
        if na > 5:
            tb = np.arange(tc - sg - 0.12, tc + sg + 0.12, 1 / 24)
            bs = [np.median(f[np.abs(t - x) < 1 / 48]) for x in tb if (np.abs(t - x) < 1 / 48).sum() >= 2]
            ref = np.median(f[w & ~win]) if (w & ~win).sum() > 5 else np.median(f[w])
            if len(bs) > 2: lim = f'deepest 1-h bin {(1 - min(bs) / ref)*100:+.2f}%  bins {len(bs)}'
        print(f'   {src:5s}: cadences in window {na} (q==0 {n0}) {lim}')
        a.plot(t[w], f[w] - 0.01 * k, '.', color=c, ms=2)
        a.plot(t[w & (q != 0)], f[w & (q != 0)] - 0.01 * k, 'r.', ms=2)
    a.axvspan(tc - sg, tc + sg, color='gold', alpha=0.3); a.axvline(tc, color='orange'); a.set_ylim(0.96, 1.01); a.set_title(f'{lab} s{s} {tc:.2f}', fontsize=9)
plt.tight_layout(); plt.savefig('windows.png', dpi=55)
