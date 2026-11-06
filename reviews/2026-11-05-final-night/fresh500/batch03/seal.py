import csv,json,hashlib
from pathlib import Path
from datetime import datetime,timezone
from collections import Counter
b=Path(__file__).resolve().parent;sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();q=list(csv.DictReader((b/'queue.csv').open()));r=list(csv.DictReader((b/'RESULTS.csv').open()));assert [x['tic'] for x in q]==[x['tic'] for x in r];assert len(r)==8 and all(x['completion']=='complete' for x in r)
h=json.loads((b/'helper-final-freeze-audit.json').read_text());assert not h['checks']['mismatches'];assert all(sha(b/p)==v for p,v in h['sha256'].items())
files=[dict(path=p.relative_to(b).as_posix(),bytes=p.stat().st_size,sha256=sha(p)) for p in sorted(b.rglob('*')) if p.is_file() and p.name!='BATCH-SEAL.json' and '__pycache__' not in p.parts]
s=dict(created_utc=datetime.now(timezone.utc).isoformat(),queue_exact=True,n=8,completion='all8complete',tiers=dict(Counter(x['tier'] for x in r)),eligible=sum(x['publication_eligible']=='true' for x in r),results_sha256=sha(b/'RESULTS.csv'),shared_catalogue_seal=dict(path=str(b.parent/'shared-catalogues/ROOT-CATALOGUE-SEAL.json'),sha256=sha(b.parent/'shared-catalogues/ROOT-CATALOGUE-SEAL.json')),files=files,total_bytes=sum(x['bytes'] for x in files),note='No ledger/public edits. 45 raw-source hashes and TIC headers verified; bounded pixels and current-sector receipts retained. Supervisor acceptance required before integration.')
(b/'BATCH-SEAL.json').write_text(json.dumps(s,indent=2));print(s['tiers'],s['eligible'],s['total_bytes'],sha(b/'BATCH-SEAL.json'))
