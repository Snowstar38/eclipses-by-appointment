import zipfile,io,pathlib,numpy as np,json,matplotlib
matplotlib.use('Agg');import matplotlib.pyplot as plt
from astropy.io import fits
B=pathlib.Path(r'[local-path-redacted]');p=json.loads((B/'raw-fold.json').read_text())['fold']['P'];fig,axs=plt.subplots(3,1,figsize=(11,8))
for ax,sec in zip(axs,[98,107,108]):
 with zipfile.ZipFile(B/f'helper-tesscut-s{sec}.zip') as z:
  with fits.open(io.BytesIO(z.read(next(n for n in z.namelist() if n.endswith('.fits'))))) as h:
   a=h[1].data;t=np.asarray(a['TIME']);q=np.asarray(a['QUALITY']);cube=np.asarray(a['FLUX']);c=p['t0']+round((np.nanmedian(t)-p['t0'])/p['P'])*p['P'];m=np.isfinite(t)&(q==0)&(abs(t-c)<.7);x=t[m]-c;f=np.nansum(cube[m,1:4,1:4],axis=(1,2));side=(abs(x)>.2)&(abs(x)<.5);core=abs(x)<p['dur']/2;baseline=np.median(f[side]);y=1000*(f/baseline-1);ax.plot(x,y,'.',ms=2);ax.axvspan(-p['dur']/2,p['dur']/2,color='red',alpha=.2);ax.set_title(f'S{sec} {c:.5f} 3x3 depth {(-np.median(y[core])):.2f} ppt');print(sec,c,'depth',-np.median(y[core]),'core firstlast',x[core].min(),x[core].max(),'core maxgap',np.diff(x[core]).max(),'scatter side',1.4826*np.median(abs(y[side]-np.median(y[side]))))
fig.tight_layout();fig.savefig(B/'helper-newsectors.png',dpi=140)
