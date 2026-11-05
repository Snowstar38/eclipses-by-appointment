"""Explicit integer cycle test of non-singular F028 same-kind raw-SAP dip centers."""
from pathlib import Path
import json
import numpy as np
B=Path(__file__).resolve().parent
tic='19385783';d=json.loads((B/tic/'lead-measurements.json').read_text(encoding='utf8'))
ev=[x for x in d['screen_flagged_dips'] if 'measured_center_btjd' in x and not x['fit_singular'] and not x['fit_boundary']]
t=np.array(sorted(x['measured_center_btjd'] for x in ev));t0=t[0]
trial=[]
for P in np.linspace(2.04,2.09,100001):
    n=np.rint((t-t0)/P).astype(int)
    X=np.stack([np.ones(len(n)),n],axis=1);coef=np.linalg.lstsq(X,t,rcond=None)[0]
    if abs(coef[1]-P)>.0002:continue
    resid=t-X@coef;rms=float(np.sqrt(np.mean(resid**2)))
    trial.append((rms,float(coef[1]),float(coef[0]),n.tolist(),resid.tolist()))
trial.sort();keep=[]
for rms,p,ep,n,res in trial:
    if all(abs(p-x['period_days'])>.0004 for x in keep):
        keep.append(dict(period_days=p,epoch_btjd=ep,rms_residual_days=rms,cycles=n,residual_days=res))
    if len(keep)>=12:break
out=dict(tic=tic,event_centers_btjd=t.tolist(),event_count=len(t),search_range_days=[2.04,2.09],trial_step_days=.0000005,aliases=keep,note='Cycle assignments rounded at each trial, then period/epoch refit; competing integer aliases are compared by event-center residual. Local center covariance singular/bound fits excluded. Residual is model-dependent, not calibrated uncertainty.')
(B/tic/'lead-alias.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf8')
print([(round(x['period_days'],7),round(x['rms_residual_days'],4)) for x in keep])
