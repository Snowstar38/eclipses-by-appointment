import pathlib,hashlib,json,csv
b=pathlib.Path(__file__).resolve().parent.parent
files=[b/'RESULTS.csv',b/'pixel-audit.json',b/'gaia-geometry.json',b/'alias-audit.json']
for r in csv.DictReader((b/'queue.csv').open()):
 files.extend(b/r['tic']/x for x in ('measurements.json','REPORT.md','raw-events.png','raw-windows.csv'))
out={str(p.relative_to(b)).replace('\\','/'):hashlib.sha256(p.read_bytes()).hexdigest() for p in files}
(b/'helper'/'audited-hashes.json').write_text(json.dumps(out,indent=2)+'\n')
