"""Does the main search's yield rise with Gaia significance because of the search or because of the orbits?

Rebuilds the per-target frame of main_search_yield.py (same model, same seed) and fits, for each
channel separately, count = model chance x exp(b0 + depth/duration group + band + beta log10 significance):
  appointment finds (expected = p_det, which includes window coverage),
  catalogued eclipsing binaries (Prsa 2022 / IJspeert 2024; expected = p_ecl, the geometric chance with no
  window coverage, since those catalogues never saw the windows),
  any eclipser = appointment find, period-free find or catalogued (expected = p_ecl).
A beta shared by the catalogue channel says the trend lives in the Gaia orbits (spurious or overstated
orbits at low significance), not in the windows or the box search.

Run from the repository root: python3 reviews/duet-findings/yield/significance_channels.py
Needs numpy, pandas and SciPy. Writes significance-channels-output.txt here.
"""
import glob, importlib.util, json, os, sys
sys.dont_write_bytecode = True
import numpy as np, pandas as pd
from scipy import stats
from scipy.optimize import minimize

HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location('msy', os.path.join(HERE, 'main_search_yield.py'))
msy = importlib.util.module_from_spec(spec); spec.loader.exec_module(msy)
fby = msy.fby

def frame():
    m = pd.read_csv(msy.ROWS, dtype={'tic': str, 'source_id': str, 'veb': str})
    covtab, _ = msy.coverage_by_nwin()
    m = m[m.veb.isna()].copy()
    nw = m.n_windows.fillna(0).clip(upper=20).astype(int)
    m['coverage'] = [0.0 if n == 0 else float(covtab.get(n, covtab.iloc[-1])) for n in nw]
    pops = {r.tic: r._asdict() for r in m.itertuples(index=False)}
    cover = dict(zip(m.tic, m.coverage)); band = dict(zip(m.tic, m.band))
    extra = m.set_index('tic')[['phot_variable_flag', 'z', 'goodness_of_fit', 'ruwe', 'semi_amplitude_primary', 'period_error', 't_periastron_error', 'nsec', 'Tmag']]
    acc = pd.read_csv('accepted-systems.csv', dtype=str)
    reg = pd.read_csv('scientific-review-register.csv', dtype=str).set_index('review_id').search_method.to_dict()
    meth, perA = msy.table_a1(); perR = msy.review_periods()
    acc['method'] = acc.review_id.map(meth).fillna(acc.review_id.map(reg))
    acc['P_ecl'] = [perA.get(r, perR.get(t, np.nan)) for r, t in zip(acc.review_id, acc.tic)]
    acc = acc[acc.tic.isin(pops)].drop_duplicates('tic')
    rng = np.random.default_rng(20261126)
    rows = fby.stars(pops, cover)
    for r in rows:
        r['p_det'], r['p_ecl'], r['dur_h'] = fby.chances(r, rng)
        r['depth_ppt'] = 1e3*min(r['R2']/r['R1'], 1.0)**2
    d = pd.DataFrame(rows); d['band'] = d.tic.map(band)
    d = d.join(extra, on='tic')
    a = acc.set_index('tic')
    d['method'] = d.tic.map(a.method).fillna(''); d['P_ecl'] = d.tic.map(a.P_ecl)
    d['same_P'] = np.abs(d.P_ecl/d.P - 1) < 0.02
    d['found'] = d.method.isin(msy.CONJ) & d.same_P
    d['periodfree'] = d.method == 'Period-free dip screening'
    idn = pd.read_csv(msy.IDENT, dtype={'tic': str})
    known = set(idn.tic[idn.cached_primary_identity_match.astype(str) == 'True'])
    d['catalogued'] = d.tic.isin(known)
    d['anyecl'] = d.found | d.periodfree | d.catalogued | d.method.isin(msy.CONJ)
    d['group'] = np.where(d.dur_h > 30, 'long', np.where(d.depth_ppt < 60, 'shallow', 'deep'))
    return d

def pfit(f, y, E, cols, names):
    X = np.column_stack([np.ones(len(f))] + cols)
    nll = lambda b: -(y*(np.log(E) + X @ b) - E*np.exp(X @ b)).sum()
    r = minimize(nll, np.zeros(X.shape[1]), method='BFGS')
    H = X.T @ (X*(E*np.exp(X @ r.x))[:, None]); s = np.sqrt(np.diag(np.linalg.inv(H)))
    return dict(zip(['b0'] + names, zip(r.x, s))), r.fun

