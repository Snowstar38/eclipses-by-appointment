"""Does the appointment search lose eclipsers on poorly fitted Gaia orbits?

Gaia DR3's conjunction errors are about right for well-fitted orbits and too small for poor fits (gaia-errors:
SB1 scale 1.24 exp(0.18 F2), SB2 sqrt(chi2/nu)), and the appointment windows are built from those errors. If the
windows miss eclipses on poor fits, the appointment finds should fall with the goodness of fit F2 at fixed predicted
depth, while eclipsers found without the windows (period-free finds at Gaia's period, and catalogued eclipsers
not robustly contradicted in catalogue_check.py, a test that never used the windows) should not.

Each channel is fitted as count = chance x exp(b0 + depth/duration groups + bands + giant + log10 significance + terms),
on the per-target frame of significance_channels.py (expected = p_det for appointment finds, p_ecl otherwise).

Run from the repository root: python3 reviews/duet-findings/yield/fit_quality_yield.py
Needs numpy, pandas and SciPy. Writes fit-quality-yield-output.txt here.
"""
import importlib.util, os, sys
sys.dont_write_bytecode = True
import numpy as np, pandas as pd
from scipy import stats

HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location('sc', os.path.join(HERE, 'significance_channels.py'))
sc = importlib.util.module_from_spec(spec); spec.loader.exec_module(sc)
ROWS = 'reviews/2026-11-26-fable51-main-search-gaia/main-search-gaia-rows.csv'


