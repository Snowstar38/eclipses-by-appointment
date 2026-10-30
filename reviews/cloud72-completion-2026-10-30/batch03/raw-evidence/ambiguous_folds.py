from pathlib import Path
import json,numpy as np
from astropy.io import fits
import matplotlib;matplotlib.use('Agg')
import matplotlib.pyplot as plt
R=Path(__file__).parent;raw=json.load(open(R/'raw-events.json'));ids=['12320469','450217907','86908196','411647453'];out={};fig,axs=plt.subplots(4,3,figsize=(15,12))
for row,tic in enumerate(ids):
 P=raw[tic]['search_period'];t0=raw[tic]['search_epoch'];out[tic]=[]
 for col,f in enumerate(sorted((R/tic).glob('qlp*.fits'))[:3]):
  with fits.open(f) as h:
   a=h[1].data;t=np.asarray(a['TIME'],float);y=np.asarray(a['SAP_FLUX'],float);q=np.asarray(a['QUALITY']);m=np.isfinite(t)&np.isfinite(y)&(y>0)&(q==0);t=t[m];y=y[m];y/=np.median(y)
  phase=((t-t0)/P+.5)%1-.5;ax=axs[row,col];ax.plot(phase,y,'.',ms=1,alpha=.3);bins=np.linspace(-.5,.5,81);v=np.array([np.median(y[(phase>=l)&(phase<u)]) for l,u in zip(bins[:-1],bins[1:])]);ax.plot((bins[:-1]+bins[1:])/2,v,'r-');ax.set_title(f'{tic} {f.stem} P={P:.6f}');ax.set_ylim(np.percentile(y,[.5,99.5]));out[tic].append(dict(sector=f.stem,phase_bin_centers=((bins[:-1]+bins[1:])/2).tolist(),median_flux=v.tolist()))
fig.tight_layout();fig.savefig(R/'ambiguous-folds.png',dpi=140);json.dump(out,open(R/'ambiguous-folds.json','w'),indent=2)
