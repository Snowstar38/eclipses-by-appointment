import json
from pathlib import Path
import numpy as np
b=Path(r'[workspace]/Astra\made\final-night-2026-11-05\fresh18\batch02')
choices={'159860053':(23.966,lambda e:e['depth_ppt']<30),'162437782':(37.574,lambda e:True),'167461087':(1.4092,lambda e:True),'277772867':(22.509,lambda e:e['depth_ppt']>40),'436205524':(23.403,lambda e:e['depth_ppt']>80),'440995465':(9.03,lambda e:e['kind']=='B')}
out={}
for tic,(trial,keep) in choices.items():
 es=[e for e in json.loads((b/tic/'lead-timing.json').read_text()) if e.get('fit_usable') and keep(e)];es.sort(key=lambda e:e['center_btjd']);t=np.array([e['center_btjd'] for e in es]);n=np.rint((t-t[0])/trial).astype(int);err=np.array([max(e['center_formal_error_d'],e['cadence_d']/2) for e in es]);X=np.stack([np.ones(len(t)),n],axis=1);W=1/err**2;cov=np.linalg.inv(X.T@(W[:,None]*X));beta=cov@(X.T@(W*t));res=t-X@beta
 out[tic]=dict(period_d=float(beta[1]),epoch_btjd=float(beta[0]),cycles=n.tolist(),event_btjd=t.tolist(),residuals_d=res.tolist(),formal_period_error_d=float(np.sqrt(cov[1,1])),scatter_inflated_error_d=float(np.sqrt(cov[1,1])*max(1,np.sqrt(np.sum((res/err)**2)/max(1,len(t)-2)))),note='Local trapezoid covariance errors with half-cadence floor. Conditional integer cycles, not total/calibrated uncertainty; 1.409-d Y012 recurrence may be half orbital period.')
 print(tic,out[tic])
(b/'lead-clocks.json').write_text(json.dumps(out,indent=2))
