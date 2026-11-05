"""Check Q097 S86 target aperture against cutout background and QLP SAP."""
import hashlib,json
from pathlib import Path
import numpy as np
from astropy.io import fits
from astropy.wcs import WCS
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
B=Path(__file__).resolve().parent;tic='47675509';sec=86
p=B/tic/f'helper-tesscut-s{sec}.fits';q=B.parent.parent.parent/'x'
with fits.open(p,memmap=False) as h:
 a=h[1].data;t=np.asarray(a['TIME'],float);f=np.asarray(a['FLUX'],float);qual=np.asarray(a['QUALITY'],int);w=WCS(h[2].header)
 x,y=w.all_world2pix(279.3303335189728,50.29530195114051,0);x=float(x);y=float(y)
yy,xx=np.indices(f.shape[1:]);ap=(abs(xx-round(x))<=1)&(abs(yy-round(y))<=1)
bg=(xx<2)|(xx>8)|(yy<2)|(yy>8)
apflux=np.nansum(f[:,ap],axis=1)-ap.sum()*np.nanmedian(f[:,bg],axis=1)
center=f[:,round(y),round(x)];right=f[:,3,8];left=f[:,5,1]
with fits.open(r'[local-path-redacted]',memmap=False) as h:
 d=h[1].data;qt=np.asarray(d['TIME'],float);qf=np.asarray(d['SAP_FLUX'],float);qq=np.asarray(d['QUALITY'],int)
fig,axs=plt.subplots(5,1,figsize=(11,11),sharex=True)
for ax,tt,ff,name,qv in zip(axs,[t,t,t,t,qt],[apflux,center,right,left,qf],['TESSCut target 3x3 minus edge median','TESSCut center pixel','TESSCut x8,y3','TESSCut x1,y5','QLP SAP'],[qual]*4+[qq]):
 m=(tt>=3636.5)&(tt<=3639.2)&(qv==0)&np.isfinite(ff)
 ax.plot(tt[m],ff[m]/np.nanmedian(ff[m][:30]) if len(ff[m])>=30 else ff[m],'.',ms=2);ax.set_ylabel(name,fontsize=8);ax.axvspan(3637.48,3637.63,color='tab:red',alpha=.15)
axs[-1].set_xlabel('BTJD');fig.tight_layout();fig.savefig(B/tic/'helper-s86-control.png',dpi=150)
print('target',x,y,'apflux range',np.nanpercentile(apflux[(t>=3636.5)&(t<=3639.2)],[5,50,95]))
