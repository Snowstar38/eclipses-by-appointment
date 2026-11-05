"""Mechanical validation only; this never grants root scientific acceptance."""
from pathlib import Path
import csv,json,hashlib,sys
from collections import Counter
W=Path(__file__).resolve().parent
b=W/sys.argv[1]
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
lock=json.loads((W/'queue-seal.json').read_text(encoding='utf8'))
assert sha(b/'queue.csv')==lock['batch_sha256'][b.name]
q=list(csv.DictReader((b/'queue.csv').open(encoding='utf8')))
r=list(csv.DictReader((b/'RESULTS.csv').open(encoding='utf8')))
assert len(r)==len(q)==10 and Counter(x['tic'] for x in r)==Counter(x['tic'] for x in q)
lookup={x['tic']:x for x in q}
for x in r:
 assert all(k in x for k in ['sample_id','sample_stratum','physical_verdict','full_review_completion','novelty_status','limitations','next_check','report'])
 for k in ['sample_id','sample_stratum']: assert x[k]==lookup[x['tic']][k],(x['tic'],k)
 assert Path(x['report']).is_file(),x['report']
 assert x['full_review_completion'] in ['COMPLETE','INCOMPLETE']
 assert x['physical_verdict'] in ['CONFIRMED','PROBABLE','PLAUSIBLE','REFUTED','NON_ECLIPSE_VARIABLE','UNRESOLVED']
 assert x['novelty_status'] and x['limitations']
manifest=b/'SHA256SUMS.json';m=json.loads(manifest.read_text(encoding='utf8'));files=m.get('files',m)
assert isinstance(files,dict)
for name,h in files.items():
 p=Path(name)
 if not p.is_absolute():p=b/p
 assert p.is_file(),str(p)
 assert sha(p)==h,str(p)
 if p.suffix.lower() in ['.md','.json','.csv','.py','.txt']:
  text=p.read_text(encoding='utf8')
  assert '\ufffd' not in text,('replacement character in UTF8 text',str(p))
out={'batch':b.name,'rows':len(r),'verdicts':dict(Counter(x['physical_verdict'] for x in r)),
 'completion':dict(Counter(x['full_review_completion'] for x in r)),
 'queue_sha256':sha(b/'queue.csv'),'results_sha256':sha(b/'RESULTS.csv'),
 'manifest_sha256':sha(manifest),'manifest_files':len(files),'mechanical_validation':'pass',
 'root_scientific_acceptance':'not conferred by this script'}
print(json.dumps(out,indent=2))
