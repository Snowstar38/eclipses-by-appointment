"""Expected against found eclipsing binaries in the main appointment search (G < 11.5, 6,357 targets).

Same geometric model as fresh_band_yield.py (primary radius from parallax, G and BP-RP with no
extinction; companion minimum mass from Gaia's K1; isotropic orientations; both conjunctions;
depth floor 2 ppt) applied to the Gaia rows the main search was built from
(reviews/2026-11-26-fable51-main-search-gaia/main-search-gaia-rows.csv). Window coverage per star
comes from its number of covered windows, calibrated on the fresh-band cohorts, where each window's
covered fraction is saved. Found = accepted systems whose Table A1 method is the appointments
search (App) or whose register method is a conjunction-window search, at Gaia's period (within 2%).
Accepted systems on the same targets from the period-free dip screening are counted separately:
real eclipses on these orbits that the appointment search did not return. Targets already in the
Prsa et al. (2022) TESS or IJspeert et al. (2024) eclipsing-binary catalogues (the identity flag of
reviews/2026-11-05-period-free/selection/all-targets.csv) are eclipsers the search could not count as new.

Run from the repository root: python3 reviews/duet-findings/yield/main_search_yield.py
Needs numpy, pandas and SciPy. Writes main-search-yield.csv and main-search-yield-output.txt here.
"""
import glob, html, importlib.util, json, os, re, sys
sys.dont_write_bytecode = True
import numpy as np, pandas as pd
from scipy import stats
from scipy.optimize import minimize

HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location('fby', os.path.join(HERE, 'fresh_band_yield.py'))
fby = importlib.util.module_from_spec(spec); spec.loader.exec_module(fby)
ROWS = 'reviews/2026-11-26-fable51-main-search-gaia/main-search-gaia-rows.csv'
IDENT = 'reviews/2026-11-05-period-free/selection/all-targets.csv'
CONJ = ('App', 'conjunction_windows', 'Gaia spectroscopic conjunction windows')

def coverage_by_nwin():
    """Mean of the per-conjunction covered chance against the number of covered windows (fresh-band cohorts)."""
    pts = []
    for g in glob.glob('reviews/2026-11-05-*/fresh-band*/appointment-results/*.json'):
        if 'stage1' in g: continue
        d = json.load(open(g)); ws = d.get('windows') or []
        if not ws: continue
        cov = [1 - np.prod([1 - w['frac_covered'] for w in ws if w['kind'] == k]) if any(w['kind'] == k for w in ws) else 0.
               for k in 'AB']
        pts.append((min(d['n_windows'], 20), float(np.mean(cov))))
    t = pd.DataFrame(pts, columns=['n', 'cov']).groupby('n')['cov'].mean()
    return t, len(pts)

def table_a1():
    t = open('paper.html').read(); meth, per = {}, {}
    for r in re.findall(r'<tr[^>]*>(.*?)</tr>', t, re.S):
        c = [re.sub(r'\s+', ' ', html.unescape(re.sub(r'<[^>]+>', '', x))).strip() for x in re.findall(r'<t[dh][^>]*>(.*?)</t[dh]>', r, re.S)]
        if len(c) >= 6 and re.fullmatch(r'A\d+', c[0]) and c[5] in ('confirmed', 'probable'):
            meth.setdefault(c[0], c[4])
        elif len(c) >= 3 and re.fullmatch(r'A\d+', c[0]):   # ephemeris table: 'P +- eP'
            m = re.match(r'([\d.]+) ± ', c[1])
            if m: per.setdefault(c[0], float(m.group(1)))
    return meth, per

def review_periods():
    per = {}
    for f in ['appointments-review.csv', 'period-free-review.csv'] + glob.glob('reviews/**/RESULTS.csv', recursive=True):
        try: d = pd.read_csv(f, dtype=str)
        except Exception: continue
        if 'tic' not in d or 'period_days' not in d: continue
        for t, p in zip(d.tic, d.period_days):
            try: per.setdefault(str(t), float(p))
            except (TypeError, ValueError): pass
    return per

