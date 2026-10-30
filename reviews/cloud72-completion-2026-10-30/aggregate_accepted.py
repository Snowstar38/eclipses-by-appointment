"""Verify and aggregate only root-accepted Cloud completion batches."""
from pathlib import Path
import csv,json,hashlib
from collections import Counter
ROOT=Path(__file__).parent
queue=list(csv.DictReader((ROOT/'queue.csv').open(encoding='utf-8-sig')))
byid={r['tic']:r for r in queue}; result=[]; audit=[]
for name in json.loads((ROOT/'accepted-batches.json').read_text()):
    base=ROOT/name
    manifest=json.loads((base/'manifest.json').read_text(encoding='utf-8'))
    files=manifest['files'] if isinstance(manifest,dict) else manifest
    for item in files:
        p=base/item['path']
        assert p.resolve().is_relative_to(base)
        assert hashlib.sha256(p.read_bytes()).hexdigest()==item['sha256'],p
    rows=list(csv.DictReader((base/'RESULTS.csv').open(encoding='utf-8-sig')))
    expected={r['tic'] for r in queue if r['batch']==name}
    assert len(rows)==len(expected) and {r['tic'] for r in rows}==expected
    for row in rows:
        p=Path(row['report'])
        if not p.is_absolute():
            p=(ROOT/p) if (ROOT/p).is_file() else (base/p)
        assert p.is_file() and p.resolve().is_relative_to(ROOT)
        assert row['physical_verdict'] in {'CONFIRMED','PROBABLE','PLAUSIBLE','REFUTED','BY-CATCH'}
        result.append(dict(queue_position=int(byid[row['tic']]['queue_position']),tic=row['tic'],physical_verdict=row['physical_verdict'],full_review_completion=row['full_review_completion'],novelty_status=row['novelty_status'],report=p.relative_to(ROOT).as_posix(),next_check=row.get('next_check','See report.'),batch=name))
    audit.append(dict(batch=name,rows=len(rows),hashes_verified=len(files)))
assert len(result)==len({r['tic'] for r in result})
result.sort(key=lambda r:r['queue_position'])
with (ROOT/'FULL-RESULTS.csv').open('w',newline='',encoding='utf-8') as f:
    w=csv.DictWriter(f,list(result[0]));w.writeheader();w.writerows(result)
counts=dict(accepted=len(result),verdicts=dict(Counter(r['physical_verdict'] for r in result)),batch_audit=audit)
(ROOT/'accepted-counts.json').write_text(json.dumps(counts,indent=2)+'\n',encoding='utf-8')
print(json.dumps(counts))
