import numpy as np,matplotlib;matplotlib.use('Agg')
import matplotlib.pyplot as plt
from astropy.io import fits
from astropy.wcs import WCS
from pathlib import Path
B=Path(r'[local-path-redacted]')
with fits.open(B/'helper-362778566-s91-tesscut.fits',memmap=False) as h:
 d=h[1].data;t=d['TIME'];q=d['QUALITY'];f=np.asarray(d['FLUX'],float);f-=np.nanmedian(np.sort(f.reshape(len(f),-1),axis=1)[:,:48],axis=1)[:,None,None];w=WCS(h[2].header);x,y=w.all_world2pix(271.4743001692025,-12.030042465995317,0);ix,iy=round(float(x)),round(float(y));core=(t>3775.5)&(t<3776)&(q==0);base=(t>3777)&(t<3778)&(q==0);dif=np.nanmedian(f[base],axis=0)-np.nanmedian(f[core],axis=0);fig,ax=plt.subplots(1,2,figsize=(12,4));im=ax[0].imshow(dif,origin='lower');ax[0].plot(x,y,'rx');fig.colorbar(im,ax=ax[0]);ax[0].set_title('3777-78 minus 3775.5-76');
 for n in [0,1,2]:
  v=np.nansum(f[:,iy-n:iy+n+1,ix-n:ix+n+1],axis=(1,2));m=(t>3775)&(t<3779)&(q==0);ax[1].plot(t[m],v[m]/np.nanmedian(v[base]),'.',ms=1,label=f'{2*n+1}x{2*n+1}')
 ax[1].legend();ax[1].grid();ax[1].set_title('low-48 background subtracted');fig.tight_layout();fig.savefig(B/'helper-T033-s91-pixels.png',dpi=120)
