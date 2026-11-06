from pathlib import Path
import numpy as np
from astropy.io import fits
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
B=Path(__file__).resolve().parent;S=B.parent.parent/'fresh-band'/'data'
fig,axs=plt.subplots(3,1,figsize=(13,8),squeeze=False)
for ax,sec in zip(axs[:,0],[5,32,98]):
 with fits.open(S/f'768070_s{sec:03d}.fits') as h:
  a=h[1].data;t=np.asarray(a['TIME'],float);y=np.asarray(a['SAP_FLUX'],float);q=np.asarray(a['QUALITY'],int)
 ok=np.isfinite(t)&np.isfinite(y)&(y>0)&(q==0);t=t[ok];y=y[ok]/np.median(y[ok])
 ax.plot(t,y,'.',ms=1);ax.set_title(f'S{sec}');ax.set_ylim(np.quantile(y,.001)-.05,np.quantile(y,.999)+.05);ax.set_ylabel('raw SAP normalized');ax.grid(alpha=.2)
axs[-1,0].set_xlabel('BTJD');fig.tight_layout();fig.savefig(B/'lead-qlp-all.png',dpi=140)
