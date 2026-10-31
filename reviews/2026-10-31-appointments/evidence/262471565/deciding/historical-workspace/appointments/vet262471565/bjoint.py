"""Joint B search over phase separation x (B = T0 + n P + x P), s001+s027 (+s095 if covered), W-h box, quadratic
baseline per event (bscan.boxfit). Empirical per-sector sd from bscan null. Also the same statistic at random 'fake A'
phases away from A as a null distribution of the combined depth. python bjoint.py [W_h=24]"""
import sys, numpy as np
sys.argv = [sys.argv[0]] + sys.argv[1:]
exec(open('bscan.py').read().split('for s in (1, 27, 95):')[0])
data = {s: load(s) for s in (1, 27, 95)}
def comb(x):
    num = den = 0; parts = []
    for s, (t, f) in data.items():
        for n in range(-2, 130):
            c = T0 + n * P + x * P
            if t.min() + 0.3 < c < t.max() - 0.3:
                d, e, m = boxfit(t, f, c)
                if np.isfinite(d): parts.append((s, round(c, 2), d, e)); 
    if not parts: return np.nan, np.nan, parts
    sd = {1: 245e-6, 27: 190e-6, 95: 145e-6}
    w = np.array([1 / sd[p[0]] ** 2 for p in parts]); d = np.array([p[2] for p in parts])
    return np.sum(w * d) / np.sum(w), 1 / np.sqrt(np.sum(w)), parts
xs = np.arange(0.40, 0.60, 0.004); R = [comb(x) for x in xs]
print(f'W = {W*24:.0f} h; Gaia phase sep 0.4978 +- 0.0258')
for x, (d, e, p) in zip(xs, R):
    if abs(x - 0.4978) < 0.08: print(f'x {x:.3f}: combined {d*1e6:+5.0f} +- {e*1e6:.0f} ppm  ' + '  '.join(f's{q[0]} {q[1]} {q[2]*1e6:+.0f}' for q in p))
xa = np.array(xs); da = np.array([r[0] for r in R]); win = np.abs(xa - 0.4978) < 0.0258
print(f'max combined in Gaia 1-sigma window: {np.nanmax(da[win])*1e6:+.0f} ppm at x {xa[win][np.nanargmax(da[win])]:.3f}; 3-sigma window max {np.nanmax(da[np.abs(xa-0.4978)<0.077])*1e6:+.0f}')
# null: same statistic at phase offsets far from both A (0) and B (~0.5)
xn = np.concatenate([np.arange(0.06, 0.40, 0.004), np.arange(0.60, 0.94, 0.004)]); Rn = np.array([comb(x)[0] for x in xn])
Rn = Rn[np.isfinite(Rn)]
print(f'null (x in 0.06-0.40, 0.60-0.94): n {len(Rn)}, median {np.median(Rn)*1e6:+.0f}, sd {np.std(Rn)*1e6:.0f}, 95th pct {np.percentile(Rn,95)*1e6:+.0f}, max {Rn.max()*1e6:+.0f} ppm')
