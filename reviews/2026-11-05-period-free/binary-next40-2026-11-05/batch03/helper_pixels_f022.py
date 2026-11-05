from pathlib import Path
import numpy as np,json,hashlib
from astropy.io import fits
from astropy.wcs import WCS
import matplotlib;matplotlib.use('Agg')
import matplotlib.pyplot as plt
p=Path('batch03/324424395/helper-tesscut-s093.fits')
with fits.open(p) as h:t=np.array(h[1].data['TIME']);F=np.array(h[1].data['FLUX']);q=np.array(h[1].data['QUALITY']);w=WCS(h[2].header)
g=np.isfinite(t)&(q==0)&np.isfinite(F).all(axis=(1,2));t=t[g];F=F[g];bg=np.median(F[:,[0,0,-1,-1],[0,-1,0,-1]],axis=1);F=F-bg[:,None,None];i=(t>3843.25)&(t<3843.9); o=((t>3840.3)&(t<3841.3))|((t>3844.8)&(t<3845.8));O=np.median(F[o],axis=0);D=O-np.median(F[i],axis=0);tx,ty=w.all_world2pix(285.51475471576595,-73.66926980232525,0);tx=float(tx);ty=float(ty);coords=[(285.524884,-73.665022),(285.511480,-73.675287),(285.539804,-73.661585)]; nn=[w.all_world2pix(*c,0) for c in coords]; yy,xx=np.indices(D.shape);mask=(abs(xx-tx)<3)&(abs(yy-ty)<3);z=np.clip(D,0,None)*mask;cx=float((z*xx).sum()/z.sum());cy=float((z*yy).sum()/z.sum());print('target',tx,ty,'neighbors',nn,'diffcenter',cx,cy,'n',i.sum(),o.sum(),'target',np.median(F[:,round(ty),round(tx)]),'sky',np.median(bg))
fig,ax=plt.subplots(1,3,figsize=(12,4));ax[0].imshow(O,origin='lower');ax[1].imshow(D,origin='lower');f=F[:,round(ty)-1:round(ty)+2,round(tx)-1:round(tx)+2].sum(axis=(1,2));ax[2].plot(t,f/np.median(f),'.',ms=1);ax[2].set_xlim(3840,3847)
for a in ax[:2]:
 a.plot(tx,ty,'r+',ms=12);a.plot(cx,cy,'wx',ms=10)
 for x,y in nn:a.plot(x,y,'cx',ms=8)
fig.tight_layout();fig.savefig('batch03/324424395/helper-pixels.png',dpi=130)
out=dict(fits_sha256=hashlib.sha256(p.read_bytes()).hexdigest(),target_xy=[float(tx),float(ty)],neighbor_xy=[[float(x),float(y)] for x,y in nn],difference_centroid_xy=[cx,cy],n_in=int(i.sum()),n_out=int(o.sum()),sky_median=float(np.median(bg)),target_pixel_median=float(np.median(F[:,round(ty),round(tx)])),inside_btjd=[3843.25,3843.9],outside_btjd=[[3840.3,3841.3],[3844.8,3845.8]],caveat='difference centroid clipped positive within 3 pixels; variable background and blending can bias; same photons')
Path('batch03/324424395/helper-pixels.json').write_text(json.dumps(out,indent=2))


