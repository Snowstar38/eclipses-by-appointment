import json,math
from pathlib import Path
import numpy as np
from astropy.io import fits
from astropy.wcs import WCS
B=Path(__file__).resolve().parent;H=B/'helper-pixels';D=json.loads((B/'SOURCE-SNAPSHOT.json').read_text(encoding='utf8'));R=json.loads((H/'conservative-neighbors.json').read_text(encoding='utf8'))
for o in R:
 tic=o['tic'];h=H/tic;g=D[tic]['target']['gaia'];r=json.loads((h/'receipt.json').read_text());e=r['event'];
 with fits.open(h/'tesscut.fits',memmap=False) as hd:t=np.array(hd[1].data['TIME'],float);f=np.array(hd[1].data['FLUX'],float);q=np.array(hd[1].data['QUALITY'],int);w=WCS(hd[2].header)
 good=np.isfinite(t)&(q==0)&np.isfinite(f).all(axis=(1,2));t=t[good];f=f[good];x=t-e['mid_btjd'];d=e['duration_days'];core=abs(x)<.3*d;pre=(x<-.75*d)&(x>-1.75*d);post=(x>.75*d)&(x<1.75*d);tx,ty=w.all_world2pix(float(g['ra']),float(g['dec']),0);ix=int(round(float(tx)));iy=int(round(float(ty)));bg=np.median(np.sort(f.reshape(len(f),-1),axis=1)[:,:48],axis=1);f=f-bg[:,None,None];ap={}
 for rad in (0,1,2):
  y=f[:,iy-rad:iy+rad+1,ix-rad:ix+rad+1].sum(axis=(1,2));base=.5*(np.median(y[pre])+np.median(y[post]));ap[f'{2*rad+1}x{2*rad+1}']=float(1000*(1-np.median(y[core])/base))
 o['pixel_apertures_ppt']=ap
 for n in o['capable_at_conservative_depth']:n['separation_tess_pixels']=n['sep_arcsec']/21.0
 print(tic,ap)
(H/'aperture-neighbors.json').write_text(json.dumps(R,indent=2)+'\n',encoding='utf8')

