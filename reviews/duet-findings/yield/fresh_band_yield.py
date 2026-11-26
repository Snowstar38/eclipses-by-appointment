"""Expected against found eclipsing binaries in the frozen G 11.5-12 appointment cohorts.

For each science target of the five fresh-band cohorts (Gaia DR3 SB1/SB2 orbits, 20-60 d,
selected before any flux was examined) the Gaia row gives the primary's radius (parallax, G,
BP-RP; no extinction), the companion's minimum mass (mass function at i = 90 deg) and the orbit
(P, e, omega). Isotropic orientations then give the chance that TESS saw at least one eclipse
deeper than DMIN at a conjunction the observed windows covered (window coverage from the
appointment results). Summed per group, that is the expected number of eclipsing systems,
compared with the accepted systems in accepted-systems.csv.

Run from the repository root: python3 reviews/duet-findings/yield/fresh_band_yield.py
Needs numpy, pandas and SciPy. Writes fresh-band-yield.csv and fresh-band-yield-output.txt here.
"""
import csv, glob, json, os
import numpy as np, pandas as pd
from scipy import stats

HERE = os.path.dirname(os.path.abspath(__file__))
G = 6.674e-11; MSUN = 1.989e30; RSUN = 6.957e8; DAY = 86400.

def teff(c, giant):  # Mucciarelli & Bellazzini 2020, unreddened BP-RP
    c = min(max(c, 0.2), 2.6)
    th = (0.5323 + 0.4775*c - 0.0344*c*c) if giant else (0.4929 + 0.5092*c - 0.0353*c*c)
    return 5040/th

def bc_g(T):  # Andrae et al. 2018
    x = T - 5772.
    a = ([6.000e-02, 6.731e-05, -6.647e-08, 2.859e-11, -7.197e-15] if T >= 4000 else
         [1.749, 1.977e-3, 3.737e-7, -8.966e-11, -4.183e-14])
    return sum(a[i]*x**i for i in range(5))

def load():
    pops, cover = {}, {}
    for f in sorted(glob.glob('reviews/2026-11-05-*/fresh-band*/population.json')):
        if 'stage1' in f: continue
        for tic, v in json.load(open(f))['targets'].items():
            if not v.get('control') and v.get('files'): pops[tic] = v['gaia']
        for g in glob.glob(os.path.join(os.path.dirname(f), 'appointment-results', '*.json')):
            d = json.load(open(g)); tic = str(d.get('tic'))
            cov = []
            for kind in 'AB':
                fr = [w['frac_covered'] for w in d.get('windows', []) if w['kind'] == kind]
                cov.append(1 - np.prod([1 - x for x in fr]) if fr else 0.)
            cover[tic] = float(np.mean(cov)) if d.get('windows') else np.nan
    return pops, cover

def stars(pops, cover, m_giant=1.4, r2_scale=1.0):
    rows = []
    for tic, g in pops.items():
        try:
            plx = float(g['parallax']); Gm = float(g['phot_g_mean_mag']); c = float(g['bp_rp'])
            P = float(g['period']); e = float(g['eccentricity'] or 0)
            w = float(g['arg_periastron'] or 90); K = float(g['semi_amplitude_primary'])
        except (TypeError, ValueError):
            continue
        if plx <= 0.2 or not np.isfinite(cover.get(tic, np.nan)): continue
        MG = Gm + 5*np.log10(plx/100.)
        giant = MG < 3.0 and c > 0.85
        T = teff(c, giant); L = 10**(-0.4*(MG + bc_g(T) - 4.74)); R1 = np.sqrt(L)/(T/5772.)**2
        M1 = m_giant if giant else float(np.clip(L**0.25 if L > 1 else L**0.4 if L > 0.1 else 0.4, 0.3, 3.0))
        f = P*DAY*(K*1e3)**3*(1 - e*e)**1.5/(2*np.pi*G)/MSUN
        M2 = 0.1
        for _ in range(80): M2 = (f*(M1 + M2)**2)**(1/3)
        R2 = r2_scale*(M2**0.8 if M2 < 1.2 else 1.11*M2**0.57)
        a = ((G*(M1 + M2)*MSUN*(P*DAY)**2)/(4*np.pi**2))**(1/3)/RSUN
        try: sig = float(g['significance'])
        except (TypeError, ValueError): sig = np.nan
        rows.append(dict(tic=tic, significance=sig, G=Gm, MG=MG, bp_rp=c, giant=giant, teff=T, R1=R1, M1=M1, M2=M2, R2=R2,
                         P=P, e=e, omega=w, a=a, coverage=cover[tic]))
    return rows

