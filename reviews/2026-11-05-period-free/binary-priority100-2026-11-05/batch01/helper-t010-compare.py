import json,numpy as np
from pathlib import Path
from astropy.io import fits
import matplotlib;matplotlib.use('Agg');import matplotlib.pyplot as plt
B=Path(__file__).resolve().parent;tic='271782868';tm=3691.7046284502735
with fits.open(B/f'helper-{tic}-tesscut.fits',memmap=False) as h:
 d=h[1].data;t=np.array(d['TIME'],float);f=np.array(d['FLUX'],float);q=np.array(d['QUALITY']);good=(q==0)&np.isfinite(t)&np.isfinite(f).all(axis=(1,2));t=t[good];f=f[good];bg=np.median(np.sort(f.reshape(len(f),-1),axis=1)[:,:40],axis=1);yy,xx=np.indices(f.shape[1:]);ap=(abs(xx-6)<=1)&(abs(yy-5)<=1);v=f[:,ap].sum(axis=1)-ap.sum()*bg
src=json.loads((B/tic/'lead-numeric.json').read_text());p=next(z['path'] for z in src['sources'] if z['sector']==88)
with fits.open(p,memmap=False) as h:
 d=h[1].data;tq=np.array(d['TIME'],float);fq=np.array(d['SAP_FLUX'],float);qq=np.array(d['QUALITY']);g=(qq==0)&np.isfinite(tq)&np.isfinite(fq);tq=tq[g];fq=fq[g]
fig,ax=plt.subplots(2,1,figsize=(10,6),sharex=True)
for a,tt,y,title in [(ax[0],t,v,'TESSCut target 3x3 background subtracted'),(ax[1],tq,fq,'QLP SAP')]:
 sel=abs(tt-tm)<2;a.plot(tt[sel]-tm,y[sel],'.',ms=2);a.set_title(title)
fig.tight_layout();fig.savefig(B/'helper-T010-comparison.png',dpi=140)
for name,tt,y in [('cut',t,v),('qlp',tq,fq)]:
 x=tt-tm;core=abs(x)<.12;left=(x>-.65)&(x<-.35);right=(x>.35)&(x<.65);base=.5*(np.median(y[left])+np.median(y[right]));print(name,'n',core.sum(),left.sum(),right.sum(),'medians',np.median(y[core]),np.median(y[left]),np.median(y[right]),'depth',1000*(1-np.median(y[core])/base))
