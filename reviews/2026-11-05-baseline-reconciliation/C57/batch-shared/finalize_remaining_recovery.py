"""Root verifies recovered scope and clearly supersedes copied outage summaries."""
from pathlib import Path
from collections import Counter
import csv,hashlib,json,shutil
W=Path(__file__).resolve().parent;B=W/'remaining_cached/catalogue-recovery-late';S=B.parent/'shared-catalogues'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
original=json.loads((B/'original-manifest.json').read_text())
assert all(sha(S/p)==h for p,h in original.items())
rows=list(csv.DictReader((B/'coverage-matrix.csv').open(encoding='utf-8-sig')))
assert len(rows)==75 and len({r['tic'] for r in rows})==75
assert all(r['coverage_complete']=='True' for r in rows)
receipts={p.stem:json.loads(p.read_text()) for p in (B/'receipts').glob('*.json')}
assert len(receipts)==454 and all(r['status']=='success' for r in receipts.values())
for r in receipts.values():assert sha(B/r['file'])==r['sha256']
for r in rows:
    assert all(v=='success' for v in json.loads(r['catalogue_statuses']).values())
    for table in ['vsx','asassn','prsa2022','ijspeert2024','kostov2025_table3','kostov2025_table4']:
        rec=receipts[r['tic']+'-'+table];assert rec['queue_sha256']==sha(S/'queue.csv')
for name in ['REPORT.md','verification.json','verify.py','missing-checks.csv']:
    if (B/name).exists() and not (B/('pre-recovery-'+name)).exists():shutil.copy2(B/name,B/('pre-recovery-'+name))
counts=dict(Counter(r['scoped_prior_eb_status'] for r in rows))
validation=dict(result='pass',targets=75,successful_receipts=454,recovered_cones=450,status_counts=counts,original_manifest_unchanged=True,controls='Six prior positive controls copied unchanged and already parser-verified in original verification; later exact-ID positive-control probe is availability evidence only.',matrix_sha256=sha(B/'coverage-matrix.csv'),recovery_script_sha256=sha(W/'recover_remaining_catalogues.py'),finalizer_sha256=sha(Path(__file__)))
(B/'verification.json').write_text(json.dumps(validation,indent=2)+'\n',encoding='utf-8')
(B/'REPORT.md').write_text('''# Completed remaining-cached catalogue recovery

All 450 missing or unattempted cone scopes were retrieved successfully after a
later positive-control availability probe. All 75 targets now have complete
scoped coverage. Four original successful Gaia/SIMBAD bulk receipts and six
previously verified positive controls remain unchanged. The root audit checks
454 successful receipt/raw hashes, every target/table key, the exact 75-row
matrix, and preservation of the entire original shared-catalogues folder.

There are 17 known prior EB identities, one unresolved nearby EB identity,
and 57 scoped nonmatches. Three targets had close positional alerts overall;
two also have resolved exact EB identities. A close positional
alert is not silently converted into a confirmed identity or a nonmatch.
Among review_cached10, nine are known prior EBs. TIC 121277143 has an exact
ASAS-SN ROT: classification but no identified prior EB in the queried scope.
Among review_cached5, TIC 257992903 and 380395732 are known; TIC 70561926 has
a VSX EA only 0.30 arcsec away requiring identity resolution; TIC 280950412
and 188908998 have no identified prior EB within scope.

The original outage summary, verification and missing-check declaration are
preserved here with pre-recovery- prefixes and in the unchanged sibling folder.
They describe the previous attempt, not the completed recovery. The copied
verify.py likewise describes the earlier outage; use verification.json and
the root finalizer for the recovered state. The original frozen queue remains
unchanged. No physical verdict or new-claim acceptance follows automatically
from a scoped catalogue nonmatch. Hashes are in SHA256SUMS.json.
''',encoding='utf-8')
assert counts=={'no identified prior EB in queried scope':57,'known prior EB in queried scope':17,'nearby EB identity unresolved':1},counts
files={str(p.relative_to(B)):sha(p) for p in B.rglob('*') if p.is_file() and '__pycache__' not in str(p) and p.name!='SHA256SUMS.json'}
(B/'SHA256SUMS.json').write_text(json.dumps(files,indent=2)+'\n',encoding='utf-8')
print(json.dumps(validation,indent=2));print('manifest files',len(files))
