import json,numpy as np
from pathlib import Path
B=Path(__file__).resolve().parent;p=B/'lead-clocks.json';d=json.loads(p.read_text());(B/'initial-minima-diagnostics.json').write_text(json.dumps(d,indent=2))
# Only local coherent primary sequences used. Independent helper refines short clocks.
r=json.loads((B/'27681485/lead-trapezoids.json').read_text());use=[r[0],r[1],r[3]];t=np.array([v['center_btjd'] for v in use]);n=np.array([0,1,21]);X=np.stack([np.ones(3),n],axis=1);err=np.array([.03,.03,.15]);W=1/err**2;cov=np.linalg.inv(X.T@(W[:,None]*X));b=cov@(X.T@(W*t));d['27681485']=dict(period_d=float(b[1]),epoch_btjd=float(b[0]),event_btjd=t.tolist(),cycles=n.tolist(),adopted_conservative_timing_allowances_d=err.tolist(),residuals_d=(t-X@b).tolist(),timing_note='S44/S45 complete local trapezoid events; S72 compatible notch on steep trend, model dependent. Allowances are conservative guides, not calibrated statistical errors. Partial S46 and S71 support shape only, not timings. Initial centroid estimate superseded.',events=r)
p.write_text(json.dumps(d,indent=2));print(d['27681485'])
