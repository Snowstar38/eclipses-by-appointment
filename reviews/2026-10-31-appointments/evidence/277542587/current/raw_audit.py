"""Bounded representative raw-SAP sanity checks; no historical writes."""
from pathlib import Path
import json, hashlib
import numpy as np
from astropy.io import fits
OUT=Path(__file__).parent
D=Path('[local path omitted]')
jobs=[(466336052,55,2818.483,9.62),(466336052,82,3557.684,9.64),
      (64066759,87,3674.521,4.16),(64066759,88,3715.459,4.22),
      (49416839,36,2286.853,6.05),(49416839,72,3272.5624,5.79),
      (60583013,33,2210.9657,9.77),(60583013,33,2225.0600,10.4),
      (60583013,6,1478.8272,9.4)]
results=[]
for tic,sec,t0,dur in jobs:
 p=D/f'{tic}_s{sec:03d}.fits'
 with fits.open(p) as h:
  z=h[1].data;t=np.array(z['TIME'],float);f=np.array(z['SAP_FLUX'],float);q=np.array(z['QUALITY'])
 k=np.isfinite(t)&np.isfinite(f)&(f>0)&(q==0)&(abs(t-t0)<0.8)
 x=t[k]-t0;y=f[k]/np.nanmedian(f[k]);inner=abs(x)<dur/24/4;outer=(abs(x)>dur/24*0.6)&(abs(x)<0.8)
 co=np.polyfit(x[outer],y[outer],1);base=np.polyval(co,x)
 dep=float(np.median(1-y[inner]/base[inner]))
 results.append(dict(tic=tic,sector=sec,t0_btjd=t0,central_half_median_depth_ppt=dep*1000,n_inner=int(inner.sum()),n_outer=int(outer.sum()),source=str(p),sha256=hashlib.sha256(p.read_bytes()).hexdigest()))
print(json.dumps(results,indent=2))
(OUT/'raw-audit.json').write_text(json.dumps(results,indent=2)+'\n')
