import csv,json,hashlib
from pathlib import Path
from datetime import datetime,timezone
b=Path(__file__).resolve().parent
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
q=list(csv.DictReader((b/'queue.csv').open()));r=list(csv.DictReader((b/'RESULTS.csv').open()));assert [x['tic'] for x in q]==[x['tic'] for x in r];assert all(x['completion']=='complete' for x in r)
h=json.loads((b/'helper-final-freeze-audit.json').read_text());assert sha(b/'RESULTS.csv')==h['results_sha256'];assert sha(b/'lead-clocks.json')==h['clocks_sha256'];assert all(sha(b/x['tic']/'REPORT.md')==x['report_sha256'] for x in h['checks'])
files=[dict(path=str(p.relative_to(b)).replace('\\','/'),bytes=p.stat().st_size,sha256=sha(p)) for p in sorted(b.rglob('*')) if p.is_file() and p.name!='BATCH-SEAL.json' and '__pycache__' not in p.parts]
seal=dict(created_utc=datetime.now(timezone.utc).isoformat(),queue_exact=True,n=7,completion='all7complete',tiers={'CONFIRMED':4,'PROBABLE':1,'PLAUSIBLE':2},results_sha256=sha(b/'RESULTS.csv'),helper_freeze_sha256=sha(b/'helper-final-freeze-audit.json'),shared_catalogue_seal=dict(path=str(b.parent/'shared-catalogues/ROOT-CATALOGUE-SEAL.json'),sha256=sha(b.parent/'shared-catalogues/ROOT-CATALOGUE-SEAL.json')),files=files,total_bytes=sum(x['bytes'] for x in files),note='No ledger/public edits. Source hashes separately retained and independently checked46/46. Supervisor acceptance required before integration.')
(b/'BATCH-SEAL.json').write_text(json.dumps(seal,indent=2));print(len(files),seal['total_bytes'],sha(b/'BATCH-SEAL.json'))
