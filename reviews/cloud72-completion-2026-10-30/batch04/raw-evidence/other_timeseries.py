import json,numpy as np,pathlib,matplotlib
matplotlib.use('Agg');import matplotlib.pyplot as plt
from astropy.io import fits
R=pathlib.Path(__file__).parent; ids=['428769301','436947190','311206604','71866523','92452368','402940895'];fig,ax=plt.subplots(6,3,figsize=(16,14))
for i,tic in enumerate(ids):
 for j,f in enumerate(sorted((R/tic).glob('qlp*.fits'))):
  with fits.open(f) as h:
   a=h[1].data;t=np.asarray(a['TIME'],float);y=np.asarray(a['SAP_FLUX'],float);q=np.asarray(a['QUALITY']);ok=np.isfinite(t)&np.isfinite(y)&(y>0)&(q==0);t=t[ok];y=y[ok]/np.median(y[ok]);ax[i,j].plot(t,y,'.',ms=1,alpha=.5);ax[i,j].set_ylim(*np.percentile(y,[.5,99.5]));ax[i,j].set_title(tic+' '+f.stem)
fig.tight_layout();fig.savefig(R/'other-target-timeseries.png',dpi=140)
