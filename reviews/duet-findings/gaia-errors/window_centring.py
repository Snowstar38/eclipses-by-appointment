"""Where appoint.py centres a conjunction window when Gaia's omega is poorly known.

The windows themselves: the fresh-band cohorts ran the same frozen appoint.py and saved every window (centre tc,
spread sig, half-width hw) beside the Gaia row it was built from (population.json). For each window this script
measures the centre against Gaia's nominal conjunction and against T_p + P/2, by omega error.

The main search: R763's window centre (find time less its phase offset; Earthshine's find time, Sol's audit) against
the same two references, and the main-search targets counted by omega error, with the yield model's expected
detections and the share of windows that miss the conjunction in the fresh-band cohorts at the same omega error.

Run from the repository root: python3 reviews/duet-findings/gaia-errors/window_centring.py
Needs numpy and pandas. Writes window-centring-output.txt and window-centring.csv (first window of each conjunction kind per target) here.
"""
import glob, json, os, sys
sys.dont_write_bytecode = True
import numpy as np, pandas as pd

HERE = os.path.dirname(os.path.abspath(__file__))
ROWS = 'reviews/2026-11-26-fable51-main-search-gaia/main-search-gaia-rows.csv'
AUD = 'reviews/duet-findings/yield/periodfree-cut-audit.csv'
NUL = 'reviews/duet-findings/yield/null-vetoes-earthshine.csv'
YLD = 'reviews/duet-findings/yield/main-search-yield.csv'
BINS = ((0, 30), (30, 60), (60, 90), (90, 120), (120, 180), (180, 400))


def mean_anom(nu, e):
    E = 2*np.arctan2(np.sqrt(1 - e)*np.sin(nu/2), np.sqrt(1 + e)*np.cos(nu/2))
    return (E - e*np.sin(E)) % (2*np.pi)


def wrap(d, P):
    return (d/P + 0.5) % 1*P - P/2


def nominal(P, e, w_deg, tp, kind):
    nu0 = np.pi/2 if kind == 'A' else 1.5*np.pi
    return tp + mean_anom(nu0 - np.radians(w_deg), e)/(2*np.pi)*P


def fresh_windows():
    rows, seen = [], set()
    for pop in sorted(glob.glob('reviews/**/fresh-band*/population.json', recursive=True)):
        if 'stage1' in pop: continue
        T = json.load(open(pop))['targets']; rd = os.path.join(os.path.dirname(pop), 'appointment-results')
        for tic, v in T.items():
            f = os.path.join(rd, f'{tic}.json')
            if tic in seen or not os.path.exists(f): continue
            seen.add(tic); d = json.load(open(f)); g = v['gaia']
            if d.get('circular_assumed_omega0') or g['arg_periastron'] in ('', None): continue
            P, e, w, werr = (float(g[k]) for k in ('period', 'eccentricity', 'arg_periastron', 'arg_periastron_error'))
            tp = float(g['t_periastron']) + 389
            for x in d.get('windows') or []:
                nom = nominal(P, e, w, tp, x['kind'])
                rows.append(dict(tic=tic, kind=x['kind'], P=P, e=e, w_err=werr, e_snr=e/float(g['eccentricity_error']),
                                 tc=x['tc'], sig=x['sig'], hw=x['hw'], off_nominal=wrap(x['tc'] - nom, P),
                                 phase_from_tp=wrap(x['tc'] - tp, P)/P))
    return pd.DataFrame(rows)


