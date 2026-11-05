import pathlib,zipfile,io,hashlib,numpy as np,matplotlib
matplotlib.use('Agg');import matplotlib.pyplot as plt
from astropy.io import fits
p=pathlib.Path(r'[local-path-redacted]');print(hashlib.sha256(p.read_bytes()).hexdigest())
with zipfile.ZipFile(p) as z:
 with fits.open(io.BytesIO(z.read(next(n for n in z.namelist() if n.endswith('.fits'))))) as h:
  a=h[1].data;t=np.asarray(a['TIME']);q=np.asarray(a['QUALITY']); f=np.asarray(a['FLUX']); x=t-3640.159518244652;m=np.isfinite(t)&(q==0);core=m&(abs(x)<.036);side=m&(abs(x)>.09)&(abs(x)<.2);inside=np.nanmedian(f[core],axis=0);outside=np.nanmedian(f[side],axis=0);delta=outside-inside;print('core/side',core.sum(),side.sum()); print(np.round(delta,1));print('central9 diff',delta[3:6,3:6].sum(),'totaldiff',delta.sum());fig,ax=plt.subplots(1,3,figsize=(12,4));
  for a,d,title in zip(ax,[outside,inside,delta],['outside','inside','outside-inside']):
   im=a.imshow(d,origin='lower');a.set_title(title);fig.colorbar(im,ax=a)
  fig.tight_layout();fig.savefig(p.parent/'helper-pixel-difference.png',dpi=140)
