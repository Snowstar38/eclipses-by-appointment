"""Blind box census (every sector, raw SAP q==0, local linear baseline from +-1 d outside box) and B-window limits.
python -X utf8 census.py"""
import sys, json, numpy as np
sys.path.insert(0, '.'); import vetlib as v
E = json.load(open('ephem.json')); T0, P = E['T0'], E['P']
D = {v.load_qlp(f)['sec']: v.load_qlp(f) for f in v.qlp_files(275065610)}
def box(t, f, tc, w, side=0.6):
    i = np.abs(t - tc) < w / 2; o = (np.abs(t - tc) > w / 2 + 0.05) & (np.abs(t - tc) < w / 2 + side)
    if i.sum() < 3 or o.sum() < 10 or (t[o] < tc).sum() < 4 or (t[o] > tc).sum() < 4: return np.nan, np.nan
    c = np.polyfit(t[o] - tc, f[o], 1); r = f[o] - np.polyval(c, t[o] - tc)
    dt = np.median(np.diff(t)); nb = max(1, int(w / dt))
    sig = np.std(r) / np.sqrt(min(i.sum(), nb))
    # red noise: scatter of same-width box means out of eclipse in the sector computed outside
    return -np.mean(f[i] - np.polyval(c, t[i] - tc)), sig
print('== blind census (q0): every box with depth > 4 sigma and > 2000 ppm, widths 3/7/14/21 h')
for s, d in sorted(D.items()):
    g = d['q'] == 0; t, f = d['t'][g], d['f'][g]
    hits = []
    for w in (3 / 24, 7 / 24, 14 / 24, 21 / 24):
        for tc in np.arange(t.min(), t.max(), w / 4):
            dep, sg = box(t, f, tc, w)
            if np.isfinite(dep) and dep > 0.002 and dep / sg > 4: hits.append((tc, w * 24, dep, dep / sg))
    # cluster
    hits.sort(); cl = []
    for h in hits:
        if cl and h[0] - cl[-1][-1][0] < 0.5: cl[-1].append(h)
        else: cl.append([h])
    for c in cl:
        b = max(c, key=lambda h: h[2]); ph = ((b[0] - T0) / P) % 1
        print(f'  s{s}: t {b[0]:.2f} w {b[1]:.0f} h depth {b[2]*1e6:.0f} ppm ({b[3]:.0f} sig) phase {ph:.3f}')
print('== B windows: box depth on q0 and all cadences, centre scanned over +-0.75 d (3 sigma), widths 7/14/21 h')
res = []
for s, d in sorted(D.items()):
    for k in range(-3, 60):
        tb = T0 + (k + 0.5396) * P
        if not (d['t'].min() - 0.5 < tb < d['t'].max() + 0.5): continue
        for lab, use in (('q0', d['q'] == 0), ('all', np.ones_like(d['q'], bool))):
            t, f = d['t'][use], d['f'][use]
            for w in (7 / 24, 14 / 24, 21 / 24):
                cov = []; mx = (-1, 0, 0)
                for tc in np.arange(tb - 0.75, tb + 0.75, 0.02):
                    dep, sg = box(t, f, tc, w)
                    if np.isfinite(dep):
                        cov.append(tc)
                        if dep > mx[0]: mx = (dep, sg, tc)
                frac = len(cov) / 75
                print(f'  s{s} B {tb:.2f} {lab:3s} w{w*24:4.0f}h: centres covered {frac*100:3.0f}%  max box depth {mx[0]*1e6:6.0f} +- {mx[1]*1e6:.0f} ppm at {mx[2]:.2f}')
                if lab == 'q0': res.append((s, w, frac, mx[0], mx[1]))
json.dump(res, open('bnull.json', 'w'))
