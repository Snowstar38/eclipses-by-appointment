import json
from pathlib import Path
import numpy as np
B=Path(__file__).resolve().parent;out={}
for tic in ('241479387','421331604'):
 m=json.loads((B/tic/'measurements.json').read_text());es=[e for e in m['events'] if e.get('timing_usable')];loo=[]
 for e0 in es:
  rest=[e for e in es if e is not e0];n=np.array([e['cycle'] for e in rest]);t=np.array([e['mid_btjd'] for e in rest]);er=np.array([e['timing_error_days'] for e in rest]);X=np.column_stack((np.ones(len(n)),n-n.min()));v=np.linalg.lstsq(X/er[:,None],t/er,rcond=None)[0];loo.append(dict(omitted_sector=e0['sector'],omitted_cycle=e0['cycle'],period_days=float(v[1]),difference_from_adopted_days=float(v[1]-m['period_days'])))
 out[tic]=dict(accepted_event_count=len(es),adopted_period_days=m['period_days'],conditional_fit_error_days=m['period_error_days'],leave_one_event_out=loo,note='Sensitivity diagnostic using identical source midpoints and weights; not an independent timing measurement or calibrated systematic allowance.')
(B/'timing-sensitivity.json').write_text(json.dumps(out,indent=2)+'\n');print(out)
