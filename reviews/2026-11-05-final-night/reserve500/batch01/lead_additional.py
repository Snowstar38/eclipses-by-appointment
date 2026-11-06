from pathlib import Path
import json,numpy as np,matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from astropy.io import fits
b=Path(__file__).resolve().parent
for tic,events in {'37951551':[(5,1462.2),(32,2187.7),(98,4025.5)],'93104494':[(4,1418.1),(31,2164.5)]}.items():
 d=json.loads((b/tic/'lead-context.json').read_text());fig,axs=plt.subplots(len(events),1,figsize=(11,3*len(events)),squeeze=False)
 for ax,(sec,c) in zip(axs[:,0],events):
  src=next(s for s in d['source'] if s['sector']==sec)
  with fits.open(src['path']) as h:
   a=h[1].data;t=np.array(a['TIME']);y=np.array(a['SAP_FLUX']);q=np.array(a['QUALITY'])
  ok=np.isfinite(t)&np.isfinite(y)&(y>0)&(abs(t-c)<1.5);t=t[ok];y=y[ok];q=q[ok];y/=np.median(y[q==0]);ax.plot(t[q==0],y[q==0],'.',ms=2);ax.plot(t[q!=0],y[q!=0],'x',color='red');ax.set_title(f'{tic} S{sec}');ax.grid(alpha=.2)
 fig.tight_layout();fig.savefig(b/tic/'lead-additional-context.png');plt.close(fig)
