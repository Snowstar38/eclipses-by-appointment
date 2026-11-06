import json,numpy as np,matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from pathlib import Path
from astropy.io import fits
b=Path(__file__).resolve().parent
for tic in [x.name for x in b.iterdir() if x.is_dir()]:
 d=json.loads((b/tic/'lead-context.json').read_text());ev=json.loads((b/tic/'lead-timing.json').read_text());fig,axs=plt.subplots(len(ev),1,figsize=(9,2*len(ev)),squeeze=False)
 for ax,e in zip(axs[:,0],ev):
  src=next(s for s in d['source'] if s['sector']==e['sector'])
  with fits.open(src['path']) as h:a=h[1].data;t=np.array(a['TIME']);f=np.array(a['SAP_FLUX']);q=np.array(a['QUALITY'])
  ok=np.isfinite(t)&np.isfinite(f)&(f>0)&(q==0)&(abs(t-e['screen_btjd'])<.9);x=t[ok]-e['screen_btjd'];y=f[ok];ax.plot(x,y/np.median(y),'.',ms=2);ax.set_title(f"{tic} S{e['sector']} around {e['screen_btjd']:.5f}");ax.grid(alpha=.2)
 fig.tight_layout();fig.savefig(b/tic/'lead-selected-events.png',dpi=120);plt.close(fig)


