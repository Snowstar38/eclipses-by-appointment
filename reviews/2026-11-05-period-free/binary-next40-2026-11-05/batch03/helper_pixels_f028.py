from pathlib import Path
import numpy as np,json,hashlib
from astropy.io import fits
from astropy.wcs import WCS
from astropy.timeseries import BoxLeastSquares
import matplotlib;matplotlib.use('Agg')
import matplotlib.pyplot as plt
p=Path('batch03/19385783/helper-tesscut-s034.fits')
with fits.open(p) as h:t=np.array(h[1].data['TIME']);F=np.array(h[1].data['FLUX']);q=np.array(h[1].data['QUALITY']);w=WCS(h[2].header)
g=np.isfinite(t)&(q==0)&np.isfinite(F).all(axis=(1,2));t=t[g];F=F[g];bg=np.median(F[:,[0,0,-1,-1],[0,-1,0,-1]],axis=1);F=F-bg[:,None,None];tx,ty=map(float,w.all_world2pix(124.2953972265556,-9.026619109899057,0));f=F[:,4:7,4:7].sum(axis=(1,2));f/=np.median(f);b=BoxLeastSquares(t,f).power(np.linspace(1.02,1.05,3000),[.1,.15,.2]);i=np.argmax(b.power);P=float(b.period[i]);epoch=float(b.transit_time[i]);ph=(t-epoch+P/2)%P-P/2;inside=abs(ph)<.05;outside=(abs(ph)>.2)&(abs(ph)<.4);O=np.median(F[outside],axis=0);D=O-np.median(F[inside],axis=0);yy,xx=np.indices(D.shape);mask=(abs(xx-tx)<3)&(abs(yy-ty)<3);z=np.clip(D,0,None)*mask;cx=float((z*xx).sum()/z.sum());cy=float((z*yy).sum()/z.sum());print(tx,ty,cx,cy,P,epoch,inside.sum(),outside.sum(),np.median(F[:,round(ty),round(tx)]),np.median(bg));fig,ax=plt.subplots(1,3,figsize=(12,4));ax[0].imshow(O,origin='lower');ax[1].imshow(D,origin='lower');ax[2].plot(ph,f,'.',ms=1,alpha=.4)
for a in ax[:2]:a.plot(tx,ty,'r+',ms=12);a.plot(cx,cy,'wx',ms=10)
fig.tight_layout();fig.savefig('batch03/19385783/helper-pixels.png',dpi=130)
out=dict(fits_sha256=hashlib.sha256(p.read_bytes()).hexdigest(),target_xy=[tx,ty],difference_centroid_xy=[cx,cy],local_period_days=P,epoch_btjd=epoch,n_in=int(inside.sum()),n_out=int(outside.sum()),sky_median=float(np.median(bg)),target_pixel_median=float(np.median(F[:,round(ty),round(tx)])),caveat='Fold at half nominal 2.066-day clock combines alternate troughs; clipped centroid biased by PSF and noise, same photons as QLP')
Path('batch03/19385783/helper-pixels.json').write_text(json.dumps(out,indent=2))
