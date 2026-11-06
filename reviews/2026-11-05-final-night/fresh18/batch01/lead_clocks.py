import json,math
from pathlib import Path
import numpy as np
B=Path(__file__).resolve().parent
P=json.loads((B.parent.parent/'fresh-band-next400'/'population.json').read_text())['targets']
CHOICES={'22559994':('deep',47.12),'65684549':('candidate',1.1372),'70554665':('candidate',29.42),'111230893':('candidate',21.694),'122766753':('candidate',2.21),'140777703':('candidate',25.067),'156747165':('deep',37.887)}
out={}
for tic,(kind,trial) in CHOICES.items():
 events=[e for e in json.loads((B/tic/'lead-timing.json').read_text()) if e['kind']==kind and e.get('fit_usable')]
 first=events[0]['center_btjd'];n=np.array([round((e['center_btjd']-first)/trial) for e in events],int)
 t=np.array([e['center_btjd'] for e in events]);err=np.array([max(e['center_formal_error_d'],e['cadence_d']/2) for e in events])
 X=np.stack([np.ones(len(t)),n],axis=1);W=1/err**2;cov=np.linalg.inv(X.T@(W[:,None]*X));beta=cov@(X.T@(W*t));res=t-X@beta
 red=float(np.sum((res/err)**2)/max(len(t)-2,1));infl=max(1,red)**.5
 out[tic]=dict(event_kind=kind,cycle_trial_d=trial,cycles=n.tolist(),event_btjd=t.tolist(),conservative_errors_d=err.tolist(),period_d=float(beta[1]),formal_period_error_d=float(cov[1,1]**.5),scatter_inflated_period_error_d=float(cov[1,1]**.5*infl),epoch_btjd=float(beta[0]),residuals_d=res.tolist(),rms_residual_d=float(np.std(res)),reduced_chi_square=red,gaia_period_d=float(P[tic]['gaia']['period']),note='Cycle integers assumed from trial; uniqueness needs explicit alias/null audit. Errors are local trapezoid covariance with cadence floor; inflation is scatter diagnostic, not total calibrated uncertainty.')
 print(tic,'P',round(beta[1],8),'rms',round(np.std(res),5),'cycles',n.tolist())
(B/'lead-clocks.json').write_text(json.dumps(out,indent=2),encoding='utf8')

