"""Are Gaia DR3 SB1 period errors calibrated? The pull distribution against eclipse periods.
Run from the repository root:
  python3 reviews/duet-findings/gaia-errors/gaia_pulls.py
Collects every Gaia NSS two-body table in the repository that carries
period_error (deduplicated by source_id), joins it to run 8's
gaia-vs-eclipse.csv (accepted systems whose Gaia period matches the eclipse
period within 3%), and studies z = (P_gaia - P_ecl) / period_error. Eclipse
periods from years of TESS data are far more precise than Gaia's, so their
errors are neglected (this can only widen the distribution).
"""
import glob, os
import numpy as np, pandas as pd
from math import erf, sqrt
D = 'reviews/duet-findings/'
frames = []
for f in sorted(glob.glob('**/*.csv', recursive=True)):
    if os.path.getsize(f) > 50e6 or 'duet-findings' in f: continue
    try: c = pd.read_csv(f, nrows=0).columns
    except Exception: continue
    if {'source_id', 'period', 'period_error'} <= set(c):
        x = pd.read_csv(f, usecols=[k for k in ['source_id', 'period', 'period_error', 'eccentricity', 'eccentricity_error',
                                                 'nss_solution_type', 'goodness_of_fit'] if k in c])
        x['file'] = f; frames.append(x)
nss = pd.concat(frames, ignore_index=True)
nss = nss[pd.to_numeric(nss.source_id, errors='coerce').notna()]
nss['source_id'] = nss.source_id.astype('int64')
for k in ['period', 'period_error', 'eccentricity', 'eccentricity_error']:
    if k in nss: nss[k] = pd.to_numeric(nss[k], errors='coerce')
nss = nss[nss.period_error > 0].dropna(subset=['period', 'period_error']).drop_duplicates('source_id')
print(f'Gaia NSS rows with period errors in the repository: {len(nss)} distinct sources from {len(frames)} files')
g = pd.read_csv(D + 'gaia-geometry/gaia-vs-eclipse.csv')
g['eclipse_period_days'] = pd.to_numeric(g.eclipse_period_days, errors='coerce')
g['ratio_gaia_over_ecl'] = pd.to_numeric(g.ratio_gaia_over_ecl, errors='coerce')
g = g[g['class'].astype(str).str.startswith('match') | (abs(g.ratio_gaia_over_ecl - 1) < 0.03)]
g['sid'] = g.gaia_source.astype(str).str.split('|')
g = g.explode('sid'); g['sid'] = pd.to_numeric(g.sid, errors='coerce')
m = g.merge(nss, left_on='sid', right_on='source_id', how='inner').drop_duplicates('review_id')
m = m[abs(m.period / m.eclipse_period_days - 1) < 0.03]
m['z'] = (m.period - m.eclipse_period_days) / m.period_error
m = m[np.isfinite(m.z)]
print(f'accepted systems joined (Gaia period within 3% of eclipse period): {len(m)}')
z = m.z.values
mad = 1.4826 * np.median(np.abs(z - np.median(z)))
print(f'median z {np.median(z):+.2f}; robust width (1.4826 MAD) {mad:.2f}; std of |z|<10: {z[abs(z)<10].std():.2f}')
for k in [2, 3, 5]:
    n = (abs(z) >= k).sum(); exp = len(z) * (1 - erf(k / sqrt(2)))
    print(f'|z| >= {k}: {n} ({n/len(z):.1%}); expected if calibrated {exp:.1f}; '
          f'expected with errors x{mad:.2f}: {len(z) * (1 - erf(k / mad / sqrt(2))):.1f}')
print()
print('robust width by Gaia period:')
m['Pbin'] = pd.cut(m.eclipse_period_days, [0, 3, 6, 10, 20, 60, 1000])
for b, s in m.groupby('Pbin', observed=True):
    zz = s.z.values
    print(f'  {str(b):12s} n={len(zz):4d} width {1.4826*np.median(abs(zz-np.median(zz))):.2f}  |z|>=3: {(abs(zz)>=3).sum()}')
if 'nss_solution_type' in m:
    print('\nby solution type:')
    for b, s in m.groupby('nss_solution_type'):
        zz = s.z.values; print(f'  {b:22s} n={len(zz):4d} width {1.4826*np.median(abs(zz-np.median(zz))):.2f}  |z|>=3: {(abs(zz)>=3).sum()}')
m[['review_id', 'tier', 'sid', 'nss_solution_type', 'eclipse_period_days', 'period', 'period_error', 'z', 'file']].sort_values('z').to_csv(
    os.path.join(os.path.dirname(os.path.abspath(__file__)), 'gaia-period-pulls.csv'), index=False)

print('\nby tier:')
from scipy.stats import fisher_exact
for b, s in m.groupby('tier'):
    zz = s.z.values
    print(f'  {b:10s} n={len(zz):4d} width {1.4826*np.median(abs(zz-np.median(zz))):.2f}  |z|>=3: {(abs(zz)>=3).sum()}')
a = m.groupby('tier').apply(lambda s: ((abs(s.z) >= 3).sum(), (abs(s.z) < 3).sum()))
print('  Fisher exact (probable vs confirmed, |z|>=3):', fisher_exact([list(a['probable']), list(a['confirmed'])]))
print('\nsystems at |z| >= 3:')
print(m[abs(m.z) >= 3][['review_id', 'tier', 'nss_solution_type', 'eclipse_period_days', 'period', 'period_error', 'z']].round(5).to_string(index=False))

print('\ntier within 20-60 d only (removes the period confound):')
s = m[(m.eclipse_period_days > 20) & (m.eclipse_period_days <= 60)]
for b, q in s.groupby('tier'):
    zz = q.z.values
    print(f'  {b:10s} n={len(zz):4d} width {1.4826*np.median(abs(zz-np.median(zz))):.2f}  |z|>=3: {(abs(zz)>=3).sum()}')
c = s.groupby('tier').apply(lambda q: ((abs(q.z) >= 3).sum(), (abs(q.z) < 3).sum()))
print('  Fisher exact:', fisher_exact([list(c['probable']), list(c['confirmed'])]))
print('  where the period came from (probable, 20-60 d):')
print(s[s.tier == 'probable'].file.str.extract(r'reviews/([^/]+)/')[0].value_counts().to_string())
