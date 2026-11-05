"""Root check of four post-helper verdict changes; aperture sensitivity and context."""
from pathlib import Path
import json
import numpy as np
from astropy.io import fits
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
W=Path(__file__).resolve().parent; B=W/'batch02'
rows=json.loads((B/'lead-exception-pixels.json').read_text())
fig,axs=plt.subplots(4,1,figsize=(11,12)); out=[]
for ax,r in zip(axs,rows):
 tic=r['tic']; sec=r['sector']; tm=r['time_btjd']
 with fits.open(B/f'lead-{tic}-s{sec}.fits') as h:
  d=h[1].data;t=np.asarray(d['TIME'],float); f=np.asarray(d['FLUX'],float);q=d['QUALITY']
 g=np.isfinite(t)&np.isfinite(f).all(axis=(1,2))&(q==0);t=t[g];f=f[g];x=t-tm
 bg=np.median(np.sort(f.reshape(len(f),-1),axis=1)[:,:40],axis=1); f=f-bg[:,None,None]
 yy,xx=np.indices(f.shape[1:]);tx,ty=r['target_xy']; rec={'sample_id':r['sample_id'],'apertures':[]}
 co,pr,po=[r['windows_days'][k] for k in ['core','pre','post']]
 core=(x>=co[0])&(x<=co[1]);pre=(x>=pr[0])&(x<=pr[1]);post=(x>=po[0])&(x<=po[1])
 for rad in [1,2]:
  ap=f[:,(abs(xx-round(tx))<=rad)&(abs(yy-round(ty))<=rad)].sum(axis=1)
  base=np.median(ap[pre|post]); dep=1000*(1-np.median(ap[core])/base)
  rec['apertures'].append({'width':2*rad+1,'baseline_counts':float(base),'deficit_ppt':float(dep),'pre_counts':float(np.median(ap[pre])),'post_counts':float(np.median(ap[post]))})
  m=abs(x)<3;ax.plot(x[m],ap[m]/base,'.',ms=1,label=f'{2*rad+1}x{2*rad+1} pixels')
 with fits.open(Path('[local-path-redacted]')/f'{tic}_s{sec:03d}.fits') as h:
  d=h[1].data;qt=np.asarray(d['TIME'],float);qf=np.asarray(d['SAP_FLUX'],float);good=(d['QUALITY']==0)&np.isfinite(qf)
 qx=qt-tm; sides=good&(((qx>=pr[0])&(qx<=pr[1]))|((qx>=po[0])&(qx<=po[1])))
 m=good&(abs(qx)<3);ax.plot(qx[m],qf[m]/np.median(qf[sides]),'.',ms=1,label='QLP SAP')
 ax.axvspan(*co,alpha=.15,color='orange');ax.set_title(f"{r['sample_id']} S{sec}");ax.legend(loc='best');out.append(rec)
fig.tight_layout();fig.savefig(W/'root-check02-pixels.png',dpi=120)
(W/'root-check02-pixels.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf8')
print(json.dumps(out,indent=2))
