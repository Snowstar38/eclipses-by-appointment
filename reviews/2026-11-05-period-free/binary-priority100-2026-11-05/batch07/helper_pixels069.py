from pathlib import Path
import numpy as np,json,hashlib
from astropy.io import fits
from astropy.wcs import WCS
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
p=Path(__file__).parent/'159851783';outs=[]
for sec in (25,26,52):
 fp=p/f'helper-s{sec}-tesscut.fits';qp=Path(fr'[local-path-redacted]')
 with fits.open(fp,memmap=False) as h:
  d=h[1].data;t=np.array(d['TIME']);q=np.array(d['QUALITY']);f=np.array(d['FLUX']);w=WCS(h[2].header);x,y=w.all_world2pix(269.20305283850354,39.29748048697943,0)
 ix,iy=round(float(x)),round(float(y));med=np.nanmedian(f[q==0],axis=0); yy,xx=np.indices(med.shape); sky=(np.hypot(xx-x,yy-y)>3)&(med>0)&np.isfinite(med);bg=np.nanmedian(f[:,sky],axis=1);ap=f[:,iy-1:iy+2,ix-1:ix+2].sum(axis=(1,2))-9*bg;g=(q==0)&np.isfinite(t)&np.isfinite(ap)
 with fits.open(qp) as h:
  d=h[1].data;tt=np.array(d['TIME']);qq=np.array(d['QUALITY']);sap=np.array(d['SAP_FLUX']);ks=np.array(d['KSPSAP_FLUX'])
 gq=(qq==0)&np.isfinite(tt)&np.isfinite(sap);pred=2016.5550618320601+round((np.nanmedian(t)-2016.5550618320601)/30.117145560860603)*30.117145560860603
 fig,ax=plt.subplots(3,1,figsize=(12,7),sharex=True);ax[0].plot(t[g],ap[g]/np.nanmedian(ap[g]),'.',ms=1);ax[1].plot(tt[gq],sap[gq]/np.nanmedian(sap[gq]),'.',ms=1);ax[2].plot(tt[gq],ks[gq]/np.nanmedian(ks[gq]),'.',ms=1)
 for a,label in zip(ax,['sky-corrected 3x3','QLP SAP','QLP KSPSAP']):a.axvline(pred,color='red');a.set_ylabel(label)
 ax[2].set_xlabel('BTJD');fig.suptitle(f'T069 s{sec}; Gaia-period phase red; target ({x:.2f},{y:.2f})');fig.tight_layout();fig.savefig(p/f'helper-s{sec}-pixels.png',dpi=120);plt.close(fig)
 core=g&(abs(t-pred)<.8);side=g&(abs(t-pred)>2)&(abs(t-pred)<4); c=gq&(abs(tt-pred)<.8);s=gq&(abs(tt-pred)>2)&(abs(tt-pred)<4)
 o=dict(sector=sec,pred=pred,target_xy=[float(x),float(y)],target_median=float(med[iy,ix]),zero_pixels=int((med==0).sum()),sky_pixels=int(sky.sum()),pixel_core_n=int(core.sum()),pixel_side_n=int(side.sum()),pixel_deficit_ppt=float(1000*(1-np.median(ap[core])/np.median(ap[side]))) if core.sum() and side.sum() else None,sap_deficit_ppt=float(1000*(1-np.median(sap[c])/np.median(sap[s]))) if c.sum() and s.sum() else None,pixel_sha256=hashlib.sha256(fp.read_bytes()).hexdigest(),qlp_sha256=hashlib.sha256(qp.read_bytes()).hexdigest());outs.append(o);print(o,flush=True)
(p/'helper-pixel-numeric.json').write_text(json.dumps(outs,indent=2))
