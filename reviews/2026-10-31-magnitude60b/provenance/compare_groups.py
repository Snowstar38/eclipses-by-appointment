"""Fixed-denominator round and cumulative descriptive comparisons."""
import csv,json,math
from collections import Counter
from pathlib import Path
W=Path(__file__).resolve().parent
def rows(p): return list(csv.DictReader(p.open(encoding='utf-8-sig')))
def wilson(k,n):
    z=1.959963984540054;p=k/n;d=1+z*z/n
    c=(p+z*z/(2*n))/d;r=z*math.sqrt(p*(1-p)/n+z*z/(4*n*n))/d
    return [c-r,c+r]
def summarize(rr,n):
    out={}
    for g in ['11.5-12','12-12.5']:
        group=[r for r in rr if r['magnitude_group']==g]
        assert len(group)==n
        counts=Counter(r['physical_verdict'] for r in group)
        out[g]=dict(selected=n,outcomes=dict(counts),confirmed_fraction=counts['CONFIRMED']/n,
            confirmed_wilson95=wilson(counts['CONFIRMED'],n),
            completed=sum(r['full_review_completion'].startswith('COMPLETE') for r in group),
            new_additions=sum(r['count_addition']=='true' for r in group),
            magnitude_range=[min(float(r['gaia_g']) for r in group),max(float(r['gaia_g']) for r in group)],
            catalogue_statuses=dict(Counter(r['novelty_status'] for r in group)))
    return dict(groups=out,faint_minus_bright_confirmation_fraction=out['12-12.5']['confirmed_fraction']-out['11.5-12']['confirmed_fraction'])
a=rows(W.parent/'magnitude60a-2026-10-31/FULL-RESULTS.csv')
b=rows(W/'FULL-RESULTS.csv');q=rows(W/'queue.csv')
assert len(a)==len(b)==len(q)==60
assert {r['tic'] for r in b}=={r['tic'] for r in q}
assert len({r['tic'] for r in a+b})==120
out={**summarize(b,30),'round1':summarize(a,30),'cumulative':summarize(a+b,60),
    'interpretation': 'Fixed screened-candidate samples, not blind search or completeness. Descriptive Wilson binomial model intervals; finite historical strata, depleted bright pool, crowding and coverage complicate interpretation. Differences need not be caused by magnitude. Known confirmed recoveries count toward physical confirmation, not additions. No target removed from selected denominators.'}
(W/'magnitude-comparison.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