def main():
    out = open(os.path.join(HERE, 'window-centring-output.txt'), 'w')
    P_ = lambda *a: print(*a, file=out)
    F = fresh_windows()
    F['miss'] = F.off_nominal.abs() > F.hw
    F.drop_duplicates(['tic', 'kind']).drop(columns='tc').round(4).to_csv(os.path.join(HERE, 'window-centring.csv'), index=False)
    P_(f'1. appoint.py windows in the fresh-band cohorts: {F.tic.nunique()} targets with omega, {len(F)} windows')
    P_('   omega error | targets windows | median |centre - nominal| | median |phase from T_p| | median sig/P | nominal outside window | A and B centres within 0.05 P')
    miss = {}
    for lo, hi in BINS:
        s = F[(F.w_err >= lo) & (F.w_err < hi)]
        if not len(s): continue
        ab = s.pivot_table(index='tic', columns='kind', values='phase_from_tp', aggfunc='first').dropna()
        same = (wrap(ab['A'] - ab['B'], 1.0).abs() < 0.05).mean()
        miss[(lo, hi)] = s.miss.mean()
        P_(f'   {lo:>3}-{hi:<3} deg | {s.tic.nunique():5} {len(s):6} | {s.off_nominal.abs().median():6.2f} d | {s.phase_from_tp.abs().median():.3f} '
           f'| {(s.sig/s.P).median():.3f} | {s.miss.mean():.3f} | {same:.2f}')
    P_(f'   uniform over one period: |phase| 0.5 for the centre, sig/P = 1/sqrt(12) = {1/np.sqrt(12):.3f}')

    G = pd.read_csv(ROWS, dtype={'tic': str, 'source_id': str}).drop_duplicates('tic').set_index('tic')
    A = pd.read_csv(AUD, dtype={'tic': str}); E = pd.read_csv(NUL, dtype={'tic': str}).merge(A[['review_id', 'dphase']])
    r = E[E.review_id == 'R763'].iloc[0]; g = G.loc[r.tic]
    P, tp = g.period, g.t_periastron + 389; tc = r.find_t - r.dphase*P
    P_(f'\n2. Main search, R763 (TIC {r.tic}): P {P:.3f} d, e {g.eccentricity:.4f} +- {g.eccentricity_error:.4f}, omega error {g.arg_periastron_error:.0f} deg, '
       f'T_p error {g.t_periastron_error:.1f} d')
    for k in 'AB':
        P_(f'   window centre - nominal {k}: {wrap(tc - nominal(P, g.eccentricity, g.arg_periastron, tp, k), P):7.2f} d')
    P_(f'   window centre - T_p: {wrap(tc - tp, P)/P:.3f} P  (T_p + P/2 would be 0.500)')

    H = pd.read_csv('reviews/duet-findings/gaia-errors/fable51-window-halfwidths.csv', dtype={'source_id': str})
    H = H.merge(G.reset_index()[['source_id', 'arg_periastron_error']], on='source_id')
    P_('\n3. Main-search targets (Gaia rows) by omega error, with the conjunction error at BTJD 2500 (Fable 5.1, correlated and independent)')
    for lo, hi in ((60, 90), (90, 400)):
        n = int(((G.arg_periastron_error >= lo) & (G.arg_periastron_error < hi)).sum())
        h = H[(H.arg_periastron_error >= lo) & (H.arg_periastron_error < hi)]
        P_(f'   {lo:>3}-{hi:<3} deg: {n} targets; sigma_T median {h.sigma_T_corr_vec_d.median():.2f} d correlated (90th percentile {h.sigma_T_corr_vec_d.quantile(.9):.2f}), '
           f'{h.sigma_T_independent_d.median():.1f} d independent; correlated half-width median {h.halfwidth_corr_vec_d.median():.2f} d')
    Y = pd.read_csv(YLD, dtype={'tic': str}).merge(G[['arg_periastron_error']], left_on='tic', right_index=True)
    P_('\n   In the yield model (6,295 targets) by omega error ( expected detections; found = search finds at Gaia period)')
    P_('   omega error | targets | expected | found | period-free finds | catalogued | fresh-band share of windows missing the conjunction')
    for lo, hi in ((0, 60), (60, 90), (90, 400)):
        s = Y[(Y.arg_periastron_error >= lo) & (Y.arg_periastron_error < hi)]
        fm = F[(F.w_err >= lo) & (F.w_err < hi)].miss.mean()
        P_(f'   {lo:>3}-{hi:<3} deg | {len(s):5} | {s.p_det.sum():6.2f} | {int(s.found.sum()):3} | {int(s.periodfree.sum()):3} | {int(s.catalogued.sum()):3} | {fm:.3f}')
    a = Y[Y.arg_periastron_error < 60]; rate = a.found.sum()/a.p_det.sum()
    b = Y[Y.arg_periastron_error >= 90]
    lost = sum(Y[(Y.arg_periastron_error >= lo) & (Y.arg_periastron_error < hi)].p_det.sum()*m for (lo, hi), m in miss.items() if lo >= 60)
    P_(f'   found per expected below 60 deg: {rate:.3f}; at 90 deg and above that rate predicts {rate*b.p_det.sum():.1f} finds, '
       f'Poisson chance of none {np.exp(-rate*b.p_det.sum()):.2f}')
    P_(f'   expected detections whose conjunction the window misses (omega error >= 60 deg, fresh-band shares): {lost:.1f} geometric, '
       f'{lost*rate:.1f} at the search\'s found rate')
    out.close()


if __name__ == '__main__':
    main()
