from pathlib import Path
import json,numpy as np,matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from astropy.io import fits
R=Path(__file__).parent;recs=json.load(open(R/'search-receipts.json'));fig,axs=plt.subplots(5,3,figsize=(18,14))
for row,rec in enumerate(recs):
 for ax,p in zip(axs[row],sorted((R/rec['tic']).glob('qlp*.fits'))):
  with fits.open(p) as h:
   a=h[1].data;t=np.array(a['TIME']);y=np.array(a['SAP_FLUX']);q=np.array(a['QUALITY']);m=np.isfinite(t)&np.isfinite(y)&(y>0)&(q==0);t=t[m];y=y[m]/np.median(y[m])
  ax.plot(t,y,'.',ms=1);ax.set_title(rec['tic']+' '+p.stem);ax.set_ylim(np.percentile(y,.2)-.005,np.percentile(y,99.8)+.005)
  tc=rec['P']['t0'];P=rec['P']['P']
  for n in range(int(np.floor((t.min()-tc)/P)),int(np.ceil((t.max()-tc)/P))+1):ax.axvline(tc+n*P,color='r',alpha=.4)
fig.tight_layout();fig.savefig(R/'morphology.png',dpi=130)
