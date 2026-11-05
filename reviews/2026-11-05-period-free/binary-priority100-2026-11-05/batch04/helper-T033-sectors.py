import numpy as np,matplotlib;matplotlib.use('Agg')
import matplotlib.pyplot as plt
from astropy.io import fits
from pathlib import Path
B=Path(r'[local-path-redacted]');D=Path(r'[local-path-redacted]')
fig,axs=plt.subplots(3,1,figsize=(12,8))
for ax,s in zip(axs,[80,91,92]):
 with fits.open(D/f'362778566_s{s:03}.fits') as h:
  d=h[1].data;t=d['TIME'];q=d['QUALITY'];f=d['SAP_FLUX'];m=np.isfinite(t)&np.isfinite(f); v=f/np.median(f[m&(q==0)]); ax.plot(t[m&(q==0)],v[m&(q==0)],'.',ms=1);ax.plot(t[m&(q!=0)],v[m&(q!=0)],'.',ms=1,color='r');ax.set_ylim(.97,1.03);ax.set_title(f's{s}');ax.grid()
fig.tight_layout();fig.savefig(B/'helper-T033-sectors.png',dpi=120)
