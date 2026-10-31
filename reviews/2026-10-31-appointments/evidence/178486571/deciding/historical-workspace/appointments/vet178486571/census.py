"""Blind dip census (QLP SAP, q==0 and all-q): running 0.2-d box vs 1.5-d local median, every sector; plus the B-window
(s87 3677.42 +- 0.62 d from observed A ephemeris and Gaia phase sep 0.8222+-0.0184) in QLP all-q and TARS.
python census.py -> census.txt, bwin.png"""
import numpy as np, matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
from astropy.io import fits
D = '[local path omitted]'
def box(t, f, w=0.2, base=1.5):
    out = []
    for tc in np.arange(t.min(), t.max(), 0.02):
        i = np.abs(t - tc) < w / 2; o = (np.abs(t - tc) < base / 2) & ~(np.abs(t - tc) < w)
        if i.sum() < 3 or o.sum() < 6: continue
        out.append((tc, 1 - np.median(f[i]) / np.median(f[o]), i.sum()))
    return np.array(out)
for s in (7, 33, 87):
    d = fits.open(D + f'178486571_s{s:03d}.fits')[1].data
    for allq in (False, True):
        t = np.array(d['TIME'], float); f = np.array(d['SAP_FLUX'], float); q = np.array(d['QUALITY'], int)
        ok = np.isfinite(t) & np.isfinite(f) & (f > 0) & ((q == 0) | allq); t, f = t[ok], f[ok]
        b = box(t, f); sd = 1.4826 * np.median(np.abs(b[:, 1] - np.median(b[:, 1])))
        hits = b[b[:, 1] > max(0.004, 5 * sd)]
        groups = []
        for h in hits:
            if groups and h[0] - groups[-1][-1][0] < 0.3: groups[-1].append(h)
            else: groups.append([h])
        print(f's{s} {"allq" if allq else "q0  "} box-depth robust sd {sd*1e6:.0f} ppm; dips > max(0.4%, 5 sd):',
              [f'{max(g, key=lambda x: x[1])[0]:.2f} ({max(g, key=lambda x: x[1])[1]*100:.2f}%)' for g in groups])
# B window
d = fits.open(D + '178486571_s087.fits')[1].data
t = np.array(d['TIME'], float); f = np.array(d['SAP_FLUX'], float); q = np.array(d['QUALITY'], int); bk = np.array(d['SAP_BKG'], float)
ok = np.isfinite(t) & np.isfinite(f); t, f, q, bk = t[ok], f[ok], q[ok], bk[ok]; f /= np.median(f[q == 0])
h = fits.open(D + 'vet178486571/hlsp_tars_tess_ffi_s0087-0000000178486571_tess_v01_lc.fits')[1].data
tt, ff = np.array(h['TIME'], float), np.array(h['FLUX'], float); o = np.isfinite(tt) & np.isfinite(ff); tt, ff = tt[o], ff[o] / np.nanmedian(ff[o])
tB, sB = 3677.42, 0.62
for lo, hi in ((tB - sB, tB + sB), (tB - 2 * sB, tB + 2 * sB)):
    m = (t > lo) & (t < hi); m0 = m & (q == 0); mt = (tt > lo) & (tt < hi)
    print(f'B window {lo:.2f}-{hi:.2f}: QLP cadences {m.sum()} (q==0 {m0.sum()}), TARS {mt.sum()}; QLP flags present {sorted(set(q[m]))}')
gaps = np.flatnonzero(np.diff(t) > 0.1); print('QLP s87 gaps >0.1 d:', [(round(t[i], 3), round(t[i + 1], 3)) for i in gaps])
gaps = np.flatnonzero(np.diff(tt) > 0.1); print('TARS s87 gaps >0.1 d:', [(round(tt[i], 3), round(tt[i + 1], 3)) for i in gaps])
fig, ax = plt.subplots(3, 1, figsize=(14, 9), sharex=True)
w = np.abs(t - tB) < 3; ax[0].plot(t[w & (q == 0)], f[w & (q == 0)], 'k.', ms=2); ax[0].plot(t[w & (q != 0)], f[w & (q != 0)], 'r.', ms=2)
wt = np.abs(tt - tB) < 3; ax[1].plot(tt[wt], ff[wt], 'b.', ms=2); ax[2].plot(t[w], bk[w], 'g.', ms=2)
for a in ax: a.axvspan(tB - sB, tB + sB, color='gold', alpha=0.3); a.axvspan(tB - 2 * sB, tB + 2 * sB, color='gold', alpha=0.15)
ax[0].set_ylim(0.98, 1.01); ax[1].set_ylim(0.98, 1.01); ax[0].set_title('s87 B window: QLP SAP (red flagged) / TARS / QLP SAP_BKG')
plt.tight_layout(); plt.savefig('bwin.png', dpi=60)
# binned scatter in the window for a limit
for name, T_, F_ in (('QLP all', t, f), ('TARS', tt, ff)):
    m = np.abs(T_ - tB) < 2 * sB
    if m.sum() > 10:
        tb = np.arange(T_[m].min(), T_[m].max(), 1 / 24); bs = [np.median(F_[m][np.abs(T_[m] - x) < 1 / 48]) for x in tb if (np.abs(T_[m] - x) < 1 / 48).sum() > 3]
        print(f'  {name}: 1-h binned scatter in +-2 sigma window {np.std(bs)*1e6:.0f} ppm, min bin {(1-np.min(bs))*100:.2f}% below median')
