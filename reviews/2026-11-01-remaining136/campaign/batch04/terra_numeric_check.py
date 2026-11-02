import json,csv,re,math,pathlib
b=pathlib.Path(__file__).parent
rows=list(csv.DictReader(open(b/'RESULTS.csv'))); q=list(csv.DictReader(open(b/'queue.csv'))); print('queue exact', [r['tic'] for r in rows]==[r['tic'] for r in q]); errors=[]
for r in rows:
 t=r['tic'];m=json.load(open(b/t/'measurements.json')); g=json.load(open(b/'gaia-geometry.json'))[t];d=json.load(open(b/t/'fresh-pixels/diff_fresh.json'));s=(b/t/'REPORT.md').read_text()
 for k in ['period_days','period_error_days','primary_epoch_btjd','depth_ppt']:
  if float(r[k])!=m[k]:errors.append((t,k,'RESULT mismatch'))
 for key in ['source_report','report']:
  if not pathlib.Path(r[key]).exists():errors.append((t,key,'missing'))
 for expected in [f"P={m['period_days']:.10f} +/- {m['period_error_days']:.10f}",f"BTJD={m['primary_epoch_btjd']:.7f}",f"offset={g['closest']['offset_days']:.5f}",f"phase={g['other_conjunction_relative_phase']:.5f}"]:
  if expected not in s: errors.append((t,expected,'not in report'))
 for z in d['neighbours_60']:
  if z['possible'] and str(z['source_id']) not in s:errors.append((t,z['source_id'],'missing neighbor'))
 for e in m['events']:
  if 'mid_btjd' in e and f"{e['mid_btjd']:.7f}" not in s:errors.append((t,e['mid_btjd'],'event absent'))
print('errors',errors)
