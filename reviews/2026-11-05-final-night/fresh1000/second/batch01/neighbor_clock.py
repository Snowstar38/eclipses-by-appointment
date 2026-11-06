import json,requests,hashlib,numpy as np
from pathlib import Path
from astropy.io import fits
b=Path(__file__).resolve().parent;tic='240615813';u=f'https://mast.stsci.edu/api/v0.1/Download/file?uri=mast:HLSP/qlp/s0083/0000/0002/4061/5813/hlsp_qlp_tess_ffi_s0083-0000000240615813_tess_v01_llc.fits';r=requests.get(u,timeout=35);r.raise_for_status();p=b/'240615841'/'lead-neighbor240615813-s83.fits';p.write_bytes(r.content)
with fits.open(p) as h:
 a=h[1].data;t=np.array(a['TIME'],float);f=np.array(a['SAP_FLUX'],float);q=np.array(a['QUALITY']);o=[]
 for c in [3559.92028,3569.63141,3574.84653]:
  core=(abs(t-c)<.05)&(q==0);side=(abs(t-c)>.2)&(abs(t-c)<.4)&(q==0);o.append({'btjd':c,'core_n':int(core.sum()),'loss':float(1-np.median(f[core])/np.median(f[side]))})
 out={'tic':tic,'url':u,'sha256':hashlib.sha256(r.content).hexdigest(),'TICID':h[0].header['TICID'],'sector':h[0].header['SECTOR'],'events':o}
(b/'240615841'/'lead-neighbor-clock.json').write_text(json.dumps(out,indent=2));print(out)
