import numpy as np,json,hashlib
from astropy.io import fits
from astropy.wcs import WCS
from pathlib import Path
B=Path(__file__).resolve().parent;p=B/'62374377/s105-tesscut.fits';tm=4217.35
with fits.open(p) as h:
 print(h.info());t=np.array(h[1].data['TIME']);f=np.array(h[1].data['FLUX']);q=np.array(h[1].data['QUALITY']);w=WCS(h[2].header)
g=np.isfinite(t)&(q==0)&np.isfinite(f).all(axis=(1,2));t=t[g];f=f[g];x=t-tm; core=abs(x)<.3;pre=(x>-1.5)&(x<-1);post=(x>1)&(x<1.5);base=.5*(np.median(f[pre],axis=0)+np.median(f[post],axis=0));dif=base-np.median(f[core],axis=0);r={'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'counts':[int(core.sum()),int(pre.sum()),int(post.sum())],'shape':list(f.shape[1:]),'base':base.tolist(),'difference':dif.tolist(),'target_xy':list(map(float,w.all_world2pix(291.81051000578583,-45.22009891950508,0))),'minimum_pixel':float(np.min(f)),'zero_fraction':float(np.mean(f==0))};(B/'helper-N008-s105.json').write_text(json.dumps(r,indent=2));print(r)
