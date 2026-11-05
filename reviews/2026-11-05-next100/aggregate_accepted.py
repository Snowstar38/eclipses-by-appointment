"""Aggregate only root-accepted hash-bound decisions; pending never means refuted."""
from pathlib import Path
from collections import Counter
import csv,json,hashlib
W=Path(__file__).resolve().parent
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
lock=json.loads((W/'queue-seal.json').read_text(encoding='utf8'))
assert sha(W/'queue.csv')==lock['queue_sha256']
rows=[];accepted=[]
for batch,h in lock['batch_sha256'].items():
 b=W/batch;assert sha(b/'queue.csv')==h
 if not (b/'ROOT-ACCEPTANCE.json').exists():continue
 a=json.loads((b/'ROOT-ACCEPTANCE.json').read_text(encoding='utf8'));assert a['accepted'] is True
 for p,key in [('queue.csv','queue_sha256'),('RESULTS.csv','results_sha256'),('SHA256SUMS.json','manifest_sha256')]:assert sha(b/p)==a[key]
 rs=list(csv.DictReader((b/'RESULTS.csv').open(encoding='utf8')));q=list(csv.DictReader((b/'queue.csv').open(encoding='utf8')))
 assert len(rs)==10 and {r['tic'] for r in rs}=={r['tic'] for r in q}
 assert all(r['full_review_completion']=='COMPLETE' for r in rs)
 for r in rs:r['batch']=batch
 rows+=rs;accepted.append(batch)
assert len(rows)==len({r['tic'] for r in rows})
summary={'selected':100,'root_accepted_complete':len(rows),'pending':100-len(rows),'accepted_batches':accepted,'verdicts':dict(Counter(r['physical_verdict'] for r in rows)),'novelty':dict(Counter(r['novelty_status'] for r in rows)),'original_priority_ranks':[151,250],'remaining_after_selected100':2554,'caveat':'Outcome-informed priority selection; not a random sample, calibrated ranker or survey yield. Novelty remains separate from physical outcome.'}
(W/'accepted-summary.json').write_text(json.dumps(summary,indent=2)+'\n',encoding='utf8')
if rows:
 with (W/'accepted-results.csv').open('w',encoding='utf8',newline='') as f:
  writer=csv.DictWriter(f,fieldnames=list(rows[0]));writer.writeheader();writer.writerows(rows)
print(json.dumps(summary,indent=2))