def chances(r, rng, n=4000, dmin=2.0, use_cov=True):
    P, e, w, a, R1, R2 = r['P'], r['e'], np.radians(r['omega']), r['a'], r['R1'], r['R2']
    cosi = rng.uniform(0, 1, n); S = R1 + R2; cov = r['coverage'] if use_cov else 1.0
    miss = np.ones(n); tlong = np.zeros(n); anyecl = np.zeros(n, bool)
    for s in (+1, -1):
        rc = a*(1 - e*e)/(1 + s*e*np.sin(w)); b = rc*cosi/S; m = b < 1
        dur = P*24/np.pi*S/a*np.sqrt(1 - e*e)/(1 + s*e*np.sin(w))*np.sqrt(np.clip(1 - b*b, 0, 1))
        depth = 1e3*min(R2/R1, 1.0)**2   # ppt, companion's disc on the primary, central
        ok = m & (depth >= dmin)
        miss *= np.where(ok, 1 - cov, 1.0); anyecl |= m
        tlong = np.where(ok & (dur > tlong), dur, tlong)
    return 1 - miss.mean(), anyecl.mean(), (np.median(tlong[tlong > 0]) if (tlong > 0).any() else np.nan)

def run(pops, cover, acc, offp, label, out, **kw):
    use_cov = kw.pop('use_cov', True); dmin = kw.pop('dmin', 2.0)
    rng = np.random.default_rng(20261126)
    rows = stars(pops, cover, **kw)
    for r in rows:
        r['p_det'], r['p_ecl'], r['dur_h'] = chances(r, rng, dmin=dmin, use_cov=use_cov)
        r['depth_ppt'] = 1e3*min(r['R2']/r['R1'], 1.0)**2
        r['accepted'] = acc.get(r['tic'], '')
        r['off_gaia_period'] = r['tic'] in offp
    d = pd.DataFrame(rows)
    d['found'] = (d.accepted != '') & ~d.off_gaia_period
    d['group'] = np.where(d.dur_h > 30, 'long (>30 h)', np.where(d.depth_ppt < 60, 'shallow (<60 ppt)', 'deep (>=60 ppt)'))
    g = d.groupby('group').agg(targets=('tic', 'size'), expected=('p_det', 'sum'), found=('found', 'sum'))
    g['found/expected'] = g.found/g.expected
    tot_e, tot_f = d.p_det.sum(), d.found.sum()
    print(f'\n[{label}] targets {len(d)}, expected {tot_e:.1f}, found {tot_f} (ratio {tot_f/tot_e:.2f})', file=out)
    print(g.round(2).to_string(), file=out)
    deep = g.loc['deep (>=60 ppt)']; rest = g.drop('deep (>=60 ppt)')
    p0 = deep.expected/tot_e
    pb = stats.binomtest(int(deep.found), int(tot_f), p0, alternative='greater').pvalue
    print(f'share of finds in the deep group {int(deep.found)}/{int(tot_f)} against {p0:.2f} expected: p = {pb:.1e}', file=out)
    return d

