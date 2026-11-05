"""Exclude visibly non-identifiable centers; preserve the fitted event records."""
import json
from pathlib import Path
import numpy as np

B=Path(__file__).resolve().parent
p=B/'121277143'/'measurements.json'
m=json.loads(p.read_text(encoding='utf-8'))
reasons={40:'Only ingress and minimum are usable; egress is in a data gap.',53:'Broad baseline modulation blends with the sharp eclipse; fitted center and duration are not identifiable.'}
for e in m['events']:
    if e.get('sector') in reasons and e.get('timing_usable'):
        e['timing_usable']=False
        e['timing_exclusion_reason']=reasons[e['sector']]
good=[e for e in m['events'] if e.get('timing_usable')]
n=np.array([e['cycle'] for e in good]); t=np.array([e['mid_btjd'] for e in good]);err=np.array([e['timing_error_days'] for e in good])
X=np.column_stack([np.ones(len(n)),n-n.min()]);A=X/err[:,None];C=np.linalg.inv(A.T@A);beta=C@(A.T@(t/err));res=t-X@beta
red=float(np.sum((res/err)**2)/(len(n)-2));C*=max(red,1)
m.update(timing_event_count=len(good),period_days=float(beta[1]),period_error_days=float(np.sqrt(C[1,1])),reference_epoch_btjd=float(beta[0]),epoch_error_days=float(np.sqrt(C[0,0])),reference_cycle=int(n.min()),reduced_chi_square=red,timing_residual_days=res.tolist(),depth_ppt=float(np.median([e['depth_ppt'] for e in good])),timing_curation='Sector 40 gap-shaped ingress-only and sector 53 broad modulated dip excluded from timing; both remain in event list and visible panel.')
p.write_text(json.dumps(m,indent=2)+'\n',encoding='utf-8')
print(m['period_days'],m['period_error_days'],m['reduced_chi_square'],len(good))
