from pathlib import Path
import csv,json,numpy as np
from astropy.io import fits
import matplotlib;matplotlib.use('Agg')
import matplotlib.pyplot as plt
B=Path(__file__).parent
for row in csv.DictReader(open(B/'queue.csv')):
 tic=row['tic'];m=json.load(open(B/tic/'measurements.json'));P=m['period_days'];ep=m['primary_epoch_btjd'];fig,axs=plt.subplots(3,1,figsize=(11,8))
 for s in m['sources']:
  with fits.open(s['path']) as h:
   d=h[1].data;t=np.array(d['TIME']);f=np.array(d['SAP_FLUX']);q=np.array(d['QUALITY']);ok=np.isfinite(t)&np.isfinite(f)&(f>0)&(q==0)
  if sum(ok)<12:continue
  t=t[ok];f=f[ok];y=f/np.median(f);phase=((t-ep)/P+.15)%1-.15
  axs[0].plot(phase,y,'.',ms=1,label=str(s['sector']))
  axs[1].plot(((t-ep)/(2*P)+.1)%1-.1,y,'.',ms=1)
  axs[2].plot(t,y,'.',ms=1)
 axs[0].set_title(tic+' raw QLP folded at measured P');axs[0].legend(ncol=6,fontsize=6);axs[1].set_title('2P parity view (eclipses at 0 and 0.5)');axs[2].set_title('Raw sector time series; quality-zero only')
 fig.tight_layout();fig.savefig(B/tic/'phase-review.png',dpi=110);plt.close(fig)
