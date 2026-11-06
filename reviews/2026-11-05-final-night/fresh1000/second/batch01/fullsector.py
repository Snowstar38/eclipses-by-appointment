import json,numpy as np,matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from astropy.io import fits
from pathlib import Path
b=Path(__file__).resolve().parent
for tic in ['238407344','240615841','241100642','258216510','271763138','272726082','278185284','280692653']:
 d=json.loads((b/tic/'lead-context.json').read_text());fig,axs=plt.subplots(len(d['source']),1,figsize=(12,2*len(d['source'])),squeeze=False)
 for ax,src in zip(axs[:,0],d['source']):
  with fits.open(src['path']) as h:a=h[1].data;t=np.asarray(a['TIME']);f=np.asarray(a['SAP_FLUX']);q=np.asarray(a['QUALITY'])
  ok=np.isfinite(t)&np.isfinite(f)&(q==0)&(f>0);ax.plot(t[ok],f[ok]/np.median(f[ok]),'.',ms=1);ax.set_title(f"{tic} sector{src['sector']}");ax.grid(alpha=.2)
 fig.tight_layout();fig.savefig(b/tic/'lead-fullsectors.png',dpi=120);plt.close(fig)