def main():
    out = open(os.path.join(HERE, 'main-search-yield-output.txt'), 'w')
    m = pd.read_csv(ROWS, dtype={'tic': str, 'source_id': str, 'veb': str})
    covtab, ncal = coverage_by_nwin()
    print(f'{len(m)} main-search rows; {m.veb.notna().sum()} are Gaia eclipsing binaries (controls, left out)', file=out)
    print(f'window coverage calibrated on {ncal} fresh-band targets: ' +
          ', '.join(f'{int(k)}:{v:.2f}' for k, v in covtab.items() if k in (1, 2, 4, 6, 9, 12, 15, 20)), file=out)
    m = m[m.veb.isna()].copy()
    nw = m.n_windows.fillna(0).clip(upper=20).astype(int)
    m['coverage'] = [0.0 if n == 0 else float(covtab.get(n, covtab.iloc[-1])) for n in nw]
    pops = {r.tic: r._asdict() for r in m.itertuples(index=False)}
    cover = dict(zip(m.tic, m.coverage)); band = dict(zip(m.tic, m.band))
    acc = pd.read_csv('accepted-systems.csv', dtype=str)
    reg = pd.read_csv('scientific-review-register.csv', dtype=str).set_index('review_id').search_method.to_dict()
    meth, perA = table_a1(); perR = review_periods()
    acc['method'] = acc.review_id.map(meth).fillna(acc.review_id.map(reg))
    acc['P_ecl'] = [perA.get(r, perR.get(t, np.nan)) for r, t in zip(acc.review_id, acc.tic)]
    acc = acc[acc.tic.isin(pops)].drop_duplicates('tic')
    rng = np.random.default_rng(20261126)
    rows = fby.stars(pops, cover)
    for r in rows:
        r['p_det'], r['p_ecl'], r['dur_h'] = fby.chances(r, rng)
        r['depth_ppt'] = 1e3*min(r['R2']/r['R1'], 1.0)**2
    d = pd.DataFrame(rows); d['band'] = d.tic.map(band)
    a = acc.set_index('tic')
    d['method'] = d.tic.map(a.method).fillna(''); d['review_id'] = d.tic.map(a.review_id).fillna('')
    d['P_ecl'] = d.tic.map(a.P_ecl)
    d['same_P'] = (np.abs(d.P_ecl/d.P - 1) < 0.02)
    d['found'] = d.method.isin(CONJ) & d.same_P
    d['found_any_P'] = d.method.isin(CONJ)
    d['periodfree'] = (d.method == 'Period-free dip screening')
    d['group'] = np.where(d.dur_h > 30, 'long (>30 h)', np.where(d.depth_ppt < 60, 'shallow (<60 ppt)', 'deep (>=60 ppt)'))
    print(f'{len(d)} targets modelled (parallax > 0.2 mas, finite photometry); appointment finds {int(d.found_any_P.sum())}, '
          f'{int(d.found.sum())} at Gaia\'s period; period-free finds on the same targets {int(d.periodfree.sum())} '
          f'({int((d.periodfree & d.same_P).sum())} at Gaia\'s period)', file=out)
    off = d[d.found_any_P & ~d.same_P]
    print('appointment finds not at Gaia\'s period: ' + ', '.join(f'{r.review_id} ({r.P_ecl:g} vs {r.P:.2f} d)' for r in off.itertuples()), file=out)

    def tab(by, sub=d):
        t = sub.groupby(by, observed=True).agg(targets=('tic', 'size'), giants=('giant', 'mean'), expected=('p_det', 'sum'),
                                              found=('found', 'sum'), periodfree=('periodfree', 'sum'))
        t['found/expected'] = t.found/t.expected; t['per_100_found'] = 100*t.found/t.targets; t['per_100_expected'] = 100*t.expected/t.targets
        return t.round(2)
    print('\nby band:', file=out); print(tab('band').to_string(), file=out)
    print('\nby band and group:', file=out); print(tab(['band', 'group']).to_string(), file=out)
    d['sig_band'] = pd.cut(d.significance, [0, 15, 30, 60, 1e4])
    print('\ndeep (>=60 ppt) by band and Gaia significance:', file=out)
    print(tab(['band', 'sig_band'], d[d.group == 'deep (>=60 ppt)']).to_string(), file=out)
    print('\nshallow (<60 ppt) by band and Gaia significance:', file=out)
    print(tab(['band', 'sig_band'], d[d.group == 'shallow (<60 ppt)']).to_string(), file=out)

    f = d[np.isfinite(d.significance) & (d.p_det > 0)].copy()
    def fit(cols, y):
        X = np.column_stack([np.ones(len(f))] + cols); E = f.p_det.values
        nll = lambda b: (E*np.exp(X @ b) - y*(X @ b)).sum()
        r = minimize(nll, np.zeros(X.shape[1]), method='BFGS'); return r.x, np.sqrt(np.diag(r.hess_inv)), r.fun
    base = [(f.group == 'shallow (<60 ppt)').astype(float).values, (f.group == 'long (>30 h)').astype(float).values,
            np.log10(f.significance/30).values]
    bands = [(f.band == 'G10-11').astype(float).values, (f.band == 'G11-11.5').astype(float).values]
    y = f.found.values.astype(float)
    b0, s0, l0 = fit(base, y); b1, s1, l1 = fit(base + bands, y)
    names = ['b0 (deep, sig 30, G<10)', 'b1 shallow', 'b2 long', 'b3 log10 sig', 'b4 G10-11', 'b5 G11-11.5']
    print(f'\njoint Poisson fit, found = expected x exp(X b), {len(f)} targets with a significance:', file=out)
    for n_, b, e_ in zip(names, b1, s1):
        print(f'  {n_:24s} {b:+.2f} +- {e_:.2f}   factor {np.exp(b):.2f}', file=out)
    print(f'  found rate goes as significance^{b1[3]/np.log(10):.2f} +- {s1[3]/np.log(10):.2f}', file=out)
    print(f'  band terms improve the fit by 2 dlogL = {2*(l0-l1):.1f} for 2 parameters (p = {stats.chi2.sf(2*(l0-l1), 2):.2g})', file=out)
    print(f'  without band terms: deep factor {np.exp(b0[0]):.2f}, shallow x{np.exp(b0[1]):.2f} +- {np.exp(b0[1])*s0[1]:.2f}, '
          f'long x{np.exp(b0[2]):.2f}, significance^{b0[3]/np.log(10):.2f}', file=out)
    # the paper's band ratio: expected under the fit without band terms, per band
    f['pred'] = f.p_det*np.exp(np.column_stack([np.ones(len(f))] + base) @ b0)
    t = f.groupby('band').agg(targets=('tic', 'size'), found=('found', 'sum'), predicted=('pred', 'sum'), geometric=('p_det', 'sum'))
    t['found_per_100'] = 100*t.found/t.targets; t['predicted_per_100'] = 100*t.predicted/t.targets; t['geometric_per_100'] = 100*t.geometric/t.targets
    t['p_poisson'] = [min(stats.poisson.cdf(r.found, r.predicted), stats.poisson.sf(r.found - 1, r.predicted)) for r in t.itertuples()]
    print('\nper band, found against the band-free fit (depth, duration and significance only):', file=out); print(t.round(3).to_string(), file=out)
    # period-free finds on these targets: what the appointment search left
    pf = d[d.periodfree]
    print(f'\nperiod-free finds on main-search targets ({len(pf)}): by band {pf.band.value_counts().to_dict()}; '
          f'by group {pf.group.value_counts().to_dict()}; at Gaia\'s period {int(pf.same_P.sum())}; '
          f'median predicted depth {pf.depth_ppt.median():.0f} ppt, duration {pf.dur_h.median():.0f} h', file=out)
    # where in depth is the G<10 shortfall?  G<10 against G10-11 per group, and a deep-only band term
    print('\nG<10 found/expected over G10-11 found/expected, per group:', file=out)
    for grp in ['deep (>=60 ppt)', 'shallow (<60 ppt)', 'long (>30 h)']:
        a_, b_ = d[(d.band == 'G<10') & (d.group == grp)], d[(d.band == 'G10-11') & (d.group == grp)]
        ra, rb = a_.found.sum()/a_.p_det.sum(), b_.found.sum()/b_.p_det.sum()
        print(f'  {grp:18s} {ra:.2f} / {rb:.2f} = {ra/rb:.2f}', file=out)
    bright = (f.band == 'G<10').astype(float).values; deep = (f.group == 'deep (>=60 ppt)').astype(float).values
    _, _, la = fit(base + bands, y)
    bb, sb, lb = fit(base + bands + [bright*deep], y)
    print(f'  extra term for deep eclipses at G<10: factor {np.exp(bb[-1]):.2f} (+{sb[-1]:.2f} in log), 2 dlogL = {2*(la-lb):.1f} '
          f'(p = {stats.chi2.sf(2*(la-lb), 1):.2g})', file=out)
    # robustness of the band ratio to the model's assumptions
    print('\nrobustness, found/expected per band:', file=out)
    for lab, kw in [('default', {}), ('1 ppt floor', dict(dmin=1.0)), ('5 ppt floor', dict(dmin=5.0)),
                    ('giants 2.0 Msun', dict(m_giant=2.0)), ('companion radii x1.2', dict(r2_scale=1.2)), ('no window coverage', dict(use_cov=False))]:
        rng2 = np.random.default_rng(20261126); rs = fby.stars(pops, cover, **{k: v for k, v in kw.items() if k in ('m_giant', 'r2_scale')})
        e_ = {}
        for r in rs:
            e_[r['tic']] = fby.chances(r, rng2, dmin=kw.get('dmin', 2.0), use_cov=kw.get('use_cov', True))[0]
        z_ = d.assign(e=d.tic.map(e_)).groupby('band').agg(e=('e', 'sum'), f=('found', 'sum'))
        print(f'  {lab:22s} ' + ', '.join(f'{b}: {r.f}/{r.e:.1f} = {r.f/r.e:.2f}' for b, r in z_.iterrows()), file=out)
    # catalogued eclipsing binaries among the targets: real eclipsers the novelty rule removes
    idn = pd.read_csv(IDENT, dtype={'tic': str})
    known = set(idn.tic[idn.cached_primary_identity_match.astype(str) == 'True'])
    d['catalogued'] = d.tic.isin(known) & ~d.found
    print(f'\ncatalogued eclipsing binaries (Prsa 2022 or IJspeert 2024) among the modelled targets, none of them accepted: {int(d.catalogued.sum())}', file=out)
    t = d.groupby('band').agg(expected=('p_det', 'sum'), found=('found', 'sum'), catalogued=('catalogued', 'sum'))
    t['catalogued_share'] = t.catalogued/(t.found + t.catalogued); t['(found+catalogued)/expected'] = (t.found + t.catalogued)/t.expected
    print(t.round(2).to_string(), file=out)
    t = d.groupby(['band', 'group']).agg(expected=('p_det', 'sum'), found=('found', 'sum'), catalogued=('catalogued', 'sum'))
    t['(found+catalogued)/expected'] = (t.found + t.catalogued)/t.expected
    print(t.round(2).to_string(), file=out)
    f['yk'] = (f.found | f.tic.isin(known)).astype(float)
    k0, _, m0 = fit(base, f.yk.values); k1, sk1, m1 = fit(base + bands, f.yk.values)
    print(f'  found or catalogued, joint fit: band factors G10-11 {np.exp(k1[4]):.2f} +- {np.exp(k1[4])*sk1[4]:.2f}, '
          f'G11-11.5 {np.exp(k1[5]):.2f} +- {np.exp(k1[5])*sk1[5]:.2f} (relative to G<10); band terms 2 dlogL = {2*(m0-m1):.1f} '
          f'(p = {stats.chi2.sf(2*(m0-m1), 2):.2g})', file=out)
    f['pk'] = f.p_det*np.exp(np.column_stack([np.ones(len(f))] + base) @ k0)
    t = f.groupby('band').agg(found_or_catalogued=('yk', 'sum'), predicted=('pk', 'sum'))
    t['p_poisson'] = [min(stats.poisson.cdf(r.found_or_catalogued, r.predicted), stats.poisson.sf(r.found_or_catalogued - 1, r.predicted)) for r in t.itertuples()]
    print(t.round(3).to_string(), file=out)
    cols = ['tic', 'band', 'significance', 'G', 'bp_rp', 'giant', 'R1', 'M2', 'P', 'e', 'coverage', 'p_det', 'depth_ppt', 'dur_h',
            'group', 'review_id', 'method', 'P_ecl', 'found', 'periodfree', 'catalogued']
    d[cols].round(4).to_csv(os.path.join(HERE, 'main-search-yield.csv'), index=False, lineterminator='\n')
    out.close()
    fn = os.path.join(HERE, 'main-search-yield-output.txt')
    txt = '\n'.join(l.rstrip() for l in open(fn).read().split('\n'))
    open(fn, 'w').write(txt); print(txt)

if __name__ == '__main__':
    main()
