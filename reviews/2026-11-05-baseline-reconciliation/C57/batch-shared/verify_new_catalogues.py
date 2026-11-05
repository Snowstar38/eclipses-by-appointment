"""Root exact-coverage and immutable-receipt audit of completed catalogue passes."""
import csv,hashlib,json
from pathlib import Path
W=Path(__file__).resolve().parent
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
summary=[]
for rel,expected in [('resolved125/shared-catalogues',12),('next256/catalogue-recovery-20261105T0117',21)]:
    p=W/rel; manifest=json.loads((p/'SHA256SUMS.json').read_text(encoding='utf-8'))
    for path,digest in manifest.items():
        f=Path(path);f=f if f.is_absolute() else p/f
        assert sha(f)==digest,str(f)
    rows=list(csv.DictReader((p/'coverage-matrix.csv').open(encoding='utf-8-sig')))
    queue=list(csv.DictReader((p/'queue.csv').open(encoding='utf-8-sig')))
    assert len(rows)==len(queue)==expected and len({r['tic'] for r in rows})==expected
    assert {r['tic'] for r in rows}=={r['tic'] for r in queue}
    assert all(r['coverage_complete']=='True' for r in rows)
    summary.append({'folder':rel,'targets':expected,'manifest_files':len(manifest),'manifest_sha256':sha(p/'SHA256SUMS.json'),'matrix_sha256':sha(p/'coverage-matrix.csv'),'statuses':{r['tic']:r['scoped_prior_eb_status'] for r in rows}})
(W/'root-new-catalogue-verification.json').write_text(json.dumps(summary,indent=2)+'\n',encoding='utf-8')
print(json.dumps(summary,indent=2))
