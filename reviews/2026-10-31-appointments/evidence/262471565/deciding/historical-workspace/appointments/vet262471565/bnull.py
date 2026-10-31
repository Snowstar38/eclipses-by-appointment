"""Empirical noise of the combined box statistic: box depth (local quadratic +-0.6 d, q==0 QLP) combined over all epochs at each
trial phase 0.04-0.96 (A eclipse +-0.03 excluded), for 4.5 h and 2 h boxes; compares the B-window values with the full-phase
distribution. python -X utf8 bnull.py"""
import json, numpy as np, matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
from lc import all_lc
ep = json.load(open('ephem.json')); P = ep['P']; T0 = ep['T0_n0']; L = all_lc()
t = np.concatenate([d['t'][d['q'] == 0] for d in L]); f = np.concatenate([d['f'][d['q'] == 0] for d in L])
def box(tc, dur):
    w = np.abs(t - tc) < 0.6; tt, ff = t[w] - tc, f[w]; inb = np.abs(tt) < dur / 2
    if inb.sum() < 3 or (~inb).sum() < 10 or (tt[~inb] < 0).sum() < 5 or (tt[~inb] > 0).sum() < 5: return None
    A = np.vstack([np.ones_like(tt), tt, tt ** 2, -inb.astype(float)]).T
    c, *_ = np.linalg.lstsq(A, ff, rcond=None); r = ff - A @ c; s = 1.4826 * np.median(np.abs(r))
    return c[3], s * np.sqrt(np.linalg.inv(A.T @ A)[3, 3])
fig, ax = plt.subplots(2, 1, figsize=(12, 7))
for j, dh in enumerate((4.5, 2.0)):
    dur = dh / 24; res = []
    for phi in np.arange(0.04, 0.9601, 0.0025):
        if abs(phi) < 0.03 or abs(phi - 1) < 0.03: continue
        dd = []
        for n in range(-2, 60):
            tc = T0 + (n + phi) * P
            if t.min() - 1 < tc < t.max() + 1:
                r = box(tc, dur)
                if r: dd.append((n, r[0], r[1]))
        dd = np.array(dd); w = 1 / dd[:, 2] ** 2; m = np.sum(dd[:, 1] * w) / np.sum(w); e = 1 / np.sqrt(np.sum(w))
        res.append((phi, m, e, len(dd), np.std(dd[:, 1]) / np.sqrt(len(dd)) if len(dd) > 2 else np.nan))
    R = np.array(res); snr = R[:, 1] / R[:, 2]
    print(f'{dh} h box: combined S/N over all phases: median {np.median(snr):.2f}, robust sd {1.4826*np.median(np.abs(snr-np.median(snr))):.2f}, sd {np.std(snr):.2f}; depth sd {np.std(R[:,1])*1e3:.2f} ppt (median formal err {np.median(R[:,2])*1e3:.2f})')
    print(f'   max S/N {snr.max():.1f} at phase {R[np.argmax(snr),0]:.4f}; min S/N {snr.min():.1f} at {R[np.argmin(snr),0]:.4f}; # phases with S/N>4.5: {(snr>4.5).sum()} of {len(snr)}; with S/N<-4.5: {(snr<-4.5).sum()}')
    b = (R[:, 0] >= 0.4416) & (R[:, 0] <= 0.5220)
    print(f'   Gaia 1-sigma B window 0.442-0.522: max depth {R[b,1].max()*1e3:.2f} ppt (S/N {snr[b].max():.1f}); empirical depth sd {np.std(R[:,1])*1e3:.2f} ppt -> 3-sigma empirical upper limit {(R[b,1].max()+3*np.std(R[:,1]))*1e3:.2f} ppt')
    b3 = (R[:, 0] >= 0.36) & (R[:, 0] <= 0.60)
    print(f'   Gaia 3-sigma window 0.36-0.60: max depth {R[b3,1].max()*1e3:.2f} ppt at {R[b3,0][np.argmax(R[b3,1])]:.4f}; 3-sigma empirical upper limit {(R[b3,1].max()+3*np.std(R[:,1]))*1e3:.2f} ppt')
    ax[j].errorbar(R[:, 0], R[:, 1] * 1e3, R[:, 2] * 1e3, fmt='.', ms=3); ax[j].axvspan(0.4416, 0.5220, color='gold', alpha=.3); ax[j].axhline(0, c='k'); ax[j].set_ylabel(f'{dh} h box depth ppt')
    json.dump(R.tolist(), open(f'bnull_{dh}h.json', 'w'))
ax[1].set_xlabel('phase from primary'); plt.tight_layout(); plt.savefig('bnull.png', dpi=90)
