import numpy as np,matplotlib;matplotlib.use('Agg')
import matplotlib.pyplot as plt,json
from pathlib import Path
from astropy.io import fits
from astropy.wcs import WCS
b=Path(__file__).resolve().parent;h=b/'helper-pixels/454228598';z=json.load(open(b.parent/'source-packets/454228598/sources.json'))['queue_row']
with fits.open(h/'tesscut.fits') as f:
 t=np.asarray(f[1].data['TIME'],float);F=np.asarray(f[1].data['FLUX'],float);q=np.asarray(f[1].data['QUALITY']);w=WCS(f[2].header)
x,y=w.all_world2pix(float(z['ra_deg']),float(z['dec_deg']),0);yy,xx=np.indices(F.shape[1:]);bg=np.nanmedian(np.sort(F.reshape(len(F),-1),axis=1)[:,:40],axis=1);f=np.nansum((F-bg[:,None,None])[:,(abs(xx-x)<=2)&(abs(yy-y)<=2)],axis=1);ok=np.isfinite(t)&np.isfinite(f)&(q==0);plt.figure(figsize=(10,4));plt.scatter(t[ok],f[ok]/np.nanmedian(f[ok]),s=4);plt.xlim(1624,1634);plt.grid();plt.savefig(h/'helper-aperture.png',dpi=140)
print('xy',x,y,'start',np.min(t[ok]),'coverage around 1625.85',[(float(t[i]),int(q[i]),float(f[i]/np.nanmedian(f[ok]))) for i in np.where(ok&(t>1625.7)&(t<1625.9))[0][::3]])
