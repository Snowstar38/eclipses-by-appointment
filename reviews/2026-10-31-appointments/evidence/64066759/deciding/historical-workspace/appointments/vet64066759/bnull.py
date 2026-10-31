"""Search for B (and aliases) in every sector: box-trapezoid of durations 3, 6, 10, 14 h slid over raw QLP SAP q==0
(and TARS), local quadratic baseline over +-1.5 d excluding the box. Reports the depth (+-err) at the predicted B
windows and the deepest box per sector. python bnull.py -> bnull.txt"""
import glob, json, numpy as np
from astropy.io import fits
D = '[local path omitted]'; V = D + 'vet64066759/'
ep = json.load(open('ephem.json')); T0, P = ep['T0'], ep['P']
phB, sphB = 0.6713, 0.0091
def ld(fn, fc, qc):
    d = fits.open(fn)[1].data; t = np.array(d['TIME'], float); f = np.array(d[fc], float)
    q = np.array(d[qc], int) if qc else np.zeros(len(t), int); ok = np.isfinite(t) & np.isfinite(f) & (f > 0) & (q == 0)
    return t[ok], f[ok] / np.median(f[ok])
def boxdep(t, f, tc, dur):
    inn = np.abs(t - tc) < dur / 2; out = (np.abs(t - tc) > dur / 2 + 0.05) & (np.abs(t - tc) < dur / 2 + 1.5)
    if inn.sum() < 0.6 * dur / np.median(np.diff(t)) or (out & (t < tc)).sum() < 10 or (out & (t > tc)).sum() < 10: return None
    c = np.polyfit(t[out] - tc, f[out], 2); r = f[out] - np.polyval(c, t[out] - tc); s = np.std(r)
    # red noise: bin residuals to dur
    d = 1 - np.mean(f[inn] / np.polyval(c, t[inn] - tc)); e = s / np.sqrt(inn.sum())
    nb = max(1, int(inn.sum())); nn = len(r) // nb
    if nn >= 4: e = max(e, np.std(r[:nn * nb].reshape(nn, nb).mean(1)))
    return d, e
for s in (7, 33, 34, 87, 88):
    for lab, fn, fc, qc in (('QLP', D + f'64066759_s{s:03d}.fits', 'SAP_FLUX', 'QUALITY'), ('TARS', (glob.glob(V + f'hlsp_tars*s{s:04d}*') or [None])[0], 'FLUX', None)):
        if fn is None: continue
        t, f = ld(fn, fc, qc)
        for dur_h in (3, 6, 10, 14):
            dur = dur_h / 24; best = None; res = []
            for tc in np.arange(t.min() + dur / 2, t.max() - dur / 2, 0.02):
                x = boxdep(t, f, tc, dur)
                if x is None: continue
                ph = ((tc - T0) / P) % 1; res.append((tc, ph, *x))
            res = np.array(res)
            if not len(res): continue
            # exclude A eclipses
            mA = np.minimum(res[:, 1], 1 - res[:, 1]) * P > 0.3
            r2 = res[mA]; i = np.argmax(r2[:, 2] / r2[:, 3]); j = np.argmax(r2[:, 2])
            line = f's{s:03d} {lab:4s} {dur_h:2d}h: max SNR {r2[i,2]/r2[i,3]:.1f} at {r2[i,0]:.2f} (dep {r2[i,2]*100:.2f}%); deepest {r2[j,2]*100:.2f}% at {r2[j,0]:.2f}'
            w = np.abs(r2[:, 1] - phB) * P < 3 * sphB * P + dur / 2
            if w.any():
                k = np.argmax(r2[w, 2]); line += f' | B window ({w.sum()} boxes, ph {r2[w,1].min():.3f}-{r2[w,1].max():.3f}): max dep {r2[w,2][k]*100:.3f}+-{r2[w,3][k]*100:.3f}% at {r2[w,0][k]:.2f}; 3sig UL {np.max(r2[w,2]+3*r2[w,3])*100:.2f}%'
            print(line)
# aliases P/2, P/3 epochs covered
for m in (2, 3):
    for s in (7, 33, 34, 87, 88):
        t, f = ld(D + f'64066759_s{s:03d}.fits', 'SAP_FLUX', 'QUALITY')
        for k in range(int((t.min() - T0) / P * m) - 1, int((t.max() - T0) / P * m) + 2):
            if k % m == 0: continue
            tc = T0 + k * P / m
            if t.min() < tc < t.max():
                x = boxdep(t, f, tc, 4 / 24); print(f'alias P/{m} at {tc:.3f} (s{s:03d}):', 'no data' if x is None else f'dep {x[0]*100:.3f}+-{x[1]*100:.3f}%')
# B predicted times in/near each sector
for k in range(-60, 3):
    tb = T0 + (k + phB) * P
    if 1480 < tb < 3720: print(f'B pred {tb:.3f} +- {sphB*P:.2f} d (E {k})')
