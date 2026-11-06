from astropy.io import fits
from astropy.wcs import WCS
from astropy.timeseries import LombScargle
from pathlib import Path
import numpy as np, matplotlib.pyplot as plt, json, hashlib
b=Path(__file__).parent; p=next((b/'helper-v017-cut').glob('*.fits')); h=fits.open(p); d=h[1].data; t=np.asarray(d['TIME']); f=np.asarray(d['FLUX']); q=np.asarray(d['QUALITY']); m=np.isfinite(t)&(q==0)&(t>2685)&(t<2690)&np.isfinite(f).all(axis=(1,2)); t=t[m]; f=f[m]; w=WCS(h[2].header); target=w.all_world2pix([[204.446961,2.445429]],0)[0]; ix,iy=np.rint(target).astype(int); y=f[:,iy,ix]; freq=np.linspace(2,8,30000); pow=LombScargle(t,y).power(freq); P=0.27941916134200184; x=np.column_stack([np.ones(len(t)),t-t.mean(),np.sin(2*np.pi*t/P),np.cos(2*np.pi*t/P)]); coef=np.linalg.lstsq(x,f.reshape(len(t),-1),rcond=None)[0]; amp=np.hypot(coef[2],coef[3]).reshape(15,15); peak=np.unravel_index(np.argmax(amp),amp.shape); fig,ax=plt.subplots(); im=ax.imshow(amp,origin='lower'); ax.plot(*target,'wx',ms=12,mew=2,label='target'); ax.legend(); fig.colorbar(im,label='sine amplitude e-/s'); fig.savefig(b/'helper-v017-amplitude.png',dpi=150); print(json.dumps({'n':len(t),'range':[float(t.min()),float(t.max())],'period_days':P,'target_xy':target.tolist(),'peak_yx':peak,'peak_amplitude':float(amp[peak]),'sha256_fits':hashlib.sha256(p.read_bytes()).hexdigest()},indent=2,default=int))

