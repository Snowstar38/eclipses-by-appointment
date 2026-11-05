import json
from pathlib import Path
import numpy as np
from astropy.io import fits
from astropy.timeseries import LombScargle
from scipy.ndimage import median_filter
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
B=Path(__file__).resolve().parent;D=B/'191416124'
ctx=json.loads((D/'lead-context.json').read_text());series=[];results=[]
fig,axs=plt.subplots(3,1,figsize=(11,8),sharex=True)
freq=np.linspace(1/5,1/.5,20000)
for ax,s in zip(axs,ctx['sectors']):
 with fits.open(s['source_path'],memmap=False) as h:
  a=h[1].data;t=np.array(a['TIME'],float);f=np.array(a['SAP_FLUX'],float);q=np.array(a['QUALITY'],int);k=np.array(a['KSPSAP_FLUX'],float) if 'KSPSAP_FLUX' in h[1].columns.names else np.full(len(t),np.nan)
 g=np.isfinite(t)&np.isfinite(f)&(f>0)&(q==0);t=t[g];f=f[g];k=k[g]
 p=LombScargle(t,f/np.median(f)-1).power(freq)
 j=np.argmax(p)
 results.append(dict(sector=s['sector'],period_days=float(1/freq[j]),power=float(p[j]),points=len(t),source_sha256=s['source_sha256']))
 ax.plot(1/freq,p,lw=.5);ax.axvline(1/freq[j],color='r',lw=.6);ax.set_title(f"S{s['sector']}: best {1/freq[j]:.4f} d")
 axs[-1].set_xlabel('period d')
fig.tight_layout();fig.savefig(D/'lead-wave-periods.png',dpi=130)
(D/'lead-wave-periods.json').write_text(json.dumps(results,indent=2)+'\n')
print(results)
