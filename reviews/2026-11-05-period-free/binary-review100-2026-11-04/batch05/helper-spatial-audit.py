import json,hashlib
from pathlib import Path
import numpy as np
from astropy.io import fits
from scipy.ndimage import shift
B=Path(__file__).resolve().parent
A=json.loads((B/'lead-source-attribution.json').read_text());out={}
for tic,mid,dur,neighbor in [('246124257',3101.055,.12,'5939588377656341504'),('313617927',1729.9,2.,'2177341612115542144')]:
 z=A[tic];q=B/'lead-pixels'/tic/'tesscut.fits'
 with fits.open(q) as h:
  t=np.array(h[1].data['TIME'],float); f=np.array(h[1].data['FLUX'],float); qual=np.array(h[1].data['QUALITY'])
 ok=np.isfinite(t)&(qual==0)&np.isfinite(f).all(axis=(1,2));t=t[ok];f=f[ok]; bg=np.median(np.sort(f.reshape(len(f),-1),axis=1)[:,:48],axis=1); f-=bg[:,None,None];x=t-mid
 core=abs(x)<.25*dur; pre=(x<-.65*dur)&(x>-1.4*dur);post=(x>.65*dur)&(x<1.4*dur)
 o=.5*(np.median(f[pre],axis=0)+np.median(f[post],axis=0)); d=o-np.median(f[core],axis=0)
 target=np.array(z['target_xy']); n=next(n for n in z['gaia_neighbors'] if n['source_id']==neighbor); delta=np.array(n['pixel_xy'])-target
 yy,xx=np.indices(o.shape);mask=(abs(xx-target[0])<=3)&(abs(yy-target[1])<=3)
 fitscores={}
 for label,template in [('target',o),('neighbor',shift(o,shift=(delta[1],delta[0]),order=1,mode='constant'))]:
  X=np.column_stack([template[mask],np.ones(mask.sum())]);coef=np.linalg.lstsq(X,d[mask],rcond=None)[0]; residual=d[mask]-X@coef
  fitscores[label]={'rms':float(np.sqrt(np.mean(residual**2))),'amplitude':float(coef[0])}
 out[tic]={'target_xy':target.tolist(),'neighbor':n,'relative_shift_xy':delta.tolist(),'fit':fitscores,'method':'Compare 7x7 difference image against out-of-event image and its bilinearly shifted copy with free amplitude and constant. Empirical target image includes background and neighboring flux; interpolation is not a calibrated TESS PRF. RMS is descriptive, not a likelihood or exclusion. Same photons as SAP.','fits_sha256':hashlib.sha256(q.read_bytes()).hexdigest()}
(B/'helper-spatial-audit.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
