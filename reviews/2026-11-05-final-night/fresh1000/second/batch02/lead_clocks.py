import json,csv,numpy as np
from pathlib import Path
b=Path(__file__).resolve().parent
trials={'284764266':26.1,'294833711':58.917,'317322586':34.761,'322438528':47.78,'347159772':25.978}
out={}
for tic,p in trials.items():
 ev=json.loads((b/tic/'lead-timing.json').read_text());ev=[e for e in ev if e.get('fit_usable')]
 if tic=='317322586':ev=[e for e in ev if e['depth_ppt']>85 or e['sector']==17]
 if tic=='322438528':ev=[e for e in ev if e['depth_ppt']<20]
 if tic=='347159772':ev=[e for e in ev if e['depth_ppt']>100]
 t=np.array([e['center_btjd'] for e in ev]);n=np.round((t-t[0])/p).astype(int);err=np.array([max(e['center_formal_error_d'],e['cadence_d']/2,.002) for e in ev]);X=np.array([np.ones(len(n)),n]).T;W=1/err**2;cv=np.linalg.inv(X.T@(W[:,None]*X));v=cv@(X.T@(W*t));res=t-X@v
 out[tic]=dict(period_d=v[1],epoch_btjd=v[0],formal_period_error_d=cv[1,1]**.5,cycles=n.tolist(),times=t.tolist(),residuals=res.tolist(),duration_d=float(np.median([e['duration_d'] for e in ev])),depth_ppt=float(np.median([e['depth_ppt'] for e in ev])),max_residual_d=float(max(abs(res))),gaia_period_d=float(json.loads((b/tic/'lead-context.json').read_text())['gaia_period_d']),note='Trials inferred from eclipse intervals; integer-cycle selection requires covered-window audit. Timing error includes cadence/2 and .002d floors.')
 print(tic,v,'res',res)
(b/'lead-clocks.json').write_text(json.dumps(out,indent=2))




