import numpy as np,matplotlib;matplotlib.use('Agg')
import matplotlib.pyplot as plt
from astropy.io import fits
p=13.576868477565943;t0=1690.0687
with fits.open('[local path omitted]') as h:
 d=h[1].data;t=np.array(d['TIME']); f=np.array(d['FLUX']);q=np.array(d['QUALITY']);bg=np.median(np.sort(f.reshape(len(t),-1),axis=1)[:,:90],axis=1);y=np.sum(f[:,6:9,6:9]-bg[:,None,None],axis=(1,2))
fig,axs=plt.subplots(2,1,figsize=(9,6));
for ax,n in zip(axs,[52,53]):
 tp=t0+n*p;i=np.isfinite(t)&np.isfinite(y)&(abs(t-tp)<.55);oot=i&(abs(t-tp)>.25); norm=np.median(y[oot]);
 for flag,lab in [(0,'quality 0'),(2048,'quality 2048')]:
  z=i&(q==flag);ax.scatter(t[z]-tp,y[z]/norm,s=8,label=lab)
 ax.axvline(0,color='gray');ax.set_title(f'Sector 40 cycle {n}; predicted BTJD {tp:.5f}');ax.set_ylabel('3x3 flux / local baseline');ax.legend()
axs[-1].set_xlabel('Days from predicted midpoint');fig.tight_layout();fig.savefig('sector40-raw-aperture.png',dpi=150)
