import json, pathlib, numpy as np, matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from astropy.io import fits
B=pathlib.Path(r'[local-path-redacted]')
for tic in ['118207666','317718737','336670019','341854405','390853987']:
 d=json.loads((B/tic/'raw-fold.json').read_text()); wins=[x for x in d['windows'] if x['kind']=='P' and x['n_core']>2]
 fig,axes=plt.subplots(len(wins),1,figsize=(12,2.3*len(wins)),squeeze=False)
 for ax,w in zip(axes[:,0],wins):
  s=next(s for s in d['sectors'] if s['sector']==w['sector']);
  with fits.open(s['path']) as h:
   a=h[1].data;t=np.array(a['TIME']); f=np.array(a['SAP_FLUX']); q=np.array(a['QUALITY']); m=np.isfinite(t)&np.isfinite(f)&(q==0)&(f>0)&(abs(t-w['predicted_btjd'])<2); t=t[m];f=f[m];f=1000*(f/np.median(f)-1)
  ax.plot(t-w['predicted_btjd'],f,'.',ms=2);ax.axvspan(-w['duration']/2,w['duration']/2,color='red',alpha=.2);ax.set_title(f"{tic} sector {w['sector']} t0 {w['predicted_btjd']:.3f}, depth {w['depth_ppt']:.2f} ppt");ax.set_ylabel('SAP ppt')
 fig.tight_layout();fig.savefig(B/tic/'helper-windows.png',dpi=130);plt.close(fig)
 print(tic,[(w['sector'],round(w['predicted_btjd'],3),w['n_core'],round(w['depth_ppt'],2) if w['depth_ppt'] is not None else None) for w in wins])
