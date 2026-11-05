import json,hashlib
from pathlib import Path
import numpy as np
from astropy.io import fits
from scipy.optimize import least_squares
B=Path(__file__).resolve().parent;tic='467963921'; events=[]
for sec,c in [(66,3119.8942),(94,3865.6332),(103,4163.9319)]:
 p=Path(f'[local-path-redacted]')
 with fits.open(p) as h:
  a=h[1].data;t=np.array(a['TIME'],float);f=np.array(a['SAP_FLUX'],float);q=np.array(a['QUALITY'])
 ok=np.isfinite(t)&np.isfinite(f)&(q==0)&(abs(t-c)<.3);x=t[ok]-c;y=f[ok]/np.median(f[ok]);
 # triangular profile local baseline, measured on raw SAP
 def residual(v):
  b,s,d,offset,w=v;return b+s*x-d*np.maximum(0,1-abs(x-offset)/w)-y
 fit=least_squares(residual,[1,0,.014,0,.07],bounds=([.95,-.1,0,-.1,.015],[1.05,.1,.1,.1,.2]));v=fit.x
 events.append({'sector':sec,'center_btjd':c+v[3],'depth_ppt':v[2]*1000,'half_width_d':v[4],'n':int(ok.sum()),'source_sha256':hashlib.sha256(p.read_bytes()).hexdigest()})
a,b,c=[v['center_btjd'] for v in events];aliases=[]
for n in range(12,19):
 p=(b-a)/n;m=round((c-b)/p);p2=(c-b)/m
 aliases.append({'cycles_66_94':n,'cycles_94_103':m,'p_first':p,'p_second':p2,'mismatch_days':p2-p})
(B/'helper-timing.json').write_text(json.dumps({'events':events,'aliases':aliases,'method':'independent local triangular least squares raw SAP quality 0; widths/profile approximate; no timing uncertainties claimed'},indent=2));print(json.dumps({'events':events,'aliases':aliases},indent=2))
