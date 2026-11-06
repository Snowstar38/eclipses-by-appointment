import zipfile,glob,numpy as np,hashlib,json
from astropy.io import fits
from astropy.wcs import WCS
from astropy.coordinates import SkyCoord
import astropy.units as u
p='[workspace]/Astra/made/final-night-2026-11-05/fresh1000/first/batch04/helper/'
out={}
for z in glob.glob(p+'*.zip'):
 with zipfile.ZipFile(z) as f:
  with f.open(f.namelist()[0]) as a:
   with fits.open(a) as h:
    d=h[1].data;t=d['TIME']; pix=d['FLUX']; q=d['QUALITY']; name=z.split('\\')[-1]; out[name]={'sha256':hashlib.sha256(open(z,'rb').read()).hexdigest(),'time_bounds':[float(np.nanmin(t)),float(np.nanmax(t))]}
    if '232631' in z:
     c=3592.967669; good=(q==0)&np.isfinite(t); inside=good&(abs(t-c)<.38); outside=good&(abs(t-c)>.8)&(abs(t-c)<1.5)
     diff=np.nanmedian(pix[outside],axis=0)-np.nanmedian(pix[inside],axis=0)
     print('diff matrix',np.round(diff,1)); print('N',inside.sum(),outside.sum())
     w=WCS(h[2].header); x,y=w.world_to_pixel(SkyCoord(269.339603329087*u.deg,56.7263391016778*u.deg)); print('target xy',x,y,'peak',np.unravel_index(np.nanargmax(diff),diff.shape));print(h[2].header)
     out[name].update(diff=diff.tolist(),target_xy=[float(x),float(y)],inside=int(inside.sum()),outside=int(outside.sum()))
    else:
     s=np.nansum(pix[:,2:5,2:5],axis=(1,2)); good=(q==0)&np.isfinite(t)&np.isfinite(s); c=2971.1+24*56.54317309516961; core=good&(abs(t-c)<.3); side=good&(abs(t-c)>.7)&(abs(t-c)<1.5)
     print(name,'pred',c,'N',core.sum(),side.sum(),'relative',np.nanmedian(s[core])/np.nanmedian(s[side])-1 if core.sum() and side.sum() else None)
     out[name].update(predicted_btjd=c,core=int(core.sum()),side=int(side.sum()),relative=float(np.nanmedian(s[core])/np.nanmedian(s[side])-1) if core.sum() and side.sum() else None)
json.dump(out,open(p+'helper-pixel-summary.json','w'),indent=2)
