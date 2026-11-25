"""Run 11c: what the November 23 host table's depth_ppt measures.
Run from the repository root:
  python3 reviews/2026-11-24-duet-research-runs-1-4/run11-ledger/depth_column.py
Compares the table's depth_ppt and duration_h with Earthshine's trapezoid
fits (depth, T14, T23/T14) for the 855 rows, and with the mean depth a box of
the table's width would measure on Earthshine's trapezoid.
"""
import numpy as np, pandas as pd
D = 'reviews/2026-11-24-duet-research-runs-1-4/run10-twins-and-r1003/'
e = pd.read_csv(D + 'earthshine-pop-results-855.csv').set_index('review_id')
e['r'] = e.depth_fit_ppt / e.depth_tab_ppt          # fitted / tabled depth
e['w'] = e.dur_tab_h / e.T14_fit_h                   # tabled duration as a fraction of T14
ok = e[np.isfinite(e.r) & (e.depth_snr > 10) & np.isfinite(e.T23_over_T14) & np.isfinite(e.w)].copy()

def box_mean(f, w):
    """mean depth of a unit-depth trapezoid (T14 = 1, flat part f) inside a centred box of width w"""
    t = np.linspace(-w / 2, w / 2, 2001); a = np.abs(t)
    return np.where(a < f / 2, 1.0, np.clip((0.5 - a) / ((1 - f) / 2 + 1e-12), 0, 1)).mean()

ok['r_box'] = [1 / box_mean(f, w) for f, w in zip(ok.T23_over_T14, ok.w)]
print(f'rows (depth SNR > 10): {len(ok)}')
print(f'fitted/tabled depth: median {ok.r.median():.3f} (IQR {ok.r.quantile(.25):.3f}-{ok.r.quantile(.75):.3f})')
print(f'tabled duration / fitted T14: median {ok.w.median():.3f} (IQR {ok.w.quantile(.25):.3f}-{ok.w.quantile(.75):.3f})')
print()
print('by eclipse shape (T23/T14 = flat-bottom fraction):')
g = ok.groupby(pd.cut(ok.T23_over_T14, [-.01, .1, .3, .5, .7, 1.0]), observed=True)
print(pd.DataFrame({'n': g.size(), 'fitted/tabled': g.r.median().round(3),
                    'box-mean model': g.r_box.median().round(3)}).to_string())
print()
for k in ['cadence_min']:
    gg = ok.groupby(k).r.agg(['count', 'median']).round(3); print(gg.to_string()); print()
print(f'observed / box-mean model: median {(ok.r / ok.r_box).median():.3f}')
print(f'largest fitted/tabled (> 1.5):')
print(ok[ok.r > 1.5][['depth_tab_ppt', 'depth_fit_ppt', 'T23_over_T14', 'dur_tab_h', 'T14_fit_h']].round(2).to_string())
