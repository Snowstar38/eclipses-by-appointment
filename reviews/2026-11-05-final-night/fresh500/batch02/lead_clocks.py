import json,csv,numpy as np
from pathlib import Path
b=Path(__file__).resolve().parent
sels={'170402154':(37.2165,lambda e:True),'200925588':(2.345,lambda e:True),'293514968':(24.2978,lambda e:e.get('depth_ppt',0)>100),'313271160':(45.987,lambda e:True),'319472502':(14.014,lambda e:e.get('duration_d',0)<.23),'332915881':(29.844,lambda e:True),'372172730':(38.0,lambda e:e.get('fit_usable',False))}
out={}
for tic,(p,sel) in sels.items():
 ev=[e for e in json.loads((b/tic/'lead-timing.json').read_text()) if sel(e) and e.get('center_btjd') and e.get('fit_usable')];t=np.array([e['center_btjd'] for e in ev]);n=np.round((t-t[0])/p).astype(int);err=np.array([max(e['center_formal_error_d'],e['cadence_d']/2,.002) for e in ev]);X=np.array([np.ones(len(n)),n]).T;W=1/err**2;cv=np.linalg.inv(X.T@(W[:,None]*X));v=cv@(X.T@(W*t));res=t-X@v
 out[tic]=dict(period_d=v[1],epoch_btjd=v[0],formal_period_error_d=cv[1,1]**.5,cycles=n.tolist(),times=t.tolist(),residuals=res.tolist(),duration_d=float(np.median([e['duration_d'] for e in ev])),depth_ppt=float(np.median([e['depth_ppt'] for e in ev])),max_residual_d=float(max(abs(res))),note='Same-kind chosen from morphology; covariance formal with cadence/2 and .002d floors; alias audit required. E018 trial Gaia-guided period not validated.')
 print(tic,out[tic])
(b/'lead-clocks.json').write_text(json.dumps(out,indent=2))

