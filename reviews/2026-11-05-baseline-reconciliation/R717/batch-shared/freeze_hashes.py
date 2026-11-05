"""Freeze every local artifact and bind external catalogue provenance, excluding self-referential manifests."""
import csv,hashlib,json
from collections import Counter
from pathlib import Path
B=Path(__file__).resolve().parent
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
q=list(csv.DictReader((B/'queue.csv').open()));r=list(csv.DictReader((B/'RESULTS.csv').open()));a=json.loads((B/'helper-final-audit.json').read_text())
assert [x['tic'] for x in q]==[x['tic'] for x in r]
assert len(r)==10 and len(set(x['tic'] for x in r))==10
assert a['results_sha256']==sha(B/'RESULTS.csv')
for x in a['rows']:
 assert all(x['checks'].values()),x['tic']
 assert x['report_sha256']==sha(B/x['tic']/'REPORT.md')
 assert x['measurements_sha256']==sha(B/x['tic']/'measurements.json')
for x in r:
 assert x['full_review_completion']=='COMPLETE'
 if x['tic'] in ('25320385','349527829','95836684'):assert not x['period_days'] and not x['period_error_days'] and not x['reference_epoch_btjd']
assert Counter(x['physical_verdict'] for x in r)=={'CONFIRMED':2,'PROBABLE':6,'PLAUSIBLE':2}
c=B.parent/'unmatched512'/'catalogue-recovery-selected12';paths=[c/'REPORT.md',c/'coverage-matrix.csv',c/'SHA256SUMS.json',c/'verification.json']
paths += [c/'live-vsx'/f'{tic}{suffix}' for tic in ('117930511','198358825') for suffix in ('.txt','.json') if (c/'live-vsx'/f'{tic}{suffix}').exists()]
(B/'catalogue-provenance.json').write_text(json.dumps(dict(status='2 positional known EA counterparts; 8 unknown due incomplete scoped gates; no new claims',sources=[dict(path=str(p),sha256=sha(p)) for p in paths]),indent=2)+'\n')
exclude={'SHA256SUMS.json','ROOT-ACCEPTANCE.json'}
manifest={str(p.relative_to(B)).replace('\\','/'):sha(p) for p in sorted(B.rglob('*')) if p.is_file() and p.name not in exclude and '__pycache__' not in str(p)}
(B/'SHA256SUMS.json').write_text(json.dumps(manifest,indent=2)+'\n')
assert all(sha(B/p)==h for p,h in manifest.items())
print(json.dumps(dict(files=len(manifest),results_sha256=sha(B/'RESULTS.csv'),manifest_sha256=sha(B/'SHA256SUMS.json'),physical_counts=dict(Counter(x['physical_verdict'] for x in r)),exact_queue=True,helper_final_audit_passed=True)))
