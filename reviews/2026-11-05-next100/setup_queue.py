"""Freeze the next untouched hundred from the original priority ranking."""
from pathlib import Path
import csv
import hashlib
import json

W = Path(__file__).resolve().parent
P = W.parent / 'binary-prioritization-2026-11-05' / 'ranked-remaining.csv'
CAMPAIGNS = [
    W.parent / 'binary-review100-2026-11-04' / 'accepted-results.csv',
    W.parent / 'binary-priority100-2026-11-05' / 'accepted-results.csv',
    W.parent / 'binary-next10-2026-11-05' / 'accepted-results.csv',
    W.parent / 'binary-next40-2026-11-05' / 'accepted-results.csv',
]
LEDGER = W.parent / 'binary-claim-review-2026-11-05' / 'accepted-ledger.csv'

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def read(path):
    with path.open(encoding='utf8', newline='') as f:
        return list(csv.DictReader(f))

def write(path, rows):
    with path.open('w', encoding='utf8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)

ranked = read(P)
completed_rows = [r for path in CAMPAIGNS for r in read(path)]
ledger_rows = read(LEDGER)
assert len(ranked) == 2804
assert len(completed_rows) == 250
completed = {r['tic'] for r in completed_rows}
assert len(completed) == 250
assert {int(r['priority_rank']) for r in ranked if r['tic'] in completed} == set(range(1, 151))
assert len({r['tic'] for r in ranked}) == 2804
ledger_tics = {r['tic'] for r in ledger_rows if r['tic']}
selected = [dict(r) for r in ranked if 151 <= int(r['priority_rank']) <= 250]
assert len(selected) == 100
assert [int(r['priority_rank']) for r in selected] == list(range(151, 251))
assert not ({r['tic'] for r in selected} & completed)
assert not ({r['tic'] for r in selected} & ledger_tics)
selected_gaia = {r['gaia_dr3'] for r in selected if r['gaia_dr3']}
completed_gaia = {r['gaia_dr3'] for r in ranked if r['tic'] in completed and r['gaia_dr3']}
ledger_gaia = {r['gaia_dr3'] for r in ledger_rows if r['gaia_dr3']}
assert len(selected_gaia) == 100
assert not (selected_gaia & completed_gaia)
assert not (selected_gaia & ledger_gaia)
for i, row in enumerate(selected, 1):
    row.update(sample_id=f'Q{i:03}', sample_stratum=row['priority_group'], batch=f'batch{(i-1)//10+1:02}')
write(W / 'queue.csv', selected)
batch_hashes = {}
for n in range(1, 11):
    batch = W / f'batch{n:02}'
    batch.mkdir(exist_ok=True)
    write(batch / 'queue.csv', selected[(n-1)*10:n*10])
    batch_hashes[batch.name] = sha(batch / 'queue.csv')
seal = {
    'selection': 'Exact original priority ranks 151-250; no substitutions; outcome-informed descriptive priority, not a random or calibrated sample.',
    'selected': 100,
    'parent_rows': 2804,
    'previously_accepted': 250,
    'remaining_before': 2654,
    'remaining_after_if_completed': 2554,
    'rank_span': [151, 250],
    'excluded_completed_tics': sorted(completed, key=int),
    'excluded_current_ledger_tics': sorted(ledger_tics, key=int),
    'selected_ledger_tic_overlap': [],
    'selected_ledger_gaia_overlap': [],
    'source_sha256': {str(path): sha(path) for path in [P, *CAMPAIGNS, LEDGER]},
    'queue_sha256': sha(W / 'queue.csv'),
    'batch_sha256': batch_hashes,
}
(W / 'queue-seal.json').write_text(json.dumps(seal, indent=2) + '\n', encoding='utf8')
print(json.dumps({'selected': len(selected), 'completed_excluded': len(completed), 'ledger_tics': len(ledger_tics), 'queue_sha256': seal['queue_sha256']}, indent=2))
