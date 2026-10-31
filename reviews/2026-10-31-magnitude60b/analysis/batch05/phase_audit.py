from pathlib import Path
import csv,json,numpy as np
from astropy.io import fits
import matplotlib;matplotlib.use('Agg')
import matplotlib.pyplot as plt
B=Path(__file__).parent;fig,axs=plt.subplots(5,2,figsize=(15,17))
coverage={}
for ax,r in zip(axs.flat,csv.DictReader(open(B/'queue.csv'))):
 tic=r['tic'];m=json.load(open(B/tic/'measurements.json'));p=m['period_days'];epoch=m['primary_epoch_btjd'];rr=[]
 for src in m['sources']:
  with fits.open(src['path']) as h:
   d=h[1].data;t=np.array(d['TIME']);f=np.array(d['SAP_FLUX']);q=np.array(d['QUALITY']);ok=np.isfinite(t)&np.isfinite(f)&(q==0)&(f>0);t=t[ok];f=f[ok]/np.median(f[ok]);phase=((t-epoch)/p+.15)%1-.15;ax.plot(phase,f,'.',ms=.7,alpha=.35,label=f"s{src['sector']}")
  if tic=='331861613':
   for n in range(int(np.ceil((t.min()-epoch)/p)),int(np.floor((t.max()-epoch)/p))+1):
    ctr=epoch+n*p;ix=abs(t-ctr)<.2;rr.append(dict(sector=src['sector'],cycle=n,quality_zero_in_window=int(sum(ix)),times=t[ix].tolist(),flux=f[ix].tolist()))
 coverage[tic]=rr;ax.set_title(tic);ax.set_xlim(-.15,.85);ax.legend(fontsize=6);ax.set_xlabel('Phase at selected measured period')
fig.tight_layout();fig.savefig(B/'phase-audit.png',dpi=150);json.dump(coverage,open(B/'recurrence-coverage.json','w'),indent=2)
