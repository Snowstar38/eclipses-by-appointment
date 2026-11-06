import json,numpy as np
from pathlib import Path
from astropy.io import fits
B=Path(__file__).resolve().parent;p=B/'122766753'/'helper-short-cut-s59.fits'
with fits.open(p) as h:
 a=h[1].data;t=np.array(a['TIME']);q=np.array(a['QUALITY']);f=np.array(a['FLUX'])
out=[]
for c in [2919.30511926,2921.52398363,2925.94262409,2932.56833635]:
 ok=(q==0)&np.isfinite(t); i=ok&(abs(t-c)<.035);b=ok&(abs(t-c)>.12)&(abs(t-c)<.30);d=np.nanmedian(f[b],axis=0)-np.nanmedian(f[i],axis=0);d-=np.nanmedian(np.r_[d[0],d[-1],d[1:-1,0],d[1:-1,-1]]);w=np.maximum(d,0);w[:1]=0;w[6:]=0;w[:,:1]=0;w[:,6:]=0;y,x=np.indices(d.shape);out.append(dict(center=c,n_in=int(i.sum()),n_base=int(b.sum()),peak=list(map(int,np.unravel_index(np.nanargmax(d),d.shape)[::-1])),centroid=[float((w*x).sum()/w.sum()),float((w*y).sum()/w.sum())],diff=d.tolist()))
(B/'helper-y006-events.json').write_text(json.dumps(out,indent=2));print(json.dumps([{k:v for k,v in x.items() if k!='diff'} for x in out],indent=2))
