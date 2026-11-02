from pathlib import Path
import csv,json,numpy as np
from astropy.io import fits
b=Path(__file__).parent;out={}
for r in csv.DictReader(open(b/'queue.csv')):
 tic=r['tic'];m=json.load(open(b/tic/'measurements.json'));P=m['period_days'];ep=m['primary_epoch_btjd'];dur=np.median([e['duration_days'] for e in m['events'] if e.get('timing_usable')]);wins=[]
 for s in m['sources']:
  with fits.open(s['path']) as h:a=h[1].data;t=np.array(a['TIME']);f=np.array(a['SAP_FLUX']);q=np.array(a['QUALITY'])
  good=np.isfinite(t)&np.isfinite(f)&(f>0);tt=t[good];ff=f[good];qq=q[good]
  for n in range(int(np.ceil((tt.min()-ep)/P-.5)),int(np.floor((tt.max()-ep)/P-.5))+1):
   c=ep+(n+.5)*P;dt=abs(tt-c);core=(dt<dur*.25)&(qq==0);pre=(tt<c-.75*dur)&(tt>c-1.75*dur)&(qq==0);post=(tt>c+.75*dur)&(tt<c+1.75*dur)&(qq==0)
   covered=min(sum(core),sum(pre),sum(post))>=3
   base=.5*(np.median(ff[pre])+np.median(ff[post])) if covered else None;dep=1000*(1-np.median(ff[core])/base) if covered else None;wins.append(dict(sector=s['sector'],orbital_cycle=n,predicted_half_phase_btjd=c,n_quality_zero_core=int(sum(core)),n_flagged_core=int(sum((dt<dur*.25)&(qq!=0))),n_pre=int(sum(pre)),n_post=int(sum(post)),clean_bilateral_coverage=bool(covered),n_finite_core=int(sum(dt<dur*.25)),local_core_depth_ppt=float(dep) if dep is not None else None))
 out[tic]=dict(half_period_predicted_opposite_phase_windows=wins,note='Predicted half-phase search windows, not measured timings. Counts refer to quality-zero finite positive SAP; flagged cadences reported separately, never a clean null. Core depth is descriptive local sideband statistic, not fitted secondary depth or significance. Unequal measured secondaries reject P/2 as same-kind recurrence; for cases without secure secondaries use the explicit sampled coverage; baseline noise limits shallower claims.')
json.dump(out,open(b/'half-period-coverage.json','w'),indent=2)
