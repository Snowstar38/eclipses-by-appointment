"""Collect only root-accepted batch results; never infer acceptance from files."""
import csv, json
from pathlib import Path
from collections import Counter

ROOT = Path(__file__).resolve().parent
queue = list(csv.DictReader((ROOT/'queue.csv').open(encoding='utf-8-sig')))
positions = {r['tic']: int(r['position']) for r in queue}
rows = []
for rel in json.loads((ROOT/'accepted-batches.json').read_text()):
    source = ROOT/rel
    assert source.resolve().is_relative_to(ROOT)
    batch = list(csv.DictReader(source.open(encoding='utf-8-sig')))
    assert len(batch) == 10 and len({r['tic'] for r in batch}) == 10
    for r in batch:
        tic = r['tic']
        report = Path(r['report']) if r.get('report') else source.parent/f'TIC-{tic}.md'
        if not report.is_absolute(): report = source.parent/report
        assert report.is_file() and report.resolve().is_relative_to(ROOT), report
        assert r['physical_verdict'] in ('CONFIRMED', 'PLAUSIBLE', 'REFUTED')
        rows.append(dict(position=positions[tic], tic=tic,
            physical_verdict=r['physical_verdict'],
            full_review_completion=r.get('full_review_completion') or r.get('execution_completion', ''),
            novelty_status=r['novelty_status'], report=report.relative_to(ROOT).as_posix(),
            batch_source=rel, next_check=r.get('next_check', 'See target report for limitations.')))
assert len(rows) == len({r['tic'] for r in rows})
rows.sort(key=lambda r:r['position'])
with (ROOT/'FULL-RESULTS.csv').open('w', newline='', encoding='utf-8') as f:
    w = csv.DictWriter(f, fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)
counts = dict(Counter(r['physical_verdict'] for r in rows))
(ROOT/'accepted-counts.json').write_text(json.dumps(dict(accepted=len(rows), verdicts=counts), indent=2)+'\n')
print(json.dumps(dict(accepted=len(rows), verdicts=counts)))
