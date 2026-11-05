import json,hashlib
import numpy as np
from pathlib import Path
from astropy.io import fits
from scipy.ndimage import gaussian_filter1d
B=Path(__file__).parent
out=[]
for sec,centers in [(57,[2869.832,2872.425,2874.872,2877.295,2879.540]),(84,[3600.055,3602.601,3605.141,3607.620,3609.462])]:
 p=Path(fr'[local-path-redacted]')
 with fits.open(p) as h:d=h[1].data;t=np.array(d['TIME'],float);f=np.array(d['SAP_FLUX'],float);q=np.array(d['QUALITY'])
 g=np.isfinite(t)&np.isfinite(f)&(q==0)&(f>0);t=t[g];f=f[g]/np.median(f[g]);
 for c in centers:
  core=(abs(t-c)<.2);side=(abs(t-c)>.8)&(abs(t-c)<1.05);left=(t>c-1.05)&(t<c-.8);right=(t>c+.8)&(t<c+1.05)
  def med(x):return float(np.median(f[x])) if x.sum() else None
  coverage=t[(t>c-1.05)&(t<c+1.05)]; gaps=np.diff(coverage)
  out.append(dict(sector=sec,center=c,ncore=int(core.sum()),nleft=int(left.sum()),nright=int(right.sum()),core=med(core),left=med(left),right=med(right),depth_ppt=float((np.median(f[side])-np.median(f[core]))*1000) if side.sum() and core.sum() else None,max_gap=float(max(gaps)) if len(gaps) else None,sha256=hashlib.sha256(p.read_bytes()).hexdigest()))
(B/'helper-q083-alternation.json').write_text(json.dumps(out,indent=2));print(json.dumps(out,indent=2))
