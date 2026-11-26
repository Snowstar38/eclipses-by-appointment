"""Are the paper's QLP-only eclipse timing variations in A204 and A167 the house clock?

The per-sector O-C values are those printed in reviews/supplement-evidence/A204-source/report.md
(both kinds: about +2.5..+3 min in s099 falling to -3..-3.7 min in s102, s011-s065 near 0)
and A167-source/report.md (primaries -1.0, -2.7, +2.8, +3.0, +0.6, -2.0 and secondaries
-1.6, -2.3, +2.6, +3.1, +1.3, -1.6 min in s011, s038, s064, s065, s100, s101). Sector mid-times
are approximate (+-5 d, which changes the Roemer delay by < 0.3 min). The clock model is
time_offsets.correction_min; the predicted O-C pattern is that model after the same linear
ephemeris fit, and the bias of a prediction for BTJD 5000 is the fitted line's value there.
usage (from the repo root): python3 reviews/duet-findings/timing/a_system_etvs.py
"""
import os, sys
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from time_offsets import correction_min  # noqa: E402

SYS = {
    'A204': dict(ra=205.74543, dec=-58.85052, sectors=[11, 38, 65, 99, 100, 101, 102], t=[1610, 2320, 3050, 4060, 4087, 4113, 4139],
                 obs={'both kinds': [0, 0, 0, 2.75, np.nan, np.nan, -3.35]}),
    'A167': dict(ra=200.31887, dec=-62.05478, sectors=[11, 38, 64, 65, 100, 101], t=[1610, 2320, 3035, 3062, 4087, 4113],
                 obs={'primaries': [-1.0, -2.7, 2.8, 3.0, 0.6, -2.0], 'secondaries': [-1.6, -2.3, 2.6, 3.1, 1.3, -1.6]}),
}
for name, d in SYS.items():
    t = np.array(d['t'], float); s = np.array(d['sectors'])
    c = correction_min(s, t, d['ra'], d['dec'])
    A = np.vstack([np.ones_like(t), t - t.mean()]).T

    def detrend(y):
        m = np.isfinite(y)
        p = np.linalg.lstsq(A[m], y[m], rcond=None)[0]
        return y - A @ p, p
    pred, p = detrend(c)
    print(f'{name}: clock offsets by sector (min) ' + ' '.join(f's{a}:{b:+.2f}' for a, b in zip(s, c)))
    print('   predicted O-C after a linear fit   ' + ' '.join(f'{x:+5.1f}' for x in pred))
    for k, o in d['obs'].items():
        o = np.array(o, float)
        r0, _ = detrend(o); r1, _ = detrend(o - c); m = np.isfinite(o)
        print(f'   observed, {k:11s}            ' + ' '.join(f'{x:+5.1f}' for x in o))
        print(f'   left after the correction        ' + ' '.join(f'{x:+5.1f}' for x in r1) +
              f'   rms {np.sqrt(np.nanmean(r0[m] ** 2)):.1f} -> {np.sqrt(np.nanmean(r1[m] ** 2)):.1f} min')
    i100, i101 = list(s).index(100), list(s).index(101)
    print(f'   s100 -> s101 step predicted {c[i101] - c[i100]:+.1f} min; first s99+ sector -> last sector swing predicted {pred[-1] - pred[np.argmax(s >= 99)]:+.1f} min')
    print(f'   bias of a prediction at BTJD 5000 from this fit: {p[0] + p[1] * (5000 - t.mean()):+.1f} min\n')
