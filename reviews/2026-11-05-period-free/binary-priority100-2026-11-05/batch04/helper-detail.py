import pathlib,numpy as np,matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
from astropy.io import fits
B=pathlib.Path(r'[local-path-redacted]'); D=pathlib.Path(r'[local-path-redacted]')
fig,axes=plt.subplots(4,2,figsize=(14,10))
for ax,(tic,s,t0) in zip(axes.flat,[(309965535,73,3300.867),(237212952,85,3625.14),(362778566,80,3501.68),(466098039,104,4197.354)]):
 with fits.open(D/f'{tic}_s{s:03}.fits') as h:
  d=h[1].data;t=d['TIME'];q=d['QUALITY'];m=np.isfinite(t)&(abs(t-t0)<5)
  for col in ['SAP_FLUX','DET_FLUX']:
   v=np.array(d[col],float); z=m&np.isfinite(v)&(q==0); ax.plot(t[z],v[z]/np.median(v[z]),'.',ms=1,label=col)
  ax.set_ylim(.94,1.06);ax.set_title(f'TIC {tic} s{s}');ax.legend();ax.grid()
  bx=axes.flat[list(axes.flat).index(ax)+1] if False else None
fig.tight_layout(); fig.savefig(B/'helper-detail.png',dpi=120)
