"""Common-mode test: for each event time, measure the same box depth (|t-tc|<half) vs a linear baseline fitted to
0.4<|t-tc|<1.2 d in every other QLP star of the sector (same camera/CCD and whole sector), raw SAP_FLUX q==0 (and all-q).
Writes commonmode.txt and cm_<sec>_<tc>.png (median stack of same-CCD stars vs target). python commonmode.py"""
import glob, os, sys, numpy as np, matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
from astropy.io import fits
D = '[local path omitted]'; TIC = '255077215'
EV = [(12, 1645.30, 0.17), (39, 2380.638, 0.17), (65, 3089.745, 0.17), (103, 4166.477, 0.17), (39, 2372.685, 0.25), (65, 3081.761, 0.25)]
def meas(fn, tc, half, allq):
    with fits.open(fn, memmap=False) as h:
        hd = h[0].header; d = h[1].data; t = np.array(d['TIME'], float); f = np.array(d['SAP_FLUX'], float); q = np.array(d['QUALITY'], int)
    ok = np.isfinite(t) & np.isfinite(f) & (f > 0) & (np.abs(t - tc) < 1.2)
    if not allq: ok &= q == 0
    t, f = t[ok], f[ok]
    inn = np.abs(t - tc) < half; out = np.abs(t - tc) > 0.4
    if inn.sum() < 3 or (out & (t < tc)).sum() < 5 or (out & (t > tc)).sum() < 5: return None, (hd.get('CAMERA'), hd.get('CCD')), None
    c = np.polyfit(t[out] - tc, f[out], 1); r = f / np.polyval(c, t - tc) - 1
    return -np.median(r[inn]), (hd.get('CAMERA'), hd.get('CCD')), (t - tc, r)
L = []
for sec, tc, half in EV:
    for allq in (False, True):
        fs = sorted(glob.glob(D + f'*_s{sec:03d}.fits')); tg = D + f'{TIC}_s{sec:03d}.fits'
        d0, cc0, cur0 = meas(tg, tc, half, allq)
        if d0 is None: d0 = np.nan
        dd, ddc, stack = [], [], []
        for fn in fs:
            if os.path.basename(fn).startswith(TIC): continue
            try: d, cc, cur = meas(fn, tc, half, allq)
            except Exception: continue
            if d is None: continue
            dd.append(d)
            if cc == cc0: ddc.append(d); stack.append(cur)
        dd, ddc = np.array(dd), np.array(ddc)
        def st(a): return f'n {len(a)} median {np.median(a)*1e6:+.0f} ppm  MAD-sd {1.4826*np.median(np.abs(a-np.median(a)))*1e6:.0f}  frac>=target/2 {np.mean(a >= d0/2):.3f}' if len(a) else 'n 0'
        s = (f"s{sec} tc {tc} half {half} {'allq' if allq else 'q0'}: target {d0*1e6 :+.0f} ppm | same CCD {cc0}: {st(ddc)} | whole sector: {st(dd)}")
        print(s); L.append(s)
        if stack and cur0 is not None:
            bins = np.arange(-1.2, 1.2001, 1 / 24); mids = (bins[1:] + bins[:-1]) / 2
            M = np.array([[np.nanmedian(r[(x >= a) & (x < b)]) if np.any((x >= a) & (x < b)) else np.nan for a, b in zip(bins[:-1], bins[1:])] for x, r in stack])
            plt.figure(figsize=(8, 4)); plt.plot(cur0[0], cur0[1], 'k.', ms=2, label='target')
            plt.plot(mids, np.nanmedian(M, 0), 'r-', lw=2, label=f'median of {len(stack)} same-CCD stars')
            plt.axvspan(-half, half, alpha=.15); plt.legend(); plt.title(f's{sec} {tc} {"allq" if allq else "q0"}')
            plt.savefig(f'cm_{sec}_{tc:.0f}_{"all" if allq else "q0"}.png', dpi=60); plt.close()
open('commonmode.txt', 'w').write('\n'.join(L) + '\n')
