import json,hashlib
from pathlib import Path
import numpy as np
from astropy.io import fits
from astropy.wcs import WCS
import matplotlib;matplotlib.use('Agg')
import matplotlib.pyplot as plt
B=Path(__file__).resolve().parent;D=B/'392924671'
q=json.loads((B.parent/'source-packets/392924671/sources.json').read_text())['queue_row']
p=D/'tesscut.fits';expected=json.loads((D/'tesscut-receipt.json').read_text())['fits_sha256'];assert hashlib.sha256(p.read_bytes()).hexdigest()==expected
with fits.open(p,memmap=False) as h:
 a=h[1].data;t=np.asarray(a['TIME'],float);Q=np.asarray(a['QUALITY'],int);F=np.asarray(a['FLUX'],float);w=WCS(h[2].header)
x,y=w.all_world2pix(float(q['ra_deg']),float(q['dec_deg']),0);yy,xx=np.indices(F.shape[1:]);bgmask=(abs(xx-x)>=3)|(abs(yy-y)>=3)
bg=np.nanmedian(F[:,bgmask],axis=1)
curves={}
for radius in [1,2]:
 mask=(abs(xx-x)<=radius)&(abs(yy-y)<=radius)
 curves[str(radius)]=np.nansum((F-bg[:,None,None])[:,mask],axis=1)
valid=np.isfinite(t)&(Q==0)
fig,axes=plt.subplots(2,1,figsize=(10,6),sharex=True)
out={'source':'TESSCut same sector 23 pixels; independent aperture, not independent observing occasion','tesscut_sha256':expected,'wcs_target_pixel':[float(x),float(y)],'apertures':{}}
for ax,(radius,c) in zip(axes,curves.items()):
 ok=valid&np.isfinite(c)&(c>0);base=np.nanmedian(c[ok&(t>1930)&(t<1932)]);sel=ok&(t>1930)&(t<1938)
 ax.plot(t[sel],c[sel]/base,'.',ms=3);ax.set_ylabel(f'{radius} pixel radius / baseline');ax.axvline(1934.3,color='red',lw=.6)
 bins=[]
 for lo,hi in [(1930,1932),(1932,1933),(1933,1934),(1934,1935),(1935,1936),(1936,1938)]:
  m=ok&(t>=lo)&(t<hi)
  bins.append({'start':lo,'end':hi,'n':int(sum(m)),'median_normalized':float(np.median(c[m])/base) if m.any() else None})
 out['apertures'][radius]={'pixel_count':int(np.sum((abs(xx-x)<=int(radius))&(abs(yy-y)<=int(radius)))),'bins':bins}
axes[-1].set_xlabel('BTJD');fig.tight_layout();fig.savefig(D/'alternate-aperture.png',dpi=140)
(D/'alternate-aperture.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
