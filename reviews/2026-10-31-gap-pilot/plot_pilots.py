import pathlib,json,sys,os
import numpy as np
import matplotlib;matplotlib.use('Agg')
import matplotlib.pyplot as plt
from astropy.io import fits
O=pathlib.Path(__file__).parent
sys.path.insert(0,'[local path omitted] 5.1/made/appointments');import appoint
def read(p):
 with fits.open(p) as ff:
  d=ff[1].data;t=np.asarray(d['TIME'],float);f=np.asarray(d['SAP_FLUX'],float);q=d['QUALITY'];m=np.isfinite(t)&np.isfinite(f)&(q==0);t=t[m];f=f[m];f/=np.median(f)
 return appoint.binit(t,f)
def band():
 rs=json.load(open(O/'band-results-72.json'))
 for r in rs:
  good=[e for e in r['events'] if np.isfinite(e['snr']) and e['snr']>8 and .6<e['far']<1.6 and e['halves']]
  if len(good)<2:continue
  fig,axs=plt.subplots(min(8,len(r['files'])),2,figsize=(12,min(8,len(r['files']))*2.2),squeeze=False)
  ep=r['historical_search']['P'];P=ep['P'];t0=ep['t0']
  for ax,ff in zip(axs,r['files']):
   t,f=read(ff['path']);ph=(t-t0+P/2)%P-P/2
   ax[0].plot(t,1000*(f-1),'.',ms=1);ax[0].set_title(pathlib.Path(ff['path']).stem,fontsize=8)
   ax[1].plot(ph,1000*(f-1),'.',ms=1);ax[1].set_xlim(-1,1);ax[1].axvline(0,c='r',lw=.5)
  fig.suptitle(f"TIC{r['tic']} rawSAP P={P:.8f}d");fig.tight_layout();fig.savefig(O/f"band-{r['tic']}.png",dpi=110);plt.close(fig)
def long():
 rs=json.load(open(O/'long-results.json'));fig,axs=plt.subplots(8,2,figsize=(13,22))
 for ax,r in zip(axs.flat,rs):
  t,f=read(r['path']);c=r['historical_best']['t'];m=abs(t-c)<5
  ax.plot(t[m]-c,(f[m]-1)*1000,'.',ms=1);ax.axvline(0,c='r',lw=.5);ax.set_title(f"{r['tic']} s{r['historical_best']['sector']} t={c}",fontsize=8)
 fig.tight_layout();fig.savefig(O/'long16.png',dpi=120)
if __name__=='__main__':band();long()
