import json,numpy as np,hashlib
from pathlib import Path
from astropy.io import fits
B=Path(__file__).resolve().parent;out=[]
for p in sorted(B.glob('helper-*-tesscut.fits')):
 with fits.open(p,memmap=False) as h:
  t=np.asarray(h[1].data['TIME']);q=np.asarray(h[1].data['QUALITY']);f=np.asarray(h[1].data['FLUX']);g=np.isfinite(t)&(q==0)&np.isfinite(f).all(axis=(1,2));a=f[g].reshape(np.sum(g),-1);bg=np.median(np.sort(a,axis=1)[:,:40],axis=1);edge=np.concatenate([f[g,0,:],f[g,-1,:],f[g,1:-1,0],f[g,1:-1,-1]],axis=1);out.append({'file':p.name,'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'good':int(g.sum()),'background_min_median_max':[float(np.min(bg)),float(np.median(bg)),float(np.max(bg))],'zero_edge_fraction':float(np.mean(edge==0))})
(B/'helper-background-audit.json').write_text(json.dumps(out,indent=2));print([(x['file'],[round(v,2) for v in x['background_min_median_max']],x['zero_edge_fraction']) for x in out])
