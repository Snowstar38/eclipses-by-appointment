"""Exploratory H042 A-eclipse timing with a local baseline plus Gaussian dip."""
import json,hashlib
from pathlib import Path
import numpy as np
from astropy.io import fits
from scipy.optimize import least_squares
B=Path(__file__).resolve().parent;T=B/'313617927'
s=json.loads((T/'raw-inspection.json').read_text())
windows=[(15,1729.9,2.5),(17,1768.4,2.5),(56,2845.5,2.5),(76,3383.5,2.5),(77,3422.0,2.5),(83,3576.5,2.5)]
out=[]
for sector,guess,half in windows:
 r=next(x for x in s['sectors'] if x['sector']==sector);p=Path(r['path']);assert hashlib.sha256(p.read_bytes()).hexdigest()==r['sha256']
 with fits.open(p,memmap=False) as h:
  a=h[1].data;t=np.asarray(a['TIME'],float);f=np.asarray(a['SAP_FLUX'],float);q=np.asarray(a['QUALITY'],int)
 ok=np.isfinite(t)&np.isfinite(f)&(f>0)&(q==0)&(abs(t-guess)<half);t=t[ok];y=f[ok]/np.median(f[ok]);x=t-guess
 def model(p):
  base,slope,curve,depth,center,width=p
  return base+slope*x+curve*x*x-depth*np.exp(-.5*((x-center)/width)**2)
 p0=[1,0,0,.04,0,.7];lo=[.7,-.1,-.05,.005,-1.5,.2];hi=[1.3,.1,.05,.2,1.5,2.0]
 fit=least_squares(lambda p:model(p)-y,p0,bounds=(lo,hi),loss='soft_l1',f_scale=.004,max_nfev=10000)
 p=fit.x;res=y-model(p)
 out.append({'sector':sector,'guess_btjd':guess,'center_btjd':float(guess+p[4]),'gaussian_depth_ppt':float(1000*p[3]),'width_days':float(p[5]),'n_quality0':len(t),'residual_mad_ppt':float(1482.6*np.median(abs(res-np.median(res)))),'fit_success':bool(fit.success),'center_at_bound':bool(abs(p[4])>1.45 or p[5]>.95*2.0)})
print(out)
pair=[]
for a,b in zip(out,out[1:]):
 delta=b['center_btjd']-a['center_btjd'];n=round(delta/38.43154404731203)
 pair.append({'from_sector':a['sector'],'to_sector':b['sector'],'elapsed_days':delta,'gaia_cycle_count':n,'conditional_period_days':delta/n if n else None,'gaia_minus_elapsed_days':delta-n*38.43154404731203})
payload={'tic':'313617927','gaia_period_days':38.43154404731203,'method':'Local quadratic baseline plus Gaussian trough, soft_l1. Approximate, broad asymmetric spots and partial/gapped sectors can bias center.','a_like_events':out,'consecutive_alias_checks':pair}
(T/'a-timing.json').write_text(json.dumps(payload,indent=2)+'\n')
