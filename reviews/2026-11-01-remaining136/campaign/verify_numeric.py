"""Independent root equality check for final row values and deciding measurements."""
import csv,json,sys,math
from pathlib import Path
W=Path(__file__).resolve().parent;B=W/sys.argv[1]
rr=list(csv.DictReader((B/'RESULTS.csv').open(encoding='utf-8-sig')))
checked=[]
for r in rr:
 p=B/r['tic']/'measurements.json'
 assert p.is_file(),str(p)
 m=json.loads(p.read_text(encoding='utf-8-sig'))
 assert str(m['tic'])==r['tic']
 for k in ['period_days','period_error_days','primary_epoch_btjd','depth_ppt']:
  assert float(r[k])==float(m[k]),(r['tic'],k,r[k],m[k])
  assert math.isfinite(float(r[k])),(r['tic'],k)
 assert m.get('error_meaning') and m.get('epoch_kind'),r['tic']
 assert float(r['period_days'])>0 and float(r['period_error_days'])>0
 report=Path(r['report']);report=report if report.is_absolute() else B/report
 text=report.read_text(encoding='utf-8-sig')
 assert r['physical_verdict'].upper() in text.upper()
 assert '\ufffd' not in text and '\u00c2\u00b1' not in text,r['tic']
 checked.append(r['tic'])
out={'exact_numeric_rows':len(checked),'tics':checked,'error_and_epoch_semantics_present':True}
(B/'root-numeric-verification.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))
