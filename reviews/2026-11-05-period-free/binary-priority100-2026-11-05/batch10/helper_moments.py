from pathlib import Path
import json,numpy as np,hashlib
from astropy.io import fits
B=Path(__file__).parent; out=[]
for tic in ['212431520','95244521']:
 p=B/tic;f=next(p.glob('helper-s*-tesscut.fits')); rec=json.loads(next(p.glob('helper-s*-receipt.json')).read_text());e=rec['event'];c=e.get('fit_mid_btjd',e['screen_btjd']);dur=e.get('fit_duration_days',e['screen_duration_days'])
 with fits.open(f) as h:
  t=np.asarray(h[1].data['TIME']);q=np.asarray(h[1].data['QUALITY']);v=np.asarray(h[1].data['FLUX']);
 g=(q==0)&np.isfinite(t);core=g&(abs(t-c)<min(dur*.18,.07));side=g&(abs(t-c)>max(dur*.8,.35))&(abs(t-c)<max(dur*1.6,.8));dif=np.nanmedian(v[side],axis=0)-np.nanmedian(v[core],axis=0); yy,xx=np.indices(dif.shape); bg=np.nanmedian(dif[(xx-4)**2+(yy-4)**2>12]); w=np.maximum(dif-bg,0);mask=(xx-4)**2+(yy-4)**2<12; w*=mask;out.append(dict(tic=tic,difference_positive_centroid=[float((w*xx).sum()/w.sum()),float((w*yy).sum()/w.sum())],difference_background=float(bg),file_sha256=hashlib.sha256(f.read_bytes()).hexdigest(),note='positive residual moment within radius sqrt(12) pixels of nominal cutout center; descriptive, not calibrated PRF fit'))
print(json.dumps(out,indent=2));(B/'helper-moments.json').write_text(json.dumps(out,indent=2))
