"""Run 11b: the five tabled secondaries run 10a called too shallow for their primaries.
Run from the repository root:
  python3 reviews/2026-11-24-duet-research-runs-1-4/run11-ledger/shallow_secondaries.py
Uses run 10a's bound (invisible_secondary.py) with both Earthshine's fitted
primary depth and the table's, and reports the secondary phase: an
eccentric orbit lets the occultation be grazing while the transit is
central, so the circular-orbit bound only applies near phase 0.5.
"""
import sys, os
import numpy as np, pandas as pd
D = 'reviews/2026-11-24-duet-research-runs-1-4/'
sys.path.insert(0, D + 'run10-twins-and-r1003')
import invisible_secondary as m
e = pd.read_csv(D + 'run10-twins-and-r1003/earthshine-pop-results-855.csv').set_index('review_id')
h = pd.read_csv('reviews/2026-11-23-pipeline-and-survey-review/host-stars.csv').set_index('review_id')
Ts = np.arange(2300, 12000, 10)
print('row    P_d     R1   T1    logg  prim_fit prim_tab  sec_tab  phase  |phase-.5|  pred_fit pred_tab  tab/pred  T2_implied')
for i in ['R978', 'R1512', 'R1504', 'R1416', 'R1225']:
    r = e.loc[i].copy()
    _, pf, _ = m.bound(r)
    r2 = r.copy(); r2['depth_fit_ppt'] = h.loc[i, 'depth_ppt']
    _, pt, _ = m.bound(r2)
    sd, ph = h.loc[i, 'secondary_depth_ppt'], h.loc[i, 'secondary_phase']
    pred = min(pf, pt)
    # companion temperature the tabled ratio implies if both eclipses are central
    target = sd / (min(r.depth_fit_ppt, h.loc[i, 'depth_ppt']) / m.F_LD)
    S = np.array([m.surf(t) for t in Ts]) / m.surf(r.teff)
    t2 = Ts[np.argmin(abs(S - target))]
    print(f'{i:6s} {r.P_d:7.3f} {r.rad:5.2f} {r.teff:5.0f} {r.logg:5.2f} {r.depth_fit_ppt:8.1f} {h.loc[i,"depth_ppt"]:8.1f} '
          f'{sd:8.2f} {ph:6.3f} {abs(ph-0.5):9.3f} {pf:9.1f} {pt:8.1f} {sd/pred:9.2f} {t2:8d}')
