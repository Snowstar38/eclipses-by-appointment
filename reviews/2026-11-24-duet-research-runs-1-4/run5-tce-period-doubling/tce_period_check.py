"""Run 5 (Duet, 2026-11-24): where the SPOC search's own period is twice the adopted one.

Reads only reviews/2026-11-23-pipeline-and-survey-review/host-stars.csv. Run from the repo root:
    python3 reviews/2026-11-24-duet-research-runs-1-4/run5-tce-period-doubling/tce_period_check.py

The SPOC rows record how the adopted period relates to the threshold-crossing event's period
in `reason`, as "(=Pc TCE)", "(=Pc/2 TCE)" or "(=2Pc TCE)". TPS finds the period that stacks the
most eclipse signal. Identical dips every P stack best at P; TPS reports 2P mainly when alternate
dips differ (or the second dip is off phase 0.5). So an "equal alternate dips" row whose TCE
period is twice the adopted period contradicts its own label.
"""
import csv, re, math, statistics as st, os
HERE = os.path.dirname(os.path.abspath(__file__))
SRC = 'reviews/2026-11-23-pipeline-and-survey-review/host-stars.csv'
rows = list(csv.DictReader(open(SRC, newline='')))
f = lambda x: float(x) if x not in ('', None) else None

def cat(r):
    s = r['period_resolution']
    if s.startswith('P: no secondary found, alternate dips equal'): return 'equal-dips'
    if s.startswith('2P: alternate dips unequal'): return '2P-unequal'
    if s.startswith('Refit'): return 'refit'
    return s.split(':')[0]

def tce(r):
    m = re.search(r'\(=([^)]*?)\s*TCE\)', r['reason'])
    return m.group(1) if m else ''

# 1. Calibrate: for rows settled at 2P from unequal dips, does TPS's period track the depth ratio?
print('Calibration on 2P rows (alternate dips unequal), secondary/primary depth ratio:')
for tag in ('Pc', '2Pc'):
    g = [f(r['secondary_depth_ppt']) / f(r['depth_ppt']) for r in rows
         if cat(r) == '2P-unequal' and tce(r) == tag and f(r['secondary_depth_ppt'])]
    q = st.quantiles(g, n=4)
    print(f'  TCE period = adopted 2P ("{tag}"): n={len(g)}, ratio quartiles {q[0]:.2f} {q[1]:.2f} {q[2]:.2f}')

# 2. Sensitivity of the alternate-dip test, from the 2P rows' reported sigmas.
seff = []
for r in rows:
    m = re.match(r'2P: alternate dips unequal \(([\d.]+) sigma\)', r['period_resolution'])
    if m and f(r['secondary_depth_ppt']) and f(r['n_events_prim']):
        d1, d2, n = f(r['depth_ppt']), f(r['secondary_depth_ppt']), f(r['n_events_prim'])
        seff.append((d1 - d2) * math.sqrt(n / 2) / float(m.group(1)))
lo, med, hi = st.quantiles(seff, n=10)[0], st.median(seff), st.quantiles(seff, n=10)[-1]
print(f'Per-event depth scatter implied by the 2P rows: median {med:.1f} ppt (10-90%: {lo:.1f}-{hi:.1f})')

# 3. Flag equal-dip rows whose TCE period is twice the adopted period.
out = []
for r in rows:
    if cat(r) == 'equal-dips' and tce(r) == 'Pc/2':
        n = f(r['n_events_prim']); d = f(r['depth_ppt'])
        dmin = lambda s: 4 * s * math.sqrt(2 / (n / 2)) if n else None  # 4-sigma odd/even difference
        adopted = f(r['adopted_period_days']); alt = f(r['period_alternative_days'])
        note = ''
        if not alt:  # R946: adopted column already holds 2P (Gaia SB2), text still describes P
            note = 'adopted period already 2x the period in the text; Gaia SB2 orbit matches 2P'
        if r['review_id'] == 'R995':
            note = 'Earthshine (Nov 24): odd 185 vs even 137 ppt in 11 sectors, 13.5 sigma: 2P'
        out.append(dict(review_id=r['review_id'], tic=r['tic'], tier=r['physical_tier'],
                        adopted_period_d=r['adopted_period_days'], tce_period_d=alt or r['adopted_period_days'],
                        depth_ppt=r['depth_ppt'], n_events=r['n_events_prim'], n_sectors=r['n_sectors'],
                        odd_even_4sigma_ppt_median_noise=f'{dmin(med):.1f}' if n else '',
                        odd_even_4sigma_frac_of_depth=f'{dmin(med)/d:.3f}' if n and d else '',
                        other_periodicity=('yes' if 'other periodicity' in r['reason'] else ''),
                        status=note or 'open: predicted unequal at 2P'))
with open(os.path.join(HERE, 'tce-doubled-equal-dip-rows.csv'), 'w', newline='') as fh:
    w = csv.DictWriter(fh, fieldnames=list(out[0])); w.writeheader(); w.writerows(out)

eq_spoc = [r for r in rows if cat(r) == 'equal-dips' and tce(r)]
print(f'Equal-dip SPOC rows with a TCE tag: {len(eq_spoc)}; TCE period = 2x adopted: {len(out)}')
pcat = [r for r in rows if cat(r) == 'P' and tce(r)]
print(f'For comparison, rows with a secondary at P: {sum(tce(r)=="Pc/2" for r in pcat)} of {len(pcat)} have TCE = 2x adopted')
for o in out: print(' ', o['review_id'], o['tier'], o['adopted_period_d'], '->', o['tce_period_d'], o['status'])
