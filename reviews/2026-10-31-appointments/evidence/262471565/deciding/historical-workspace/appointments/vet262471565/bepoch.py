"""Per-epoch B-window table: for each covered epoch, the 4.5 h box depth (local quadratic, q==0 QLP) at phases 0.4416-0.5220
(Gaia 1 sigma) and 0.36-0.60 (3 sigma): max, at which phase, phase coverage, and that epoch's empirical box-depth scatter over
all its phases away from the primary. python -X utf8 bepoch.py"""
import json, numpy as np
from lc import all_lc
ep = json.load(open('ephem.json')); P = ep['P']; T0 = ep['T0_n0']; L = all_lc()
t = np.concatenate([d['t'][d['q'] == 0] for d in L]); f = np.concatenate([d['f'][d['q'] == 0] for d in L])
sec = np.concatenate([np.full((d['q'] == 0).sum(), d['sec']) for d in L])
def box(tc, dur=4.5 / 24):
    w = np.abs(t - tc) < 0.6; tt, ff = t[w] - tc, f[w]; inb = np.abs(tt) < dur / 2
    if inb.sum() < 3 or (tt < -dur / 2).sum() < 5 or (tt > dur / 2).sum() < 5: return None
    A = np.vstack([np.ones_like(tt), tt, tt ** 2, -inb.astype(float)]).T; c, *_ = np.linalg.lstsq(A, ff, rcond=None); return c[3]
for n in range(-2, 60):
    ph = np.arange(0.05, 0.95, 0.0025); dd = np.array([box(T0 + (n + p) * P) if box(T0 + (n + p) * P) is not None else np.nan for p in ph])
    if np.all(np.isnan(dd)): continue
    w1 = (ph >= 0.4416) & (ph <= 0.522); w3 = (ph >= 0.36) & (ph <= 0.60); sd = np.nanstd(dd)
    s = sorted(set(sec[np.abs(t - (T0 + (n + 0.48) * P)) < 25].astype(int)))
    c1 = np.mean(np.isfinite(dd[w1])); c3 = np.mean(np.isfinite(dd[w3]))
    if c3 == 0: continue
    m1 = np.nanmax(dd[w1]) if c1 else np.nan
    print(f"n={n:3d} s{s}: coverage 1-sig window {c1:.2f}, 3-sig {c3:.2f}; max depth in 1-sig {m1*1e3:+.2f} ppt"
          f"{' at %.4f' % ph[w1][np.nanargmax(dd[w1])] if c1 else ''}; in 3-sig {np.nanmax(dd[w3])*1e3:+.2f} ppt at {ph[w3][np.nanargmax(dd[w3])]:.4f}; epoch box-depth scatter {sd*1e3:.2f} ppt")
