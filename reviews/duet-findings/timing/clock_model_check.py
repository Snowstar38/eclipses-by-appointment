"""How well does a single clock correction describe sectors 14 and 15?

timing/s1415-tspoc-times.csv holds Fable 5's re-times of every s14/15 event in etv-events.csv
on TESS-SPOC light curves of the same FFIs (TESS-SPOC times are barycentric in every sector;
QLP-minus-TESS-SPOC at matched cadences on three s16 controls is a constant +1.9 s). The
shift (TESS-SPOC minus QLP) is the QLP time column's error at that event. Compare it, per
star and sector, with the Roemer delay: a time that skipped the correction would need
shift = -roemer (k = 1); the earlier global model was k = 1.5.
usage (from the repo root): python3 reviews/duet-findings/timing/clock_model_check.py
"""
import os, sys
import numpy as np, pandas as pd
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from time_offsets import roemer_min, positions  # noqa: E402

D = os.path.dirname(os.path.abspath(__file__)) + '/'
pos, rid = positions()
f = pd.read_csv(D + 's1415-tspoc-times.csv'); f['tic'] = f.tic.astype(str)
print(f'{len(f)} s14/15 events: ' + ', '.join(f'{k} {v}' for k, v in f.flag.value_counts().items()))
ok = f[(f.flag == 'ok') & f.tic.isin(pos)].copy()
ok['rm_s'] = [roemer_min(t, *pos[x]) * 60 for x, t in zip(ok.tic, ok.t_mid_listed)]
ok['w'] = 1 / ok.err_s ** 2
g = ok.groupby(['tic', 'sector']).apply(lambda q: pd.Series(dict(
    n=len(q), shift_s=np.average(q.shift_s, weights=q.w), err_s=q.w.sum() ** -0.5,
    roemer_s=q.rm_s.mean(), within_rms_s=q.shift_s.std(ddof=0) if len(q) > 1 else np.nan)), include_groups=False).reset_index()
g.insert(2, 'review_id', g.tic.map(rid))
g['k'] = -g.shift_s / g.roemer_s
g['left_after_1p5_s'] = g.shift_s + 1.5 * g.roemer_s
pd.set_option('display.width', 200)
print(g.round(2).to_string(index=False))
good = g[g.err_s < 60]
print(f'\n{len(g)} star-sectors; {len(good)} with errors < 60 s')
print(f'k = -shift/roemer: median {good.k.median():.2f}, range {good.k.min():.2f} to {good.k.max():.2f}')
print(f'rms shift {np.sqrt((good.shift_s ** 2).mean()):.0f} s; rms left after the 1.5x model {np.sqrt((good.left_after_1p5_s ** 2).mean()):.0f} s; '
      f'after the best single k {np.sqrt(((good.shift_s + good.k.median() * good.roemer_s) ** 2).mean()):.0f} s')
chi = ((good.left_after_1p5_s / good.err_s) ** 2).sum()
print(f'chi2 of the 1.5x model against the re-times: {chi:.0f} for {len(good)} star-sectors')
print(f'within a star-sector the shift is steady: median rms {g.within_rms_s.median():.0f} s over the events')
