import csv,json,hashlib
from pathlib import Path
from datetime import datetime,timezone
from collections import Counter
b=Path(__file__).resolve().parent;sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();q=list(csv.DictReader((b/'queue.csv').open()));r=list(csv.DictReader((b/'RESULTS.csv').open()));assert [x['tic'] for x in q]==[x['tic'] for x in r];assert len(r)==6 and all(x['completion']=='complete' for x in r)
h=json.load(open(b/'helper-final-freeze.json'));assert h['all_match'];assert all(sha(b/k)==v for k,v in h['freeze'].items())
files=[dict(path=str(p.relative_to(b)).replace('\\','/'),bytes=p.stat().st_size,sha256=sha(p)) for p in sorted(b.rglob('*')) if p.is_file() and p.name!='BATCH-SEAL.json' and '__pycache__' not in p.parts]
seal=dict(created_utc=datetime.now(timezone.utc).isoformat(),queue_exact=True,n=6,completion='all6complete',tiers=dict(Counter(x['tier'] for x in r)),results_sha256=sha(b/'RESULTS.csv'),helper_freeze_sha256=sha(b/'helper-final-freeze.json'),shared_catalogue_seal=dict(path=str(b.parent/'shared-catalogues/ROOT-CATALOGUE-SEAL.json'),sha256=sha(b.parent/'shared-catalogues/ROOT-CATALOGUE-SEAL.json')),files=files,total_bytes=sum(x['bytes'] for x in files),note='No ledger/public edits. 22 cached QLP files identity/hash audited; six extra sectors and four localization cutouts retained, total54.6MB FITS. Supervisor acceptance required before integration.')
(b/'BATCH-SEAL.json').write_text(json.dumps(seal,indent=2));print(len(files),seal['total_bytes'],sha(b/'BATCH-SEAL.json'))
