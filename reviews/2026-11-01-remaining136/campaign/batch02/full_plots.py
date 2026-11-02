import csv,json
from pathlib import Path
import numpy as np
from astropy.io import fits
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
B=Path(__file__).parent
for r in csv.DictReader(open(B/'queue.csv')):
 tic=r['tic'];m=json.load(open(B/tic/'measurements.json'));fig,axs=plt.subplots(len(m['sources']),2,figsize=(12,3*len(m['sources'])),squeeze=False)
 for src,ax in zip(m['sources'],axs):
  with fits.open(src['path']) as h:a=h[1].data;t=np.array(a['TIME'],float);f=np.array(a['SAP_FLUX'],float);q=np.array(a['QUALITY'])
  ok=np.isfinite(t)&np.isfinite(f)&(f>0)&(q==0);t=t[ok];f=f[ok]/np.median(f[ok]);phase=((t-m['primary_epoch_btjd'])/m['period_days']+.5)%1-.5
  ax[0].plot(t,f,'.',ms=1);ax[0].set_title(f'TIC{tic} S{src["sector"]} raw SAP');ax[1].plot(phase,f,'.',ms=1);ax[1].set_title('Measured P phase; selected eclipse at0')
 fig.tight_layout();fig.savefig(B/tic/'raw-sector-fold.png',dpi=130);plt.close(fig)
