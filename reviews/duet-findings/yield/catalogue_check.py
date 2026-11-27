"""Which of the 81 catalogued eclipsing binaries among the main-search targets are the Gaia orbit eclipsing?

Inputs (all in this folder):
  catalogue-verdicts.csv  errata's per-target verdicts (same-orbit, other-signal, unresolvable, no-period) from the
                          catalogue periods and epochs of IJspeert et al. (2024) and Prsa et al. (2022)
  catalogue-vs-gaia.csv   the 164 catalogue (period, epoch) entries behind them, folded on Gaia's orbit
  catalogue-pixels.csv    for the targets the phase test robustly calls another signal: where the catalogue signal
                          sits (Fable's TESScut pixel fits, with injected controls, and VSX cones) and what that makes it
It adds two checks: the conjunction-phase error from all of Gaia's elements (P, e, omega, T_p, sampled independently)
in place of the period error alone, and the search's own window statistic z (TESS, at Gaia's conjunctions), which
none of the catalogue tests used. It then repeats the band fit of main_search_yield.py and the catalogued-channel
significance fit of significance_channels.py with each definition of a catalogued eclipser at Gaia's period.

Run from the repository root: python3 reviews/duet-findings/yield/catalogue_check.py
Needs numpy, pandas and SciPy. Writes catalogue-check-output.txt and catalogue-check.csv here.
"""
import importlib.util, os, sys
sys.dont_write_bytecode = True
import numpy as np, pandas as pd
from scipy import stats

HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location('sc', os.path.join(HERE, 'significance_channels.py'))
sc = importlib.util.module_from_spec(spec); spec.loader.exec_module(sc)
ROWS = 'reviews/2026-11-26-fable51-main-search-gaia/main-search-gaia-rows.csv'
ZCUT = 20
NU = 40


def conj(P, e, w, tp, kind):
    nu = (np.pi/2 if kind == 'A' else 1.5*np.pi) - w
    E = 2*np.arctan2(np.sqrt(1 - e)*np.sin(nu/2), np.sqrt(1 + e)*np.cos(nu/2))
    return tp + ((E - e*np.sin(E)) % (2*np.pi))/(2*np.pi)*P


def phase_errors(cat, g, n=4000, seed=1):
    """Spread of each entry's phase offset from conjunctions A and B when all Gaia elements vary."""
    rng = np.random.default_rng(seed); out = []
    for r in cat.itertuples():
        if not np.isfinite(r.t0_cat):
            out.append((np.nan, np.nan)); continue
        x = g.loc[r.tic]
        ee = lambda v: v if np.isfinite(v) else 0.0
        P = x.period + x.period_error*rng.standard_normal(n)
        e = np.clip(x.eccentricity + ee(x.eccentricity_error)*rng.standard_normal(n), 0, 0.95)
        w = np.radians(x.arg_periastron + ee(x.arg_periastron_error)*rng.standard_normal(n))
        tp = x.t_periastron + 389 + x.t_periastron_error*rng.standard_normal(n)
        s = []
        for k, d0 in (('A', r.dphase_A), ('B', r.dphase_B)):
            d = ((r.t0_cat - conj(P, e, w, tp, k))/P + 0.5) % 1 - 0.5
            s.append(np.std((d - d0 + 0.5) % 1 - 0.5))
        out.append(tuple(s))
    return out


