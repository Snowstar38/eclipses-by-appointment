import numpy as np,json
from astropy.io import fits
from pathlib import Path
from scipy.optimize import least_squares
W=Path(__file__).resolve().parent; S=W.parent/'search256'/'fresh-data';out=[]
for s,c in [(15,1729.2),(55,2816.1),(75,3359.5),(83,3568.5)]:
 p=W/f'helper-167197264_s{s:03d}.fits' if s<76 else S/f'167197264_s{s:03d}.fits'
 with fits.open(p) as h:
  a=h[1].data;t=np.asarray(a['TIME'],float);f=np.asarray(a['SAP_FLUX'],float);q=np.asarray(a['QUALITY'])
 for radius in [1.5,2.0]:
  m=np.isfinite(t)&np.isfinite(f)&(f>0)&(q==0)&(abs(t-c)<radius);x=t[m];y=f[m]/np.median(f[m]);
  def residual(v):
   mid,amp,hw,ing,base,slope=v;return base+slope*(x-c)-amp*np.clip((hw-abs(x-mid))/ing,0,1)-y
  fit=least_squares(residual,[c,.008,.5,.25,1,0],bounds=([c-.6,0,.15,.03,.9,-.1],[c+.6,.1,1.0,.8,1.1,.1]),loss='soft_l1',f_scale=.003)
  out.append(dict(sector=s,window_half_days=radius,center_btjd=fit.x[0],depth_fraction=fit.x[1],width_days=2*fit.x[2],ingress_days=fit.x[3],n=len(x)))
(W/'helper-167-shallow.json').write_text(json.dumps(out,indent=2));print(json.dumps(out,indent=2))
