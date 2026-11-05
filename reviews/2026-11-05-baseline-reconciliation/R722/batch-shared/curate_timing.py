"""Remove gap-constrained center estimates from adopted ephemerides, preserving detections."""
import json
from pathlib import Path
import numpy as np
B=Path(__file__).resolve().parent
for tic,reasons in [('260797021',{67:'Ingress lies in a data gap; exclude model-dependent reconstructed contact from precision timing.'}),('349527829',{91:'Ingress is in a data gap; conditional two-event estimate retained in original fit fields, not a secure orbital ephemeris.'})]:
 p=B/tic/'measurements.json';m=json.loads(p.read_text())
 for e in m['events']:
  if e.get('sector') in reasons:e['timing_usable']=False;e['timing_exclusion_reason']=reasons[e['sector']]
 good=[e for e in m['events'] if e.get('timing_usable')];m['timing_event_count']=len(good)
 if len(good)>=2:
  n=np.array([e['cycle'] for e in good]);tt=np.array([e['mid_btjd'] for e in good]);er=np.array([e['timing_error_days'] for e in good]);X=np.column_stack([np.ones(len(n)),n-n.min()]);A=X/er[:,None];C=np.linalg.inv(A.T@A);be=C@(A.T@(tt/er));res=tt-X@be;red=float(sum((res/er)**2)/(len(n)-2)) if len(n)>2 else None;C*=max(red or 1,1);m.update(period_days=float(be[1]),period_error_days=float(np.sqrt(C[1,1])),reference_epoch_btjd=float(be[0]),epoch_error_days=float(np.sqrt(C[0,0])),reference_cycle=int(n.min()),reduced_chi_square=red,timing_residual_days=res.tolist(),depth_ppt=float(np.median([e['depth_ppt'] for e in good])))
 else:m['conditional_fit_warning']='Original two-event fit fields retained only as a tested conditional hypothesis; second event gap means center also model-dependent. Generic ephemeris is blank.'
 p.write_text(json.dumps(m,indent=2)+'\n')
