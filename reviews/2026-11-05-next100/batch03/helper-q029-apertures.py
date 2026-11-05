import zipfile,io,json,hashlib
from pathlib import Path
import numpy as np
from astropy.io import fits
from astropy.wcs import WCS
B=Path(__file__).resolve().parent; timing=json.loads((B/'168657537/lead-timing.json').read_text())['aliases_by_late_epoch_cycle_offset']['0']; p=timing['period_days']; ep=timing['epoch_btjd']; out={}
for s in [4,5,31]:
 z=zipfile.ZipFile(B/f'helper-q029-s{s}.zip'); h=fits.open(io.BytesIO(z.read(z.namelist()[0]))); a=h[1].data;t=np.array(a['TIME']);f=np.array(a['FLUX']);q=np.array(a['QUALITY']);w=WCS(h[2].header); coords=w.all_world2pix([[61.0087694264,-31.7792897141],[61.0113511652,-31.7568322887]],0);yy,xx=np.indices(f.shape[1:]); phase=(t-ep+p/2)%p-p/2;cyc=np.rint((t-ep)/p).astype(int); ok=np.isfinite(t)&(q==0); data={}
 for name,(x,y) in zip(['target','neighbor'],coords):
  mask=(abs(xx-round(x))<=1)&(abs(yy-round(y))<=1); lc=np.nansum(f[:,mask],axis=1); vals=[]
  for c in np.unique(cyc[ok]):
   on=ok&(cyc==c)&(abs(phase)<.045);off=ok&(cyc==c)&(abs(phase)>.09)&(abs(phase)<.20)
   if on.sum()>=2 and off.sum()>=2:
    base=np.median(lc[off]); vals.append({'cycle':int(c),'parity':int(c%2),'depth_ppt':float(1000*(1-np.median(lc[on])/base)),'loss_e_per_s':float(base-np.median(lc[on]))})
  data[name]={'mask_pixels':int(mask.sum()),'median_flux':float(np.median(lc[ok])),'events':vals,'parity_median_ppt':[float(np.median([v['depth_ppt'] for v in vals if v['parity']==k])) for k in (0,1)]}
 out[str(s)]=data
(B/'helper-q029-apertures.json').write_text(json.dumps(out,indent=2));print(json.dumps({s:{k:{'flux':round(v['median_flux']), 'parity_ppt':v['parity_median_ppt']} for k,v in d.items()} for s,d in out.items()},indent=2))