def main():
    out = open(os.path.join(HERE, 'catalogue-check-output.txt'), 'w')
    P_ = lambda *a: print(*a, file=out)
    pd.set_option('display.width', 200)
    g = pd.read_csv(ROWS, dtype={'tic': str}).drop_duplicates('tic').set_index('tic')
    v = pd.read_csv(os.path.join(HERE, 'catalogue-verdicts.csv'), dtype={'tic': str})
    cat = pd.read_csv(os.path.join(HERE, 'catalogue-vs-gaia.csv'), dtype={'tic': str})
    cat[['sig_A', 'sig_B']] = phase_errors(cat, g)
    cat['nsig'] = np.fmin(cat.dphase_A.abs()/cat.sig_A, cat.dphase_B.abs()/cat.sig_B)
    best = cat.groupby('tic').agg(nsig_min=('nsig', 'min'), sig_full=('sig_A', 'median'), drift=('phase_drift', 'median'))
    v = v.join(best, on='tic')
    v['solution'] = v.tic.map(g.nss_solution_type); v['z'] = v.tic.map(g.z)
    v['z_conj'] = v.z >= ZCUT

    P_('the 81 catalogued main-search targets: errata\'s verdicts, Gaia solution type and the search\'s window statistic z')
    t = v.groupby('verdict').agg(n=('tic', 'size'), SB2=('solution', lambda s: (s == 'SB2').sum()),
                                 z_defined=('z', lambda s: s.notna().sum()), z_ge_8=('z', lambda s: (s >= 8).sum()),
                                 z_ge_20=('z', lambda s: (s >= 20).sum()), z_median=('z', 'median'))
    P_(t.round(1).to_string())
    d = sc.frame()
    bg = d[~d.anyecl & d.z.notna()]
    P_(f'targets with no known eclipser: z >= 8 for {100*(bg.z >= 8).mean():.0f}%, z >= {ZCUT} for {100*(bg.z >= ZCUT).mean():.0f}% '
       f'({len(bg)} with z)')
    ctl = pd.read_csv(ROWS, dtype={'tic': str, 'veb': str}); ctl = ctl[ctl.veb.notna()]
    P_(f'Gaia eclipsing-binary controls: {len(ctl)}, z defined for {int(ctl.z.notna().sum())}, z >= 8 for {int((ctl.z >= 8).sum())}, '
       f'z >= {ZCUT} for {int((ctl.z >= ZCUT).sum())}')
    sh = v[(v.verdict == 'other-signal')]
    short = sh[sh.detail.str.extract(r'P_cat ([\d.]+)')[0].astype(float) < 1]
    P_(f'other-signal targets with a catalogue period under 1 d: z >= {ZCUT} for {int((short.z >= ZCUT).sum())} of {int(short.z.notna().sum())}')

    rel = cat[cat.tic.isin(v.tic[v.verdict == 'same-orbit'])].groupby('tic').relation.apply(lambda x: (x == '1:1').any())
    po = rel.index[~rel]
    P_(f'same-orbit targets matched by phase alone (no 1:1 period entry): {len(po)}, window z ' +
       ', '.join(f'{t} {g.z.get(t):.1f}' for t in po))
    P_('\nconjunction-phase error with all Gaia elements varied (median per target) against the period-only drift:')
    P_(v.groupby('verdict')[['sig_full', 'drift']].median().round(4).to_string())
    oth = v[v.verdict == 'other-signal']
    P_(f'other-signal targets still more than 3 sigma from both conjunctions with the full error: {int((oth.nsig_min > 3).sum())} of {len(oth)}; '
       f'within 3 sigma: {", ".join(oth.tic[oth.nsig_min <= 3])}')

    # Gaia's errors scaled by each solution's fit quality (gaia-errors entries: SB1 1.24 exp(0.18 F2); SB2 sqrt(chi2/nu),
    # here from F2 with nu = NU degrees of freedom, since N_RV is not in the rows)
    F2 = v.tic.map(g.goodness_of_fit)
    chi = np.clip(F2/np.sqrt(9*NU/2) + 1 - 2/(9*NU), 0.1, None)**1.5
    v['err_scale'] = np.where(v.solution == 'SB2', np.maximum(chi, 1), np.maximum(1.24*np.exp(0.18*F2), 1))
    v['nsig_scaled'] = v.nsig_min/v.err_scale
    v['short'] = v.detail.str.extract(r'P_cat ([\d.]+)')[0].astype(float) < 1
    v['robust_other'] = (v.verdict == 'other-signal') & (v.short | (v.nsig_scaled > 3))
    o = v[v.verdict == 'other-signal']
    P_(f'\nwith Gaia\'s errors scaled by fit quality (SB2 nu = {NU}): of the 19 other-signal targets, {int(o.short.sum())} have catalogue '
       f'periods under 1 d and {int((~o.short & (o.nsig_scaled > 3)).sum())} more stay beyond 3 sigma '
       f'({", ".join(o.tic[~o.short & (o.nsig_scaled > 3)])}); the other {int((~o.robust_other).sum())} become undecided '
       f'(median F2 of the 13 SB2 {F2[o.index][o.solution == "SB2"].median():.1f}); same-orbit targets within 3 sigma: '
       f'{int((v[v.verdict == "same-orbit"].nsig_scaled < 3).sum())} of 20')
    for nu in (20, 80):
        ch = np.clip(F2/np.sqrt(9*nu/2) + 1 - 2/(9*nu), 0.1, None)**1.5
        sc_ = np.where(v.solution == 'SB2', np.maximum(ch, 1), np.maximum(1.24*np.exp(0.18*F2), 1))
        P_(f'  with nu = {nu}: robust other-signal {int(((v.verdict == "other-signal") & (v.short | (v.nsig_min/sc_ > 3))).sum())}')

    # where the robustly different catalogue signals sit (catalogue-pixels.csv)
    px = pd.read_csv(os.path.join(HERE, 'catalogue-pixels.csv'), dtype={'tic': str})
    pcls = px.dropna(subset=['class']).groupby('tic')['class'].first()
    v['pixels'] = v.tic.map(pcls)
    v['phase_other'] = v.robust_other
    r9 = v[v.phase_other]
    P_(f'\nthe {len(r9)} robust other-signal targets in the pixels and archives: ' +
       '; '.join(f'{k} {", ".join(r9.tic[r9.pixels == k])}' for k in ['same-orbit', 'other-on-target', 'not-target']) +
       f'; not localized: {", ".join(r9.tic[r9.pixels.isna()]) or "none"}')
    v['not_target'] = v.pixels.eq('not-target')
    v['on_target'] = ~v.not_target
    v['robust_other'] = v.phase_other & v.pixels.eq('other-on-target')

    # definitions of "catalogued eclipser at Gaia's period"
    v['strict'] = (v.verdict == 'same-orbit') | v.pixels.eq('same-orbit')
    v['tess'] = v.strict | (~v.robust_other & v.on_target & v.z_conj)
    v['not_contra'] = ~v.robust_other & v.on_target
    P_(f'catalogued eclipsers on the target: {int(v.on_target.sum())} of {len(v)}; at Gaia\'s period (same orbit): {int(v.strict.sum())}; '
       f'another signal on the target: {int(v.robust_other.sum())}; not robustly contradicted: {int(v.not_contra.sum())}')
    v.to_csv(os.path.join(HERE, 'catalogue-check.csv'), index=False,
             columns=['tic', 'band', 'verdict', 'solution', 'z', 'nsig_min', 'sig_full', 'drift', 'err_scale', 'nsig_scaled', 'phase_other', 'pixels',
                      'on_target', 'robust_other', 'strict', 'tess', 'not_contra'])
    rate = {k: (bg.z >= ZCUT).mean() for k in ['no-period', 'unresolvable', 'other-signal']}
    for k in ['no-period', 'unresolvable', 'other-signal']:
        s = v[(v.verdict == k) & ~v.phase_other]; nz = int(s.z.notna().sum()); obs = int(s.z_conj.sum())
        P_(f'{k}: z >= {ZCUT} for {obs} of {nz} with z; chance at the no-eclipser rate {rate[k]*nz:.1f}, at the short-period other-signal rate '
           f'{nz*(short.z >= ZCUT).sum()/max(short.z.notna().sum(), 1):.1f}')

    # band fit, as main_search_yield.py (numerator = appointment finds at Gaia's period + catalogued by each definition)
    y = pd.read_csv(os.path.join(HERE, 'main-search-yield.csv'), dtype={'tic': str})
    f = y[np.isfinite(y.significance) & (y.p_det > 0)].copy()
    vv = v.set_index('tic')
    base = [(f.group == 'shallow (<60 ppt)').astype(float).values, (f.group == 'long (>30 h)').astype(float).values,
            np.log10(f.significance/30).values]
    bands = [(f.band == 'G10-11').astype(float).values, (f.band == 'G11-11.5').astype(float).values]
    E = f.p_det.values
    P_('\nband fit (count = p_det x exp(groups + log significance [+ bands])), numerator = new finds + catalogued by definition:')
    P_(f'  {"definition":34s} {"total":>5s} {"G<10":>6s} {"G10-11":>7s} {"G11-11.5":>8s} {"2 dlogL":>8s} {"p":>7s}')
    pfP = (f.periodfree & (np.abs(f.P_ecl/f.P - 1) < 0.02)).values   # period-free finds at Gaia's period
    for lab, col, pf in [('new finds only', None, False), ('+ same-orbit (errata)', 'strict', False),
                         (f'+ same-orbit or z >= {ZCUT}', 'tess', False),
                         ('+ all not robustly contradicted', 'not_contra', False), ('+ all 81 flagged', 'all', False),
                         ('+ all on the target', 'on_target', False),
                         ('new + period-free at Gaia P', None, True), (f'... + same-orbit or z >= {ZCUT}', 'tess', True)]:
        add = np.zeros(len(f), bool) if col is None else (f.catalogued.values if col == 'all' else
                                                           f.tic.map(vv[col]).fillna(False).astype(bool).values)
        yy = (f.found.values | add | (pfP & pf)).astype(float)
        _, l0 = sc.pfit(f, yy, E, base, ['a', 'b', 's'])
        _, l1 = sc.pfit(f, yy, E, base + bands, ['a', 'b', 's', 'c', 'd'])
        rr = f.assign(y=yy).groupby('band').apply(lambda q: q.y.sum()/q.p_det.sum(), include_groups=False)
        P_(f'  {lab:34s} {int(yy.sum()):5d} {rr["G<10"]:6.2f} {rr["G10-11"]:7.2f} {rr["G11-11.5"]:8.2f} {2*(l0-l1):8.1f} {stats.chi2.sf(2*(l0-l1), 2):7.3f}')

    # catalogued channel against significance, as significance_channels.py, for each definition
    d['fill'] = sc.roche_fill(d)
    ff = d[np.isfinite(d.significance) & (d.p_det > 0)].copy()
    grp = [(ff.group == 'shallow').astype(float).values, (ff.group == 'long').astype(float).values]
    bnd = [(ff.band == 'G10-11').astype(float).values, (ff.band == 'G11-11.5').astype(float).values]
    gi = [ff.giant.astype(float).values]
    ls = np.log10(ff.significance/30).values; ld = np.log10(ff.depth_ppt.clip(lower=1)/60).values
    L = np.log(10)
    P_('\ncatalogued eclipsers against Gaia significance (expected = p_ecl; groups, bands, giant), powers / ln 10:')
    for lab, col in [('all 81 flagged', 'all'), ('all on the target', 'on_target'), ('same-orbit', 'strict'), (f'same-orbit or z >= {ZCUT}', 'tess'), ('not contradicted', 'not_contra'),
                     ('other-signal', 'other'), ('robust by phase', 'pother'), ('other signal on target', 'rother')]:
        if col == 'all': yy = ff.catalogued.values
        elif col == 'other': yy = ff.tic.map(vv.verdict).eq('other-signal').values
        elif col == 'rother': yy = ff.tic.map(vv.robust_other).fillna(False).astype(bool).values
        elif col == 'pother': yy = ff.tic.map(vv.phase_other).fillna(False).astype(bool).values
        else: yy = ff.tic.map(vv[col]).fillna(False).astype(bool).values
        yy = yy.astype(float)
        b1, _ = sc.pfit(ff, yy, ff.p_ecl.values, grp + bnd + gi + [ls], ['a', 'b', 'c', 'd', 'g', 's'])
        b2, _ = sc.pfit(ff, yy, ff.p_ecl.values, grp + bnd + gi + [ld, ls], ['a', 'b', 'c', 'd', 'g', 'dd', 's'])
        P_(f'  {lab:26s} n = {int(yy.sum()):2d}  significance alone {b1["s"][0]/L:+.2f} +- {b1["s"][1]/L:.2f};  '
           f'with depth: depth {b2["dd"][0]/L:+.2f} +- {b2["dd"][1]/L:.2f}, significance {b2["s"][0]/L:+.2f} +- {b2["s"][1]/L:.2f}')

    # do weak orbits put their conjunctions on these eclipses?
    P_(f'\nwindow statistic z >= {ZCUT} by Gaia significance, for catalogued eclipsers by definition (z defined):')
    for lab, m in [('same-orbit', v.strict), ('not on target', v.not_target), ('no-period', v.verdict == 'no-period'), ('other-signal', v.verdict == 'other-signal')]:
        s = v[m & v.z.notna()]
        sig = s.tic.map(g.significance)
        P_(f'  {lab:14s} significance < 30: {int((s.z[sig < 30] >= ZCUT).sum())} of {int((sig < 30).sum())};  >= 30: '
           f'{int((s.z[sig >= 30] >= ZCUT).sum())} of {int((sig >= 30).sum())}')
    P_('\nGaia solution type of the catalogued targets against all main-search targets:')
    P_(pd.crosstab(v.verdict, v.solution).to_string())
    P_(f'all targets: SB2 {100*(g.nss_solution_type == "SB2").mean():.1f}%')
    out.close()
    fn = os.path.join(HERE, 'catalogue-check-output.txt')
    txt = '\n'.join(l.rstrip() for l in open(fn).read().split('\n'))
    open(fn, 'w').write(txt); print(txt)


if __name__ == '__main__':
    main()
