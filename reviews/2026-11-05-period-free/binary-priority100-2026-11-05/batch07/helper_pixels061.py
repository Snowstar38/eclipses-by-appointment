from pathlib import Path
import numpy as np,json,hashlib
from astropy.io import fits
from astropy.wcs import WCS
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
p=Path(__file__).parent/'174306672';fp=p/'helper-s84-tesscut.fits'
with fits.open(fp,memmap=False) as h:
 d=h[1].data;t=np.array(d['TIME']);q=np.array(d['QUALITY']);f=np.array(d['FLUX']);w=WCS(h[2].header)
xy=[w.all_world2pix(*v,0) for v in [(352.5436348384747,45.50009877742365),(352.538567,45.494551)]]
good=np.isfinite(t)&(q==0);m=np.nanmedian(f[good],axis=0);print('xy',xy,'zero',int((m==0).sum()),'shape',f.shape)
fig,ax=plt.subplots(1,3,figsize=(13,4));im=ax[0].imshow(m,origin='lower');plt.colorbar(im,ax=ax[0]);ax[0].set_title('Median flux')
results=[]
for i,(core,side) in enumerate([((3585.72,3585.95),[(3585.1,3585.35),(3586.45,3586.7)]),((3599.05,3599.55),[(3597.5,3598.1),(3600.5,3601.1)])]):
 c=good&(t>core[0])&(t<core[1]);s=good&(((t>side[0][0])&(t<side[0][1]))|((t>side[1][0])&(t<side[1][1])));dif=np.nanmedian(f[s],axis=0)-np.nanmedian(f[c],axis=0);im=ax[i+1].imshow(dif,origin='lower',cmap='RdBu_r');plt.colorbar(im,ax=ax[i+1]);ax[i+1].set_title(f'baseline minus core {core}'); yy,xx=np.indices(dif.shape); sel=np.maximum(dif,0); results.append(dict(core=core,baseline=side,ncore=int(c.sum()),nbase=int(s.sum()),peak_xy=[int(np.unravel_index(np.nanargmax(dif),dif.shape)[1]),int(np.unravel_index(np.nanargmax(dif),dif.shape)[0])],positive_centroid=[float((sel*xx).sum()/sel.sum()) if sel.sum()>0 else None,float((sel*yy).sum()/sel.sum()) if sel.sum()>0 else None],difference=dif.tolist()))
for a in ax:
 for (x,y),label,col in zip(xy,['target','neighbor'],['lime','cyan']):a.plot(x,y,'+',color=col,ms=12,mew=2);a.text(x+.2,y+.2,label,color=col)
fig.tight_layout();fig.savefig(p/'helper-s84-difference.png',dpi=140)
(p/'helper-s84-numeric.json').write_text(json.dumps(dict(fits_sha256=hashlib.sha256(fp.read_bytes()).hexdigest(),target_xy=[float(x) for x in xy[0]],neighbor_xy=[float(x) for x in xy[1]],target_pixel_median=float(m[round(float(xy[0][1])),round(float(xy[0][0]))]),zero_median_pixels=int((m==0).sum()),results=results),indent=2))
print([(v['ncore'],v['nbase'],v['peak_xy'],v['positive_centroid']) for v in results])


