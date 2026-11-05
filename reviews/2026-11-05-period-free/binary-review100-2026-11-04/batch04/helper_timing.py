"""Bounded local trapezoid fits to visually selected complete raw SAP events."""
import hashlib, json
from pathlib import Path
import numpy as np
from astropy.io import fits
from scipy.optimize import least_squares

B=Path(__file__).resolve().parent
CASES={'372989764':[(39,2379.7,3),(66,3114.25,3),(103,4159.6,3),(104,4187.8,3)]}
def model(x,p):
 base,slope,depth,center,dur,ingress=p
 return base+slope*x-depth*np.clip((dur/2-np.abs(x-center))/ingress,0,1)
for tic,windows in CASES.items():
 src=json.loads((B/tic/'raw-inspection.json').read_text()); out=[]
 for sector,guess,half in windows:
  rec=next(s for s in src['sectors'] if s['sector']==sector)
  fp=Path(rec['path'])
  assert hashlib.sha256(fp.read_bytes()).hexdigest()==rec['sha256']
  with fits.open(fp,memmap=False) as h:
   a=h[1].data;t=np.asarray(a['TIME'],float);f=np.asarray(a['SAP_FLUX'],float);q=np.asarray(a['QUALITY'],int)
  ok=np.isfinite(t)&np.isfinite(f)&(f>0)&(q==0)&(abs(t-guess)<half)
  t=t[ok];f=f[ok];x=t-guess;y=f/np.median(f)
  depth=.13 if tic=='294257329' else .018
  p0=[1,0,depth,0,2 if tic=='294257329' else .8,.4 if tic=='294257329' else .12]
  lo=[.7,-.04,.001,-.6,.35,.025];hi=[1.3,.04,.3,.6,4.5,1.5]
  fit=least_squares(lambda p:model(x,p)-y,p0,bounds=(lo,hi),loss='soft_l1',f_scale=.003,max_nfev=10000)
  p=fit.x;res=y-model(x,p)
  out.append({'sector':sector,'guess_btjd':guess,'n_quality0':int(len(x)),'center_btjd':float(guess+p[3]),'depth_ppt':float(1000*p[2]),'duration_days':float(p[4]),'ingress_days':float(p[5]),'baseline_slope_per_day':float(p[1]),'residual_mad_ppt':float(1482.6*np.median(abs(res-np.median(res)))),'success':bool(fit.success),'caution':'Exploratory local linear-baseline trapezoid; gaps and baseline trends can bias timing/depth.'})
 (B/'helper-local-fits.json').write_text(json.dumps({'tic':tic,'fits':out},indent=2)+'\n')
 print(tic,[(o['sector'],round(o['center_btjd'],4),round(o['depth_ppt'],1)) for o in out],flush=True)

