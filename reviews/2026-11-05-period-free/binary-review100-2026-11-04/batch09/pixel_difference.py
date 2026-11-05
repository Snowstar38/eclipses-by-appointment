"""Target-WCS and local difference images for three same-sector events."""
import csv,json,hashlib
from pathlib import Path
import numpy as np
from astropy.io import fits
from astropy.wcs import WCS
import matplotlib;matplotlib.use('Agg')
import matplotlib.pyplot as plt
B=Path(__file__).resolve().parent;Q={r['tic']:r for r in csv.DictReader((B/'queue.csv').open())}
WINDOWS={'146516744':(32,(2199.75,2199.82),(2199.827,2199.848)),
         '433693445':(17,(1783.49,1783.56),(1783.575,1783.66)),
         '43868028':(98,(3995.55,3995.85),(3995.95,3996.09))}
for tic,(sector,pre,high) in WINDOWS.items():
 d=B/tic;p=d/'tesscut.fits';receipt=json.loads((d/'tesscut-receipt.json').read_text());assert hashlib.sha256(p.read_bytes()).hexdigest()==receipt['fits_sha256']
 with fits.open(p,memmap=False) as h:
  a=h[1].data;t=np.asarray(a['TIME'],float);quality=np.asarray(a['QUALITY'],int);flux=np.asarray(a['FLUX'],float);w=WCS(h[2].header)
 x,y=w.all_world2pix(float(Q[tic]['ra_deg']),float(Q[tic]['dec_deg']),0);x=float(x);y=float(y)
 ok=np.isfinite(t)&(quality==0);m0=ok&(t>=pre[0])&(t<pre[1]);m1=ok&(t>=high[0])&(t<high[1]);assert m0.sum() and m1.sum(),(tic,m0.sum(),m1.sum())
 yy,xx=np.indices(flux.shape[1:]);outer=(abs(xx-x)>=3)|(abs(yy-y)>=3)
 bg=np.nanmedian(flux[:,outer],axis=1);corrected=flux-bg[:,None,None]
 A=np.nanmedian(corrected[m0],axis=0);P=np.nanmedian(corrected[m1],axis=0);D=P-A
 xi,yi=round(x),round(y);target=(abs(xx-xi)<=1)&(abs(yy-yi)<=1);far=~((abs(xx-xi)<=2)&(abs(yy-yi)<=2))
 positive=np.clip(D,0,None);wt=positive.sum();cx=float((positive*xx).sum()/wt) if wt>0 else None;cy=float((positive*yy).sum()/wt) if wt>0 else None
 out={'tic':tic,'sector':sector,'fits_sha256':receipt['fits_sha256'],'target_wcs_pixel':[float(x),float(y)],'nearest_integer_pixel':[xi,yi],'pre_interval_btjd':pre,'high_interval_btjd':high,'n_pre':int(m0.sum()),'n_high':int(m1.sum()),'local_outer_background_pre_high':[float(np.median(bg[m0])),float(np.median(bg[m1]))],
      'target_3x3_pre_sum':float(A[target].sum()),'target_3x3_difference_sum':float(D[target].sum()),'far_difference_sum':float(D[far].sum()),'positive_difference_centroid_pixel':[cx,cy],
      'difference_image':D.tolist(),'pre_image':A.tolist(),'caveat':'Same FFI photons in a different reduction; difference image is unregistered, with only local outer-pixel background subtraction. Positive-image centroid is a descriptive moment, not a fitted PSF/source localization. Pointing and background systematics can affect it.'}
 (d/'pixel-difference.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf8')
 fig,axes=plt.subplots(1,2,figsize=(9,4));axes[0].imshow(A,origin='lower',cmap='viridis');v=np.nanpercentile(abs(D),95);axes[1].imshow(D,origin='lower',cmap='RdBu_r',vmin=-v,vmax=v)
 for ax in axes:ax.plot(x,y,'r+',ms=11,mew=1.5);ax.set_xlim(0,A.shape[1]-1);ax.set_ylim(0,A.shape[0]-1)
 axes[0].set_title(f'{tic} s{sector} pre, target +');axes[1].set_title(f'peak minus pre; sum 3x3 {D[target].sum():.0f}')
 fig.tight_layout();fig.savefig(d/'pixel-difference.png',dpi=140);plt.close(fig)
 print(tic,'frames',m0.sum(),m1.sum(),'targetxy',round(x,2),round(y,2),'diffxy',round(cx,2),round(cy,2),'targetdiff',round(float(D[target].sum()),1),'far',round(float(D[far].sum()),1),flush=True)
