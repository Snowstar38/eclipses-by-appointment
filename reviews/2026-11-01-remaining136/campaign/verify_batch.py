"""Root acceptance mechanics; scientific acceptance remains an explicit decision."""
import csv,json,hashlib,sys
from pathlib import Path
W=Path(__file__).resolve().parent
name=sys.argv[1]
b=W/name
baseline=json.loads((W/'baseline.json').read_text(encoding='utf-8-sig'))
assert hashlib.sha256((b/'queue.csv').read_bytes()).hexdigest()==baseline['batch_queue_sha256'][name]
q=list(csv.DictReader((b/'queue.csv').open(encoding='utf-8-sig')))
r=list(csv.DictReader((b/'RESULTS.csv').open(encoding='utf-8-sig')))
assert len(q)==len(r) and len(q) in (6,10)
assert len({x['tic'] for x in r}) == len(q)
assert len(q)==baseline['batch_counts'][name]
assert {x['tic'] for x in q}=={x['tic'] for x in r}
assert all(x['full_review_completion'].upper().startswith('COMPLETE') for x in r)
assert all((Path(x['report']) if Path(x['report']).is_absolute() else b/x['report']).is_file() for x in r)
for n in ['LEAD-AUDIT.md','helper-audit.md']:
    assert (b/n).is_file(), n
manifest=json.loads((b/'SHA256SUMS.json').read_text(encoding='utf-8-sig'))
assert manifest
covered=set()
source_resolutions=[]
for p,h in manifest.items():
    f=Path(p)
    if not f.is_absolute(): f=b/f
    assert f.is_file(),str(f)
    actual=hashlib.sha256(f.read_bytes()).hexdigest()
    if actual!=h and f.resolve()==Path('local-source/Fable 5/made/sb1-scale/search.jsonl').resolve():
        snapshot=W/'source-snapshots/search-original-46fe1791.jsonl'
        assert hashlib.sha256(snapshot.read_bytes()).hexdigest()==h
        source_resolutions.append({'original_path':str(f.resolve()),'verified_snapshot':str(snapshot),'sha256':h,'reason':'Live append-only search log grew; exact original bytes recovered and hash-matched.'})
    else:
        assert actual==h,str(f)
    covered.add(f.resolve())
for x in r:
    report=Path(x['report'])
    if not report.is_absolute(): report=b/report
    assert report.resolve() in covered,('unhashed report',str(report))
out=dict(queue_exact=True,completion=True,verified_hashes=len(manifest),
         immutable_source_resolutions=source_resolutions,
         results_sha256=hashlib.sha256((b/'RESULTS.csv').read_bytes()).hexdigest(),
         manifest_sha256=hashlib.sha256((b/'SHA256SUMS.json').read_bytes()).hexdigest())
print(json.dumps(out,indent=2))
(b/'root-verification.json').write_text(json.dumps(out,indent=2)+'\n')
