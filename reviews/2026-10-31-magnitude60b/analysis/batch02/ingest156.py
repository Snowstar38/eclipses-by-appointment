import json,numpy as np,shutil
from pathlib import Path
B=Path(__file__).parent;p=B/'156985493/measurements.json'
if not p.with_name('pipeline_measurements.json').exists():shutil.copy2(p,p.with_name('pipeline_measurements.json'))
m=json.load(open(p));ev=json.load(open(B/'helper/156-independent.json'))['combined_events']
for e in ev:e['timing_usable']=True;e['duration_days']=.05;e['duration_kind']='Approximate sector22 TESScut FWHM, not individual fitted duration'
n=np.array([e['cycle'] for e in ev]);t=np.array([e['mid_btjd'] for e in ev]);er=np.array([e['timing_error_days'] for e in ev]);X=np.array([np.ones(len(n)),n]).T;cov=np.linalg.inv((X/er[:,None]).T@(X/er[:,None]));beta=cov@((X/er[:,None]).T@(t/er));res=t-X@beta;red=float(sum((res/er)**2)/(len(n)-2));cov*=max(red,1)
m.update(events=ev,epoch_kind='Selected repeating narrow eclipse; primary by convention, relative secondary depth unestablished',timing_event_count=4,period_days=float(beta[1]),period_error_days=float(np.sqrt(cov[1,1])),primary_epoch_btjd=float(beta[0]),epoch_cycle=0,timing_residual_days=res.tolist(),reduced_chi_square=red,error_meaning='Weighted linear fit to two sparse quadratic trough centers at sector22 and two free Gaussian plus linear centers at sector49. Inputs max(formal covariance where available, half cadence); sector22 half cadence is a coarse allowance. Covariance inflated if reduced chi square exceeds one. Mixed-model, cadence-smearing, baseline and pipeline systematics are not calibrated, not total uncertainty or coverage.',depth_ppt=float(np.median([e['depth_ppt'] for e in ev])),custom_extraction='helper/156-independent.json combined_events; original empty generic extraction retained pipeline_measurements.json')
json.dump(m,open(p,'w'),indent=2)
