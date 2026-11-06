import json,numpy as np
from pathlib import Path
b=Path(__file__).resolve().parent;out={}
for tic,p in [('365657271',41.66),('48099288',37.86)]:
 ev=[e for e in json.loads((b/tic/'lead-timing.json').read_text()) if e.get('fit_usable') and (tic=='48099288' or e['kind']=='kindA')];ev.sort(key=lambda e:e['center_btjd'])
 t=np.array([e['center_btjd'] for e in ev]);n=np.round((t-t[0])/p).astype(int);err=np.array([max(e['center_formal_error_d'],e['cadence_d']/2,.004 if tic=='365657271' else .002) for e in ev]);X=np.array([np.ones(len(n)),n]).T;W=1/err**2;cv=np.linalg.inv(X.T@(W[:,None]*X));v=cv@(X.T@(W*t));res=t-X@v
 out[tic]=dict(period_d=float(v[1]),epoch_btjd=float(v[0]),formal_period_error_d=float(cv[1,1]**.5),cycles=n.tolist(),times=t.tolist(),residuals=res.tolist(),duration_d=float(np.median([e['duration_d'] for e in ev])),depth_ppt=float(np.median([e['depth_ppt'] for e in ev])),max_residual_d=float(max(abs(res))),note='Representative same-kind formal WLS clock; cadence/2 with .004d E034 or .002d E029 floor. Partial events excluded; integer and joint Gaia audit separate.')
 print(tic,out[tic])
(b/'lead-clocks.json').write_text(json.dumps(out,indent=2))
