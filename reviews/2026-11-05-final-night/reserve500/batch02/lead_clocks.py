import json,numpy as np
from pathlib import Path
b=Path(__file__).resolve().parent
# Morphology-defined same conjunction kind. RS013's two similar depths must not be mixed.
sels={'175736093':(26.07,lambda e:True),'187242860':(1.5625,lambda e:True),'281540788':(40.754,lambda e:abs((e['center_btjd']-1337.32092)/40.754-round((e['center_btjd']-1337.32092)/40.754))<.02),'298976044':(50.96,lambda e:True),'308091169':(3.35457,lambda e:e['sector'] in (79,80)),'403192875':(35.93,lambda e:True)}
out={}
for tic,(p,sel) in sels.items():
 ev=[e for e in json.loads((b/tic/'lead-timing.json').read_text()) if sel(e) and e.get('fit_usable')]
 t=np.array([e['center_btjd'] for e in ev]);n=np.round((t-t[0])/p).astype(int)
 if tic=='187242860':
  n=np.round((t-t[0])/(p/2)).astype(int);ev=[e for e,k in zip(ev,n) if k%2==0];t=np.array([e['center_btjd'] for e in ev]);n=np.round((t-t[0])/p).astype(int)
 err=np.array([max(e['center_formal_error_d'],e['cadence_d']/2,.003) for e in ev]);X=np.array([np.ones(len(n)),n]).T;W=1/err**2;cv=np.linalg.inv(X.T@(W[:,None]*X));v=cv@(X.T@(W*t));res=t-X@v
 out[tic]=dict(period_d=v[1],epoch_btjd=v[0],formal_period_error_d=cv[1,1]**.5,cycles=n.tolist(),times=t.tolist(),residuals=res.tolist(),duration_d=float(np.median([e['duration_d'] for e in ev])),depth_ppt=float(np.median([e['depth_ppt'] for e in ev])),max_residual_d=float(max(abs(res))),note='WLS with cadence/2 or .003d floor; two-point errors conditional on integer count; period aliases tested separately. RS010 full orbital period conservatively twice successive equal minima; RS013 separate conjunction kinds.')
 print(tic,out[tic])
(b/'lead-clocks.json').write_text(json.dumps(out,indent=2))
