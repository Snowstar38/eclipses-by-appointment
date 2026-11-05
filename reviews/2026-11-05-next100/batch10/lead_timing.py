import json, numpy as np
from pathlib import Path
from scipy.optimize import least_squares
D=Path(__file__).parent/'3299934'; zs=json.loads((D/'lead-local-series.json').read_text()); out=[]
for z in zs:
 if z['kind']!='dip' or z['sector'] not in [8,9,62,89]:continue
 t=np.array(z['raw_time']);f=np.array(z['raw_sap_flux']);c=z['screen_center_btjd']; x=t-c
 def model(p):
  mid,depth,width,ingress,base,slope=p
  shape=np.clip((width/2-np.abs(x-mid))/ingress,0,1)
  return base+slope*x-depth*shape
 med=np.median(f);y=f/med
 fit=least_squares(lambda p:(model(p)-y),[0,.005,.7,.1,1,0],bounds=([-.25,0,.3,.02,.95,-.01],[.25,.02,1.1,.35,1.05,.01]))
 p=fit.x;out.append(dict(sector=z['sector'],center_btjd=c+float(p[0]),depth_ppt=1000*float(p[1]),width_days=float(p[2]),ingress_days=float(p[3]),rms_ppt=float(np.std(model(p)-y)*1000),bounds_hit=bool(np.any(fit.active_mask))))
print(json.dumps(out,indent=2));(D/'lead-timing.json').write_text(json.dumps(out,indent=2))
