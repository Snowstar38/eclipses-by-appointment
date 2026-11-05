"""Verify the frozen inclusive backlog, exclusions, and full priority ordering.

Run from this directory: python verify_selection.py
The raw FITS and per-target detector results are source-only; this checks the
published score table and deterministic queue construction, not the photons.
"""
import csv
import hashlib
from collections import Counter
from pathlib import Path

W=Path(__file__).resolve().parent
def read(name):
    with (W/name).open(encoding='utf-8-sig',newline='') as f:return list(csv.DictReader(f))
def number(r,k):return float(r[k]) if r[k] else 0.0
def group(r):
    return 'cross_method_dip' if r['period_fold_flag']=='True' and int(r['dip_flag_sectors']) else r['queue_group']
groups=['cross_method_dip','repeat_sector_dip','single_sector_dip','period_fold_only','period_fold_near','brightening_lead']
def strength(r):
    g=group(r)
    if g in groups[:3]:return number(r,'best_dip_contrast')
    if g=='brightening_lead':return number(r,'max_bright_contrast')
    return number(r,'fold_best_z')

allrows=read('all-targets.csv');parent=read('candidate-backlog.csv')
disposition=read('all-parent-dispositions.csv');ranked=read('ranked-remaining.csv')
first100=read('priority-first100.csv');first150=read('priority-first150.csv')
assert len(allrows)==6186 and len(parent)==len(disposition)==2984
assert len({r['tic'] for r in allrows})==6186
assert [r['tic'] for r in allrows if r['queue_group']!='retained_nonflag']==[r['tic'] for r in parent]
assert [r['tic'] for r in parent]==[r['tic'] for r in disposition]
assert Counter(r['disposition'] for r in disposition)=={'historical_identity_exclusion':80,'reviewed_frozen100':100,'ranked_remaining':2804}
eligible=[r for r in parent if r['cached_primary_identity_match']=='False' and r['known_prior_exact_note']!='True']
assert len(eligible)==2904
by_tic={r['tic']:r for r in parent}
assert all((d['disposition']=='historical_identity_exclusion')==(d['tic'] not in {r['tic'] for r in eligible}) for d in disposition)
remaining=[by_tic[d['tic']] for d in disposition if d['disposition']=='ranked_remaining']
remaining.sort(key=lambda r:(groups.index(group(r)),-strength(r),int(r['tic'])))
assert len(remaining)==len(ranked)==2804
assert [r['tic'] for r in remaining]==[r['tic'] for r in ranked]
assert [r['tic'] for r in first100]==[r['tic'] for r in ranked[:100]]
assert [r['tic'] for r in first150]==[r['tic'] for r in ranked[:150]]
for i,r in enumerate(ranked,1):
    assert int(r['priority_rank'])==i and r['priority_group']==group(r)
    assert float(r['within_group_score'])==strength(r)
    assert r['review_batch']==f'P{(i-1)//10+1:03d}'
alt=sorted(remaining,key=lambda r:(groups.index(group(r)),-int(r['dip_flag_sectors']),-strength(r),int(r['tic'])))
alt_rank={r['tic']:i for i,r in enumerate(alt,1)}
assert all(int(r['alternate_sector_first_rank'])==alt_rank[r['tic']] for r in ranked)
seed='astra-priority-exploration-v1'
exploration=read('exploration20.csv');want=[]
for g in groups[2:]:
    pool=[r for r in ranked if group(r)==g]
    chosen=sorted(pool,key=lambda r:hashlib.sha256((seed+'|'+g+'|'+r['tic']).encode()).hexdigest())[:5]
    want.extend(r['tic'] for r in chosen)
assert [r['tic'] for r in exploration]==want
print('PASS: 6186 screened; 2984 inclusive; 80 historical identity exclusions; 100 frozen reviews; 2804 ranked; first 150 and exploration 20 reproduce')
