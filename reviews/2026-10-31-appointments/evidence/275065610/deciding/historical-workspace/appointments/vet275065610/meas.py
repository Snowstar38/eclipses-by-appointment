"""Step 2: overview plots, trapezoid fits of the A eclipses from raw SAP (all cadences, then q==0), bkg/centroid
through each, and a blind box census. python -X utf8 meas.py"""
import sys, json, numpy as np, matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
sys.path.insert(0, '.'); import vetlib as v
D = {v.load_qlp(f)['sec']: v.load_qlp(f) for f in v.qlp_files(275065610)}
guess = {26: 2023.87, 53: 2753.15, 79: 3454.38, 80: 3482.43}
fig, ax = plt.subplots(4, 4, figsize=(22, 14))
for i, (s, d) in enumerate(sorted(D.items())):
    t, f, q = d['t'], d['f'], d['q']; g = q == 0
    a = ax[i, 0]; a.plot(t[~g], f[~g], '.', c='0.7', ms=2); a.plot(t[g], f[g], '.', ms=2); a.set_title(f's{s} SAP all (grey=flagged)')
    a.axvline(guess[s], c='r', alpha=.3)
    for c in json.load(open('conj.json')):
        if t.min() - 1 < c[2] < t.max() + 1: a.axvline(c[2], c='orange' if c[0] == 'A' else 'purple', ls='--')
    ax[i, 1].plot(t, d['bkg'], '.', ms=2); ax[i, 1].set_title('SAP_BKG/medflux')
    ax[i, 2].plot(t, d['x'] - np.nanmedian(d['x']), '.', ms=2, label='x'); ax[i, 2].plot(t, d['y'] - np.nanmedian(d['y']), '.', ms=2, label='y'); ax[i, 2].legend()
    # zoom
    m = np.abs(t - guess[s]) < 1.0; a = ax[i, 3]
    a.plot(t[m & ~g], f[m & ~g], '.', c='0.6', ms=3); a.plot(t[m & g], f[m & g], '.', ms=3)
    for c in json.load(open('conj.json')):
        if c[0] == 'A' and abs(c[2] - guess[s]) < 2: a.axvline(c[2], c='orange', ls='--')
plt.tight_layout(); plt.savefig('overview.png', dpi=70)
res = {}
for s, d in sorted(D.items()):
    for lab, use in (('all', np.ones_like(d['q'], bool)), ('q0', d['q'] == 0)):
        t, f = d['t'], d['f']; m = (np.abs(t - guess[s]) < 0.8) & use
        if m.sum() < 20: print(s, lab, 'too few', m.sum()); continue
        tt, ff = t[m], f[m]
        best, c2, sig, tref = v.fit_trap(tt, ff, guess[s], 0.05, 0.25, 0.08, npoly=2)
        et = v.t0_error(tt, ff, best, tref, sig)
        # red-noise beta from residual binning (30-min bins)
        r = ff - v.model(best, tt, tref); dt = np.median(np.diff(tt)); nb = max(1, int(round(0.0208 / dt)))
        nbin = len(r) // nb; br = r[:nbin * nb].reshape(nbin, nb).mean(1) if nbin > 3 else r
        beta = max(1, np.std(br) / (np.std(r) / np.sqrt(nb))) if nb > 1 else 1
        ing = (np.abs(tt - best[0]) < best[2] / 2)
        print(f"s{s} {lab:3s} n={m.sum():4d} n_in={ing.sum():3d} t0={best[0]:.4f}+-{et*beta:.4f} (beta {beta:.2f}) depth={best[1]*1e6:.0f}ppm T14={best[2]*24:.2f}h T12={best[3]*24:.2f}h flat={(best[2]-2*best[3])*24:.2f}h rms={sig*1e6:.0f}")
        # background and centroid through eclipse vs out
        o = (np.abs(tt - best[0]) > best[2] / 2 + 0.05)
        for k in ('bkg', 'x', 'y'):
            z = d[k][m]
            if np.all(np.isnan(z)): continue
            print(f"      {k}: in-out = {np.nanmedian(z[ing]) - np.nanmedian(z[o]):+.5f}  (out scatter {np.nanstd(z[o]):.5f})")
        print('      flags in eclipse:', dict(zip(*np.unique(d['q'][m][ing], return_counts=True))))
        res[f'{s}_{lab}'] = dict(t0=best[0], et=et * beta, dep=best[1], T14=best[2], T12=best[3], rms=sig)
json.dump(res, open('meas.json', 'w'), indent=1)
