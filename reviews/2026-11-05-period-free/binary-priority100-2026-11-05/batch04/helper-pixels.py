import numpy as np, json, pathlib, matplotlib;matplotlib.use('Agg')
import matplotlib.pyplot as plt
from astropy.io import fits
from astropy.wcs import WCS
B=pathlib.Path(r'[local-path-redacted]'); out={}
for tic,ra,dec,core,left,right in [(362778566,271.4743001692025,-12.030042465995317,(3501.3,3502.5),(3498.5,3500),(3503,3503.7)),(309965535,138.07788256853726,76.50309237623361,(3300.3,3301.2),(3297,3298.5),(3303.2,3304)),(237212952,294.8562118595401,72.1262400480597,(3624.5,3625.3),(3620,3622),(3627,3628))]:
 with fits.open(B/f'helper-{tic}-tesscut.fits',memmap=False) as h:
  d=h[1].data;t=np.asarray(d['TIME']); f=np.asarray(d['FLUX'],float);q=np.asarray(d['QUALITY']); f=f-np.nanmedian(np.sort(f.reshape(len(f),-1),axis=1)[:,:48],axis=1)[:,None,None];w=WCS(h[2].header);x,y=w.all_world2pix(ra,dec,0);ix,iy=int(round(float(x))),int(round(float(y))); med=lambda ab: np.nanmedian(f[(t>=ab[0])&(t<=ab[1])&(q==0)],axis=0); ci=med(core);base=(med(left)+med(right))/2; diff=base-ci; bg=np.nanmedian(base); fig,ax=plt.subplots(1,3,figsize=(14,4)); im=ax[0].imshow(base,origin='lower');ax[0].plot(x,y,'rx');fig.colorbar(im,ax=ax[0]); ax[0].set_title('baseline and WCS target'); im=ax[1].imshow(diff,origin='lower');ax[1].plot(x,y,'rx');fig.colorbar(im,ax=ax[1]);ax[1].set_title('baseline - core');
  for n in [0,1,2]:
   cube=f[:,max(0,iy-n):iy+n+1,max(0,ix-n):ix+n+1]; vals=np.nansum(cube,axis=(1,2)); m=(t>=left[0])&(t<=right[1])&(q==0)&np.isfinite(vals); baseline=np.nanmedian(vals[(t>=left[0])&(t<=left[1])&(q==0)]); ax[2].plot(t[m],vals[m]/baseline,'.',ms=1,label=f'{2*n+1}x{2*n+1}')
  ax[2].legend();ax[2].set_title('apertures (low-48 background subtracted)');ax[2].grid();fig.suptitle(str(tic));fig.tight_layout();fig.savefig(B/f'helper-{tic}-pixels.png',dpi=120);plt.close(fig);out[str(tic)]={'x':float(x),'y':float(y),'base_target_pixel':float(base[iy,ix]),'background_median':float(bg),'target_pixel_minus_background':float(base[iy,ix]-bg),'core':core,'baseline': [left,right]}
json.dump(out,open(B/'helper-pixel-measurements.json','w'),indent=2)


