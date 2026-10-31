import json,math,hashlib,glob
import numpy as np
from astropy.io import fits
from pathlib import Path
b=Path(__file__).resolve().parent.parent; h=b/'helper'; source=b.parent/'targets-selected.json';targets=json.load(open(source));out={'availability':{'source':str(source),'sha256':hashlib.sha256(source.read_bytes()).hexdigest(),'note':'Prefetched selected-target QLP product metadata, current queue preparation; not a fresh search at helper review time.','tic_sectors':{t:[s for s,u in targets[t]['qlp']] for t in ['156985493','5781196']}},'156_half_period_checks':[],'156_aperture_depth_ppt':[]}
p=b.parent/'shared-qlp/156985493_s049.fits'
with fits.open(p) as z:
 a=z[1].data;t=np.array(a['TIME']);f=np.array(a['SAP_FLUX']);q=np.array(a['QUALITY']);
 for c in [2649.223,2659.171]:
  good=np.isfinite(t)&np.isfinite(f)&(q==0);i=np.isfinite(t)&np.isfinite(f)&(abs(t-c)<.06);o=np.isfinite(t)&np.isfinite(f)&(abs(t-c)>.1)&(abs(t-c)<.2);sel=i&good
  out['156_half_period_checks'].append({'center_btjd':c,'n_all':int(sum(i)),'n_unflagged':int(sum(sel)),'minimum_relative_to_local_baseline':float(np.min(f[sel])/np.median(f[o])),'samples':[{'btjd':float(tt),'raw_flux':float(ff),'quality':int(qq)} for tt,ff,qq in zip(t[i],f[i],q[i])]})
p=Path(glob.glob(str(h/'tesscut156/*fits'))[0]);out['156_tesscut_sha256']=hashlib.sha256(p.read_bytes()).hexdigest()
with fits.open(p) as z:
 a=z[1].data;t=np.array(a['TIME']);im=np.array(a['FLUX']);q=np.array(a['QUALITY']);
 for c in [1908.162,1918.103974]:
  i=(abs(t-c)<.027)&(q==0);o=(abs(t-c)>.065)&(abs(t-c)<.17)&(q==0);depth=[]
  for r in [0,1,2]:
   f=np.nansum(im[:,8-r:9+r,8-r:9+r],axis=(1,2));depth.append(float(1000*(1-np.mean(f[i])/np.mean(f[o]))))
  out['156_aperture_depth_ppt'].append({'center_btjd':c,'in_count':int(sum(i)),'out_count':int(sum(o)),'square_1_3_5':depth})
(h/'156-checks.json').write_text(json.dumps(out,indent=2));print(json.dumps(out['availability'],indent=2))
