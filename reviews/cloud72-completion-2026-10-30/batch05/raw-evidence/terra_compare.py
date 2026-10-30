import pathlib,json,numpy as np,matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from astropy.io import fits
R=pathlib.Path(__file__).parent
rows=json.load(open(R/'independent-extraction.json'))
fig,axs=plt.subplots(len(rows),1,figsize=(15,35))
for ax,row in zip(axs,rows):
 tic=row['tic']; sec=row['sector']; z=np.load(R/row['file']); t=z['time']; f=z['flux']; f=f/np.nanmedian(f)
 with fits.open(R/tic/f'qlp_s{sec:03}.fits') as h:
  a=h[1].data; tq=np.array(a['TIME']);fq=np.array(a['SAP_FLUX']); q=np.array(a['QUALITY']);m=np.isfinite(tq)&np.isfinite(fq)&(q==0)&(fq>0);tq=tq[m];fq=fq[m]/np.nanmedian(fq[m])
 ax.scatter(tq,fq,s=.4,c='blue',alpha=.5);ax.scatter(t,f,s=.4,c='red',alpha=.5);ax.set_title(f'{tic} S{sec}: QLP blue / custom red');ax.set_ylim(*np.percentile(np.concatenate([fq,f]),[.3,99.7]));ax.grid(alpha=.2)
fig.tight_layout();fig.savefig(R/'terra-independent-comparison.png',dpi=120)
