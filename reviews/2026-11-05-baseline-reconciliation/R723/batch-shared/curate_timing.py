import json
from pathlib import Path
import numpy as np
B=Path(__file__).resolve().parent
p=B/'421331604'/'measurements.json';m=json.loads(p.read_text())
for e in m['events']:
 if e['sector']==26:e.update(timing_usable=False,timing_exclusion_reason='Only egress is covered; unconstrained ingress and bottom make a model-dependent center/depth, excluded from ephemeris and depth summary.')
good=[e for e in m['events'] if e.get('timing_usable')];m['timing_event_count']=len(good)
n=np.array([e['cycle'] for e in good]);tt=np.array([e['mid_btjd'] for e in good]);er=np.array([e['timing_error_days'] for e in good]);X=np.column_stack([np.ones(len(n)),n-n.min()]);A=X/er[:,None];C=np.linalg.inv(A.T@A);be=C@(A.T@(tt/er));res=tt-X@be;red=float(sum((res/er)**2)/(len(n)-2));C*=max(red,1);m.update(period_days=float(be[1]),period_error_days=float(np.sqrt(C[1,1])),reference_epoch_btjd=float(be[0]),epoch_error_days=float(np.sqrt(C[0,0])),reference_cycle=int(n.min()),reduced_chi_square=red,timing_residual_days=res.tolist(),depth_ppt=float(np.median([e['depth_ppt'] for e in good])))
p.write_text(json.dumps(m,indent=2)+'\n')
