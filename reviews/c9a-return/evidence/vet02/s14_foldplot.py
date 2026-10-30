# Phase-folded raw SAP (QUALITY==0, each event normalised by a local linear baseline outside +-0.6*T14)
# around primary and secondary, QLP and TESS-SPOC overplotted. One small PNG per star.
import numpy as np, matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
D = '/tmp/claude-0/-home-user-eclipses-paper-review/55c92ff4-798a-544f-be03-9888c6804905/scratchpad/data/vet02'
EP = {'470235665': (1795.74233, 10.326183, [(0, 6.45), (0.52275, 9.0)]), '379251709': (1961.25375, 12.323912, [(0, 4.2), (0.4960, 4.5)])}
for tic, (T0, P, kinds) in EP.items():
    z = np.load(f'{D}/{tic}/lc_sap_q0.npz'); fig, axs = plt.subplots(1, 2, figsize=(9, 3.3))
    for a, (ph0, T14) in zip(axs, kinds):
        for pipe, col in [('QLP', 'C0'), ('SPOC', 'C1')]:
            m = z['p'] == pipe; t = z['t'][m]; f = z['f'][m]
            n = np.round((t - T0) / P - ph0); dt = t - (T0 + (n + ph0) * P); keep = np.abs(dt) < 0.6
            X = []; Yv = []
            for k in np.unique(n[keep]):
                w = keep & (n == k); o = w & (np.abs(dt) > 0.6 * T14 / 24)
                if o.sum() < 10 or (w & (np.abs(dt) < 0.3 * T14 / 24)).sum() < 3: continue
                c = np.polyfit(dt[o], f[o], 1); X.append(dt[w] * 24); Yv.append(f[w] / np.polyval(c, dt[w]))
            if X:
                X = np.concatenate(X); Yv = np.concatenate(Yv)
                if tic == '379251709' and ph0 > 0:  # bin for the shallow secondary
                    b = np.arange(-14, 14.01, 0.5); i = np.digitize(X, b)
                    bx = [X[i == j].mean() for j in np.unique(i) if (i == j).sum() > 20]; by = [np.median(Yv[i == j]) for j in np.unique(i) if (i == j).sum() > 20]
                    a.plot(X, Yv, '.', ms=1, color=col, alpha=0.1); a.plot(bx, by, 'o-', ms=3, color=col, label=pipe + ' (0.5 h bins)')
                    a.set_ylim(0.99, 1.006)
                else:
                    a.plot(X, Yv, '.', ms=1.5, color=col, alpha=0.4, label=pipe)
        a.set_xlabel('hours from predicted mid-eclipse'); a.set_title(f'TIC {tic} phase {ph0}', fontsize=9); a.legend(fontsize=7, markerscale=4)
    axs[0].set_ylabel('SAP flux / local baseline'); fig.tight_layout(); fig.savefig(f's14_fold_{tic}.png', dpi=90)
print('ok')
