import json,numpy as np,matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from pathlib import Path
from astropy.io import fits
r=Path(__file__).parent;records=json.load(open(r/'search-receipts.json'));fig,axs=plt.subplots(10,3,figsize=(18,25))
for i,rec in enumerate(records):
 tic=str(rec['tic']);fs=sorted((r/tic).glob('qlp*.fits'));P=rec['P']['P'];t0=rec['P']['t0']
 for j,f in enumerate(fs[:3]):
  with fits.open(f) as h:
   a=h[1].data;t=np.array(a['TIME']);y=np.array(a['SAP_FLUX']);m=np.isfinite(t)&np.isfinite(y)&(y>0)&(a['QUALITY']==0);t=t[m];y=y[m];y/=np.median(y)
  axs[i,j].scatter(t,y,s=2);axs[i,j].set_title(f'{tic} {f.stem} P={P:.4f}');axs[i,j].set_ylim(np.percentile(y,[.1,99.9])+np.array([-.01,.01]))
fig.tight_layout();fig.savefig(r/'all-raw.png',dpi=130)
