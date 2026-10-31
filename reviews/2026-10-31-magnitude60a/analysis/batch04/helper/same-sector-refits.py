import numpy as np,json
from pathlib import Path
from scipy.optimize import least_squares
from astropy.io import fits
B=Path('[local path omitted]'); results={}
for tic,sector,centers in [('362822264',39,[2366.855,2384.977]),('314047448',24,[1956.523,1972.899])]:
 m=json.load(open(B/tic/'measurements.json')); d=json.load(open(Path('[local path omitted] 5/made/sb1-scale/diffimg')/tic/f'diff_s{sector}.json')); ix,iy=[round(z) for z in d['target_px']];dur=np.median([e['duration_days'] for e in m['events'] if e.get('timing_usable')]);p=Path(f'[local path omitted]')
 with fits.open(p) as h: a=h[1].data;t=np.array(a['TIME']);q=np.array(a['QUALITY']);f=np.nansum(a['FLUX'][:,iy-1:iy+2,ix-1:ix+2],axis=(1,2))
 ev=[]
 for c in centers:
  mask=(q==0)&np.isfinite(t)&np.isfinite(f)&(abs(t-c)<3*dur);x=t[mask]-c;y=f[mask];oot=abs(x)>dur;y=y/np.median(y[oot]);
  def fn(z):
   b,s,depth,mid,w,k=z;return b+s*x-depth*np.clip((w/2-abs(x-mid))/k,0,1)-y
  z=least_squares(fn,[1,0,.01,0,dur,dur*.25],bounds=([.5,-1,0,-dur,.3*dur,.01*dur],[1.5,1,1,dur,3*dur,1.4*dur]),max_nfev=30000); noise=np.std(fn(z.x)); cov=np.linalg.pinv(z.jac.T@z.jac)*noise**2; err=max(float(np.sqrt(max(cov[3,3],0))),float(np.median(np.diff(t[mask]))/2)); ev.append({'mid_btjd':float(c+z.x[3]),'error_days':err,'depth_ppt':float(z.x[2]*1000),'duration_days':float(z.x[4]),'residual_rms_ppt':float(noise*1000),'n':len(x),'boundary_center':bool(abs(z.x[3])>.95*dur)})
 results[tic]={'sector':sector,'events':ev,'difference_days':ev[1]['mid_btjd']-ev[0]['mid_btjd'],'difference_error_days':float(np.hypot(ev[0]['error_days'],ev[1]['error_days'])),'expected_days':m['period_days'],'note':'Local 3x3 free trapezoid; uncertainty from residual covariance floored by half cadence; not total systematic uncertainty.'}
print(json.dumps(results,indent=2));json.dump(results,open(B/'helper/same-sector-refits.json','w'),indent=2)
