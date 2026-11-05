"""Freeze the batch evidence manifest after all reports and helper artifacts settle."""
from pathlib import Path
import hashlib,json,csv
B=Path(__file__).resolve().parent;W=B.parent
external=[W/'queue-seal.json',W/'root-availability.json',W/'source-packet-index.json',W/'shared-catalogues'/'TARGET-STATUS.csv',W/'shared-catalogues'/'target-evidence.json',Path('[local-path-redacted] 5.1/made/appointments/vet318209162/REPORT.md')]
for row in csv.DictReader((B/'queue.csv').open(newline='',encoding='utf8')):external.append(W/'source-packets'/row['tic']/'sources.json')
files={}
for p in sorted(B.rglob('*')):
 if p.is_file() and p.name not in ('SHA256SUMS.json','ROOT-ACCEPTANCE.json'):
  files[str(p.relative_to(B)).replace('\\','/')]=hashlib.sha256(p.read_bytes()).hexdigest()
for p in external:
 assert p.is_file(),p
 files[str(p)]=hashlib.sha256(p.read_bytes()).hexdigest()
(B/'SHA256SUMS.json').write_text(json.dumps({'files':files,'scope':'Exact batch01 outputs plus external source/selection/catalogue/availability receipts; no root acceptance self-reference.'},indent=2)+'\n')
print('manifest entries',len(files))
