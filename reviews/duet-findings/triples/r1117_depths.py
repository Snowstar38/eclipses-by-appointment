"""R1117 (TIC 299941037, P = 2.636664 d): are the two eclipse depths changing?

Compares Fable 5's per-sector core and peak depths of eclipses A and B measured
two ways from the house QLP/SPOC cache:
  r1117-per-sector-shared.csv  both eclipses against one sector-wide median baseline
  r1117-per-sector-local.csv   each eclipse against a line fitted to its own
                               flanks, 1.0-2.5 h from centre (fold2p_local.py)
Reports B - A, the B/A ratio by era, and its trend in time.
Usage: python3 reviews/duet-findings/triples/r1117_depths.py
"""
import os, numpy as np, pandas as pd

HERE = os.path.dirname(os.path.abspath(__file__))
ERAS = [('2020-21', 27, 39), ('2023', 61, 69), ('2025', 87, 98)]
# mid-sector years: TESS sector n starts 2018-07-25 + ~27.4 d per sector (approx.)
def year(s):
    return 2018.56 + (s - 0.5) * 27.4 / 365.25

for name in ('shared', 'local'):
    d = pd.read_csv(os.path.join(HERE, f'r1117-per-sector-{name}.csv'))
    dBA = d.coreB_ppt - d.coreA_ppt
    rel = dBA / d.coreA_ppt
    print(f'== {name} baseline ({len(d)} sectors)')
    print(f'  core B - A: mean {dBA.mean():+.2f} +- {dBA.std(ddof=1)/np.sqrt(len(d)):.2f} ppt'
          f' ({100*rel.mean():+.2f}% of A); B shallower in {(dBA < 0).sum()} of {len(d)}')
    for lab, s0, s1 in ERAS:
        m = (d.sector >= s0) & (d.sector <= s1)
        print(f'  {lab}: n={m.sum():2d}  median core B/A {np.median(d.coreB_ppt[m]/d.coreA_ppt[m]):.3f}'
              f'  peak B/A {np.median(d.peak_ratio_BA[m]):.3f}  median core A {np.median(d.coreA_ppt[m]):.1f} ppt')
    t = year(d.sector.values); r = (d.coreB_ppt / d.coreA_ppt).values
    A = np.vstack([t - t.mean(), np.ones_like(t)]).T
    coef, res, *_ = np.linalg.lstsq(A, r, rcond=None)
    s2 = res[0] / (len(t) - 2) if len(res) else np.var(r - A @ coef, ddof=2)
    se = np.sqrt(s2 * np.linalg.inv(A.T @ A)[0, 0])
    print(f'  trend in core B/A: {coef[0]:+.4f} +- {se:.4f} per year')

loc = pd.read_csv(os.path.join(HERE, 'r1117-per-sector-local.csv'))
print('== local baseline: depth of A by product (QLP step between s67 and s68)')
for lab, m in [('SPOC 2-min s27-39', loc.sector <= 39), ('QLP s61-67', (loc.sector >= 61) & (loc.sector <= 67)),
               ('QLP s68-98', (loc.sector >= 68) & (loc.sector != 97)), ('SPOC 2-min s97', loc.sector == 97)]:
    print(f'  {lab:18s} n={m.sum():2d}  median core A {np.median(loc.coreA_ppt[m]):.1f}  B {np.median(loc.coreB_ppt[m]):.1f} ppt')
