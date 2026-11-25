"""Run 12b: do the eclipses fall on Gaia's predicted conjunction at Gaia's own epoch?
If the eclipse belongs to the Gaia binary and only Gaia's period is off, the eclipse ephemeris carried
back to Gaia's epoch (BTJD ~ 389 + Tp) lands on a predicted conjunction there, while carrying Gaia's
period forward to TESS gives a growing offset. An unrelated eclipsing binary lands anywhere.
This is the test the paper uses for A147 and A167 (Table 4).
Run from the repository root:
  python3 reviews/2026-11-24-duet-research-runs-1-4/run12-gaia-tiering/gaia_epoch_test.py
Uses run 4's window_covariance.py (orbit parsing, conjunction times, linear covariance propagation)
and run 11e's gaia-period-pulls.csv for the sample.
"""
import sys, os, csv, glob, math
import numpy as np, pandas as pd
D = 'reviews/2026-11-24-duet-research-runs-1-4/'
sys.path.insert(0, D)
import window_covariance as W
HERE = os.path.dirname(os.path.abspath(__file__))
pulls = pd.read_csv(sys.argv[1] if len(sys.argv) > 1 else D + 'run11-ledger/gaia-period-pulls.csv')
tiers = pd.read_csv(os.path.join(HERE, 'tier-reasons.csv')).set_index('review_id')
# Gaia rows (any solution type) with corr_vec, by source id
nss = {}
for f in sorted(glob.glob('reviews/**/*.csv', recursive=True)):
    if 'duet-research' in f or os.path.getsize(f) > 50e6: continue
    with open(f, newline='') as fh:
        r = csv.DictReader(fh)
        if not r.fieldnames or not {'source_id', 't_periastron', 'corr_vec'} <= set(r.fieldnames): continue
        for x in r:
            if x.get('corr_vec'): nss.setdefault(x['source_id'], x)
# eclipse ephemerides: review tables first (period, its error, primary epoch), then measurements.json/host table
eph = {}
for f in sorted(glob.glob('*.csv')):
    df = pd.read_csv(f, dtype=str)
    pc = 'period_days' if 'period_days' in df else ('period_days_reported' if 'period_days_reported' in df else None)
    if 'review_id' not in df or pc is None or 'primary_epoch_btjd' not in df: continue
    for _, x in df.iterrows():
        try: P, T0 = float(x[pc]), float(x['primary_epoch_btjd'])
        except (TypeError, ValueError): continue
        if not (P > 0 and T0 > 0): continue
        try: eP = float(x.get('period_error_days'))
        except (TypeError, ValueError): eP = float('nan')
        eph.setdefault(x['review_id'], (P, T0, eP))
# fallback: the first measured event in the system's REPORT.md event table (| sector | BTJD | ...)
import re
rep = {}
for f in ['reviewed-extension.csv', 'scientific-review-register.csv']:
    for r, p in zip(*[pd.read_csv(f, dtype=str)[c] for c in ('review_id', 'report')]):
        if isinstance(p, str) and os.path.isfile(p.split('#')[0]): rep.setdefault(r, p.split('#')[0])
mj = {}
for f in glob.glob('reviews/**/measurements.json', recursive=True):
    try: d = __import__('json').load(open(f))
    except Exception: continue
    if isinstance(d, dict) and d.get('tic') and d.get('reference_epoch_btjd'): mj.setdefault(str(d['tic']), float(d['reference_epoch_btjd']))
def report_event(rid):
    """First event time in the system's report: an event-table row, else the first BTJD-like number in its text."""
    tic = acc.loc[rid, 'tic'] if rid in acc.index else None
    if tic in mj: return mj[tic]
    if rid not in rep: return None
    txt = open(rep[rid]).read()
    for line in txt.splitlines():
        if line.startswith('|'):
            m = re.search(r'\|\s*(\d{4}\.\d{3,})\s*\|', line)
            if m and 1300 < float(m.group(1)) < 5000: return float(m.group(1))
    m = re.search(r'(?:near|centers|at BTJD)\s*(\d{4}\.\d{3,})', txt)
    return float(m.group(1)) if m else None
def orbit(n):
    # parameter order of corr_vec (lower triangle): SB1 P,gamma,K,e,omega,Tp; SB2 P,gamma,K1,K2,e,omega,Tp
    sb2 = n.get('nss_solution_type') == 'SB2'
    npar, idx = (7, [0, 4, 5, 6]) if sb2 else (6, [0, 3, 4, 5])
    v = np.array([float(n['period']), float(n['eccentricity']), math.radians(float(n['arg_periastron'])), float(n['t_periastron']) + W.GAIA_OFFSET])
    err = np.array([float(n['period_error']), float(n['eccentricity_error']), math.radians(float(n['arg_periastron_error'])), float(n['t_periastron_error'])])
    vals = [float(x) for x in n['corr_vec'].strip('{}[]()').split(',')]
    if len(vals) != npar * (npar - 1) // 2: raise ValueError('corr_vec length')
    C = np.eye(npar); z = 0
    for i in range(1, npar):
        for j in range(i):
            C[i, j] = C[j, i] = vals[z]; z += 1
    return v, err, C[np.ix_(idx, idx)]
