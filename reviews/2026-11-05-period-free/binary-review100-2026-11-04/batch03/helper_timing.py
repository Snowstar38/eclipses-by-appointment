import json,hashlib
from pathlib import Path
import numpy as np
from astropy.io import fits
from scipy.optimize import least_squares
B=Path(__file__).resolve().parent;tic='113645244'; events=[]
for sec,c in [(13,1676.3498),(27,2053.8773),(67,3144.4603),(94,3857.5373)]:
 p=Path(f'[local-path-redacted]')
 with fits.open(p) as h:a=h[1].data;t=np.array(a['TIME'],float);f=np.array(a['SAP_FLUX'],float);q=np.array(a['QUALITY'])
 ok=np.isfinite(t)&np.isfinite(f)&(q==0)&(abs(t-c)<.3);x=t[ok]-c;y=f[ok]/np.median(f[ok])
 def res(v):
  b,s,d,o,w=v;return b+s*x-d*np.maximum(0,1-abs(x-o)/w)-y
 v=least_squares(res,[1,0,.012,0,.07],bounds=([.95,-.1,0,-.1,.015],[1.05,.1,.1,.1,.2])).x
 events.append({'sector':sec,'center_btjd':c+v[3],'depth_ppt':v[2]*1000,'half_width_days':v[4],'n':int(ok.sum()),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()})
a=np.array([v['center_btjd'] for v in events]);aliases=[]
for n in range(5,15):
 p=(a[1]-a[0])/n; cycles=np.rint((a-a[0])/p);r=a-(a[0]+cycles*p);aliases.append({'first_interval_cycles':n,'period':p,'cycles':cycles.tolist(),'residuals_days':r.tolist()})
obj={'events':events,'aliases':aliases,'method':'Local raw SAP quality-zero triangular least squares; approximate center, profile and depth; no uncertainty claim. Aliases show integer cycle counts across all events; multiples and submultiples remain conditional.'}
(B/'helper-timing.json').write_text(json.dumps(obj,indent=2)+'\n');print(json.dumps(obj,indent=2))
