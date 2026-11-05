"""Coordinator verification without rewriting any worker evidence."""
from pathlib import Path
import csv,hashlib,json,urllib.parse
W=Path(__file__).resolve().parent;OLD=W.parent/'toward1000-2026-11-03';C=W/'catalogue-recovery'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
def rows(p):return list(csv.DictReader(p.open(encoding='utf-8-sig')))
manifest=json.loads((C/'SHA256SUMS.json').read_text());checked=0
for path,h in manifest.items():assert sha(C/path)==h,path;checked+=1
physical={}
for batch in ['batch02','batch03']:
 b=OLD/batch;v=json.loads((b/'root-verification.json').read_text())
 assert sha(b/'RESULTS.csv')==v['results_sha256']
 assert sha(b/'SHA256SUMS.json')==v['manifest_sha256']
 # Prior physical review accepted hashes are unchanged; all deciding artifacts checked.
 m=json.loads((b/'SHA256SUMS.json').read_text())
 for p,h in m.items():assert sha(b/p)==h,p
 rr=rows(b/'RESULTS.csv');q=rows(b/'queue.csv');assert [r['tic'] for r in rr]==[r['tic'] for r in q]
 cats={r['tic']:r for r in rows(C/batch/'coverage-matrix.csv')}
 assert set(cats)=={r['tic'] for r in rr}
 for r in rr:
  c=cats[r['tic']];assert c['coverage_complete']=='True'
  assert json.loads(c['nearby_eb_identity_alerts_under_5arcsec'])==[]
  assert all(x=='success' for x in json.loads(c['catalogue_statuses']).values())
 physical[batch]=dict(results_sha256=v['results_sha256'],manifest_sha256=v['manifest_sha256'],verified_physical_artifacts=len(m),rows=[dict(tic=r['tic'],verdict=r['physical_verdict'],novelty=cats[r['tic']]['scoped_prior_eb_status']) for r in rr])
for batch in ['batch02','batch03','c57']:
 b=C/batch;lock=json.loads((b/'queue-lock.json').read_text());assert sha(Path(lock['queue']))==lock['sha256']
 for p in (b/'receipts').glob('*.json'):
  r=json.loads(p.read_text());assert r['status']=='success',p
  assert sha(b/r['file'])==r['sha256'],p
  if 'retrieved_url' in r:
   old,new=map(urllib.parse.urlsplit,[r['url'],r['retrieved_url']])
   assert urllib.parse.parse_qs(old.query)==urllib.parse.parse_qs(new.query),p
controls=json.loads((C/'batch02/verification.json').read_text())
assert controls['positive_controls_success']==6
out=dict(result='pass',catalogue_artifacts_verified=checked,physical_reviews=physical,
 catalogue_audit_sha256=sha(C/'audit.json'),catalogue_manifest_sha256=sha(C/'SHA256SUMS.json'),
 eligible_newly_cleared_tics=['331650047','384744604','109560492','167197264'],
 retained_prior_tics=['24668377','155346713'],note='Root accepts catalogue evidence. Explicit identity-level acceptance to be recorded separately; C57 physical helper gate separate.')
(W/'root-recovery-verification.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out,indent=2))
