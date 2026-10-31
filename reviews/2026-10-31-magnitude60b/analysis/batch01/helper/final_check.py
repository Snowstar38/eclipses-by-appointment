import pathlib,json,csv,re,hashlib,math
p=pathlib.Path(r'[local path omitted]'); q=list(csv.DictReader(open(p/'queue.csv'))); results=list(csv.DictReader(open(p/'RESULTS.csv'))); g=json.load(open(p/'gaia-geometry.json')); mism=[]; manifest={}; by={r['tic']:r for r in results}
for x in q:
 t=x['tic']; m=json.load(open(p/t/'measurements.json')); s=(p/t/'REPORT.md').read_text(encoding='utf-8'); r=by[t]; z=g[t]
 for k in ('period_days','period_error_days','primary_epoch_btjd','depth_ppt'):
  if float(r[k])!=m[k]: mism.append((t,k,'result mismatch'))
 for v in (f"P={m['period_days']:.10f}",f"{m['period_error_days']:.10f}d",f"BTJD{m['primary_epoch_btjd']:.7f}",f"P={z['period_days']:.10f}",f"{z['closest']['offset_days']:.6f}d",f"{z['closest']['gaia_covariance_linear_error_days']:.6f}d"):
  if v not in s:mism.append((t,v,'missing report'))
 if f"# TIC {t}: {r['physical_verdict']}" not in s:mism.append((t,'verdict mismatch'))
 for e in m['events']:
  if f"{e['mid_btjd']:.7f}" not in s:mism.append((t,e['cycle'],'event missing'))
 for f in [p/t/'REPORT.md',p/t/'measurements.json',p/t/'raw-events.png',p/t/'raw-windows.csv']:
  manifest[str(f.relative_to(p))]=hashlib.sha256(f.read_bytes()).hexdigest()
for f in [p/'RESULTS.csv',p/'queue.csv',p/'gaia-geometry.json',p/'geometry.py']:
 manifest[str(f.relative_to(p))]=hashlib.sha256(f.read_bytes()).hexdigest()
(p/'helper'/'final-audited-hashes.json').write_text(json.dumps(manifest,indent=2),encoding='utf-8')
print('rows',len(q),len(results),'mismatch',mism)
