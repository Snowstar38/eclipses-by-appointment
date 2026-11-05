import json,hashlib
from pathlib import Path
import numpy as np
from astropy.io import fits
B=Path(__file__).resolve().parent; p=B/'lead-pixels'/'246124257'/'tesscut.fits'
with fits.open(p) as h:t=np.array(h[1].data['TIME'],float);f=np.array(h[1].data['FLUX'],float);q=np.array(h[1].data['QUALITY'])
ok=np.isfinite(t)&(q==0)&np.isfinite(f).all(axis=(1,2));t=t[ok];f=f[ok];bg=np.median(np.sort(f.reshape(len(f),-1),axis=1)[:,:48],axis=1);f-=bg[:,None,None]; x=t-3101.055
core=abs(x)<.03;pre=(x<-.078)&(x>-.168);post=(x>.078)&(x<.168);O=.5*(np.median(f[pre],axis=0)+np.median(f[post],axis=0));D=O-np.median(f[core],axis=0)
a={}
for name,ys,xs in [('target_2x2',slice(5,7),slice(4,6)),('neighbor_2x2',slice(5,7),slice(7,9)),('target_pixel',slice(5,6),slice(5,6)),('neighbor_pixel',slice(5,6),slice(7,8))]:
 a[name]={'difference_counts':float(D[ys,xs].sum()),'baseline_counts':float(O[ys,xs].sum()),'fractional_depth_ppt':float(1000*D[ys,xs].sum()/O[ys,xs].sum())}
out={'tic':'246124257','windows':'BTJD 3101.055 +/-0.03 core; pre/post offsets 0.078 to 0.168 d; QUALITY=0','counts':[int(core.sum()),int(pre.sum()),int(post.sum())],'apertures':a,'caveat':'Neighbor aperture overlaps target PSF wings and fitted background, so depth gradient is supportive rather than a deblended measurement; same TESS photons.','fits_sha256':hashlib.sha256(p.read_bytes()).hexdigest()};(B/'helper-aperture-audit.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
