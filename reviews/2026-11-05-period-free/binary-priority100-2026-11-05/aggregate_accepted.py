"""Aggregate only explicit root-accepted, hash-locked batch decisions."""
from pathlib import Path
from collections import Counter
import csv,json,hashlib
W=Path(__file__).resolve().parent
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
Q=list(csv.DictReader((W/'queue.csv').open(encoding='utf8')))
seal=json.loads((W/'queue-seal.json').read_text(encoding='utf8'))
assert sha(W/'queue.csv')==seal['queue_sha256']
assert len(Q)==len({r['tic'] for r in Q})==100
lookup={r['tic']:r for r in Q};allrows=[];accepted=[]
for batch,expected in seal['batch_sha256'].items():
 b=W/batch;assert sha(b/'queue.csv')==expected
 ap=b/'ROOT-ACCEPTANCE.json'
 if not ap.exists():continue
 a=json.loads(ap.read_text(encoding='utf8'))
 assert a['accepted'] is True
 assert a['queue_sha256']==expected and sha(b/'RESULTS.csv')==a['results_sha256']
 assert sha(b/'SHA256SUMS.json')==a['manifest_sha256']
 rows=list(csv.DictReader((b/'RESULTS.csv').open(encoding='utf8')))
 bq=list(csv.DictReader((b/'queue.csv').open(encoding='utf8')))
 assert Counter(r['tic'] for r in rows)==Counter(r['tic'] for r in bq)
 for r in rows:
  q=lookup[r['tic']]
  assert r['sample_id']==q['sample_id'] and r['sample_stratum']==q['sample_stratum']
  assert r['full_review_completion'] in ['COMPLETE','INCOMPLETE']
  assert r['physical_verdict'] in ['CONFIRMED','PROBABLE','PLAUSIBLE','REFUTED','NON_ECLIPSE_VARIABLE','UNRESOLVED']
  assert Path(r['report']).exists()
  r['batch']=batch
 allrows.extend(rows);accepted.append(batch)
assert len(allrows)==len({r['tic'] for r in allrows})
groups={}
for group,n in seal['allocation'].items():
 rs=[r for r in allrows if r['sample_stratum']==group]
 complete=[r for r in rs if r['full_review_completion']=='COMPLETE']
 c=Counter(r['physical_verdict'] for r in complete)
 groups[group]={'selected':n,'parent':seal['stratum_populations'][group],'root_accepted':len(rs),'completed':len(complete),'not_yet_complete':n-len(complete),'completed_verdicts':dict(c),
  'confirmed_fraction_of_selected':c['CONFIRMED']/n,'confirmed_or_probable_fraction_of_selected':(c['CONFIRMED']+c['PROBABLE'])/n,
  'fraction_status':'final' if len(complete)==n else 'provisional lower bound; pending not negative'}
out={'selected':100,'root_accepted':len(allrows),'accepted_batches':accepted,'strata':groups,'novelty_status_counts':dict(Counter(r['novelty_status'] for r in allrows)),
 'limitations':'Priority-selected follow-up from cached detector leads, with outcome-informed ordering; not a random sample. Mixed-group count is not a survey-wide rate. Physical confirmation and catalogue novelty separate. No incomplete or pending target treated as a physical rejection.'}
(W/'accepted-summary.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf8')
if allrows:
 fields=list(dict.fromkeys(k for r in allrows for k in r))
 with (W/'accepted-results.csv').open('w',encoding='utf8',newline='') as f:
  wr=csv.DictWriter(f,fieldnames=fields);wr.writeheader();wr.writerows(allrows)
print(json.dumps(out,indent=2))
