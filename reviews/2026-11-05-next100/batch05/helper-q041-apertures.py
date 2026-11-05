import json,io,zipfile,hashlib
from pathlib import Path
import numpy as np
from astropy.io import fits
B=Path(__file__).resolve().parent
out=[]
for a in json.loads((B/'helper-q041-pixels.json').read_text()):
 if a['sample_id'] not in ('Q041','Q046','Q050'):continue
 path=B/f"helper-{a['sample_id']}-s{a['sector']:03d}.zip"; z=zipfile.ZipFile(path); raw=z.read(z.namelist()[0]);
 with fits.open(io.BytesIO(raw)) as h:
  t=np.array(h[1].data['TIME']); f=np.array(h[1].data['FLUX']); q=np.array(h[1].data['QUALITY'])
 yy,xx=np.indices(f.shape[1:]); sky=((xx<2)|(xx>8))&((yy<2)|(yy>8)); bg=np.median(f[:,sky],axis=1); valid=(q==0)&np.isfinite(t)&np.all(np.isfinite(f),axis=(1,2)); c=a['center_btjd']; core=valid&(abs(t-c)<a['half_width_days']); side=valid&(abs(t-c)>.6)&(abs(t-c)<1.3)
 base=np.median(f[side],axis=0)-np.median(bg[side]); dip=np.median(f[core],axis=0)-np.median(bg[core]); diff=base-dip
 s=next(s for s in a['sources'] if s['is_target']); x=round(s['x']);y=round(s['y']); row=dict(sample_id=a['sample_id'],sector=a['sector'],zip_sha256=hashlib.sha256(path.read_bytes()).hexdigest(),target_xy=[s['x'],s['y']],pixel_difference_5x5=diff[y-2:y+3,x-2:x+3].tolist(),apertures=[])
 for radius in (0,1,2,3,4):
  ap=(abs(xx-x)<=radius)&(abs(yy-y)<=radius); denom=base[ap].sum(); row['apertures'].append(dict(size=2*radius+1,baseline=float(denom),difference=float(diff[ap].sum()),depth_ppt=float(1000*diff[ap].sum()/denom)))
 row['nearby']=[s for s in a['sources'] if not s['is_target'] and s['G_flux_ratio']>.01];out.append(row)
(B/'helper-q041-apertures.json').write_text(json.dumps(out,indent=2)+'\n')
for x in out:print(x['sample_id'],x['apertures'],'5x5',np.round(x['pixel_difference_5x5'],1).tolist(), 'neighbors',[(round(s['distance_arcsec'],1),round(s['G_flux_ratio'],3)) for s in x['nearby']])