def main():
    out = open(os.path.join(HERE, 'fit-quality-yield-output.txt'), 'w')
    P_ = lambda *a: print(*a, file=out)
    pd.set_option('display.width', 200)
    g = pd.read_csv(ROWS, dtype={'tic': str}).drop_duplicates('tic').set_index('tic')
    d = sc.frame()
    d['sol'] = d.tic.map(g.nss_solution_type); d['F2'] = d.tic.map(g.goodness_of_fit)
    d['pfP'] = d.periodfree & (np.abs(d.P_ecl/d.P - 1) < 0.02)
    cc = pd.read_csv(os.path.join(HERE, 'catalogue-check.csv'), dtype={'tic': str}).set_index('tic')
    d['cat_free'] = d.tic.map(cc.not_contra).fillna(False).astype(bool)   # not robustly contradicted; no use of the windows
    d['indep'] = d.pfP | d.cat_free
    f = d[np.isfinite(d.significance) & (d.p_det > 0) & d.sol.isin(['SB1', 'SB2']) & d.F2.notna()].copy()
    f['scale'] = np.where(f.sol == 'SB2', np.nan, 1.24*np.exp(0.18*f.F2))
    P_(f'{len(f)} SB1/SB2 targets with a significance, a detection chance and a goodness of fit')

    P_('\nby solution type and F2 tercile (within type): found / expected')
    for sol in ['SB1', 'SB2']:
        s = f[f.sol == sol].copy(); s['F2 tercile'] = pd.qcut(s.F2, 3)
        t = s.groupby('F2 tercile', observed=True).agg(targets=('tic', 'size'), median_significance=('significance', 'median'),
                                                       median_depth=('depth_ppt', 'median'), p_det=('p_det', 'sum'),
                                                       appointment=('found', 'sum'), p_ecl=('p_ecl', 'sum'),
                                                       window_free=('indep', 'sum'))
        t['appointment/p_det'] = t.appointment/t.p_det; t['window_free/p_ecl'] = t.window_free/t.p_ecl
        P_(f'{sol}:'); P_(t.round(3).to_string())

    grp = lambda q: [(q.group == 'shallow').astype(float).values, (q.group == 'long').astype(float).values,
                     (q.band == 'G10-11').astype(float).values, (q.band == 'G11-11.5').astype(float).values,
                     q.giant.astype(float).values, np.log10(q.significance/30).values]
    names = ['sh', 'lo', 'b1', 'b2', 'gi', 's']
    P_('\nPoisson fits with an F2 term (groups, bands, giant, log significance held), coefficient per unit and 2 dlogL:')
    for sol, term, lab in [('SB1', lambda q: q.F2.values, 'F2 (per unit)'),
                           ('SB1', lambda q: np.log(q.scale).values, 'log of the SB1 error scale 1.24 exp(0.18 F2)'),
                           ('SB2', lambda q: np.log10(q.F2.clip(lower=1)).values, 'log10 F2 (F2 >= 1)'),
                           ('both', lambda q: (q.sol == 'SB2').astype(float).values*(q.F2 > np.median(q.F2[q.sol == 'SB2'])).values, 'SB2 with F2 above the SB2 median')]:
        q = f if sol == 'both' else f[f.sol == sol]
        for chan, y, E in [('appointment finds / p_det', q.found, q.p_det), ('window-free eclipsers / p_ecl', q.indep, q.p_ecl)]:
            y = y.values.astype(float); E = E.values; base = grp(q)
            extra = [(q.sol == 'SB2').astype(float).values] if sol == 'both' else []
            b0, l0 = sc.pfit(q, y, E, base + extra, names + ['x'][:len(extra)])
            b1, l1 = sc.pfit(q, y, E, base + extra + [term(q)], names + ['x'][:len(extra)] + ['f'])
            P_(f'  {sol:4s} {lab:46s} {chan:30s} n = {int(y.sum()):3d}  coef {b1["f"][0]:+.2f} +- {b1["f"][1]:.2f}  '
               f'2 dlogL {2*(l0-l1):5.1f}  p = {stats.chi2.sf(2*(l0-l1), 1):.3f}')
    s = f[f.sol == 'SB2'].copy(); s['t'] = pd.qcut(s.F2, 3); v = s.tic.map(cc.verdict)
    for lab, y in [('all catalogued SB2', s.catalogued), ('period-free at Gaia P, same-orbit or no-period', s.pfP | v.isin(['same-orbit', 'no-period']))]:
        t = s.assign(y=y).groupby('t', observed=True).apply(lambda q: f'{int(q.y.sum())}/{q.p_ecl.sum():.1f} = {q.y.sum()/q.p_ecl.sum():.2f}', include_groups=False)
        P_(f'SB2 by F2 tercile, {lab}: ' + ', '.join(t.values))
    # SB2: the share of eclipses inside the window if the true error is the quoted one scaled by sqrt(chi2/nu)
    from scipy.stats import norm, poisson
    H = pd.read_csv(os.path.join(HERE, '..', 'gaia-errors', 'fable51-window-halfwidths.csv'), dtype={'tic': str})
    H['r_ind'] = H.halfwidth_independent_d/H.sigma_T_independent_d; H['r_corr'] = H.halfwidth_independent_d/H.sigma_T_corr_vec_d
    s = f[f.sol == 'SB2'].copy(); s['t'] = pd.qcut(s.F2, 3)
    s['k'] = np.maximum(np.clip(s.F2/np.sqrt(9*40/2) + 1 - 2/(9*40), 0.1, None)**1.5, 1)
    P_('\nSB2 windows against the scaled errors (nu = 40): median scale, p_det-weighted share of eclipses inside the window, predicted and found')
    for lab in ['ind', 'corr']:
        s['inw'] = 1 - 2*norm.sf(s.tic.map(H.groupby('tic')['r_' + lab].mean())/s.k)
        t = s.groupby('t', observed=True).apply(lambda q: pd.Series(dict(k=q.k.median(), inside=(q.p_det*q.inw).sum()/q.p_det.sum(),
                                                                       p_det=q.p_det.sum(), found=q.found.sum())))
        rate = t.found.iloc[0]/t.p_det.iloc[0]/t.inside.iloc[0]
        t['predicted'] = rate*t.p_det*t.inside
        pr = t.predicted.iloc[1:].sum(); fo = int(t.found.iloc[1:].sum())
        P_(f'  {lab} errors:'); P_(t.round(3).to_string())
        P_(f'  upper two terciles: predicted {pr:.1f} from the lowest tercile rate, found {fo}, P(<= found) {poisson.cdf(fo, pr):.3f}')
    out.close()
    fn = os.path.join(HERE, 'fit-quality-yield-output.txt')
    txt = '\n'.join(l.rstrip() for l in open(fn).read().split('\n'))
    open(fn, 'w').write(txt); print(txt)


if __name__ == '__main__':
    main()
