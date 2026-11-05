import numpy as np, json, hashlib
from pathlib import Path
from astropy.io import fits
from astropy.wcs import WCS
import matplotlib;matplotlib.use('Agg')
import matplotlib.pyplot as plt
p=next(Path('helper-tesscut').glob('*.fits'));h=fits.open(p,memmap=False);d=h[1].data;t=np.asarray(d['TIME']);f=np.asarray(d['FLUX']);q=np.asarray(d['QUALITY']);w=WCS(h[2].header);x,y=w.world_to_pixel_values(70.71657359926411,7.393721176385869)
good=np.isfinite(t)&(q==0)
def med(a,b):return np.nanmedian(f[good&(t>=a)&(t<=b)],axis=0)
pre=med(4028.10,4028.35);core=med(4028.85,4029.35);post=med(4030.05,4030.30);delta=(pre+post)/2-core
# local sky from outer border; flux itself is background-subtracted pipeline
Y,X=np.indices(delta.shape);mask=((X-x)**2+(Y-y)**2<16); sky=np.nanmedian(delta[~mask]); diff=delta-sky
weights=np.clip(diff,0,None)*mask; cx=(weights*X).sum()/weights.sum();cy=(weights*Y).sum()/weights.sum()
fig,ax=plt.subplots(1,3,figsize=(12,4));
for a,z,title in zip(ax,[pre,core,diff],['pre','core','baseline minus core']):
 im=a.imshow(z,origin='lower');a.plot(x,y,'r+',ms=12);a.set_title(title);fig.colorbar(im,ax=a,shrink=.7)
fig.tight_layout();fig.savefig('helper-pixels.png',dpi=140)
rec={'file':str(p),'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'target_pixel_xy':[float(x),float(y)],'positive_difference_centroid_xy':[float(cx),float(cy)],'sky_difference':float(sky),'delta_near_target':float(diff[int(np.rint(y)),int(np.rint(x))]),'counts':{str((a,b)):int((good&(t>=a)&(t<=b)).sum()) for a,b in [(4028.10,4028.35),(4028.85,4029.35),(4030.05,4030.30)]},'caveat':'Linear two-sided baseline estimated from pre and post on a strong secular trend; centroid is not unique source attribution.'};Path('helper-pixels.json').write_text(json.dumps(rec,indent=2));print(rec)

