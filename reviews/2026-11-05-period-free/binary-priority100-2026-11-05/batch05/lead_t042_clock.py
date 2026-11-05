"""Conditional four-center clock, with explicit cycle assignment and errors."""
import json
from pathlib import Path
import numpy as np
B=Path(__file__).resolve().parent/'255912894'
d=json.loads((B/'lead-numeric.json').read_text());third=json.loads((B/'lead-third.json').read_text());fourth=json.loads((B/'lead-fourth.json').read_text())
first,last=d['events']
events=[dict(sector=13,cycle=0,center=first['fit_mid_btjd'],formal=first['fit_mid_formal_error_days'],cadence=.0208333333),dict(sector=66,cycle=30,center=third['fit_center_btjd'],formal=third['formal_error_days'],cadence=.0023148148),dict(sector=100,cycle=51,center=last['fit_mid_btjd'],formal=last['fit_mid_formal_error_days'],cadence=.0023148148),dict(sector=102,cycle=52,center=fourth['fit_center_btjd'],formal=fourth['formal_error_days'],cadence=.0023148148)]
for e in events:e['adopted_error_days']=max(e['formal'],e['cadence']/2)
x=np.asarray([e['cycle'] for e in events],float);y=np.asarray([e['center'] for e in events]);er=np.asarray([e['adopted_error_days'] for e in events]);X=np.column_stack((np.ones(len(x)),x));W=1/er**2;cov=np.linalg.inv(X.T@(W[:,None]*X));beta=cov@(X.T@(W*y));res=y-X@beta;chi2=float(sum((res/er)**2));scale=max(1,chi2/(len(x)-2));cov*=scale
result=dict(tic='255912894',eclipse_kind='selected narrow dip; primary identity not established',cycle_assignment='0,30,51,52; S13 to S100 51 cycles, S102 one after S100',events=events,primary_epoch_btjd=float(beta[0]),epoch_error_days=float(np.sqrt(cov[0,0])),period_days=float(beta[1]),period_formal_error_days=float(np.sqrt(cov[1,1])),reduced_chi_square=chi2/(len(x)-2),residual_days=res.tolist(),error_meaning='Weighted linear clock; each center error max(trapezoid covariance, half QLP cadence), scatter inflated if chi2/dof > 1. No instrumental/systematic timing calibration. The cycle count is independently tested with actual covered nulls in lead-alias.json.')
(B/'lead-clock.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8');print(json.dumps(result,indent=2))
