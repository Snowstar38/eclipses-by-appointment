"""Reproduce the H046 deep-eclipse clock from local raw SAP minima."""
import json
from pathlib import Path
import numpy as np
B=Path(__file__).resolve().parent
tic='246124257';d=json.loads((B/tic/'event-check.json').read_text())
events=[{'sector':s['sector'],**m} for s in d['sectors'] for m in s['minima'] if m['residual_depth_ppt']>5.5]
t=np.array([z['btjd'] for z in events]); n=np.rint((t-2362.419)/3.41961).astype(int)
keep=np.abs(t-(2362.419+3.41961*n))<.2
coef=np.polyfit(n[keep],t[keep],1);p,epoch=map(float,coef)
for z,cyc,selected in zip(events,n,keep):
    z['cycle_from_epoch']=int(cyc);z['clock_residual_days']=float(z['btjd']-(epoch+p*cyc));z['selected_for_clock']=bool(selected)
out={'tic':tic,'clock_source':'QUALITY=0 raw SAP, one-day median detrend; local minima >5.5 ppt and within 0.2 d of trial 3.41961 d clock; two other detections excluded as off-clock','period_days':p,'epoch_btjd':epoch,'n_selected':int(sum(keep)),'selected_residual_std_days':float(np.std(t[keep]-(epoch+p*n[keep]))),'events':events,'caution':'Minima are cadence/grid values, and formal timing uncertainty is not estimated. Period/epoch are an exploratory coherent clock, not a Gaia orbital solution. Long-baseline alias alternatives are constrained by many same-sector cycles and repeated sectors but require formal transit timing to eliminate all cycle-count possibilities.'}
(B/tic/'deep-clock.json').write_text(json.dumps(out,indent=2)+'\n')
print(p,epoch,sum(keep),out['selected_residual_std_days'])
