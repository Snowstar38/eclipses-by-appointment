"""Where the measured eclipses of the period-free finds at Gaia's period fall on Gaia's orbit.

For the 31 main-search targets whose period-free find has Gaia's period (Sol's yield/periodfree-cut-audit.csv),
the period-free review's lead-numeric.json files hold fitted mid-times for 17. Each eclipse is placed against Gaia's
two conjunctions (main-search Gaia rows), with the conjunction error at that time from Fable 5.1's cycle-0 and period
terms (independent errors: sigma^2 = sigma_0^2 + (n sigma_P)^2; Gaia's T_p error as sigma_0 where Fable 5.1's file has no row), and the A-to-B phase is compared with Gaia's where
both kinds are seen. Eclipses deeper than 2 ppt whose raw in-dip deficit exceeds the scatter beside it; the summary keeps those at least 0.3 of the star's deepest.

Run from the repository root: python3 reviews/duet-findings/gaia-errors/periodfree_conjunctions.py
Needs numpy and pandas. Writes periodfree-conjunctions-output.txt and periodfree-conjunctions.csv here.
"""
import glob, json, os, sys
sys.dont_write_bytecode = True
import numpy as np, pandas as pd

HERE = os.path.dirname(os.path.abspath(__file__))
AUD = 'reviews/duet-findings/yield/periodfree-cut-audit.csv'
ROWS = 'reviews/2026-11-26-fable51-main-search-gaia/main-search-gaia-rows.csv'
HW = 'reviews/duet-findings/gaia-errors/fable51-window-halfwidths.csv'


def mean_anom(nu, e):
    E = 2*np.arctan2(np.sqrt(1 - e)*np.sin(nu/2), np.sqrt(1 + e)*np.cos(nu/2))
    return (E - e*np.sin(E)) % (2*np.pi)


def wrap(d, P):
    return (d/P + 0.5) % 1*P - P/2


