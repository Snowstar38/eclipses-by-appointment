import json,numpy as np
from pathlib import Path
B=Path(__file__).resolve().parent; out=[]
for p in sorted(B.glob('*/measurements.json')):
 m=json.loads(p.read_text(encoding='utf8'));ev=[e for e in m['events'] if e.get('timing_usable')];errs=[]
 for e in ev:
  dep=e['model_amplitude_ppt']*min(1,e['duration_days']/(2*e['ingress_parameter_days']));errs.append(abs(dep-e['depth_ppt']))
 if len(ev)>=2:
  n=np.array([e['cycle'] for e in ev],float);t=np.array([e['mid_btjd'] for e in ev]);sig=np.array([e['timing_error_days'] for e in ev]);A=np.column_stack([np.ones(len(n)),n-n.min()])/sig[:,None];b=t/sig;coef=np.linalg.lstsq(A,b,rcond=None)[0];dp=coef[1]-m['period_days'];de=coef[0]-m['reference_epoch_btjd']
 else:dp=de=None
 out.append(dict(tic=m['tic'],n=len(ev),max_depth_discrepancy_ppt=max(errs,default=None),period_difference_days=dp,epoch_difference_days=de,median_depth_ppt=float(np.median([e['depth_ppt'] for e in ev])) if ev else None))
print(json.dumps(out,indent=2));(B/'helper-numeric-audit.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf8')
