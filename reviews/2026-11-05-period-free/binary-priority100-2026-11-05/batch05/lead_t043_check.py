"""Check whether T043 S78 QLP level change appears in target cutout pixels."""
import json
from pathlib import Path
import numpy as np
from astropy.io import fits
from astropy.wcs import WCS
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
B=Path(__file__).resolve().parent/'21743048';p=B/'lead-s78-tesscut.fits';q=Path(r'[local-path-redacted]')
with fits.open(p,memmap=False) as hd:
    a=hd[1].data;t=np.asarray(a['TIME'],float);f=np.asarray(a['FLUX'],float);qu=np.asarray(a['QUALITY'],int);w=WCS(hd[2].header)
with fits.open(q,memmap=False) as hd:
    a=hd[1].data;qt=np.asarray(a['TIME'],float);qf=np.asarray(a['SAP_FLUX'],float);qq=np.asarray(a['QUALITY'],int)
x,y=map(float,w.all_world2pix(256.3962376618137,35.26914246305228,0));yy,xx=np.indices(f.shape[1:]);mask=(abs(xx-round(x))<=1)&(abs(yy-round(y))<=1);lc=np.nansum(f[:,mask],axis=1)
center=3446.923794;good=np.isfinite(t)&(qu==0);core=good&(abs(t-center)<.4);left=good&(t>center-1.5)&(t<center-1.1);right=good&(t>center+.7)&(t<center+1.1)
diff=np.nanmedian(f[left],axis=0)-np.nanmedian(f[core],axis=0)
rec=dict(target_pixel=[x,y],target_aperture_side_median=float(np.nanmedian(lc[left])),left_n=int(left.sum()),core_n=int(core.sum()),right_n=int(right.sum()),left_to_core_ppt=float(1000*(1-np.median(lc[core])/np.median(lc[left]))),right_to_core_ppt=float(1000*(1-np.median(lc[core])/np.median(lc[right]))),left_to_right_ppt=float(1000*(1-np.median(lc[right])/np.median(lc[left]))),peak_yx=list(map(int,np.unravel_index(np.nanargmax(diff),diff.shape))))
(B/'lead-s78-check.json').write_text(json.dumps(rec,indent=2)+'\n')
fig,axs=plt.subplots(1,2,figsize=(12,4));sel=good&(abs(t-center)<3);qs=(np.isfinite(qt))&(qq==0)&(abs(qt-center)<3);axs[0].plot(qt[qs]-center,qf[qs]/np.median(qf[qs]),'.',ms=1,label='QLP SAP');axs[0].plot(t[sel]-center,lc[sel]/np.median(lc[sel]),'.',ms=1,label='TESSCut 3x3');axs[0].legend();axs[0].set(xlabel='days from screen seed',ylabel='relative flux');axs[1].imshow(diff,origin='lower',cmap='coolwarm');axs[1].plot(x,y,'kx');axs[1].set_title('left minus core');fig.tight_layout();fig.savefig(B/'lead-s78-check.png',dpi=140)
print(rec)