def roche_fill(d):
    q = d.M1/d.M2
    rl = d.a*(1 - d.e)*0.49*q**(2/3)/(0.6*q**(2/3) + np.log(1 + q**(1/3)))   # Eggleton, at periastron
    return d.R1/rl

def fits(f, P, who):
    grp = [(f.group == 'shallow').astype(float).values, (f.group == 'long').astype(float).values]
    bnd = [(f.band == 'G10-11').astype(float).values, (f.band == 'G11-11.5').astype(float).values] if 'band' in f else []
    gi = [f.giant.astype(float).values] if f.giant.any() else []
    ls = np.log10(f.significance/30).values; ld = np.log10(f.depth_ppt.clip(lower=1)/60).values
    base = grp + bnd + gi; bn = ['c%d' % i for i in range(len(base))]
    P(f'\n{who}: {len(f)} targets; count = chance x exp(b0 + groups + bands{" + giant" if gi else ""} + terms below)')
    P('  powers of significance and of predicted depth (coefficient / ln 10)')
    P(f'  {"channel":30s} {"sig alone":>15s} {"depth":>14s} {"+ sig":>14s}')
    chans = [('appointment finds / p_det', f.found, f.p_det)]
    if 'catalogued' in f:
        chans += [('catalogued / p_ecl', f.catalogued, f.p_ecl), ('period-free finds / p_ecl', f.periodfree, f.p_ecl),
                  ('any eclipser / p_ecl', f.anyecl, f.p_ecl)]
    for lab, y, E in chans:
        y = y.values.astype(float); E = E.values
        b1, _ = pfit(f, y, E, base + [ls], bn + ['s'])
        b2, _ = pfit(f, y, E, base + [ld, ls], bn + ['d', 's'])
        L = np.log(10)
        P(f'  {lab:30s} {b1["s"][0]/L:+6.2f} +- {b1["s"][1]/L:.2f}   {b2["d"][0]/L:+6.2f} +- {b2["d"][1]/L:.2f}  {b2["s"][0]/L:+6.2f} +- {b2["s"][1]/L:.2f}')

