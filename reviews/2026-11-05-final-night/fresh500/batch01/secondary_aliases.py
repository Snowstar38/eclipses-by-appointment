import csv,json,numpy as np
from pathlib import Path
b=Path(__file__).resolve().parent;out={}
for tic,depth in [('141428309',30),('149847663',30)]:
 es=[e for e in json.loads((b/tic/'lead-timing.json').read_text()) if e.get('fit_usable') and e['depth_ppt']<depth];t=np.array([e['center_btjd'] for e in es]);n=round((max(t)-min(t))/json.loads((b/'lead-clocks.json').read_text())[tic]['period_d']);out[tic]={'times':t.tolist(),'cycle_difference':n,'period_d':float((max(t)-min(t))/n),'note':'Independent same-kind shallow clock; different conjunction from primary.'}
 print(tic,out[tic])
(b/'lead-secondary-clocks.json').write_text(json.dumps(out,indent=2))
a=json.loads((b/'lead-alias-covered-windows.json').read_text());o={}
for tic,rr in a.items():
 ss=[]
 for r in rr:
  if not r['timing_compatible'] or r['nulls']:continue
  if tic in out:
   ts=out[tic]['times'];dt=max(ts)-min(ts);r['secondary_clock_residual_d']=float(dt-round(dt/r['period_d'])*r['period_d']);
   if abs(r['secondary_clock_residual_d'])>.08:continue
  ss.append({k:r[k] for k in r if k not in ['dips','nulls']})
 o[tic]=ss;print(tic,'compatible survivors',[(r['label'],r['period_d']) for r in ss])
(b/'lead-alias-summary.json').write_text(json.dumps(o,indent=2))
