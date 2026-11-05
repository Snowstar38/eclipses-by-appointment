import json
from pathlib import Path
import numpy as np
from astropy.io import fits
from astropy.timeseries import LombScargle
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
B=Path(__file__).resolve().parent;D=B/'191416124';c=json.loads((D/'lead-context.json').read_text())
ts=[];fs=[];ss=[]
for s in c['sectors']:
 with fits.open(s['source_path'],memmap=False) as h:
  a=h[1].data;t=np.array(a['TIME'],float);f=np.array(a['SAP_FLUX'],float);q=np.array(a['QUALITY'],int)
 g=np.isfinite(t)&np.isfinite(f)&(f>0)&(q==0);t=t[g];f=f[g]
 ts.append(t);fs.append(f/np.median(f)-1);ss.append(np.full(len(t),s['sector']))
t=np.concatenate(ts);f=np.concatenate(fs);s=np.concatenate(ss)
freq=np.linspace(1/2.7,1/2.3,150000)
p=LombScargle(t,f).power(freq,method='fast')
inds=np.argsort(p)[-100:][::-1];peaks=[]
for i in inds:
 period=1/freq[i]
 if all(abs(period-x['period_days'])>0.0005 for x in peaks):peaks.append(dict(period_days=float(period),power=float(p[i])))
 if len(peaks)==12:break
best=peaks[0]['period_days'];phase=((t-2872.425)/best)%1
fig,ax=plt.subplots(2,1,figsize=(11,8));ax[0].plot(1/freq,p,lw=.4);ax[0].axvline(best,color='r',lw=.6)
for sec in sorted(set(s)):
 g=s==sec;ax[1].plot(phase[g],f[g],'.',ms=1,alpha=.3,label=f'S{sec}')
ax[0].set_xlabel('period d');ax[0].set_ylabel('LS power');ax[1].set_xlabel(f'phase at {best:.7f} d');ax[1].set_ylabel('SAP relative');ax[1].legend()
fig.tight_layout();fig.savefig(D/'lead-coherence.png',dpi=140)
(D/'lead-coherence.json').write_text(json.dumps(dict(peaks=peaks,all_sectors=[int(x) for x in sorted(set(s))],epoch_btjd=2872.425,n_points=len(t),source_sha256=[x['source_sha256'] for x in c['sectors']],note='LS waveform period; not an eclipse clock'),indent=2)+'\n')
print(peaks)
