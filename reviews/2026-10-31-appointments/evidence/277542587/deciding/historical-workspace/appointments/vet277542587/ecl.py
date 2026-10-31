"""Trapezoid fits (quadratic baseline) to the two s080 events from raw QLP SAP_FLUX, q0 and all-quality;
background (raw SAP_BKG e-/s) and centroid excursions through each. python -X utf8 ecl.py -> ecl.json, ecl.png"""
import sys, os, json, numpy as np, matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
from astropy.io import fits
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__))); from vetlib import fit_trap, t0_error, model
h = fits.open('[local path omitted]'); d = h[1].data
t = np.array(d['TIME'], float); f = np.array(d['SAP_FLUX'], float); q = np.array(d['QUALITY'], int)
b = np.array(d['SAP_BKG'], float); x = np.array(d['SAP_X'], float); y = np.array(d['SAP_Y'], float)
ok = np.isfinite(t) & np.isfinite(f); t, f, q, b, x, y = t[ok], f[ok], q[ok], b[ok], x[ok], y[ok]
f = f / np.median(f[q == 0])
EV = [('A', 3488.83, 0.08, 0.30), ('B', 3496.75, 0.15, 0.30)]
out = []; fig, ax = plt.subplots(4, 2, figsize=(14, 12))
for j, (k, tc, dep, T14) in enumerate(EV):
    for mode in ('q0', 'allq'):
        W = 0.8
        s = (np.abs(t - tc) < W) & (np.isfinite(f))
        if mode == 'q0': s &= q == 0
        if k == 'A': s &= t > 3488.35   # exclude the scattered-light mess before 3488.3
        tt, ff = t[s], f[s]
        best, c2, sig, tref = fit_trap(tt, ff, tc, dep, T14, 0.1)
        e0 = t0_error(tt, ff, best, tref, sig)
        # red-noise beta from 1-h binned residuals
        r = ff - model(best, tt, tref); nb = max(1, int(round((1 / 24) / np.median(np.diff(tt)))))
        rb = [np.mean(r[i:i + nb]) for i in range(0, len(r) - nb, nb)]; beta = max(1, np.std(rb) / (sig / np.sqrt(nb)))
        npre = int(np.sum(tt < best[0] - best[2] / 2)); nin = int(np.sum(np.abs(tt - best[0]) < best[2] / 2))
        row = dict(kind=k, mode=mode, tc=best[0], tc_err=e0 * beta, depth=best[1], T14_h=best[2] * 24, T12_h=best[3] * 24,
                   flat_h=(best[2] - 2 * best[3]) * 24, rms_ppt=sig * 1e3, beta=beta, n=len(tt), n_pre=npre, n_in=nin,
                   nflag_in=int(np.sum((np.abs(t - best[0]) < best[2] / 2) & (q != 0))))
        out.append(row); print({kk: (round(v, 5) if isinstance(v, float) else v) for kk, v in row.items()})
        if mode == 'allq':
            ax[0, j].plot(t[np.abs(t - tc) < 1.2], f[np.abs(t - tc) < 1.2], '.', c='r', ms=2)
            ax[0, j].plot(tt[q[s] == 0] if False else tt, ff, '.', c='k', ms=2)
            tm = np.linspace(tt.min(), tt.max(), 2000); ax[0, j].plot(tm, model(best, tm, tref), 'c'); ax[0, j].set_ylim(0.8, 1.05)
            ax[0, j].set_title(f'{k} tc={best[0]:.4f} dep={best[1]*100:.2f}% T14={best[2]*24:.2f}h')
    w = np.abs(t - tc) < 1.2; ins = np.abs(t - out[-1]['tc']) < out[-1]['T14_h'] / 48
    oot = w & ~ins & (q == 0)
    for i, (arr, lab) in enumerate(((b, 'SAP_BKG e-/s'), (x, 'SAP_X'), (y, 'SAP_Y'))):
        ax[i + 1, j].plot(t[w], arr[w], '.', ms=2); ax[i + 1, j].set_ylabel(lab)
        for a in (ax[i + 1, j],): a.axvspan(out[-1]['tc'] - out[-1]['T14_h'] / 48, out[-1]['tc'] + out[-1]['T14_h'] / 48, alpha=.2)
        print(f'  {k} {lab}: in-eclipse mean {np.nanmean(arr[ins]):.4f}  oot(q0,+-1.2d) mean {np.nanmean(arr[oot]):.4f} sd {np.nanstd(arr[oot]):.4f}  shift/sd {(np.nanmean(arr[ins])-np.nanmean(arr[oot]))/np.nanstd(arr[oot]):.2f}')
    print(f'  {k} quality values in eclipse:', sorted(set(int(v) for v in q[ins])), ' flagged', int(np.sum(q[ins] != 0)), 'of', int(ins.sum()))
plt.tight_layout(); plt.savefig('ecl.png', dpi=80); json.dump(out, open('ecl.json', 'w'), indent=0)
