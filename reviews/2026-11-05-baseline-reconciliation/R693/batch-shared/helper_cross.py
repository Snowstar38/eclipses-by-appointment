import json,math
from pathlib import Path
import numpy as np
from astropy.io import fits
from astropy.wcs import WCS
import matplotlib;matplotlib.use('Agg');import matplotlib.pyplot as plt
B=Path(__file__).resolve().parent;H=B/'helper-pixels'/'95623701';g=json.loads((B/'SOURCE-SNAPSHOT.json').read_text(encoding='utf8'))['95623701']['target']['gaia'];cs=json.loads((B/'coverage-alias.json').read_text(encoding='utf8'))['95623701']['windows'];fig,axes=plt.subplots(4,1,figsize=(10,10));out=[]
for ax,sec in zip(axes,[12,39,65,103]):
 p=H/('tesscut.fits' if sec==103 else f's{sec}.fits');ep=next(x['predicted_btjd'] for x in cs if x['sector']==sec and x['kind']=='same' and x['n_core_quality0']>0)
 with fits.open(p,memmap=False) as h:t=np.array(h[1].data['TIME'],float);f=np.array(h[1].data['FLUX'],float);q=np.array(h[1].data['QUALITY'],int);w=WCS(h[2].header)
 good=np.isfinite(t)&(q==0)&np.isfinite(f).all(axis=(1,2));t=t[good];f=f[good];x=t-ep;tx,ty=w.all_world2pix(float(g['ra']),float(g['dec']),0);ix=int(round(float(tx)));iy=int(round(float(ty)));bg=np.median(np.sort(f.reshape(len(f),-1),axis=1)[:,:48],axis=1);f=f-bg[:,None,None]; pre=(x<-.15)&(x>-.45);post=(x>.15)&(x<.45);core=abs(x)<.05
 row={'sector':sec,'predicted_btjd':ep,'samples':[int(sum(core)),int(sum(pre)),int(sum(post))]}
 for rad in (0,1,2):
  y=f[:,iy-rad:iy+rad+1,ix-rad:ix+rad+1].sum(axis=(1,2));base=.5*(np.median(y[pre])+np.median(y[post]));depth=1-np.median(y[core])/base;noise=1.4826*np.median(abs(y[pre|post]/base-np.median(y[pre|post]/base)));row[f'ap{2*rad+1}_depth_ppt']=depth*1000;row[f'ap{2*rad+1}_oot_scatter_ppt']=noise*1000
  if rad==1:ax.plot(x,y/base,'.',ms=2)
 ax.axvspan(-.05,.05,alpha=.15);ax.axhline(1,color='k',lw=.5);ax.set_xlim(-.5,.5);ax.set_title(f's{sec} 3x3, n={row["samples"]}, depth={row["ap3_depth_ppt"]:.2f} ppt');out.append(row)
fig.tight_layout();fig.savefig(H/'cross-sector.png',dpi=130);(H/'cross-sector.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf8');print(json.dumps(out,indent=2))

