"""Run 12a: is run 11e's 'Gaia period errors are calibrated for confirmed systems' circular?
Run from the repository root after run 11 is committed:
  python3 reviews/2026-11-24-duet-research-runs-1-4/run12-gaia-tiering/tier_reasons.py
For each of the 199 systems in run 11e's gaia-period-pulls.csv, collect the limitation text the
reviews give (every top-level review table with review_id and a limitation column, plus the
system's REPORT.md) and flag whether a Gaia orbit/conjunction/period tension is named.
"""
import pandas as pd, re, os, glob, sys
from scipy.stats import fisher_exact
D = 'reviews/2026-11-24-duet-research-runs-1-4/'
pulls = pd.read_csv(sys.argv[1] if len(sys.argv) > 1 else D + 'run11-ledger/gaia-period-pulls.csv')
lim = {}
for f in sorted(glob.glob('*.csv')):
    df = pd.read_csv(f, dtype=str)
    if 'review_id' not in df: continue
    cols = [c for c in df.columns if c.startswith('limitation')] + [c for c in ['next_check', 'gaia_geometry'] if c in df]
    for _, r in df.iterrows():
        t = ' '.join(str(r[c]) for c in cols if isinstance(r[c], str))
        if t: lim[r.review_id] = lim.get(r.review_id, '') + ' | ' + t
perr = {}
for f in sorted(glob.glob('*.csv')):
    df = pd.read_csv(f, dtype=str)
    if 'review_id' not in df or 'period_error_days' not in df: continue
    for r, e in zip(df.review_id, pd.to_numeric(df.period_error_days, errors='coerce')):
        if e > 0: perr.setdefault(r, e)
rep = {}
for f in ['reviewed-extension.csv', 'scientific-review-register.csv']:
    df = pd.read_csv(f, dtype=str)
    for r, p in zip(df.review_id, df.report):
        if isinstance(p, str):
            p = p.split('#')[0]
            if os.path.isfile(p): rep.setdefault(r, p)
GAIA = re.compile(r'gaia[^.|]{0,80}(tension|disagree|fail|inconsistent|offset[^.|]{0,40}sigma|beyond|contradict|retains? (about)?\s*\d(\.\d)?\s*sigma)'
                  r'|(tension|disagree|fail)[^.|]{0,60}gaia|GAIA_ASSOCIATION_TENSION|geometry-tension|Gaia orbit tension|Gaia[- ]orbit(al)? association[^.|]{0,40}(unresolved|uncertain)'
                  r'|Gaia SB2 orbital association|spectroscopic association is not fully passed|measured primary tension', re.I)
out = []
for _, r in pulls.iterrows():
    t = lim.get(r.review_id, '')
    rt = open(rep[r.review_id]).read() if r.review_id in rep else ''
    hit_lim = bool(GAIA.search(t)); hit_rep = bool(GAIA.search(rt))
    m = GAIA.search(t) or GAIA.search(rt)
    out.append(dict(review_id=r.review_id, tier=r.tier, sb=r.nss_solution_type, P=r.eclipse_period_days, z=round(r.z, 2),
                    gaia_tension_in_limitation=hit_lim, gaia_tension_in_report=hit_rep,
                    excerpt=(t if hit_lim else rt)[max(0, m.start() - 80):m.end() + 80].replace('\n', ' ') if m else ''))
o = pd.DataFrame(out)
pe = pulls.set_index('review_id').period_error
o['ecl_period_error'] = o.review_id.map(perr)
o['z_both'] = [round(z * pe[r] / (pe[r]**2 + (e if e == e else 0)**2) ** .5, 2) for r, z, e in zip(o.review_id, o.z, o.ecl_period_error)]
o['gaia_tension'] = o.gaia_tension_in_limitation | o.gaia_tension_in_report
o.sort_values('z').to_csv(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'tier-reasons.csv'), index=False)
print('systems:', len(o), ' with a report found:', sum(x in rep for x in o.review_id))
print(pd.crosstab(o.tier, o.gaia_tension, margins=True))
o['big'] = o.z_both.abs() >= 3
print('eclipse period errors found for', o.ecl_period_error.notna().sum(), 'systems; |z| uses both errors where given')
print('\n|z|>=3 by tier and named Gaia tension:'); print(pd.crosstab([o.tier, o.gaia_tension], o.big))
print('\nall 199 together (tier ignored): |z|>=3 in', o.big.sum(), f'({o.big.mean():.1%});',
      'SB1 only:', o[o.sb == 'SB1'].big.sum(), 'of', (o.sb == 'SB1').sum())
print('|z|>=2 in', (o.z.abs() >= 2).sum(), f'({(o.z.abs()>=2).mean():.1%}); Gaussian 4.6%')
# paper's appointment sample, Table 4: period >=3 sigma (non-alias) in 12 of 184
# (A12 A28 A29 A52 A86 A102 A110 A117 A147 A159 A167 A202; A159 at 3.2 sigma)
print('\npaper Table 4, appointment sample: 12 of 184 periods >= 3 sigma (non-alias)')
print('  vs R systems all tiers', o.big.sum(), 'of', len(o), fisher_exact([[12, 172], [o.big.sum(), len(o) - o.big.sum()]]))
c = o[o.tier == 'confirmed']
print('  vs R confirmed only', c.big.sum(), 'of', len(c), fisher_exact([[12, 172], [c.big.sum(), len(c) - c.big.sum()]]))
print('\nprobable systems whose reports name Gaia tension:')
print(o[(o.tier == 'probable') & o.gaia_tension][['review_id', 'sb', 'P', 'z', 'z_both', 'excerpt']].to_string(index=False, max_colwidth=150))
