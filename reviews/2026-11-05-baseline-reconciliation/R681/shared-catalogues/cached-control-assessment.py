"""Read-only assessment of batch01 controls for batch02 TIC 150465032."""
import ast
import csv
import hashlib
import json
import urllib.parse
from pathlib import Path

import run_catalogues as c

HERE = Path(__file__).resolve().parent
WORK = HERE.parent.parent
FIRST = WORK / 'shared-catalogues'
OLD = Path('[local-path-redacted]')
TIC = '150465032'


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def func_digest(path, name):
    source = path.read_text(encoding='utf-8')
    fn = next(node for node in ast.parse(source).body if isinstance(node, ast.FunctionDef) and node.name == name)
    return hashlib.sha256(ast.get_source_segment(source, fn).encode()).hexdigest()


def params(url):
    return urllib.parse.parse_qs(urllib.parse.urlsplit(url).query, keep_blank_values=True)


queue = json.loads((HERE / 'queue-lock.json').read_text())
assert digest(Path(queue['queue'])) == queue['sha256']
target = next(r for r in queue['targets'] if r['tic'] == TIC)
assert target['gaia_dr3'] == '5587540216297835136'
parser_first = func_digest(FIRST / 'run_catalogues.py', 'parse_tsv')
parser_second = func_digest(HERE / 'run_catalogues.py', 'parse_tsv')
assert parser_first == parser_second
original_controls = json.loads((OLD / 'service-controls.json').read_text())
original_by_table = {r['table']: r for r in original_controls if r.get('file')}
prior_audit = json.loads((FIRST / 'verification.json').read_text())
assert prior_audit['positive_controls_success'] == 6
prior_by_table = {r['table']: r for r in prior_audit['positive_controls']}
controls = []
for label, table, radius in c.TABLES:
    old = original_by_table[table]
    oldraw = (OLD / old['file']).read_bytes()
    assert c.sha(oldraw) == old['sha256']
    lines = [line for line in oldraw.decode('latin-1').splitlines() if line and not line.startswith('#')]
    header = [x.strip() for x in lines[0].split('\t')]
    source = dict(zip(header, [x.strip() for x in lines[3].split('\t')]))
    key = prior_by_table[table]['expected_key']
    value = prior_by_table[table]['expected_value']
    assert source[key].strip() == value.strip()
    receipt = json.loads((FIRST / 'receipts' / f'positive-control-{label}.json').read_text())
    assert receipt['status'] == 'success' and receipt['queue_sha256'] == prior_audit['queue_sha256']
    rawpath = FIRST / receipt['file']
    raw = rawpath.read_bytes()
    assert c.sha(raw) == receipt['sha256'] and len(raw) == receipt['bytes']
    p = params(receipt['url'])
    assert urllib.parse.urlsplit(receipt['url']).netloc == urllib.parse.urlsplit(c.VIZIER).netloc
    assert p['-source'] == [table] and p['-c.rs'] == [str(radius)]
    assert p['-c'] == [source['RAJ2000'] + ' ' + source['DEJ2000']]
    assert p['-out.max'] == ['100'] and p['-out.add'] == ['_r']
    found = c.parse_tsv(raw, table)
    assert any(row.get(key, '').strip() == value.strip() for row in found)
    assert prior_by_table[table]['status'] == 'success'
    fresh = json.loads((HERE / 'receipts' / f'positive-control-{label}.json').read_text())
    assert fresh['status'] == 'unavailable' and 'file' not in fresh
    controls.append({'catalogue': label, 'table': table, 'radius_arcsec': radius,
                     'expected_key': key, 'expected_value': value, 'rows': len(found),
                     'raw_sha256': receipt['sha256'], 'batch01_status': 'success',
                     'batch02_fresh_status': 'unavailable'})

