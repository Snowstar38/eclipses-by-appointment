from pathlib import Path
import json,numpy as np,matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from astropy.io import fits
b=Path(__file__).resolve().parent
for p in b.glob('*/lead-context.json'):
 d=json.loads(p.read_text());fig,axs=plt.subplots(len(d['source']),1,figsize=(13,2*len(d['source'])),squeeze=False)
 for ax,s in zip(axs[:,0],d['source']):
  with fits.open(s['path']) as h:
   a=h[1].data;t=np.array(a['TIME']);y=np.array(a['SAP_FLUX']);q=np.array(a['QUALITY'])
  ok=np.isfinite(t)&np.isfinite(y)&(y>0)&(q==0);t=t[ok];y=y[ok];y/=np.median(y);ax.plot(t,y,'.',ms=.7);ax.set_title('S'+str(s['sector']));ax.grid(alpha=.2)
 fig.tight_layout();fig.savefig(p.parent/'lead-allsectors.png',dpi=100);plt.close(fig)
