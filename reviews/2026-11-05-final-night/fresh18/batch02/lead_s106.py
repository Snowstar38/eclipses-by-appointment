import json,numpy as np
from pathlib import Path
from astropy.io import fits
import matplotlib;matplotlib.use('Agg')
import matplotlib.pyplot as plt
b=Path(r'[workspace]/Astra\made\final-night-2026-11-05\fresh18\batch02');p=b/'159860053/helper-cut-s106.fits'
with fits.open(p) as h:
 a=h[1].data;t=np.array(a['TIME']);f=np.array(a['FLUX']);q=np.array(a['QUALITY']);y=np.nansum(f[:,2:5,2:5],axis=(1,2))-9*np.nanmedian(f[:,[0,-1],:],axis=(1,2));o=(q==0)&np.isfinite(t)&(y>0);t=t[o];y=y[o];y=y/np.median(y)
fig,ax=plt.subplots(figsize=(12,3));ax.plot(t,y,'.',ms=1);ax.grid();fig.tight_layout();fig.savefig(p.parent/'lead-s106.png',dpi=120)
np.savez(p.parent/'lead-s106-photometry.npz',time=t,flux=y)
print(t.min(),t.max(),[(round(float(t[i]),4),round(float(y[i]),3)) for i in np.argsort(y)[:10]])
