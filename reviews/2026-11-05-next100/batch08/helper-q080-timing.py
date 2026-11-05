import json,hashlib
from pathlib import Path
import numpy as np
from astropy.io import fits
from scipy.optimize import least_squares
b=Path(__file__).parent;D=b/'99243741';ctx=json.loads((D/'lead-context.json').read_text());sectors={s['sector']:s for s in ctx['sectors']};out=[]
for sec,c0 in [(7,1501.431718),(34,2235.618882),(87,3670.09),(88,3703.56)]:
 s=sectors[sec];p=Path(s['source_path']);h=fits.open(p);a=h[1].data;t0=np.array(a['TIME']);f0=np.array(a['SAP_FLUX']);q=np.array(a['QUALITY']);variants=[]
 for radius in [1.5,2,2.5]:
  good=np.isfinite(t0)&np.isfinite(f0)&(f0>0)&(q==0)&(abs(t0-c0)<radius);t=t0[good];f=f0[good];f=f/np.median(f)
  if len(t)<30:continue
  def model(x):
   c,w,edge,depth,b0,b1=x; d=abs(t-c);e=np.clip((w/2+edge/2-d)/edge,0,1);return b0+b1*(t-c)-depth*e
  x0=[c0,1.1,.15,.008,1,0];lb=[c0-.8,.3,.04,.001,.8,-.05];ub=[c0+.8,2.5,1.0,.08,1.2,.05];r=least_squares(lambda x:model(x)-f,x0,bounds=(lb,ub),loss='soft_l1',f_scale=.002);x=r.x
  variants.append({'radius':radius,'center':float(x[0]),'width':float(x[1]),'edge':float(x[2]),'depth_ppt':float(1000*x[3]),'slope_ppt_day':float(1000*x[5]),'rmse_ppt':float(1000*np.sqrt(np.mean((model(x)-f)**2))),'n':len(t),'bound_hit':bool(np.any(np.minimum(x-np.array(lb),np.array(ub)-x)<1e-4))})
 out.append({'sector':sec,'variants':variants,'source_sha256':hashlib.sha256(p.read_bytes()).hexdigest()})
(D/'helper-timing.json').write_text(json.dumps(out,indent=2));print(json.dumps(out,indent=2))
