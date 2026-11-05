import numpy as np,json,hashlib
from astropy.io import fits
from pathlib import Path
p=Path(r'[local-path-redacted]'); tic='318209162'; t0=1891.8695566370886; t1=2603.6263408804184
out={}
for n in range(25,34):
 per=(t1-t0)/n; occasions=[]
 for f in p.glob(tic+'_s*.fits'):
  with fits.open(f) as h:
   d=h[1].data; t=np.array(d['TIME']); y=np.array(d['SAP_FLUX']); good=np.isfinite(t)&np.isfinite(y)&(d['QUALITY']==0); t=t[good]; y=y[good]; cad=np.median(np.diff(t));
   for k in range(-5,n+6):
    c=t0+k*per
    if t.min()-.2<c<t.max()+.2:
     masks=[(t>=c-.06)&(t<=c+.06),(t>=c-.24)&(t<c-.12),(t>c+.12)&(t<=c+.24)]
     counts=[int(np.sum(m)) for m in masks]; expected=[.12/cad]*3
     depths=None
     if all(v>=.7*e for v,e in zip(counts,expected)):
      depths=1-np.median(y[masks[0]])/np.median(np.r_[y[masks[1]],y[masks[2]]])
     occasions.append(dict(file=f.name,k=k,center=c,counts=counts,cadence=cad,depth=None if depths is None else float(depths),nearest=float(np.min(abs(t-c)))))
 out[str(n)]={'period':per,'occasions':occasions}
open('batch01/helper-N006-alias.json','w').write(json.dumps(out,indent=2))
for n,v in out.items(): print(n,round(v['period'],5),[(o['k'],round(o['center'],3),o['counts'],None if o['depth'] is None else round(o['depth']*1000,2)) for o in v['occasions']])