def main():
    out = open(os.path.join(HERE, 'periodfree-conjunctions-output.txt'), 'w')
    P_ = lambda *a: print(*a, file=out)
    a = pd.read_csv(AUD, dtype={'tic': str})
    G = pd.read_csv(ROWS, dtype={'tic': str, 'source_id': str}).drop_duplicates('tic').set_index('tic')
    H = pd.read_csv(HW, dtype={'source_id': str})
    rows, summ = [], []
    for r in a.itertuples():
        f = glob.glob(f'reviews/2026-11-05-period-free/**/{r.tic}/lead-numeric.json', recursive=True)
        if not f or r.tic not in G.index: continue
        g = G.loc[r.tic]; h = H[H.source_id == g.source_id].set_index('conjunction')
        P, e, w = g.period, g.eccentricity, np.radians(g.arg_periastron)
        if not np.isfinite(e) or not np.isfinite(w): continue      # no eccentric elements (astrometric-spectroscopic row)
        tp = g.t_periastron + 389
        c = {'A': tp + mean_anom(np.pi/2 - w, e)/(2*np.pi)*P, 'B': tp + mean_anom(1.5*np.pi - w, e)/(2*np.pi)*P}
        ev = [x for x in json.load(open(f[0]))['events'] if x.get('fit_mid_btjd') and (x.get('fit_depth_ppt') or 0) > 2
              and x.get('raw_core_median_deficit_ppt', 1) > x.get('raw_side_scatter_ppt', 0)]
        for x in ev:
            t = x['fit_mid_btjd']; best = None
            for k in 'AB':
                n = (t - c[k])/P
                s0 = h.loc[k, 'sigma_cycle0_independent_d'] if k in h.index else g.t_periastron_error
                sig = np.hypot(s0, n*g.period_error)
                d = wrap(t - c[k], P)
                if best is None or abs(d/sig) < abs(best[2]): best = (k, d, d/sig, sig)
            rows.append(dict(review_id=r.review_id, tic=r.tic, sol=g.nss_solution_type, gof=g.goodness_of_fit, sector=x['sector'], btjd=round(t, 4),
                             depth_ppt=round(x['fit_depth_ppt'], 1), conj=best[0], offset_d=round(best[1], 3), sigma_d=round(best[3], 3),
                             pull=round(best[2], 2), null_cut=bool(r.null_exceed > 0)))
    D = pd.DataFrame(rows)
    D.to_csv(os.path.join(HERE, 'periodfree-conjunctions.csv'), index=False)
    P_('eclipses of the period-free finds at Gaia period, against the nearer conjunction (in sigma)')
    for rid, d in D.groupby('review_id', sort=False):
        deep = d.depth_ppt.max()
        k = d[d.depth_ppt > 0.3*deep]
        P_(f"\n{rid} TIC {d.tic.iloc[0]} {d.sol.iloc[0]} (goodness of fit {d.gof.iloc[0]:.1f}), null cut {'failed' if d.null_cut.iloc[0] else 'passed'}:")
        P_(d[['sector', 'btjd', 'depth_ppt', 'conj', 'offset_d', 'sigma_d', 'pull']].to_string(index=False))
        mx = k.pull.abs().max()
        summ.append(dict(review_id=rid, n=len(k), max_pull=mx, kinds=''.join(sorted(set(k.conj))), null_cut=d.null_cut.iloc[0]))
    S = pd.DataFrame(summ)
    P_('\nsummary (eclipses at least 0.3 of the deepest):')
    P_(S.sort_values('max_pull').round(2).to_string(index=False))
    P_('\nlargest pull among the null-vetoed: ' + ', '.join(f'{x.review_id} {x.max_pull:.2f}' for x in S[S.null_cut].itertuples()))
    P_(f'\nfinds whose deep eclipses all lie within 3 sigma of a conjunction: {int((S.max_pull < 3).sum())} of {len(S)}; beyond 3 sigma: '
       + ', '.join(S.review_id[S.max_pull >= 3]))

    # where the search centred its windows: the find time less its phase offset (Earthshine's find times), against nominal
    E = pd.read_csv('reviews/duet-findings/yield/null-vetoes-earthshine.csv', dtype={'tic': str}).merge(a[['review_id', 'dphase']])
    P_('\nsearch window centre (find time less its offset) against Gaia\'s nominal conjunctions, for the 19 null-vetoed finds:')
    for r in E.itertuples():
        g = G.loc[r.tic]
        if not np.isfinite(g.arg_periastron): P_(f'  {r.review_id}: no omega'); continue
        P, e, w = g.period, g.eccentricity, np.radians(g.arg_periastron); tp = g.t_periastron + 389
        c = {'A': tp + mean_anom(np.pi/2 - w, e)/(2*np.pi)*P, 'B': tp + mean_anom(1.5*np.pi - w, e)/(2*np.pi)*P}
        tc = r.find_t - r.dphase*P
        d = {k: wrap(tc - v, P) for k, v in c.items()}; k = min(d, key=lambda k: abs(d[k]))
        P_(f'  {r.review_id}: e {e:.3f}, omega error {g.arg_periastron_error:6.1f} deg, centre - nominal {k} {d[k]:7.2f} d')
    b = pd.read_csv(os.path.join(HERE, 'r763-boxes-earthshine.csv'))
    g = G.loc['325817130']; P, e, w = g.period, g.eccentricity, np.radians(g.arg_periastron); tp = g.t_periastron + 389
    c = {'A': tp + mean_anom(np.pi/2 - w, e)/(2*np.pi)*P, 'B': tp + mean_anom(1.5*np.pi - w, e)/(2*np.pi)*P}
    P_('\nR763 (TIC 325817130) eclipse boxes from its null draws (Earthshine) against nominal A and B:')
    for x in b.itertuples():
        P_(f'  BTJD {x.btjd:9.3f} {x.box_depth_ppt:5.1f} ppt: from A {wrap(x.btjd - c["A"], P):7.2f} d, from B {wrap(x.btjd - c["B"], P):7.2f} d')

    c = pd.read_csv(os.path.join(HERE, 'a-window-coverage.csv'))
    c['bad'] = c.z_period.abs() >= 3
    o = c[c.z_tess_ind.abs() > 3]
    P_(f'\nA systems outside their window (|offset| > 3 sigma, independent errors, TESS epochs): {len(o)} of {len(c)}: '
       + ', '.join(f'{x.review_id} ({x.method}, period pull {x.z_period:+.2f}, {x.z_tess_ind:+.2f} sigma)' for x in o.itertuples())
       + f'; period pull >= 3 sigma in {int(c.bad.sum())}')
    out.close(); print(open(os.path.join(HERE, 'periodfree-conjunctions-output.txt')).read())


if __name__ == '__main__':
    main()
