"""Descriptive, selected-denominator comparison; not survey completeness."""
import csv, json, math
from collections import Counter
from pathlib import Path

W = Path(__file__).resolve().parent

def wilson(k, n):
    z = 1.959963984540054
    p = k / n
    denom = 1 + z*z/n
    center = (p + z*z/(2*n))/denom
    radius = z*math.sqrt(p*(1-p)/n + z*z/(4*n*n))/denom
    return [center-radius, center+radius]

queue = list(csv.DictReader((W/'queue.csv').open(encoding='utf-8-sig')))
results = {r['tic']:r for r in csv.DictReader((W/'FULL-RESULTS.csv').open(encoding='utf-8-sig'))}
assert set(results) == {r['tic'] for r in queue}
summary = {'groups': {}, 'interpretation': (
    'Fixed screened-candidate samples, not blind search or completeness. '
    'Wilson intervals are descriptive binomial model intervals; actual selection '
    'uses finite historical screening strata. Earlier brightness-ordered reviews '
    'depleted the bright stratum. Differences need not be caused by magnitude. '
    'Known confirmed recoveries count toward physical confirmation, not additions. '
    'No target is removed from the selected denominator.')}
for group in ['11.5-12', '12-12.5']:
    selected = [r for r in queue if r['magnitude_group'] == group]
    rr = [results[r['tic']] for r in selected]
    assert len(rr) == 30
    counts = Counter(r['physical_verdict'] for r in rr)
    k = counts['CONFIRMED']
    summary['groups'][group] = dict(
        selected=30, outcomes=dict(counts), confirmed_fraction=k/30,
        confirmed_wilson95=wilson(k,30),
        completed=sum(r['full_review_completion'].startswith('COMPLETE') for r in rr),
        new_additions=sum(r['count_addition']=='true' for r in rr),
        magnitude_range=[min(float(r['gaia_g']) for r in rr),max(float(r['gaia_g']) for r in rr)],
        catalogue_statuses=dict(Counter(r['novelty_status'] for r in rr)))
summary['faint_minus_bright_confirmation_fraction'] = (
    summary['groups']['12-12.5']['confirmed_fraction'] - summary['groups']['11.5-12']['confirmed_fraction'])
(W/'magnitude-comparison.json').write_text(json.dumps(summary,indent=2)+'\n',encoding='utf-8')
print(json.dumps(summary,indent=2))
