from pathlib import Path
import csv, json, hashlib
from collections import Counter

W=Path(__file__).resolve().parent
H=W.parent/'binary-exploration-2026-11-04'
source=H/'candidate-backlog.csv'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
seed='astra-review100-2026-11-04-stratified-v1'
allocation={'cross_method_dip':30,'repeat_sector_dip':20,'single_sector_dip':20,'period_fold_only':10,'brightening_lead':10,'period_fold_near':10}
rows=list(csv.DictReader(source.open(encoding='utf8')))
eligible=[r for r in rows if r['cached_primary_identity_match']=='False' and r['known_prior_exact_note']!='True']
assert len(eligible)==2904
for r in eligible:
 r['sample_stratum']='cross_method_dip' if r['period_fold_flag']=='True' and int(r['dip_flag_sectors']) else r['queue_group']
 r['selection_hash']=hashlib.sha256((seed+'|'+r['sample_stratum']+'|'+r['tic']).encode()).hexdigest()
sample=[]
for group,n in allocation.items():
 pool=sorted([r for r in eligible if r['sample_stratum']==group],key=lambda r:(r['selection_hash'],int(r['tic'])))
 for r in pool[:n]:
  r.update(sample_id=f'H{len(sample)+1:03d}',batch=f'batch{len(sample)//10+1:02d}',stratum_population=len(pool),stratum_sample=n)
  sample.append(r)
assert len(sample)==len({r['tic'] for r in sample})==100
fields=list(sample[0])
def write_csv(path,rs):
 with path.open('w',encoding='utf8',newline='') as f:
  out=csv.DictWriter(f,fieldnames=fields);out.writeheader();out.writerows(rs)
write_csv(W/'queue.csv',sample)
for i in range(10):
 p=W/f'batch{i+1:02d}';p.mkdir(exist_ok=True)
 write_csv(p/'queue.csv',sample[i*10:(i+1)*10])
lock={'seed':seed,'selection':'lowest SHA256(seed|stratum|TIC), no replacement; fixed allocation before reviewing sample',
 'source':str(source),'source_sha256':sha(source),'queue_sha256':sha(W/'queue.csv'),
 'eligible_population':len(eligible),'stratum_populations':dict(Counter(r['sample_stratum'] for r in eligible)),
 'allocation':allocation,'sample_n':100,'batch_sha256':{f'batch{i+1:02d}':sha(W/f'batch{i+1:02d}'/'queue.csv') for i in range(10)},
 'inference':'Stratum-specific review yields only. Mixed sample oversamples some groups. Not survey completeness, false-alarm probability or occurrence. Unknown/incomplete retained in denominator and reported separately.',
 'identifiers':'H001-H100 local sample identifiers. No R-series IDs assigned by this selection.'}
(W/'queue-seal.json').write_text(json.dumps(lock,indent=2)+'\n',encoding='utf8')
print(json.dumps(lock,indent=2))
