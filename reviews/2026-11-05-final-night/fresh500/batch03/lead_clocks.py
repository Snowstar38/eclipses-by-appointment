import json,numpy as np
from pathlib import Path
b=Path('[workspace]/Astra/made/final-night-2026-11-05/fresh500/batch03')
sels={'382672776':(32.214,lambda e:e.get('depth_ppt',0)>100 and e['sector'] not in [65,99] and e['screen_btjd'] not in []),'398556213':(33.11,lambda e:e.get('depth_ppt',0)>80),'399027834':(28.146,lambda e:True),'451669009':(44.272,lambda e:True),'1511057635':(36.063,lambda e:e['sector'] in (39,103))}
out={}
for tic,(p,sel) in sels.items():
 ev=[e for e in json.loads((b/tic/'lead-timing.json').read_text()) if sel(e) and e.get('fit_usable')]
 if tic=='382672776':ev=[e for e in json.loads((b/tic/'lead-timing.json').read_text()) if e.get('fit_usable') and e.get('depth_ppt',0)>100 and abs((e['center_btjd']-1618.424)/32.214-round((e['center_btjd']-1618.424)/32.214))<.02]
 t=np.array([e['center_btjd'] for e in ev]);n=np.round((t-t[0])/p).astype(int);err=np.array([max(e['center_formal_error_d'],e['cadence_d']/2,.003) for e in ev]);X=np.array([np.ones(len(n)),n]).T;W=1/err**2;cv=np.linalg.inv(X.T@(W[:,None]*X));v=cv@(X.T@(W*t));res=t-X@v
 out[tic]=dict(period_d=v[1],epoch_btjd=v[0],formal_period_error_d=cv[1,1]**.5,cycles=n.tolist(),times=t.tolist(),residuals=res.tolist(),duration_d=float(np.median([e['duration_d'] for e in ev])),depth_ppt=float(np.median([e['depth_ppt'] for e in ev])),max_residual_d=float(max(abs(res))),note='Same-kind morphology; formal WLS error with cadence/2 or .003d floor; integer alias and geometry audits separately required.')
 print(tic,out[tic])
(b/'lead-clocks.json').write_text(json.dumps(out,indent=2))
