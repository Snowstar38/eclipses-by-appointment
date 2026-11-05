import json
from pathlib import Path
import numpy as np
from astropy.io import fits
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
B=Path(__file__).resolve().parent
D=B/'243276811'
c=json.loads((D/'lead-context.json').read_text())
sectors=[19,41,54,58,74,76,78,79,80,81,82,83,85]
fig,ax=plt.subplots(len(sectors),1,figsize=(12,2.3*len(sectors)))
for a,n in zip(ax,sectors):
 s=next(z for z in c['sectors'] if z['sector']==n)
 with fits.open(s['source_path'],memmap=False) as h:
  x=h[1].data;t=np.array(x['TIME'],float);y=np.array(x['SAP_FLUX'],float);q=np.array(x['QUALITY'],int);k=np.array(x['KSPSAP_FLUX'],float) if 'KSPSAP_FLUX' in h[1].columns.names else np.full(len(t),np.nan)
 g=np.isfinite(t)&np.isfinite(y)&(y>0)&(q==0);t=t[g];y=y[g];k=k[g]
 a.plot(t,y/np.median(y),'.',ms=.6,label='SAP')
 if np.count_nonzero(np.isfinite(k)&(k>0))>100:a.plot(t,k/np.nanmedian(k),'.',ms=.5,alpha=.4,label='KSPSAP')
 for f in s['flags']:
  if f['kind']=='dip':a.axvline(f['screen_center_btjd'],color='red',lw=.5,alpha=.5)
 a.set_title(f'S{n}  {t.min():.1f}-{t.max():.1f}',fontsize=9)
 a.set_ylabel('f/median',fontsize=8)
ax[-1].legend();fig.tight_layout();fig.savefig(D/'lead-selected-sector-comparison.png',dpi=120)
