"""Run 13f: what would the 20-60 d search's windows cost with Gaia's correlations at 3, 4.5 and 6 sigma?
Uses Fable 5.1's fable51-window-halfwidths.csv (mid-mission sigma_T both ways, 12,760 source-conjunction rows).
Run from the repository root:
  python3 reviews/2026-11-24-duet-research-runs-1-4/run13-a-sample-gaia-epoch/search_window_budget.py
"""
import numpy as np, pandas as pd
h = pd.read_csv('reviews/2026-11-24-duet-research-runs-1-4/fable51-window-halfwidths.csv')
def hw(s, k): return np.clip(k * s, 0.25, 7.0)
base = hw(h.sigma_T_independent_d, 3)
assert np.allclose(base, h.halfwidth_independent_d, atol=0.01), 'recipe mismatch'   # sigma is tabled to 3 decimals
print(f'rows {len(h)}; search recipe (3 sigma independent): median half-width {base.median():.2f} d, at the 7-d cap {np.mean(base >= 7):.0%},'
      f' total {2 * base.sum() / 1e3:.1f} kd, fraction of the orbit {np.median(2 * base / h.P_d):.2f} (median)')
for k in (3, 4.5, 6):
    x = hw(h.sigma_T_corr_vec_d, k)
    print(f'corr_vec at {k} sigma: median {x.median():.2f} d, at cap {np.mean(x >= 7):.0%}, total {2 * x.sum() / 1e3:.1f} kd'
          f' ({x.sum() / base.sum():.0%} of the search), median fraction of orbit {np.median(2 * x / h.P_d):.2f}')
