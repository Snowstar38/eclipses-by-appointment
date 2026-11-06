import json,csv,numpy as np
from pathlib import Path
b=Path(__file__).resolve().parent
sels={'12319637':(25.01,lambda e:True),'55662895':(36.973,lambda e:e['sector']!=98),'141428309':(54.52,lambda e:e.get('depth_ppt',0)>90),'144157102':(47.55,lambda e:e['sector'] in (10,64)),'149847663':(31.547,lambda e:e.get('depth_ppt',0)>100),'168983144':(35.64,lambda e:True)}
out={}
for tic,(p,sel) in sels.items():
 ev=[e for e in json.loads((b/tic/'lead-timing.json').read_text()) if sel(e) and e.get('center_btjd')];t=np.array([e['center_btjd'] for e in ev]);n=np.round((t-t[0])/p).astype(int);err=np.array([max(e['center_formal_error_d'],e['cadence_d']/2,.002) for e in ev]);err=np.maximum(err,.06) if tic=='55662895' else err;X=np.array([np.ones(len(n)),n]).T;W=1/err**2;cv=np.linalg.inv(X.T@(W[:,None]*X));v=cv@(X.T@(W*t));res=t-X@v
 out[tic]=dict(period_d=v[1],epoch_btjd=v[0],formal_period_error_d=cv[1,1]**.5,cycles=n.tolist(),times=t.tolist(),residuals=res.tolist(),duration_d=float(np.median([e['duration_d'] for e in ev])),depth_ppt=float(np.median([e['depth_ppt'] for e in ev])),max_residual_d=float(max(abs(res))),note='Same-kind chosen from morphology; covariance formal with cadence/2 and .002d floors; alias audit required.')
 print(tic,out[tic])
(b/'lead-clocks.json').write_text(json.dumps(out,indent=2))
