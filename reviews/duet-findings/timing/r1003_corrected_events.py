"""Write triples/fable-r1003/r1003_events_clock_corrected.csv: Fable 5's R1003 event times with
time_offsets.correction_min applied (sector 101 QLP; sector 100 is SPOC, left as is), and oc_d recomputed against
a linear ephemeris fitted to the deep (> 50 ppt) events.
usage (from the repo root): python3 reviews/duet-findings/timing/r1003_corrected_events.py
"""
import os, sys
import numpy as np, pandas as pd
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from time_offsets import correction_min  # noqa: E402

F = 'reviews/duet-findings/triples/fable-r1003/'
e = pd.read_csv(F + 'r1003_events.csv')
e['t_btjd'] = (e.t_btjd - correction_min(e.sector.values, e.t_btjd.values, 193.786609, -65.53488, spoc=e.sector.values == 100) / 1440).round(6)
d = e[e.depth_ppt > 50]; w = 1 / d.sigma_d ** 2
A = np.vstack([np.ones(len(d)), d.epoch]).T
c = np.linalg.solve(A.T @ (A * w.values[:, None]), A.T @ (w * d.t_btjd))
e['oc_d'] = (e.t_btjd - (c[0] + c[1] * e.epoch)).round(6)
e.to_csv(F + 'r1003_events_clock_corrected.csv', index=False)
print(f'deep-event ephemeris P = {c[1]:.7f} d; wrote {F}r1003_events_clock_corrected.csv')
