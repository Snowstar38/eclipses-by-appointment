from pathlib import Path
import json,numpy as np
from astropy.io import fits
from scipy.optimize import curve_fit
B=Path(__file__).resolve().parent;tic='27681485';bulk=json.loads((B.parent.parent/'binary-exploration-2026-11-04/bulk-results'/f'{tic}.json').read_text());out=[]
def trap(x,b,s,d,c,w,ing):return b+s*x-d*np.clip((w/2-abs(x-c))/ing,0,1)
for sec,seed in [(44,2505.65),(45,2542.13),(46,2578.61),(72,3272.15)]:
 r=next(r for r in bulk['files'] if r['sector']==sec)
 with fits.open(r['path']) as h:
  a=h[1].data;t=np.array(a['TIME']);y=np.array(a['SAP_FLUX']);q=np.array(a['QUALITY'])
 z=np.isfinite(t)&np.isfinite(y)&(y>0)&(q==0)&(abs(t-seed)<2.8);x=t[z]-seed;f=y[z]/np.median(y[z]);p,cov=curve_fit(trap,x,f,p0=[1,0,.01,0,2,.2],bounds=([.8,-.05,0,-.5,.4,.03],[1.2,.05,.1,.5,3,.6]),maxfev=20000);err=np.sqrt(np.diag(cov));out.append(dict(sector=sec,center_btjd=seed+p[3],error_formal_d=err[3],depth=float(p[2]),duration_d=float(p[4]),ingress_d=float(p[5]),first=float(t[z].min()),last=float(t[z].max()),full_two_sided_event=bool(sec in [44,45]),note='Local trapezoid plus linear baseline; partialS46 not timing-quality; S72 steep trend makes timing model-dependent'))
print(out);(B/tic/'lead-trapezoids.json').write_text(json.dumps(out,indent=2))
