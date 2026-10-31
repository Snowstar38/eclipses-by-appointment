"""Linear ephemeris for the B eclipses (pipeline-mean times), Gaia comparison, A-window null scan. python ephem.py"""
import json, numpy as np
from astropy.io import fits
ev = json.load(open('ecl.json'))
T = []
for tc in (1729.54, 2438.51, 2804.44):
    r = [x for x in ev if x['tc'] == tc and not x['key'].endswith('all')]
    t = np.array([x['t0'] for x in r]); e = np.array([x['et0'] for x in r])
    m = np.average(t, weights=1 / e ** 2); s = max(np.sqrt(1 / np.sum(1 / e ** 2)), np.std(t))
    T.append((m, s)); print(f'event {tc}: pipelines {", ".join(x["key"] for x in r)}  mean {m:.5f} +- {s*1440:.1f} min (spread {np.ptp(t)*1440:.1f} min)')
t = np.array([x[0] for x in T]); s = np.array([x[1] for x in T]); P0 = 22.87
n = np.round((t - t[0]) / P0); W = 1 / s ** 2; X = np.vstack([np.ones_like(n), n]).T
C = np.linalg.inv(X.T @ (X * W[:, None])); p = C @ X.T @ (W * t); r = t - X @ p; c2 = np.sum((r / s) ** 2)
e = np.sqrt(np.diag(C))
print(f'B ephemeris: T0 {p[0]:.5f} +- {e[0]*1440:.1f} min  P {p[1]:.5f} +- {e[1]:.5f} d  chi2 {c2:.2f}/1  cycles {n}')
for nn, rr, x in zip(n, r, T): print(f'   E{int(nn):3d} {x[0]:.5f} O-C {rr*1440:+.1f} min (err {x[1]*1440:.1f})')
eS = e[1] * max(1, np.sqrt(c2))
gP, gsP = 22.91415100378641, 0.04025493
print(f'Gaia P {gP:.5f} +- {gsP:.5f}: delta {p[1]-gP:+.5f} d = {(p[1]-gP)/np.hypot(gsP, e[1]):+.2f} sigma')
# alias check: which sub-multiples P/m are excluded by coverage (any predicted time inside q==0 data with no dip)
D = '[local path omitted]'
lcs = []
for s_ in ('015', '041', '055'):
    d = fits.open(D + f'126758342_s{s_}.fits')[1].data; tt = np.array(d['TIME'], float); ff = np.array(d['SAP_FLUX'], float); q = np.array(d['QUALITY'])
    ok = np.isfinite(tt) & np.isfinite(ff) & (q == 0); tt, ff = tt[ok], ff[ok]; ff /= np.median(ff); lcs.append((tt, ff))
tt = np.concatenate([x[0] for x in lcs]); ff = np.concatenate([x[1] for x in lcs])
for m in (2, 3, 4):
    Pm = p[1] / m; hits = []
    for k in range(-200, 200):
        tk = p[0] + k * Pm
        if k % m == 0: continue
        w = np.abs(tt - tk) < 0.06
        if w.sum() >= 3:
            o = (np.abs(tt - tk) > 0.25) & (np.abs(tt - tk) < 0.8); hits.append((tk, (np.median(ff[o]) - np.median(ff[w])) * 100))
    print(f'alias P/{m}: covered extra epochs ' + ', '.join(f'{a:.2f} ({b:+.2f}%)' for a, b in hits))
# A null scan: box depth vs phase of the A eclipse (dphi = phase after B), box widths 3 and 5 h; local linear baseline +-0.8 d
print('A-window scan (phase = (t - T0B)/P mod 1; Gaia MC B-A sep 0.586 +- 0.111 -> A at phase 0.414 +- 0.111 after B)')
res = {}
for W_h in (3.0, 5.0):
    hw = W_h / 48; out = []
    for ph in np.arange(0.05, 0.951, 0.002):
        deps = []; vs = []
        for tt_, ff_ in lcs:
            for k in range(-5, 120):
                tk = p[0] + (k + ph) * p[1]
                if tk < tt_.min() or tk > tt_.max(): continue
                inn = np.abs(tt_ - tk) < hw; o = (np.abs(tt_ - tk) > hw + 0.05) & (np.abs(tt_ - tk) < 0.8)
                if inn.sum() < 3 or (o & (tt_ < tk)).sum() < 5 or (o & (tt_ > tk)).sum() < 5: continue
                cf = np.polyfit(tt_[o] - tk, ff_[o], 1); rs = ff_[o] - np.polyval(cf, tt_[o] - tk)
                d = np.mean(np.polyval(cf, tt_[inn] - tk) - ff_[inn]); sd = np.std(rs) / np.sqrt(inn.sum()) * 1.5
                deps.append(d); vs.append(sd ** 2)
        if deps:
            w_ = 1 / np.array(vs); out.append((ph, np.sum(np.array(deps) * w_) / w_.sum(), 1 / np.sqrt(w_.sum()), len(deps)))
    out = np.array(out); res[W_h] = out
    for lo, hi in ((0.303, 0.525), (0.192, 0.636), (0.05, 0.95)):
        sel = (out[:, 0] >= lo) & (out[:, 0] <= hi)
        cov = sel.sum() / ((hi - lo) / 0.002 + 1)
        i = np.argmax(out[sel, 1] / out[sel, 2])
        print(f'  box {W_h} h, phases {lo:.3f}-{hi:.3f}: covered {cov*100:.0f}% of phase grid; max depth {out[sel,1].max()*100:.3f}%, max SNR {out[sel][i,1]/out[sel][i,2]:.1f} at {out[sel][i,0]:.3f}; median 3-sigma UL {np.median(out[sel,1]+3*out[sel,2])*100:.3f}%, worst UL {np.max(out[sel,1]+3*out[sel,2])*100:.3f}%')
json.dump({str(k): v.tolist() for k, v in res.items()}, open('anull.json', 'w'))
print('next predicted B (BTJD):')
for k in range(int(np.ceil((4390 - p[0]) / p[1])), int(np.ceil((4390 - p[0]) / p[1])) + 6):
    tk = p[0] + k * p[1]; sk = np.sqrt(C[0, 0] + k * k * C[1, 1] + 2 * k * C[0, 1]) * max(1, np.sqrt(c2))
    print(f'  B E{k}: {tk:.4f} +- {sk*1440:.0f} min')
json.dump(dict(T0=p[0], P=p[1], C=C.tolist(), chi2=c2), open('ephem.json', 'w'))
