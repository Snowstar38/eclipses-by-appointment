import json,numpy as np,hashlib
from pathlib import Path
from astropy.io import fits
B=Path(__file__).resolve().parent; out=[]
for sec,tm in [(19,1832.679),(73,3292.676)]:
 p=B/(f'helper-235985439-s{sec}-tesscut.fits' if sec==19 else 'helper-235985439-tesscut.fits')
 with fits.open(p) as h:
  a=h[1].data;t=np.asarray(a['TIME'],float);q=np.asarray(a['QUALITY']);f=np.asarray(a['FLUX']);good=np.isfinite(t)&(q==0)&np.isfinite(f).all(axis=(1,2));t=t[good];cad=np.median(np.diff(t));x=t-tm
  windows={}
  for name,lo,hi in [('pre',-.55,-.25),('core',-.07,.07),('post',.25,.55)]:
   z=t[(x>lo)&(x<hi)];windows[name]={'count':int(len(z)),'first_offset':float(z.min()-tm),'last_offset':float(z.max()-tm),'max_internal_gap':float(np.max(np.diff(z))),'nominal_cadence':float(cad)}
  out.append({'sector':sec,'screen_btjd':tm,'fits_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'windows':windows})
(B/'helper-N009-coverage.json').write_text(json.dumps(out,indent=2));print(out)
