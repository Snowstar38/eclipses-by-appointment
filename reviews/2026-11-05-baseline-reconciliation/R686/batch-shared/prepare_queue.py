"""Freeze a bounded next appointment queue before target-specific review."""
import csv
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
CAMPAIGN = HERE.parent
SEARCH = CAMPAIGN / 'search256'
IDS = ('167197264', '155346713')
REASONS = {
    '167197264': 'Two broad same-kind minima in frozen latest-three screen; eclipse versus tidal/heartbeat morphology unresolved; older sectors may test recurrence.',
    '155346713': 'Frozen screen had one deep A-like event; separate adaptive older-sector check found target-centered B-like box and truncated A-like ingress; period unresolved.',
}
def sha(path): return hashlib.sha256(path.read_bytes()).hexdigest()
targets = json.loads((SEARCH / 'fresh-targets-256.json').read_text())
triage = {r['tic']: r for r in csv.DictReader((SEARCH / 'triage' / 'triage.csv').open())}
screen_lines = {r['tic']: line for line in (SEARCH / 'screening.jsonl').read_bytes().splitlines(keepends=True)
                if (r := json.loads(line))['tic'] in IDS}
downloads = json.loads((SEARCH / 'downloads.json').read_text())
source_files = ['fresh-preregister-256.json', 'fresh-targets-256.json', 'screening.jsonl', 'downloads.json']
source_hashes = {str(SEARCH / name): sha(SEARCH / name) for name in source_files}
for path in (SEARCH / 'triage' / 'triage.csv', CAMPAIGN / 'coverage-study' / 'coverage.csv',
             SEARCH / 'followups' / 'HANDOFF-155346713.md', SEARCH / 'followups' / 'SHA256SUMS-155346713.json'):
    source_hashes[str(path)] = sha(path)
rows = []
manifest = {'selection': 'Two retained appointment leads, fixed before batch03 full review; no physical or novelty acceptance implied',
            'source_sha256': source_hashes, 'targets': {}}
for i, tic in enumerate(IDS, 1):
    t = targets[tic]
    g = t['gaia']
    tri = triage[tic]
    original = [r for r in downloads if r['tic'] == tic and r['status'] == 'ok']
    assert len(original) == 3
    raw = []
    for r in original:
        p = Path(r['file'])
        assert sha(p) == r['sha256']
        raw.append({'sector': r['sector'], 'path': str(p), 'sha256': r['sha256'], 'uri': r['uri']})
    screen_plot = SEARCH / 'triage' / tri['screen_plot']
    manifest['targets'][tic] = {
        'gaia_source_id': g['source_id'], 'screening_jsonl_line_sha256': hashlib.sha256(screen_lines[tic]).hexdigest(),
        'triage_row': tri, 'raw_fits': raw, 'screen_plot': {'path': str(screen_plot), 'sha256': sha(screen_plot)},
        'qlp_all_sector_uri': t['qlp_all'],
    }
    rows.append({'queue_index': i, 'batch': 'batch03', 'tic': tic, 'gaia_dr3_source_id': g['source_id'],
                 'ra_deg': g['ra'], 'dec_deg': g['dec'], 'gaia_dr3_g': g['phot_g_mean_mag'],
                 'gaia_nss_type': g['nss_solution_type'], 'gaia_period_days': g['period'],
                 'frozen_triage_disposition': tri['visual_disposition'], 'best_screen_kind': tri['best_kind'],
                 'best_screen_btjd': tri['best_center_btjd'], 'best_screen_depth_ppm': tri['best_depth_ppm'],
                 'original_qlp_sectors': ';'.join(str(r['sector']) for r in original),
                 'selection_reason': REASONS[tic], 'status': 'queued_for_review_not_accepted'})
with (HERE / 'queue.csv').open('w', newline='') as f:
    w = csv.DictWriter(f, fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)
(HERE / 'SOURCE-SNAPSHOT.json').write_text(json.dumps(manifest, indent=2))
seal = {'count': len(rows), 'sha256': sha(HERE / 'queue.csv'), 'source_snapshot_sha256': sha(HERE / 'SOURCE-SNAPSHOT.json')}
(HERE / 'queue-seal.json').write_text(json.dumps(seal, indent=2))
print(json.dumps(seal, indent=2))
