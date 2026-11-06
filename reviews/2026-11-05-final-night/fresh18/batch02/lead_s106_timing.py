import json,numpy as np
from pathlib import Path
from scipy.optimize import curve_fit
b=Path(r'[workspace]/Astra\made\final-night-2026-11-05\fresh18\batch02');z=np.load(b/'159860053/lead-independent-s106.npz');t=z['time'];f=z['flux'];out=[]
def trap(x,b,s,d,c,w,ing):return b+s*x-d*np.clip((w/2-abs(x-c))/(w*ing),0,1)
for pred,kind in [(4246.76,'deep'),(4257.47,'shallow')]:
 o=abs(t-pred)<.8;x=t[o]-pred;y=f[o]/np.median(f[o]);noise=np.std(y[abs(x)>.4]);p,cov=curve_fit(trap,x,y,p0=[1,0,.08 if kind=='deep' else .01,0,.3,.3],bounds=([.8,-.2,0,-.13,.05,.05],[1.2,.2,.8,.13,.9,.49]),sigma=np.full(len(x),noise),absolute_sigma=True,maxfev=30000);out.append(dict(kind=kind,center_btjd=float(pred+p[3]),formal_center_error_d=float(np.sqrt(cov[3,3])),depth_ppt=float(p[2]*1000),duration_d=float(p[4]),n=len(x),note='3x3 TESScut extraction same photons; local trapezoid covariance formal error, not full uncertainty'))
(b/'lead-s106-timing.json').write_text(json.dumps(out,indent=2));print(out)
