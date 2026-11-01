import csv,json,pathlib,re
b=pathlib.Path(r'[local path omitted]')
rows=list(csv.DictReader((b/'RESULTS.csv').open(encoding='utf-8-sig')))
g=json.loads((b/'gaia-geometry.json').read_text(encoding='utf-8-sig'))
for row in rows:
 t=row['tic']; m=json.loads((b/t/'measurements.json').read_text(encoding='utf-8-sig')); s=(b/t/'REPORT.md').read_text(encoding='utf-8-sig')
 errors=[]
 for k in ('period_days','period_error_days','primary_epoch_btjd','depth_ppt'):
  if float(row[k])!=m[k]:errors.append(k)
 if abs(m['period_days']-g[t]['photometric_period_days'])>1e-10:errors.append('stale geometry')
 for k in ('source_report','report'):
  if not pathlib.Path(row[k]).exists():errors.append('missing '+k)
 for p in re.findall(r'historical/[\w.]+',s):
  if not (b/t/p).exists():errors.append('missing '+p)
 print(t,errors)
