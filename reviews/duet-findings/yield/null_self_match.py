"""The appointment search's null veto in 'centre' mode: which finds veto themselves.

In appoint.py a null window has the half-width hw of the find's window, hw = min(max(3 sigma, 0.25 d), 7 d), and in
'centre' mode (the main search) only its centre is kept hw + 1 d from each predicted centre. A null window can then
reach to 1 d of a predicted centre, so a find more than 1 d from its predicted conjunction, inside a window wider than
that, can be matched by a null window holding the same box, and '>=' counts the tie. Earthshine's re-run of the 19
null-vetoed period-free finds at Gaia's period (null-vetoes-earthshine.csv: class, exceedances in 'centre' and in
'overlap' mode) is tested here against the find's offset from its conjunction (Sol's periodfree-cut-audit.csv), and
the paper's appointment finds (a-window-coverage.csv) are checked for a shortage of events more than 1 d out.
Last, the share of eclipses that the 7-d cap on hw leaves outside the window, from Fable 5.1's conjunction errors.

Run from the repository root: python3 reviews/duet-findings/yield/null_self_match.py
Needs numpy, pandas and SciPy. Writes null-self-match-output.txt here.
"""
import os, sys
sys.dont_write_bytecode = True
import numpy as np, pandas as pd
from scipy.stats import norm, poisson

HERE = os.path.dirname(os.path.abspath(__file__))

def main():
    out = open(os.path.join(HERE, 'null-self-match-output.txt'), 'w')
    P_ = lambda *a: print(*a, file=out)
    a = pd.read_csv(os.path.join(HERE, 'periodfree-cut-audit.csv'))
    e = pd.read_csv(os.path.join(HERE, 'null-vetoes-earthshine.csv'))
    a['off_d'] = a.dphase * a.P_gaia_d
    a['sig_d'] = np.where(a.dt_sigma != 0, a.off_d / a.dt_sigma.replace(0, np.nan), np.nan)
    a['hw'] = np.clip(3 * a.sig_d, 0.25, 7)
    a = a.merge(e[['review_id', 'class', 'centre_exceed', 'overlap_n', 'overlap_exceed']], on='review_id', how='left')
    a['class'] = a['class'].fillna('not null-vetoed')
    a['reach'] = (a.off_d.abs() > 1) & (a.hw.fillna(7) > 1)
    P_('the 31 period-free finds at Gaia period: offset from the predicted conjunction against the null class')
    P_(a[['review_id', 'P_gaia_d', 'off_d', 'sig_d', 'hw', 'null_exceed', 'class', 'centre_exceed', 'overlap_n', 'overlap_exceed']]
       .sort_values(['class', 'off_d']).round(2).to_string(index=False))
    t = pd.crosstab(a['class'], a.reach.map({True: '|t - tc| > 1 d', False: '|t - tc| <= 1 d'}))
    P_('\n', t.to_string())
    s = a[a['class'] == 'self']
    P_(f"\nself-matched: {len(s)}, offsets {s.off_d.abs().min():.2f}-{s.off_d.abs().max():.2f} d; in overlap mode all go to 0 exceedances, "
       f"{int((s.overlap_n > 0).sum())} with a null placed, {int((s.overlap_n == 0).sum())} with none")
    r = a[a.reach & a.null_exceed.notna()]
    P_(f"finds more than 1 d out with a null: {len(r)}, self-vetoed {int((r['class'] == 'self').sum())}; "
       f"finds within 1 d with a null: {int((~a.reach & a.null_exceed.notna()).sum())}, self-vetoed {int(((~a.reach) & (a['class'] == 'self')).sum())}")

    c = pd.read_csv(os.path.join(HERE, '..', 'gaia-errors', 'a-window-coverage.csv'))
    P_('\nthe paper\'s A systems: events more than 1 d from the conjunction, observed and expected from each sigma (inside the window)')
    for col in ['sig_tess_ind', 'sig_tess_full']:
        for m, g in c.groupby('method'):
            sg = g[col]
            if sg.isna().any() or len(g) < 10: continue
            hw = np.clip(3 * sg, 0.25, 7)
            ex = (2 * (norm.cdf(hw / sg) - norm.cdf(1 / sg))).clip(0, None).sum()
            ob = int((g.offset_tess_d.abs() > 1).sum())
            P_(f'  {col:13s} {m:5s} n {len(g):3d}  observed {ob:3d}  expected {ex:5.1f}  P(<= observed) {poisson.cdf(ob, ex):.3f}')
    P_(f"  App pulls with the independent errors: standard deviation {c[c.method == 'App'].z_tess_ind.std():.2f}")

    h = pd.read_csv(os.path.join(HERE, '..', 'gaia-errors', 'fable51-window-halfwidths.csv'))
    hw = np.clip(3 * h.sigma_T_independent_d, 0.25, 7)
    P_(f'\nthe 7-d cap: {(hw >= 7).mean():.0%} of the {len(h)} main-search conjunction windows (mid-mission) sit at it')
    sb2 = h.nss_solution_type.str.startswith('SB2')
    for col in ['sigma_T_independent_d', 'sigma_T_corr_vec_d']:
        lost = 2 * norm.sf(hw / h[col])
        P_(f'  eclipses outside their window with {col}: {lost.mean():.1%} (capped conjunctions {lost[hw >= 7].mean():.1%}; SB1 {lost[~sb2].mean():.1%}, SB2 {lost[sb2].mean():.1%})')
    out.close()

if __name__ == '__main__':
    main()
