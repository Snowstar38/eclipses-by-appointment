import json,csv,math
from pathlib import Path
import numpy as np
p=Path(__file__).parent
out={}
for row in csv.DictReader((p/'queue.csv').open()):
 t=row['tic']; d=json.loads((p/t/'measurements.json').read_text()); checks=[]; fits={}
 for e in d['events']:
  if 'fit_parameters' not in e: continue
  b,s,a,c,w,k=e['fit_parameters']; dep=1000*a*min(1,w/(2*k)); checks.append({'kind':e['kind'],'sector':e['sector'],'realized_depth_ppt':dep,'delta_ppt':dep-e['depth_ppt']})
 for kind in ['A','B']:
  ev=sorted([e for e in d['events'] if e.get('timing_usable') and e['kind']==kind],key=lambda e:e['mid_btjd'])
  if len(ev)<2:continue
  tm=np.array([e['mid_btjd'] for e in ev]); sig=np.array([e['conservative_timing_error_days'] for e in ev]); n=np.rint((tm-tm[0])/float(row['gaia_period_days'])).astype(int); n0=np.average(n,weights=1/sig**2); t0=np.average(tm,weights=1/sig**2); slope=np.sum((n-n0)*(tm-t0)/sig**2)/np.sum((n-n0)**2/sig**2); intercept=t0-slope*n0; resid=tm-(intercept+slope*n); chi2=np.sum((resid/sig)**2); err=(1/np.sum((n-n0)**2/sig**2))**.5*max(1,chi2/(len(n)-2))**.5 if len(n)>2 else (1/np.sum((n-n0)**2/sig**2))**.5
  fits[kind]={'cycles':n.tolist(),'period':slope,'error':err,'residual_h':(resid*24).tolist(),'gcd_cycle_intervals':int(np.gcd.reduce(np.diff(n)))}
 out[t]={'depth_checks':checks,'timing_fits':fits}
(p/'helper-numeric-audit.json').write_text(json.dumps(out,indent=2)); print(json.dumps(out,indent=2))
