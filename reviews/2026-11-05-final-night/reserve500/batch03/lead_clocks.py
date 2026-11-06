import csv,json,numpy as np
from pathlib import Path
b=Path(__file__).resolve().parent
out={}
for tic,p,kind in [('408996985',59.64,'all'),('455100744',44.52,'secondary')]:
 ev=[e for e in json.loads((b/tic/'lead-timing.json').read_text()) if e.get('fit_usable') and (kind=='all' or e['depth_ppt']<30)]
 t=np.array([e['center_btjd'] for e in ev]);n=np.round((t-t[0])/p).astype(int);err=np.array([max(e['center_formal_error_d'],e['cadence_d']/2,.01) for e in ev]);X=np.array([np.ones(len(n)),n]).T;W=1/err**2;cv=np.linalg.inv(X.T@(W[:,None]*X));v=cv@(X.T@(W*t));res=t-X@v
 out[tic]=dict(period_d=v[1],epoch_btjd=v[0],formal_period_error_d=cv[1,1]**.5,cycles=n.tolist(),times=t.tolist(),residuals=res.tolist(),duration_d=float(np.median([e['duration_d'] for e in ev])),depth_ppt=float(np.median([e['depth_ppt'] for e in ev])),max_residual_d=float(max(abs(res))),note='WLS cadence/2 or .01d floor; errors conditional on integer count, alias tests separate. RS019 secondary clock only; primary distinct.')
pa=json.loads((b/'lead-partial-templates.json').read_text())[0]
out['467864145']=dict(period_d=pa['period_d'],epoch_btjd=pa['template_center_btjd'],formal_period_error_d=.005,cycles=[0,10],times=[pa['template_center_btjd'],pa['partial_event_trials'][1]['center_btjd']],duration_d=pa['template_width_d'],depth_ppt=29,max_residual_d=0,note='S73 fixed-template partial event; period allowance0.005d from width sensitivity, not formal/calibrated. Secondary kind has consistent36.45303d9cycle recurrence. Opposite unequal minima excluded from same-kind clock.')
(b/'lead-clocks.json').write_text(json.dumps(out,indent=2))
print(out)
