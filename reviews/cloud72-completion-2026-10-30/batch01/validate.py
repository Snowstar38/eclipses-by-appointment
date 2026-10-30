import csv, json, hashlib
from pathlib import Path
from collections import Counter
B=Path(__file__).parent
rows=list(csv.DictReader((B/'RESULTS.csv').open()))
queue=list(csv.DictReader((B/'queue.csv').open()))
assert len(rows)==10 and {r['tic'] for r in rows}=={r['tic'] for r in queue}
assert len({r['tic'] for r in rows})==10
for r in rows:
    p=Path(r['report']); assert p.is_file()
    s=p.read_text(encoding='utf-8')
    assert f"TIC {r['tic']}: {r['physical_verdict']}" in s
    assert all(f'{j}. ' in s for j in range(1,6))
    assert 'Execution is complete' in s or 'full review is complete' in s
receipts=json.loads((B/'raw-evidence/receipt-manifest.json').read_text())
for r in receipts:
    p=B/'raw-evidence'/r['path']; assert p.is_file()
    assert hashlib.sha256(p.read_bytes()).hexdigest()==r['sha256'], p
out=dict(status='pass',unique_targets=10,reports=10,raw_receipt_hashes_checked=len(receipts),counts=dict(Counter(r['physical_verdict'] for r in rows)),known_prior_eb=['300903537'],note='Physical and catalogue verdicts remain separate. 23112764 confirmed target EB with Gaia orbit tension; 465263741 probable host attribution; 10790605 narrow-eclipse interpretation refuted, variability retained.')
(B/'validation.json').write_text(json.dumps(out,indent=2))
manifest=[]
for p in sorted(B.rglob('*')):
    if p.is_file() and p.name!='manifest.json':manifest.append(dict(path=str(p.relative_to(B)).replace('\\','/'),bytes=p.stat().st_size,sha256=hashlib.sha256(p.read_bytes()).hexdigest()))
(B/'manifest.json').write_text(json.dumps(manifest,indent=2))
print(json.dumps(out))
