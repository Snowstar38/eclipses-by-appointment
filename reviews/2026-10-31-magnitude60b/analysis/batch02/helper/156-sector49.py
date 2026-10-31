import numpy as np,json,hashlib
from scipy.optimize import curve_fit
from astropy.io import fits
from pathlib import Path
out=Path('[local path omitted]');res=json.load(open(out/'156-independent.json'));ev=[]
for cycle,x in enumerate(res['events']):ev.append(dict(sector=22,cycle=cycle,mid_btjd=x['measured_btjd'],timing_error_days=x['half_cadence_days'],depth_ppt=x['depth_ppt'],method='quadratic through 3-4 trough samples, cadence/2 allowance'))
p=out.parent.parent/'shared-qlp/156985493_s049.fits'
with fits.open(p) as h:
 a=h[1].data;t=np.array(a['TIME']);y=np.array(a['SAP_FLUX']);q=np.array(a['QUALITY']);cad=np.nanmedian(np.diff(t[np.isfinite(t)]));
 for cycle,c in [(74,2644.25),(76,2664.15)]:
  ok=np.isfinite(t)&np.isfinite(y)&(q==0)&(abs(t-c)<.18);x=t[ok]-c;v=y[ok]/np.median(y[ok]);
  def model(x,b,s,d,mu,sig):return b+s*x-d*np.exp(-.5*((x-mu)/sig)**2)
  f,cov=curve_fit(model,x,v,p0=[1,0,.012,0,.025],bounds=([.9,-.1,0,-.07,.005],[1.1,.1,.1,.07,.08]),maxfev=10000)
  ev.append(dict(sector=49,cycle=cycle,mid_btjd=float(c+f[3]),timing_error_days=float(max(cad/2,np.sqrt(cov[3,3]))),formal_timing_error_days=float(np.sqrt(cov[3,3])),depth_ppt=float(f[2]*1000),gaussian_sigma_days=float(f[4]),sample_count=len(x),method='Gaussian plus linear baseline, unflagged SAP, sigma max(formal, cadence/2)',source_sha256=hashlib.sha256(p.read_bytes()).hexdigest()))
res['combined_events']=ev;res['caution']='Quadratic 3-4-point and Gaussian timing mix; cadence floor is an allowance, not total or calibrated uncertainty. Sector 49 event cycle75 is interrupted by scattered light/gap.'
(out/'156-independent.json').write_text(json.dumps(res,indent=2));print(json.dumps(ev,indent=2))
