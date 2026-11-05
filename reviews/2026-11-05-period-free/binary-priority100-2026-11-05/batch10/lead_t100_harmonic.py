"""Check whether T100's frequent dips are one kind or two half-cycle kinds."""
import json,hashlib
from pathlib import Path
import numpy as np
from astropy.io import fits
from scipy.ndimage import median_filter
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
B=Path(__file__).resolve().parent;tic='95244521';m=json.loads((B/tic/'lead-numeric.json').read_text());P=.6791780661141588;epoch=2231.2857423093324;out=[]
fig,axs=plt.subplots(4,2,figsize=(12,12))
for i,src in enumerate(m['sources']):
 p=Path(src['path']);assert hashlib.sha256(p.read_bytes()).hexdigest()==src['sha256']
 with fits.open(p,memmap=False) as h:
  d=h[1].data;t=np.array(d['TIME'],float);f=np.array(d['SAP_FLUX'],float);q=np.array(d['QUALITY'],int)
 sel=np.isfinite(t)&np.isfinite(f)&(f>0)&(q==0);t=t[sel];f=f[sel]
 # Running median removes multi-day trends only, leaving narrow 0.08-d eclipses.
 cad=np.median(np.diff(t));n=max(7,int(round(1/cad))|1);base=median_filter(f,size=n,mode='nearest');y=f/base
 sec=src['sector'];r=dict(sector=sec,cadence_days=float(cad),n_quality0=len(t),phase_bins=[])
 for j,pd in enumerate((P,P/2)):
  phase=((t-epoch)/pd+.5)%1-.5
  axs[i,j].plot(phase,y,'.',ms=1,alpha=.14);axs[i,j].set_ylim(.945,1.015);axs[i,j].set_xlim(-.5,.5);axs[i,j].set_title(f's{sec} fold {pd:.6f} d');axs[i,j].set_xlabel('phase');axs[i,j].set_ylabel('SAP/running median')
  bins=np.linspace(-.5,.5,101);med=[]
  for k in range(100):
   z=y[(phase>=bins[k])&(phase<bins[k+1])];med.append(float(np.median(z)) if len(z)>5 else None)
  r['phase_bins'].append(dict(period_days=pd,bin_centers=((bins[:-1]+bins[1:])/2).tolist(),median_flux=med))
 out.append(r)
fig.tight_layout();fig.savefig(B/'lead-t100-harmonic.png',dpi=140);plt.close(fig)
(B/'lead-t100-harmonic.json').write_text(json.dumps(dict(target=tic,reference_epoch_btjd=epoch,period_days=P,method='Quality-zero raw SAP divided by 1-d running median, folded at P and P/2; inspect phase split and sector agreement. Same photons, not a new occasion.',sectors=out),indent=2)+'\n')