acc = pd.read_csv('accepted-systems.csv', dtype=str).set_index('review_id')
me = W.measured_epochs()
rows = []
for _, s in pulls.iterrows():
    sid = str(s.sid); n = nss.get(sid)
    if n is None: continue
    st = n.get('nss_solution_type', '')
    try: v, err, corr = orbit(n)
    except (ValueError, KeyError): continue
    if s.review_id in eph: P, T0, eP = eph[s.review_id]
    elif acc.loc[s.review_id, 'tic'] in me: (P, T0), eP = me[acc.loc[s.review_id, 'tic']], float('nan')
    elif report_event(s.review_id): P, T0, eP = s.eclipse_period_days, report_event(s.review_id), float('nan')
    else: continue
    if abs(P / s.eclipse_period_days - 1) > 1e-3: continue   # a different ephemeris than run 11e's
    eP = eP if eP == eP else 0.0
    best = None
    for k in (0, 1):
        tg = W.conj(v, k)                                   # Gaia conjunction at its own epoch (cycle 0)
        n_back = round((tg - T0) / P)
        o0 = T0 + n_back * P - tg                           # eclipse ephemeris carried back
        s0_full, s0_ind = W.sigmas(v, err, corr, k, 0)
        sb = abs(n_back) * eP                               # eclipse-ephemeris error at Gaia's epoch
        cyc = round((T0 - tg) / v[0])
        oT = T0 - W.t_at(v, k, cyc)                         # Gaia period carried forward to TESS
        sT_full, _ = W.sigmas(v, err, corr, k, cyc)
        cand = dict(review_id=s.review_id, tier=s.tier, sol=st, P_ecl=P, P_gaia=v[0], z_period=round(s.z, 2), e=round(v[1], 3), kind=k,
                    offset_gaia_epoch_d=round(o0, 3), sigma_gaia_epoch_d=round(math.hypot(s0_full, sb), 3),
                    z_gaia_epoch=round(o0 / math.hypot(s0_full, sb), 2), z_gaia_epoch_ind=round(o0 / math.hypot(s0_ind, sb), 2),
                    gaia_cycles_to_tess=cyc, offset_tess_d=round(oT, 3), sigma_tess_d=round(sT_full, 3), z_tess=round(oT / sT_full, 2),
                    gaia_tension_named=bool(tiers.loc[s.review_id, 'gaia_tension']))
        if best is None or abs(o0) < abs(best['offset_gaia_epoch_d']): best = cand
    rows.append(best)
o = pd.DataFrame(rows)
o['phase_gaia_epoch'] = (o.offset_gaia_epoch_d / o.P_gaia).round(4)
o.sort_values('z_period').to_csv(os.path.join(HERE, 'gaia-epoch-test.csv'), index=False)
print(f'systems tested: {len(o)} of {len(pulls)} (Gaia corr_vec and an eclipse ephemeris matching run 11e)')
for lab, q in [('all', o), ('confirmed', o[o.tier == 'confirmed']), ('probable', o[o.tier == 'probable']),
               ('|z_period| < 3', o[o.z_period.abs() < 3]), ('|z_period| >= 3', o[o.z_period.abs() >= 3])]:
    z = q.z_gaia_epoch
    print(f'{lab:16s} n={len(q):3d}  |z| at Gaia epoch: median {z.abs().median():.2f}, <2: {(z.abs()<2).sum()}, >=3: {(z.abs()>=3).sum()};'
          f'  |phase| median {q.phase_gaia_epoch.abs().median():.4f};  |z| at TESS median {q.z_tess.abs().median():.2f}')
print('\nsystems with |z_period| >= 2.5 or named Gaia tension:')
cols = ['review_id', 'tier', 'sol', 'P_ecl', 'z_period', 'e', 'kind', 'offset_gaia_epoch_d', 'sigma_gaia_epoch_d', 'z_gaia_epoch',
        'phase_gaia_epoch', 'offset_tess_d', 'z_tess']
print(o[(o.z_period.abs() >= 2.5) | o.gaia_tension_named].sort_values('z_period')[cols].to_string(index=False))
# chance that an unrelated eclipse lands this close to either conjunction at Gaia's epoch: ~ 4|offset|/P
t = o[o.z_period.abs() >= 3]
pr = np.clip(4 * t.offset_gaia_epoch_d.abs() / t.P_gaia, 0, 1)
print('\n|z_period| >= 3: chance each lands this close if unrelated (4|offset|/P):', dict(zip(t.review_id, pr.round(3))))
print('  joint chance all of them do:', f'{np.prod(pr):.1e}')
print('\nGaia conjunction-time errors at Gaia epoch, all tested systems (does the covariance describe them?):')
for lab, q in [('all', o), ('SB1', o[o.sol == 'SB1']), ('e < 0.1', o[o.e < 0.1]), ('e >= 0.1', o[o.e >= 0.1])]:
    z = q.z_gaia_epoch.values
    print(f'  {lab:9s} n={len(z):3d} robust width {W.robust_sd(z):.2f} (independent errors {W.robust_sd(q.z_gaia_epoch_ind):.2f});'
          f' |z|>=3: {(abs(z)>=3).sum()} ({(abs(z)>=3).mean():.1%})')
print('the 5 |z|>=3 at Gaia epoch:', o[o.z_gaia_epoch.abs() >= 3][['review_id', 'tier', 'z_period', 'z_gaia_epoch', 'phase_gaia_epoch']].to_dict('records'))
