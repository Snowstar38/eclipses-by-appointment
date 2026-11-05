import numpy as np
from astropy.io import fits
from astropy.wcs import WCS
import matplotlib;matplotlib.use('Agg')
import matplotlib.pyplot as plt
from pathlib import Path
import json
B=Path(__file__).resolve().parent;tic='449012335';g=json.loads((B/'SOURCE-SNAPSHOT.json').read_text())[tic]['target']['gaia'];h=B/'helper-pixels'/tic
with fits.open(h/'tesscut.fits',memmap=False) as f: t=np.array(f[1].data['TIME'],float);v=np.array(f[1].data['FLUX'],float);q=np.array(f[1].data['QUALITY']);w=WCS(f[2].header)
tx,ty=w.all_world2pix(float(g['ra']),float(g['dec']),0);ix=round(float(tx));iy=round(float(ty));ok=np.isfinite(t)&(q==0)&np.isfinite(v).all(axis=(1,2))&(t>4080)&(t<4091);t=t[ok];v=v[ok];bg=np.median(np.sort(v.reshape(len(v),-1),axis=1)[:,:48],axis=1);v-=bg[:,None,None]
fig,ax=plt.subplots(figsize=(12,4))
for r in (0,1,2):
 y=v[:,iy-r:iy+r+1,ix-r:ix+r+1].sum(axis=(1,2));base=np.median(y[(t>4081)&(t<4083)]);ax.plot(t,y/base,'.',ms=1,label=f'{2*r+1}x{2*r+1}')
ax.set_ylim(.93,1.03);ax.set_xlabel('BTJD');ax.set_ylabel('relative flux');ax.legend();fig.tight_layout();fig.savefig(h/'custom-lightcurve.png',dpi=160)
