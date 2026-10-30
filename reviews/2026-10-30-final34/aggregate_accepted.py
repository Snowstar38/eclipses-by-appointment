"""Validate hashes and exact queue coverage for explicitly root-accepted batches."""
from pathlib import Path
import csv,json,hashlib
from collections import Counter
ROOT=Path(__file__).parent
def read(p):return list(csv.DictReader(p.open(encoding='utf-8-sig')))
queue=read(ROOT/'queue.csv'); byid={r['tic']:r for r in queue}
results=[]; audit=[]
for name in json.loads((ROOT/'accepted-batches.json').read_text()):
    base=ROOT/name
    manifest=json.loads((base/'manifest.json').read_text(encoding='utf-8'))
    files=(manifest['files'] if 'files' in manifest else [dict(path=p,sha256=h) for p,h in manifest.items()]) if isinstance(manifest,dict) else manifest
    if isinstance(files,dict): files=[dict(path=p,sha256=h['sha256'] if isinstance(h,dict) else h) for p,h in files.items()]
    assert files,'No artifact manifest'
    for item in files:
        p=base/item['path']
        assert p.resolve().is_relative_to(ROOT.resolve()) and p.is_file(),p
        assert hashlib.sha256(p.read_bytes()).hexdigest()==item['sha256'],p
    rows=read(base/'RESULTS.csv')
    num=int(name.removeprefix('batch'))
    expected={r['tic'] for r in queue if int(r['batch'])==num}
    assert len(rows)==len(expected) and {r['tic'] for r in rows}==expected
    for row in rows:
        p=Path(row['report'])
        if not p.is_absolute():p=ROOT/p if (ROOT/p).is_file() else base/p
        assert p.is_file() and p.resolve().is_relative_to(ROOT.resolve()),p
        assert row['physical_verdict'] in {'CONFIRMED','PROBABLE','PLAUSIBLE','REFUTED','BY-CATCH'}
        completion=row.get('full_review_completion',row.get('execution_completion',''))
        assert completion, row['tic']
        results.append(dict(position=int(byid[row['tic']]['position']),tic=row['tic'],physical_verdict=row['physical_verdict'],full_review_completion=completion,novelty_status=row['novelty_status'],report=p.relative_to(ROOT).as_posix(),next_check=row.get('next_check','See report.'),batch=name))
    audit.append(dict(batch=name,rows=len(rows),hashes_verified=len(files)))
assert len(results)==len({r['tic'] for r in results})
results.sort(key=lambda r:r['position'])
if results:
    with (ROOT/'FULL-RESULTS.csv').open('w',newline='',encoding='utf-8') as f:
        w=csv.DictWriter(f,list(results[0]));w.writeheader();w.writerows(results)
counts=dict(accepted=len(results),verdicts=dict(Counter(r['physical_verdict'] for r in results)),batch_audit=audit)
(ROOT/'accepted-counts.json').write_text(json.dumps(counts,indent=2)+'\n',encoding='utf-8')
print(json.dumps(counts))
