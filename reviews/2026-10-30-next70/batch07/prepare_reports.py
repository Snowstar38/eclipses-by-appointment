from pathlib import Path
import csv,json
D=Path('[local working path omitted; see provenance receipts]');B=D/'batch07'
ids=set(json.loads((B/'targets-selected.json').read_text()))
c=[x for x in csv.DictReader((D/'shared-catalogues/coverage-matrix.csv').open()) if x['tic'] in ids]
(B/'catalogue-review.json').write_text(json.dumps(c,indent=2))
for name in ['make_reports.py','validate.py']:
 s=(D/'batch05'/name).read_text().replace('batch05','batch07').replace("r['batch']=='5'","r['batch']=='7'")
 (B/name).write_text(s)
