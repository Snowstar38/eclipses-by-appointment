"""Validate exact batch07 coverage and make a SHA-256 manifest after helper freeze."""
import csv
import hashlib
import json
from pathlib import Path

B = Path(__file__).resolve().parent
P = B.parent

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

queue = list(csv.DictReader((B / 'queue.csv').open(newline='', encoding='utf-8')))
rows = list(csv.DictReader((B / 'RESULTS.csv').open(newline='', encoding='utf-8')))
assert len(queue) == len(rows) == 10
assert [(q['sample_id'], q['tic']) for q in queue] == [(r['sample_id'], r['tic']) for r in rows]
seal = json.loads((P / 'queue-seal.json').read_text())
assert sha(B / 'queue.csv') == seal['batch_sha256']['batch07']
assert all(q['batch'] == 'batch07' and q['sample_stratum'] == 'single_sector_dip' for q in queue)
assert all(r['full_review_completion'] == 'COMPLETE' and r['novelty_status'] == 'UNKNOWN' for r in rows)

for q, r in zip(queue, rows):
    d = B / q['tic']
    assert Path(r['report']).resolve() == (d / 'REPORT.md').resolve()
    assert (d / 'REPORT.md').is_file() and (d / 'raw-inspection.json').is_file()
    assert (d / 'source-receipt.json').is_file()
    source = json.loads((d / 'source-receipt.json').read_text())
    assert source['sample_id'] == q['sample_id'] and source['tic'] == q['tic']
    assert sha(Path(source['bulk_json'])) == source['bulk_json_sha256']
    assert sha(Path(source['source_packet'])) == source['source_packet_sha256']
    for fit in source['verified_qlp_fits']:
        assert sha(Path(fit['path'])) == fit['sha256']
    for rec in source.get('new_cutout_receipts', []):
        assert sha(d / f"s{rec['sector']}-tesscut.raw") == rec['response_sha256']
        assert sha(d / f"s{rec['sector']}-tesscut.fits") == rec['fits_sha256']
    assert r['period_days'] == r['period_error_days'] == r['primary_epoch_btjd'] == r['depth_ppt'] == ''

files = sorted(p for p in B.rglob('*') if p.is_file() and p.name != 'SHA256SUMS.json')
manifest = {'batch': 'batch07', 'queue_sha256': sha(B / 'queue.csv'),
            'files': {p.relative_to(B).as_posix(): sha(p) for p in files}}
(B / 'SHA256SUMS.json').write_text(json.dumps(manifest, indent=2) + '\n', encoding='utf-8')
print('Validated 10 rows,', sum(len(json.loads((B / q['tic'] / 'source-receipt.json').read_text())['verified_qlp_fits']) for q in queue),
      'QLP FITS hashes and', len(files), 'local files')
