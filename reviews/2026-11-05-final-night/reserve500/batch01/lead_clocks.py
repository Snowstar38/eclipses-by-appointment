import json,csv,numpy as np
from pathlib import Path
b=Path(__file__).resolve().parent
sels={'37951551':(48.365,lambda e:True),'100826297':(43.0522,lambda e:e['sector'] in [27,67,94]),'138351298':(29.4313,lambda e:True),'160166846':(34.6418,lambda e:True),'165828134':(38.0585,lambda e:e['sector'] in [37,102] and e['kind']!='kindB')}
out={}
for tic,(p,sel) in sels.items():
 ev=[e for e in json.loads((b/tic/'lead-timing.json').read_text()) if sel(e) and e.get('fit_usable')]
 t=np.array([e['center_btjd'] for e in ev]);n=np.round((t-t[0])/p).astype(int);err=np.array([max(e['center_formal_error_d'],e['cadence_d']/2,.003) for e in ev]);X=np.array([np.ones(len(n)),n]).T;W=1/err**2;cv=np.linalg.inv(X.T@(W[:,None]*X));v=cv@(X.T@(W*t));res=t-X@v
 out[tic]=dict(period_d=v[1],epoch_btjd=v[0],formal_period_error_d=cv[1,1]**.5,cycles=n.tolist(),times=t.tolist(),residuals=res.tolist(),duration_d=float(np.median([e['duration_d'] for e in ev])),depth_ppt=float(np.median([e['depth_ppt'] for e in ev])),max_residual_d=float(max(abs(res))),note='Same-kind morphology. WLS errors are formal with cadence/2 or .003d floor, not calibrated coverage. Integer aliases tested separately; two-event fit alone does not determine unique clock.')
 print(tic,out[tic])
(b/'lead-clocks.json').write_text(json.dumps(out,indent=2))