def main():
    pops, cover = load()
    acc = {r['tic']: r['tier'] for r in csv.DictReader(open('accepted-systems.csv'))}
    # accepted systems whose reviewed eclipse period is not Gaia's (not Gaia-orbit eclipses)
    offp = set()
    for f in glob.glob('reviews/2026-11-05-final-night/**/RESULTS.csv', recursive=True):
        for r in csv.DictReader(open(f)):
            try: per = float(r['period_days'])
            except (KeyError, ValueError): continue
            g = pops.get(r['tic'])
            if g and abs(per/float(g['period']) - 1) > 0.02: offp.add(r['tic'])
    out = open(os.path.join(HERE, 'fresh-band-yield-output.txt'), 'w')
    print(f'{len(pops)} science targets with data; {sum(t in acc for t in pops)} accepted, '
          f'{len(offp & set(acc))} of them reviewed at a period other than Gaia\'s (left out of "found": '
          f'{", ".join(sorted(offp & set(acc)))})', file=out)
    d = run(pops, cover, acc, offp, 'default: 2 ppt floor, window coverage, giants 1.4 Msun', out)
    d['dur_bin'] = pd.cut(d.dur_h, [0, 15, 30, 300]); d['depth_bin'] = pd.cut(d.depth_ppt, [0, 20, 60, 1001])
    t = d.groupby(['depth_bin', 'dur_bin'], observed=True).agg(expected=('p_det', 'sum'), found=('found', 'sum'))
    t['found/expected'] = t.found/t.expected
    print('\nby predicted depth (ppt) and duration (h):', file=out); print(t.round(2).to_string(), file=out)
    d['depth_band'] = pd.cut(d.depth_ppt, [0, 20, 60, 1001], labels=['<20', '20-60', '>=60'])
    t = d.groupby('depth_band', observed=True).agg(expected=('p_det', 'sum'), found=('found', 'sum'))
    t['found/expected'] = t.found/t.expected
    print('\nby predicted depth (ppt), all durations:', file=out); print(t.round(2).to_string(), file=out)
    d['sig_band'] = pd.cut(d.significance, [0, 15, 30, 60, 1e4])
    for grp in ['deep (>=60 ppt)', 'shallow (<60 ppt)']:
        s_ = d[d.group == grp]
        t = s_.groupby('sig_band', observed=True).agg(targets=('tic', 'size'), expected=('p_det', 'sum'), found=('found', 'sum'))
        t['found/expected'] = t.found/t.expected
        print(f'\n{grp} by Gaia orbit significance:', file=out); print(t.round(2).to_string(), file=out)
    from scipy.optimize import minimize
    f = d[np.isfinite(d.significance) & (d.p_det > 0)]
    X = np.column_stack([np.ones(len(f)), (f.group == 'shallow (<60 ppt)').astype(float),
                         (f.group == 'long (>30 h)').astype(float), np.log10(f.significance/30)])
    y = f.found.values.astype(float); E = f.p_det.values
    nll = lambda b: (E*np.exp(X @ b) - y*(X @ b)).sum()
    fit = minimize(nll, np.zeros(4), method='BFGS'); se = np.sqrt(np.diag(fit.hess_inv))
    print(f'\njoint Poisson fit, found = expected x exp(b0 + b1 shallow + b2 long + b3 log10(sig/30)), {len(f)} targets with a significance:', file=out)
    for n_, b, e_ in zip(['b0 (deep, sig 30)', 'b1 shallow', 'b2 long', 'b3 log10 sig'], fit.x, se):
        print(f'  {n_:18s} {b:+.2f} +- {e_:.2f}   factor {np.exp(b):.2f}', file=out)
    print(f'  so the found rate goes as significance^{fit.x[3]/np.log(10):.2f} +- {se[3]/np.log(10):.2f}', file=out)
    st = d[d.significance >= 30]
    print(f'\norbits with significance >= 30: {len(st)} targets, expected {st.p_det.sum():.1f}, found {int(st.found.sum())}; '
          f'deep {st[st.group=="deep (>=60 ppt)"].p_det.sum():.1f} expected, {int(st[st.group=="deep (>=60 ppt)"].found.sum())} found', file=out)
    pool = d[(d.significance >= 20) & ~d.found & (d.accepted == '')]
    q = pd.concat([pool[pool.group == g_].sort_values('p_det', ascending=False).head(30) for g_ in ['long (>30 h)', 'shallow (<60 ppt)']])
    q[['tic', 'group', 'significance', 'P', 'e', 'R1', 'M2', 'depth_ppt', 'dur_h', 'coverage', 'p_det']].round(3).to_csv(
        os.path.join(HERE, 'fresh-band-research-list.csv'), index=False, lineterminator='\n')
    for g_ in ['long (>30 h)', 'shallow (<60 ppt)']:
        x = q[q.group == g_]
        print(f're-search list, {g_}: 30 not-found orbits (significance >= 20) with the highest chance sum to {x.p_det.sum():.1f} expected '
              f'(median depth {x.depth_ppt.median():.0f} ppt, duration {x.dur_h.median():.0f} h)', file=out)
    dw = d[~d.giant]; dw = dw.assign(sh=dw.depth_ppt < 60)
    tw = dw.groupby('sh').agg(expected=('p_det', 'sum'), found=('found', 'sum'))
    print('\ndwarfs and subgiants only (shallow = True):', file=out); print(tw.round(2).to_string(), file=out)
    for lab, kw in [('1 ppt floor', dict(dmin=1.0)), ('5 ppt floor', dict(dmin=5.0)),
                    ('giants 2.0 Msun', dict(m_giant=2.0)), ('companion radii x1.2', dict(r2_scale=1.2)),
                    ('no window coverage', dict(use_cov=False))]:
        run(pops, cover, acc, offp, lab, out, **kw)
    cols = ['tic', 'significance', 'G', 'bp_rp', 'giant', 'teff', 'R1', 'M1', 'M2', 'R2', 'P', 'e', 'omega', 'coverage',
            'p_ecl', 'p_det', 'depth_ppt', 'dur_h', 'group', 'accepted', 'off_gaia_period']
    d[cols].round(4).to_csv(os.path.join(HERE, 'fresh-band-yield.csv'), index=False, lineterminator='\n')
    # among systems that do eclipse, do Gaia's pulls depend on significance? (run on gaia-errors/fit-quality-scaling.csv)
    sig = {}
    for f in glob.glob('reviews/**/*nss*.csv', recursive=True):
        try:
            for n in csv.DictReader(open(f)):
                try: sig[n['source_id']] = float(n['significance'])
                except (KeyError, TypeError, ValueError): pass
        except (UnicodeDecodeError, csv.Error, OSError): pass
    fq = pd.read_csv(os.path.join(HERE, '..', 'gaia-errors', 'fit-quality-scaling.csv'), dtype={'source_id': str})
    fq['sig'] = fq.source_id.map(sig)
    print('\neclipsing systems, |Gaia pull| against orbit significance (Spearman):', file=out)
    for t_, s_ in fq.dropna(subset=['sig']).groupby('test'):
        rho, p_ = stats.spearmanr(np.abs(s_.z), s_.sig)
        print(f'  {t_}: n = {len(s_)}, rho = {rho:+.2f}, p = {p_:.2f}, 3-sigma misses {int((np.abs(s_.z) > 3).sum())}, '
              f'of them at significance < 20: {int(((np.abs(s_.z) > 3) & (s_.sig < 20)).sum())}', file=out)
    # the F2 law (gaia-errors/fit_quality_scaling.py) on the G 11.5-12 finds: offset of the best event from
    # Gaia's predicted conjunction in units of the window's quoted (independent) sigma, TESS epochs
    rows_ = []
    for fj in glob.glob('reviews/2026-11-05-*/fresh-band*/appointment-results/*.json'):
        if 'stage1' in fj: continue
        j = json.load(open(fj)); t_ = str(j['tic']); b_ = j.get('best')
        if not b_ or t_ not in set(d.tic[d.found]): continue
        off = b_['t'] - b_['tc']
        same = [w for w in j['windows'] if w['kind'] == b_['kind'] and w.get('best') and w['best']['snr'] > 10
                and abs((w['best']['t'] - w['tc']) - off) < 0.3]
        if b_['snr'] > 15 and len(same) >= 2:
            rows_.append((b_['dt_sigma'], float(pops[t_]['goodness_of_fit'])))
    z_, f2_ = np.array(rows_).T
    w_ = lambda x: 1.4826*np.median(np.abs(x - np.median(x)))
    rho, p_ = stats.spearmanr(np.abs(z_), f2_)
    print(f'\nG 11.5-12 finds with clean repeated eclipses ({len(z_)}): offset from Gaia conjunction / quoted sigma, robust width '
          f'{w_(z_):.2f}; {w_(z_[f2_ <= 1.5]):.2f} at F2 <= 1.5 ({int((f2_ <= 1.5).sum())}), {w_(z_[f2_ > 1.5]):.2f} above ({int((f2_ > 1.5).sum())}); '
          f'Spearman |z| vs F2 rho = {rho:+.2f}, p = {p_:.2f}', file=out)
    out.close(); print(open(os.path.join(HERE, 'fresh-band-yield-output.txt')).read())

if __name__ == '__main__':
    main()
