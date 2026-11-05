from pathlib import Path
import csv,json,hashlib
W=Path(__file__).resolve().parent;out={}
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
for name in ('catalogue-recovery-full-primary','catalogue-recovery-selected12'):
 O=W/'unmatched512'/name;manifest=json.loads((O/'SHA256SUMS.json').read_text());assert isinstance(manifest,dict)
 for p,d in manifest.items():assert sha(O/p)==d,p
 rows=list(csv.DictReader((O/'coverage-matrix.csv').open(encoding='utf-8-sig')))
 assert len(rows)==58 and len({r['tic'] for r in rows})==58
 assert not any(r['coverage_complete']=='True' for r in rows)
 out[name]=dict(manifest_files=len(manifest),manifest_sha256=sha(O/'SHA256SUMS.json'),matrix_sha256=sha(O/'coverage-matrix.csv'),rows=58,complete_targets=0)
 if name.endswith('selected12'):
  selected={r['tic'] for n in ('review_unmatched10','review_unmatched2') for r in csv.DictReader((W/n/'queue.csv').open())}
  live=json.loads((O/'selected12-live-vsx-results.json').read_text())['results']
  assert {r['tic'] for r in live}==selected and len(live)==12
  assert all(r['status']=='success_scoped_supplement' for r in live)
  out[name]['live_vsx_supplements']=12
(W/'root-unmatched-catalogue-verification.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8');print(json.dumps(out,indent=2))
