import csv,json,math
from pathlib import Path
B=Path(__file__).resolve().parent;out=[]
for r in csv.DictReader((B/'RESULTS.csv').open(encoding='utf8')):
 m=json.loads((B/r['tic']/'measurements.json').read_text(encoding='utf8')); errors={}
 for a,k in [('period_days','period_days'),('period_error_days','period_error_days'),('primary_epoch_btjd','reference_epoch_btjd'),('depth_ppt','depth_ppt')]:
  errors[a]=float(r[a])-m[k]
 out.append({'tic':r['tic'],'differences':errors,'report_exists':Path(r['report']).exists(),'measurement_exists':Path(r['source_report']).exists()})
print(json.dumps(out,indent=2));(B/'helper-result-audit.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf8')
