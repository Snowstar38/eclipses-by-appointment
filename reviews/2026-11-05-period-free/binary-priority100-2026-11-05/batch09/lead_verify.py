"""Verify fixed queue coverage, result integrity and frozen local/source hashes."""
import csv,hashlib,json
from pathlib import Path
B=Path(__file__).resolve().parent
q=list(csv.DictReader((B/'queue.csv').open(newline='',encoding='utf-8')))
r=list(csv.DictReader((B/'RESULTS.csv').open(newline='',encoding='utf-8')))
assert [x['sample_id'] for x in q]==[x['sample_id'] for x in r]==[f'T{i:03d}' for i in range(81,91)]
assert [x['tic'] for x in q]==[x['tic'] for x in r]
assert all(x['full_review_completion']=='COMPLETE' and Path(x['report']).is_file() for x in r)
assert all((B/x['tic']/'lead-numeric.json').is_file() for x in r)
assert next(x for x in r if x['sample_id']=='T086')['novelty_status']=='KNOWN'
assert set(x['physical_verdict'] for x in r)<={'CONFIRMED','PROBABLE','PLAUSIBLE','REFUTED'}
source_count=0
for x in r:
 n=json.loads((B/x['tic']/'lead-numeric.json').read_text())
 for s in n['sources']:
  assert hashlib.sha256(Path(s['path']).read_bytes()).hexdigest()==s['sha256']
  source_count+=1
m=json.loads((B/'SHA256SUMS.json').read_text())['files']
for name,digest in m.items():assert hashlib.sha256((B/name).read_bytes()).hexdigest()==digest,name
assert set(m)=={str(p.relative_to(B)).replace('\\','/') for p in B.rglob('*') if p.is_file() and p.name not in ('SHA256SUMS.json','ROOT-ACCEPTANCE.json') and '__pycache__' not in p.parts}
print(json.dumps({'result_rows':len(r),'queue_first':q[0]['sample_id'],'queue_last':q[-1]['sample_id'],'verified_source_fits':source_count,'verified_local_files':len(m),'verdict_counts':{v:sum(x['physical_verdict']==v for x in r) for v in ('CONFIRMED','PROBABLE','PLAUSIBLE','REFUTED')}},indent=2))
