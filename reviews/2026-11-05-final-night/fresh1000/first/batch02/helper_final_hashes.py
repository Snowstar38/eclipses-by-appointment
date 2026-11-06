import csv,json,hashlib
from pathlib import Path
B=Path(__file__).resolve().parent
rows=list(csv.DictReader((B/'queue.csv').open()))
files=[B/x for x in ['queue.csv','RESULTS.csv','lead-clocks.json','lead-gaia-covariance.json','lead-alias-covered-windows.json','lead-current-sector-inventory.json','helper-numeric-audit.json','independent-audit.md','HELPER-AUDIT.md']]
files += [B/r['tic']/'lead-timing.json' for r in rows]
files += [B/r['tic']/'REPORT.md' for r in rows]
out={str(p.relative_to(B)):hashlib.sha256(p.read_bytes()).hexdigest() for p in files}
(B/'helper-final-hashes.json').write_text(json.dumps(out,indent=2),encoding='utf8')
for k,v in out.items():
 assert hashlib.sha256((B/k).read_bytes()).hexdigest()==v
print('Verified',len(out),'final files')