results = json.loads((HERE / 'catalogue-results.json').read_text())
target_rows = [r for r in results if r.get('tic') == TIC]
assert len(target_rows) == len(c.TABLES)
target_queries = []
for (label, table, radius), row in zip(c.TABLES, target_rows):
    assert row['catalogue'] == label and row['table'] == table and row['status'] == 'success'
    receipt = json.loads((HERE / row['receipt']).read_text())
    assert receipt['status'] == 'success' and receipt['queue_sha256'] == queue['sha256']
    assert receipt['body'] is None
    raw = (HERE / receipt['file']).read_bytes()
    assert c.sha(raw) == receipt['sha256'] and len(raw) == receipt['bytes']
    p = params(receipt['url'])
    assert p['-source'] == [table] and p['-c.rs'] == [str(radius)]
    assert p['-c'] == [f"{target['ra']} {target['dec']}"]
    assert p['-out.max'] == ['100'] and p['-out.add'] == ['_r'] and '-out.all' in p
    parsed = c.parse_tsv(raw, table)
    assert parsed == row['rows'] == [], (label, parsed)
    target_queries.append({'catalogue': label, 'radius_arcsec': radius,
                           'target_rows': len(parsed), 'raw_sha256': receipt['sha256']})

bulk = {r['catalogue']: r for r in results if not r.get('tic')}
for label in ('gaia_eb', 'gaia_summary', 'gaia_nss', 'simbad'):
    row = bulk[label]
    receipt = json.loads((HERE / row['receipt']).read_text())
    assert row['status'] == receipt['status'] == 'success'
    assert receipt['queue_sha256'] == queue['sha256']
    assert c.sha((HERE / receipt['file']).read_bytes()) == receipt['sha256']
assert any(r['source_id'] == target['gaia_dr3'] for r in bulk['gaia_nss']['rows'])
assert not any(r.get('source_id') == target['gaia_dr3'] for r in bulk['gaia_eb']['rows'])
assert not any(r.get('source_id') == target['gaia_dr3'] for r in bulk['gaia_summary']['rows'])
assert any(r['id'] == 'Gaia DR3 ' + target['gaia_dr3'] for r in bulk['simbad']['rows'])

tm = json.loads((HERE / 'tarrants-mendes-overlaps.json').read_text())
cross = Path(tm['source']['path'])
primary = Path(tm['primary_html_exact_gaia_check']['path'])
assert digest(cross) == tm['source']['sha256']
assert digest(primary) == tm['primary_html_exact_gaia_check']['sha256']
assert tm['targets'][TIC] is None and tm['primary_html_exact_gaia_check']['matches'] == []
source_text = primary.read_text(encoding='utf-8', errors='replace')
assert TIC not in source_text and target['gaia_dr3'] not in source_text
hb = json.loads((HERE / 'heartbeat-overlaps.json').read_text())
assert hb['targets'][TIC] == []
assert all(digest(Path(s['path'])) == s['sha256'] for s in hb['sources'])
chop = json.loads((HERE / 'chopard-overlaps.json').read_text())
assert chop['targets'][TIC] == []
assert all(digest(Path(s['path'])) == s['sha256'] for s in chop['sources'])
matrix = {r['tic']: r for r in csv.DictReader((HERE / 'coverage-matrix.csv').open(encoding='utf-8', newline=''))}
assert matrix[TIC]['coverage_complete'] == 'True'
assert matrix[TIC]['scoped_prior_eb_status'] == 'no identified prior EB in queried scope'

assessment = {'result': 'adequate for TIC 150465032 bounded catalogue novelty gate only',
              'queue_sha256': queue['sha256'], 'tic': TIC, 'gaia_dr3': target['gaia_dr3'],
              'parser_source_sha256': parser_second, 'same_parser_as_batch01': True,
              'cached_batch01_positive_controls': controls, 'batch02_fresh_controls_success': 0,
              'target_cone_queries': target_queries, 'bulk_gaia_simbad_receipts_verified': 4,
              'tarrants_mendes': 'cached same-parent cross-match and original HTML exact TIC/Gaia scan: no overlap',
              'heartbeat': 'nine locally cached sources: no exact TIC overlap',
              'chopard': 'cached public v1.2.0: no exact TIC/Gaia overlap; embargoed identities unknown',
              'limits': 'bounded scoped nonidentification, not exhaustive literature clearance; no physical verdict',
              'other_targets': '24668377 known prior EB; 331650047, 384744604, 109560492 incomplete scoped queries'}
(HERE / 'cached-control-assessment.json').write_text(json.dumps(assessment, indent=2) + '\n', encoding='utf-8')
print(json.dumps({'result': assessment['result'], 'cached_controls': len(controls),
                  'target_successful_cones': len(target_queries), 'fresh_controls_success': 0}))
