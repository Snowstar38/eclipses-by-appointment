import numpy as np,json,hashlib
from pathlib import Path
from astropy.io import fits
from scipy.optimize import least_squares
W=Path(__file__).resolve().parent; data=W.parent/'search256'/'fresh-data'
rows=[]
for tic,sec,c in [(167197264,56,2836.94)]:
 p=W/f'helper-{tic}_s{sec:03d}.fits'
 with fits.open(p) as h:
  assert int(h[0].header['TICID'])==tic
  x=h[1].data; t=np.array(x['TIME'],float); f=np.array(x['SAP_FLUX'],float); q=np.array(x['QUALITY'])
 for radius in [1.2,1.5,1.7]:
  m=np.isfinite(t)&np.isfinite(f)&(f>0)&(q==0)&(abs(t-c)<radius); tt=t[m]; ff=f[m]; ff=ff/np.median(ff[abs(tt-c)>1])
  def residual(v):
   mid,depth,half,ing,base,slope=v; z=abs(tt-mid); shape=np.clip((half-z)/ing,0,1); return base+slope*(tt-c)-depth*shape-ff
  sol=least_squares(residual,[c,.03 if tic==167197264 else .12,.65,.3,1,0],bounds=([c-.35,0,.1,.02,.8,-.2],[c+.35,.3,1.3,.9,1.2,.2]),loss='soft_l1',f_scale=.003)
  rows.append(dict(tic=tic,sector=sec,window_half_days=radius,mid_btjd=sol.x[0],depth=sol.x[1],full_width_days=2*sol.x[2],ingress_days=sol.x[3],rms=float(np.sqrt(np.mean(residual(sol.x)**2))),n=len(tt),source_sha256=hashlib.sha256(p.read_bytes()).hexdigest()))
(W/'helper-morphology-s56-fits.json').write_text(json.dumps(rows,indent=2));print(json.dumps(rows,indent=2))

