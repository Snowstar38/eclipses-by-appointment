import csv,json,hashlib
from pathlib import Path
B=Path(__file__).parent.parent
files=[B/'RESULTS.csv',B/'gaia-geometry.json',B/'alias-audit.json',B/'LEAD-AUDIT.md',B/'helper'/'pixel-audit.json',B/'helper'/'timing-audit.json',B/'helper'/'pixel_audit.py',B/'helper'/'timing_audit.py']
for r in csv.DictReader(open(B/'queue.csv')):
 t=r['tic']; m=json.load(open(B/t/'measurements.json')); row=next(x for x in csv.DictReader(open(B/'RESULTS.csv')) if x['tic']==t); assert all(float(row[k])==m[k] for k in ['period_days','period_error_days','primary_epoch_btjd','depth_ppt']); files += [B/t/'REPORT.md',B/t/'measurements.json',B/t/'raw-events.png',B/t/'raw-windows.csv']
out={str(p.relative_to(B)):hashlib.sha256(p.read_bytes()).hexdigest() for p in files};json.dump(out,open(B/'helper'/'final-hashes.json','w'),indent=2)
print('Verified ten numerical result rows; hashed',len(files),'final artifacts.')
