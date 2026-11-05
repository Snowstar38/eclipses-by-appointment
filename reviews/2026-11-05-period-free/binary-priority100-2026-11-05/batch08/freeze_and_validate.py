"""Validate queue coverage, source identity/hashes and freeze local batch artifacts."""
import csv,hashlib,json
from pathlib import Path
B=Path(__file__).resolve().parent;ROOT=B.parent
q=list(csv.DictReader((B/'queue.csv').open(newline='',encoding='utf-8')))
r=list(csv.DictReader((B/'RESULTS.csv').open(newline='',encoding='utf-8')))
expected=['sample_id','tic','sample_stratum','physical_verdict','full_review_completion','novelty_status','period_days','period_error_days','primary_epoch_btjd','depth_ppt','limitations','next_check','report']
assert list(r[0])==expected
assert len(q)==len(r)==10 and [x['sample_id'] for x in q]==[x['sample_id'] for x in r]
assert [x['tic'] for x in q]==[x['tic'] for x in r]
for a,z in zip(q,r):
 assert z['sample_stratum']==a['sample_stratum'] and z['full_review_completion']=='COMPLETE'
 assert Path(z['report']).resolve()==(B/a['tic']/'REPORT.md').resolve() and Path(z['report']).is_file()
 p=json.loads((ROOT/'source-packets'/a['tic']/'sources.json').read_text(encoding='utf-8'))
 assert p['queue_row']['sample_id']==a['sample_id'] and str(p['target']['gaia']['source_id'])==a['gaia_dr3']
 m=json.loads((B/a['tic']/'lead-numeric.json').read_text(encoding='utf-8'))
 for s in m['sources']:
  assert hashlib.sha256(Path(s['path']).read_bytes()).hexdigest()==s['sha256'],s['path']
 if a['sample_id'] in ('T073','T074','T075','T076','T077','T078','T079','T080'):
  assert any((B/a['tic']).glob('helper-*-receipt.json'))
assert [z['novelty_status'] for z in r].count('KNOWN')==1
files={p.relative_to(B).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(B.rglob('*')) if p.is_file() and p.name!='SHA256SUMS.json'}
(B/'SHA256SUMS.json').write_text(json.dumps({'scope':'batch08','algorithm':'SHA-256','files':files},indent=2)+'\n',encoding='utf-8')
print('Validated exact queue and',len(files),'local artifact hashes')
