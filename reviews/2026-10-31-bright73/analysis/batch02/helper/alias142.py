import json,numpy as np
from astropy.io import fits
from pathlib import Path
m=json.load(open('142932503/measurements.json')); ev=m['events']; t=np.array([e['mid_btjd'] for e in ev]); err=np.array([e['timing_error_days'] for e in ev]);
# Counts for periods between 1 and 25 d; fit three observed centers (not predictions).
rows=[]
for n1 in range(36,898):
 for n2 in [round(n1*(t[2]-t[0])/(t[1]-t[0]))]:
  if n2<=n1:continue
  n=np.array([0,n1,n2]);x=np.column_stack((np.ones(3),n));w=1/err**2; c=np.linalg.inv(x.T@(w[:,None]*x)); b=c@x.T@(w*t); resid=t-x@b
  if np.max(abs(resid))<.05:rows.append([n1,n2,float(b[1]),*[float(z) for z in resid]])
print('aliases residual < .05 d',rows)
# For integer submultiples check predicted eclipse centers in clean data: local median in +/- .05d relative to side bands .15-.4d.
for div in [2,3,4]:
 p=m['period_days']/div; epoch=m['primary_epoch_btjd']; checks=[]
 for src in m['sources']:
  with fits.open(src['path']) as h:
   a=h[1].data; tt=np.asarray(a['TIME'],float);f=np.asarray(a['SAP_FLUX'],float);q=np.asarray(a['QUALITY']);ok=np.isfinite(tt)&np.isfinite(f)&(q==0)&(f>0);tt=tt[ok];f=f[ok]
  for n in range(int(np.ceil((min(tt)-epoch)/p)),int(np.floor((max(tt)-epoch)/p))+1):
   if n%div==0:continue
   center=epoch+n*p; inn=abs(tt-center)<.05; side=(abs(tt-center)>.15)&(abs(tt-center)<.4)
   if sum(inn)>=3 and sum(side)>=8:checks.append([src['sector'],round(center,5),int(sum(inn)),round(float(1-np.median(f[inn])/np.median(f[side])),5)])
 print('divisor',div,'checks',checks)
