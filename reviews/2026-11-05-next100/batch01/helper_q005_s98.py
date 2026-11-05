from pathlib import Path
import json,numpy as np
from astropy.io import fits
from astropy.wcs import WCS
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
B=Path(__file__).parent
with fits.open(B/'helper-cut-1535458-s98.fits') as h:
 a=h[1].data;t=np.array(a['TIME']);f=np.array(a['FLUX']);q=np.array(a['QUALITY']);w=WCS(h[2].header);tx,ty=w.all_world2pix(76.02231052016369,-31.955054951066305,0);ix=int(round(float(tx)));iy=int(round(float(ty)));ok=(q==0)&np.isfinite(t)&np.isfinite(f).all(axis=(1,2));t=t[ok];f=f[ok];bg=np.median(np.sort(f.reshape(len(f),-1),axis=1)[:,:30],axis=1);ap=f[:,iy-1:iy+2,ix-1:ix+2].sum(axis=(1,2))-9*bg
with fits.open('[local-path-redacted]') as h:
 a=h[1].data;tq=np.array(a['TIME']);fq=np.array(a['SAP_FLUX']);qq=np.array(a['QUALITY']);ok=(qq==0)&np.isfinite(tq)&np.isfinite(fq)&(fq>0);tq=tq[ok];fq=fq[ok]
fig,axs=plt.subplots(2,2,figsize=(12,6));out=[]
for j,c in enumerate([4016.644,4039.713]):
 for ax,tt,ff,label in [(axs[0,j],tq,fq,'QLP SAP'),(axs[1,j],t,ap,'TESSCut 3x3 sky-subtracted')]:
  sel=abs(tt-c)<3;x=tt[sel];y=ff[sel];ax.plot(x,y/np.median(y),'.',ms=1);ax.axvline(c,color='r');ax.set_title(label+' '+str(c));ax.grid()
 sel=abs(t-c)<2;x=t[sel];y=ap[sel];diff=np.diff(x);z=np.where(diff>.05)[0];out.append({'center':c,'wcs_xy':[float(tx),float(ty)],'target_pixel':[ix,iy],'n':int(len(x)),'window_first':float(x.min()),'window_last':float(x.max()),'gaps':[[float(x[k]),float(x[k+1])] for k in z],'positive_3x3_sky_subtracted_fraction':float(np.mean(y>0)),'median_3x3_sky_subtracted':float(np.median(y))})
fig.tight_layout();fig.savefig(B/'helper-Q005-s98-alias.png');(B/'helper-Q005-s98-alias.json').write_text(json.dumps(out,indent=2));print(out)
