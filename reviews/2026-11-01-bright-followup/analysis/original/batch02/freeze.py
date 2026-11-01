"""Validate exact queue/result/report coverage and write relative SHA256 manifest."""
import csv
import hashlib
import json
import os
from pathlib import Path

B = Path(__file__).resolve().parent
q = list(csv.DictReader(open(B / 'queue.csv', newline='')))
r = list(csv.DictReader(open(B / 'RESULTS.csv', newline='')))
qt = [x['tic'] for x in q]
rt = [x['tic'] for x in r]
assert len(qt) == len(set(qt)) == 10
assert rt == qt
assert all((B / x['report']).is_file() for x in r)
assert all(x['full_review_completion'] == 'complete' for x in r)
assert sum(x['physical_verdict'] == 'confirmed' for x in r) == 8
assert {x['tic'] for x in r if x['physical_verdict'] == 'probable'} == {'251731963', '409852500'}
for x in r:
    m = json.load(open(B / x['tic'] / 'measurements.json'))
    for field in ('period_days', 'period_error_days', 'primary_epoch_btjd', 'depth_ppt'):
        assert abs(float(x[field]) - m[field]) <= 0.51 * 10 ** (-len(x[field].split('.')[1]))

sources = json.load(open(B / 'source-receipts.json'))
paths = {p for p in B.rglob('*') if p.is_file() and p.name != 'SHA256SUMS.json'}
for entries in sources.values():
    for entry in entries:
        p = (B / entry['path']).resolve()
        assert p.is_file()
        paths.add(p)

def digest(p):
    h = hashlib.sha256()
    with open(p, 'rb') as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b''):
            h.update(chunk)
    return h.hexdigest()

manifest = {Path(os.path.relpath(p, B)).as_posix(): digest(p) for p in sorted(paths)}
for entries in sources.values():
    for entry in entries:
        assert manifest[entry['path']] == entry['sha256']
(B / 'SHA256SUMS.json').write_text(json.dumps(manifest, indent=2))
print('Validated', len(qt), 'queue rows, result/report coverage, numeric fields; hashed', len(manifest), 'artifacts and sources')
