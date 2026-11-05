import json,hashlib,io,zipfile
from pathlib import Path
import numpy as np
from astropy.io import fits
from astropy.wcs import WCS
B=Path(__file__).resolve().parent
out=[]
for a in json.loads((B/'lead-pixels.json').read_text()):
 sid=a['sample_id']; sec=a['sector']; path=B/f'lead-{sid}-s{sec:03d}.zip'; data=path.read_bytes()
 with zipfile.ZipFile(io.BytesIO(data)) as z:
  raw=z.read(z.namelist()[0])
 with fits.open(io.BytesIO(raw),memmap=False) as h:
  t=np.array(h[1].data['TIME'],float); f=np.array(h[1].data['FLUX'],float); q=np.array(h[1].data['QUALITY'],int); w=WCS(h[2].header)
 yy,xx=np.indices(f.shape[1:]); sky=((xx<2)|(xx>8))&((yy<2)|(yy>8)); bg=np.median(f[:,sky],axis=1)
 target=next(s for s in a['sources'] if s['is_target']); x,y=target['x'],target['y']; ap=(abs(xx-round(x))<=1)&(abs(yy-round(y))<=1)
 valid=(q==0)&np.isfinite(t)&np.all(np.isfinite(f),axis=(1,2)); c=a['center_btjd']; half=a['half_width_days']; core=valid&(abs(t-c)<half); side=valid&(abs(t-c)>.6)&(abs(t-c)<1.3)
 apflux=f[:,ap].sum(axis=1)-bg*ap.sum(); med=np.median(apflux[side]); skyvals=f[side][:,sky]
 out.append(dict(sample_id=sid,sector=sec,sha256=hashlib.sha256(data).hexdigest(),hash_matches_lead=hashlib.sha256(data).hexdigest()==a['zip_sha256'],sky_finite_fraction=float(np.isfinite(skyvals).mean()),sky_zero_fraction=float((skyvals==0).mean()),sky_median=float(np.median(skyvals)),sky_min=float(np.min(skyvals)),side_aperture_median=float(med),side_aperture_positive_fraction=float((apflux[side]>0).mean()),core_aperture_loss_ppt=float(1000*(1-np.median(apflux[core])/med)),target_xy=[x,y],nearby=[dict(id=s['source_id'],separation_arcsec=s['distance_arcsec'],ratio=s['G_flux_ratio'],xy=[s['x'],s['y']]) for s in a['sources'] if not s['is_target'] and s['G_flux_ratio']>.01]))
(B/'helper-pixel-audit.json').write_text(json.dumps(out,indent=2)+'\n')
for d in out: print(d['sample_id'],d['sector'],'sky zero',d['sky_zero_fraction'],'sky min',d['sky_min'],'ap',d['side_aperture_median'],'loss',d['core_aperture_loss_ppt'])
