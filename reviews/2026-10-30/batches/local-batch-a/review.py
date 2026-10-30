import json,csv
import numpy as np
from pathlib import Path
p=Path(__file__).parent
r=json.load(open(p/'receipts.json')); e=json.load(open(p/'events.json')); out=[]
cat={x['tic']:x for x in r['batch_candidates.csv']}
for row in r['search.jsonl']:
 tic=row['tic']; a=[x for x in e if x['tic']==tic]; m=[x for x in a if x['status']=='measured']; d=[x['depth_ppt'] for x in m]
 assert abs(row['P']['P']-float(cat[tic]['period_d']))<0.0000051
 assert row['P']['z']>=row['P2']['z']
 o=dict(tic=tic,windows=len(a),measured=len(m),insufficient=len(a)-len(m),median_ppt=float(np.median(d)),min_ppt=min(d),max_ppt=max(d),flagged_core_cadences=sum(x['n_core_flagged'] for x in a),measured_near_systematics=[(x['sector'],x['pred_btjd']) for x in m if x['near_systematic']],sectors=sorted(set(x['sector'] for x in a)),used_period=row['P']['P'],csv_period=cat[tic]['period_d'],t0=row['P']['t0'],search_width=row['P']['dur'])
 out.append(o)
json.dump(out,open(p/'review-summary.json','w'),indent=2)
print('Period selection checks pass: all five P win by z and match resolved CSV to rounding.')
print('Window counts',[(x['tic'],x['windows'],x['measured']) for x in out])