def main():
    out = open(os.path.join(HERE, 'significance-channels-output.txt'), 'w')
    P = lambda *a: print(*a, file=out)
    d = frame()
    d['fill'] = roche_fill(d)
    f = d[np.isfinite(d.significance) & (d.p_det > 0)].copy()
    P(f'{len(f)} modelled targets with a significance and a nonzero detection chance')
    P(f'appointment finds {int(f.found.sum())}, period-free {int(f.periodfree.sum())}, catalogued {int(f.catalogued.sum())}, '
      f'any eclipser {int(f.anyecl.sum())}')
    fits(f, P, 'all targets')
    fits(f[~f.giant].copy(), P, 'dwarfs and subgiants')
    t = d.groupby('band').agg(targets=('tic', 'size'), catalogued=('catalogued', 'sum'))
    pre = [x for g_ in sorted(glob.glob('reviews/2026-11-05-*/fresh-band*/exact-prior-identities.json')) for x in json.load(open(g_))['targets']]
    t.loc['G11.5-12 (exact precheck cohorts)'] = [len(pre), sum(bool(x.get('prsa') or x.get('ijspeert')) for x in pre)]
    t['share_%'] = 100*t.catalogued/t.targets
    P('\ncatalogued eclipsing binaries (Prsa 2022 or IJspeert 2024) as a share of targets, by band:'); P(t.round(2).to_string())
    fb = pd.read_csv(os.path.join(HERE, 'fresh-band-yield.csv'), dtype={'tic': str, 'accepted': str})
    fb['found'] = fb.accepted.notna() & ~fb.off_gaia_period.astype(bool)
    fb['group'] = fb.group.str.split(' ').str[0]
    fits(fb[np.isfinite(fb.significance) & (fb.p_det > 0)].copy(), P, 'G 11.5-12 fresh-band cohorts (fresh-band-yield.csv), appointment finds only')
    w = f[~f.giant & (f.t_periastron_error > 0)].copy()
    w['sigT'] = np.sqrt(w.t_periastron_error**2 + (1611/w.P*w.period_error)**2)   # conjunction error at mid-TESS (about 1,611 d after Gaia's epoch)
    grp = [(w.group == 'shallow').astype(float).values, (w.group == 'long').astype(float).values]
    bnd = [(w.band == 'G10-11').astype(float).values, (w.band == 'G11-11.5').astype(float).values]
    ls = np.log10(w.significance/30).values; lt = np.log10(w.sigT).values
    b, _ = pfit(w, w.found.values.astype(float), w.p_det.values, grp + bnd + [lt], ['a', 'b', 'c', 'd', 't'])
    b2, _ = pfit(w, w.found.values.astype(float), w.p_det.values, grp + bnd + [ls, lt], ['a', 'b', 'c', 'd', 's', 't'])
    L = np.log(10)
    P(f'\ndwarfs, appointment finds against the predicted conjunction error at mid-TESS ({len(w)} targets; Spearman with significance '
      f'{stats.spearmanr(w.sigT, w.significance)[0]:.2f}): power {b["t"][0]/L:+.2f} +- {b["t"][1]/L:.2f} alone; with significance, '
      f'error {b2["t"][0]/L:+.2f} +- {b2["t"][1]/L:.2f} and significance {b2["s"][0]/L:+.2f} +- {b2["s"][1]/L:.2f}')
    z = d[d.z.notna()].copy()
    z['strength'] = np.where(z.significance < 30, 'significance < 30', 'significance >= 30')
    z['channel'] = np.where(z.catalogued, 'catalogued', np.where(z.found, 'appointment', np.where(z.anyecl, 'period-free', 'no eclipser')))
    t = z.groupby(['strength', 'channel']).z.agg(n='size', z_ge_8=lambda x: (x >= 8).mean(), z_ge_20=lambda x: (x >= 20).mean()).unstack(0)
    P('\nthe search\'s window statistic z (best event in Gaia\'s windows against the star\'s own null) where it is defined:')
    P(t.round(2).to_string())
    m_ = pd.read_csv(msy.ROWS, dtype={'tic': str, 'veb': str})
    m_['sb'] = pd.cut(m_.significance, [0, 15, 30, 45, 70, 1e5])
    sT = np.sqrt(m_.t_periastron_error**2 + (1611/m_.period*m_.period_error)**2)
    m_['duty'] = pd.cut(np.clip(4*np.clip(3*sT, 0.25, 7)/m_.period, 0, 1), [0, 0.3, 0.5, 0.7, 0.9, 1.0])
    P('z blank, by significance: ' + ', '.join(f'{k} {v:.2f}' for k, v in m_.groupby('sb', observed=True).z.apply(lambda x: x.isna().mean()).items()))
    P('z blank, by the share of the orbit inside the two windows (half-width max(3 sigma_T, 0.25 d), capped at 7 d): ' +
      ', '.join(f'{k} {v:.2f}' for k, v in m_.groupby('duty', observed=True).z.apply(lambda x: x.isna().mean()).items()))
    sci = m_[m_.veb.isna() & m_.band.isin(['G<10', 'G10-11'])]
    P(f'z blank for {int(sci.z.isna().sum())} of {len(sci)} science rows at G < 11 (the paper counts 165 with no null and 591 with MAD = 0)')
    P('\nBy significance bin, dwarfs and subgiants:')
    w = f[~f.giant].copy(); w['sb'] = pd.cut(w.significance, [0, 15, 30, 45, 70, 1e5])
    t = w.groupby('sb', observed=True).agg(n=('tic', 'size'), K1=('semi_amplitude_primary', 'median'), M2=('M2', 'median'),
                                           depth=('depth_ppt', 'median'), p_det=('p_det', 'sum'), found=('found', 'sum'),
                                           p_ecl=('p_ecl', 'sum'), cat=('catalogued', 'sum'), pf=('periodfree', 'sum'))
    t['found/p_det'] = t.found/t.p_det; t['cat/p_ecl'] = t.cat/t.p_ecl; t['pf/p_ecl'] = t.pf/t.p_ecl
    P(t.round(3).to_string())
    P('\nGiants (M_G < 3, BP-RP > 0.85) by absolute magnitude: Roche-lobe filling at periastron for Gaia\'s orbit')
    g = d[d.giant & np.isfinite(d.significance)].copy(); g['MG_bin'] = pd.cut(g.MG, [-10, -1, 0, 1, 2, 3])
    t = g.groupby('MG_bin', observed=True).agg(n=('tic', 'size'), R1=('R1', 'median'), K1=('semi_amplitude_primary', 'median'),
                                               M2=('M2', 'median'), sig=('significance', 'median'), e=('e', 'median'),
                                               sig_lt15=('significance', lambda x: (x < 15).mean()),
                                               overfilled=('fill', lambda x: (x > 1).mean()), p_ecl=('p_ecl', 'sum'),
                                               p_det=('p_det', 'sum'), found=('found', 'sum'), any=('anyecl', 'sum'))
    P(t.round(3).to_string())
    lo, hi = g[g.significance < 15], g[g.significance > 45]
    P(f'giants with significance < 15: {len(lo)}, median K1 {lo.semi_amplitude_primary.median():.1f} km/s, median e {lo.e.median():.2f}, '
      f'{(lo.fill > 1).mean():.0%} overfill the Roche lobe; significance > 45: {len(hi)}, K1 {hi.semi_amplitude_primary.median():.1f}, '
      f'e {hi.e.median():.2f}, {(hi.fill > 1).mean():.1%} overfill')
    ov = d[d.fill > 1]
    lum = g[g.MG < -1]
    P(f'M_G < -1: {len(lum)} giants, median BP-RP {lum.bp_rp.median():.2f} ({lum.teff.median():.0f} K), star larger than the semi-major axis '
      f'in {(lum.R1 > lum.a).mean():.0%}, Gaia VARIABLE flag {(lum.phot_variable_flag == 'VARIABLE').mean():.0%}, eclipsers among them {int(lum.anyecl.sum())} '
      f'({", ".join(f"TIC {t} at {p:g} d against Gaia {q:.1f} d" for t, p, q in zip(lum[lum.anyecl].tic, lum[lum.anyecl].P_ecl, lum[lum.anyecl].P))})')
    P(f'all overfilled orbits: {len(ov)} ({int(ov.giant.sum())} giants); geometric chance {ov.p_ecl.sum():.1f}, detection chance '
      f'{ov.p_det.sum():.1f}, eclipsers among them {int(ov.anyecl.sum())}')
    r = pd.read_csv('faint-band-review.csv', dtype={'tic': str}).merge(fb[['tic', 'significance']], on='tic', how='left')
    r['weak'] = r.significance < 15
    P(f'\nG 11.5-12 reviewed leads (faint-band-review.csv, {r.significance.notna().sum()} of {len(r)} matched to the cohorts):')
    P(pd.crosstab(np.where(r.weak, 'significance < 15', 'significance >= 15'), r.physical_verdict).to_string())
    a = [[int((r.weak & (r.physical_verdict == 'PLAUSIBLE')).sum()), int((r.weak & (r.physical_verdict != 'PLAUSIBLE')).sum())],
         [int((~r.weak & (r.physical_verdict == 'PLAUSIBLE')).sum()), int((~r.weak & (r.physical_verdict != 'PLAUSIBLE')).sum())]]
    ft = stats.fisher_exact(a)
    P(f'plausible share {a[0][0]}/{sum(a[0])} against {a[1][0]}/{sum(a[1])}: odds ratio {ft[0]:.1f}, Fisher p = {ft[1]:.3f}; '
      f'without an eclipse period {int((r.weak & r.period_days.isna()).sum())}/{int(r.weak.sum())} against '
      f'{int((~r.weak & r.period_days.isna()).sum())}/{int((~r.weak).sum())}')
    fb['sb'] = pd.cut(fb.significance, [0, 15, 30, 60, 1e5]); r['sb'] = pd.cut(r.significance, [0, 15, 30, 60, 1e5])
    t = fb.groupby('sb', observed=True).agg(targets=('tic', 'size'), p_det=('p_det', 'sum'))
    t['leads'] = r.groupby('sb', observed=True).size(); t['accepted'] = r.groupby('sb', observed=True).claim_member.apply(lambda x: (x.astype(str) == 'True').sum())
    t['leads/p_det'] = t.leads/t.p_det; t['accepted/leads'] = t.accepted/t.leads
    P(t.round(2).to_string())
    fb['a'] = ((6.674e-11*(fb.M1 + fb.M2)*1.989e30*(fb.P*86400)**2)/(4*np.pi**2))**(1/3)/6.957e8
    fb['fill'] = roche_fill(fb); o = fb[fb.fill > 1]
    P(f'G 11.5-12 cohorts: {len(o)} overfilled orbits of {len(fb)}, {int(o.giant.sum())} giants, median BP-RP {o.bp_rp.median():.2f}, '
      f'median significance {o.significance.median():.1f}, accepted {int(o.found.sum())}')
    out.close()
    fn = os.path.join(HERE, 'significance-channels-output.txt')
    txt = '\n'.join(l.rstrip() for l in open(fn).read().split('\n'))
    open(fn, 'w').write(txt); print(txt)

if __name__ == '__main__':
    main()
