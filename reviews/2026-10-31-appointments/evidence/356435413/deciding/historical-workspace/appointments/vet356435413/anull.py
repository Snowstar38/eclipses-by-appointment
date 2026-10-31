"""A-conjunction coverage and upper limits. For each A window (B ephemeris + Gaia phase separation, +-3 sigma = 0.79 d),
in each pipeline (QLP q0, QLP all, TESS-SPOC all cadences, SPOC 2-min all, TARS): fraction of window covered and the
deepest box dip for box widths 3.4 h (B-like) and 6.7 h (A central duration if it scaled with separation).
Box depth = median of 1.2-d flanks minus mean in box; noise from the same statistic at random off-window positions. -> anull.txt, anull.png"""
import json, numpy as np, matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
from ecl import load, F
ep = json.load(open('ephemB.json')); P, T0 = ep['P'], ep['T0']; sA = 0.0096 * P
wins = [T0 + (k + 1 - 0.7014) * P for k in range(-1, 60)]; wins = [min(wins, key=lambda w: abs(w - x)) for x in (1992.5, 2019.9, 2734.3, 2761.8, 3476.2)]
fig, axs = plt.subplots(5, 1, figsize=(14, 16)); comb = {}
for i, (wA, s) in enumerate(zip(wins, (25, 26, 52, 53, 79))):
    a = axs[i]
    for j, key in enumerate(['QLP%d' % s, 'QLP%dall' % s, 'TSPOC%dall' % s, 'TARS%d' % s] + (['SPOC79all'] if s == 79 else [])):
        allq = key.endswith('all'); k = key[:-3] if allq else key
        t, f, q, bk, x, y = load(k, allq)
        w = np.abs(t - wA) < 2.5; t, f, q = t[w], f[w], q[w]
        if len(t) < 10: print(f's{s} A {wA:.2f} {key}: no data'); continue
        f = f / np.median(f); dt = np.median(np.diff(t))
        grid = np.arange(wA - 3 * sA, wA + 3 * sA, dt)
        cov = np.mean([np.any(np.abs(t - g) < dt) for g in grid])
        res = []
        for W in (3.4 / 24, 6.7 / 24):
            best = (0, None)
            for c in np.arange(wA - 3 * sA, wA + 3 * sA, 0.01):
                ii = np.abs(t - c) < W / 2; oo = (np.abs(t - c) > W / 2 + 0.05) & (np.abs(t - c) < W / 2 + 1.2)
                if ii.sum() >= max(3, 0.5 * W / dt) and oo.sum() > 10:
                    dd = np.median(f[oo]) - np.mean(f[ii])
                    if dd > best[0] or best[1] is None: best = (dd, c)
            # noise: same statistic in-window spread
            vals = []
            for c in np.arange(t.min() + W, t.max() - W, W / 2):
                ii = np.abs(t - c) < W / 2; oo = (np.abs(t - c) > W / 2 + 0.05) & (np.abs(t - c) < W / 2 + 1.2)
                if ii.sum() >= max(3, 0.5 * W / dt) and oo.sum() > 10: vals.append(np.median(f[oo]) - np.mean(f[ii]))
            res.append((W * 24, best[0], best[1], np.std(vals) if len(vals) > 3 else np.nan))
        line = f's{s} A {wA:.2f}+-{sA:.2f} {key:10s}: coverage(+-3sig) {cov*100:4.0f}%  flagged-in-window {np.mean(q[np.abs(t-wA)<3*sA]!=0)*100 if np.any(np.abs(t-wA)<3*sA) else np.nan:4.0f}%  ' + \
               '  '.join(f'box{W:.1f}h max dip {d*100:+.3f}% at {c} (sd {sd*100:.3f}%)' for W, d, c, sd in res)
        print(line)
        a.plot(t, f - 0.02 * j, '.', ms=2, label=key)
    a.axvspan(wA - 3 * sA, wA + 3 * sA, color='b', alpha=0.1); a.axvline(wA, color='b'); a.set_ylim(0.9, 1.02); a.legend(fontsize=7); a.set_title(f's{s} A window {wA:.2f}')
plt.tight_layout(); plt.savefig('anull.png', dpi=60)
