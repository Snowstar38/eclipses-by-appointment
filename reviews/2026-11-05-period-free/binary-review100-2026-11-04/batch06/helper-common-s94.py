import numpy as np,json,hashlib
from pathlib import Path
from astropy.io import fits
import matplotlib;matplotlib.use('Agg')
import matplotlib.pyplot as plt
B=Path(__file__).resolve().parent;ids=['318649725','278081787','129543547'];edges=np.arange(3872,3877.001,.1);curves=[];out={}
fig,ax=plt.subplots(figsize=(10,5))
for tic in ids:
 p=Path('[local-path-redacted]')/f'{tic}_s094.fits'
 with fits.open(p) as h:
  d=h[1].data;t=np.asarray(d['TIME']);f=np.asarray(d['SAP_FLUX']);q=np.asarray(d['QUALITY']);ok=(q==0)&np.isfinite(t)&np.isfinite(f); base=np.median(f[ok&(t>3872)&(t<3873.5)]);y=1000*(f/base-1);v=np.array([np.median(y[ok&(t>=lo)&(t<hi)]) if np.sum(ok&(t>=lo)&(t<hi))>=3 else np.nan for lo,hi in zip(edges[:-1],edges[1:])]);curves.append(v);ax.plot((edges[:-1]+edges[1:])/2,v,'.-',label=tic)
 out[tic]={'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'n':int(ok.sum()),'base_3872_3873_5':float(base)}
ax.axhline(0,color='k',lw=.5);ax.set(xlabel='BTJD',ylabel='SAP relative to 3872 to 3873.5 (ppt)');ax.legend();fig.tight_layout();fig.savefig(B/'helper-common-s94.png',dpi=150)
for i in range(3):
 for j in range(i+1,3):
  m=np.isfinite(curves[i])&np.isfinite(curves[j]);out[ids[i]+'_'+ids[j]]={'n_paired_bins':int(m.sum()),'correlation':float(np.corrcoef(curves[i][m],curves[j][m])[0,1])}
out['note']='0.1-day bins, quality 0, same sector/time and baseline; correlations descriptive, gaps are not zeros.'
(B/'helper-common-s94.json').write_text(json.dumps(out,indent=2));print(json.dumps(out,indent=2))

