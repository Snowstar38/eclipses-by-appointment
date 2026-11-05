import json
from pathlib import Path
import numpy as np
from astropy.io import fits
from scipy.optimize import least_squares
B=Path(__file__).resolve().parent;tic='280051953';C=json.loads((B/tic/'lead-context.json').read_text())
sectors={s['sector']:s for s in C['sectors']}
seed=[(2,1379.8),(13,1663.45),(36,2286.68),(63,3023.81),(67,3136.60),(68,3164.95),(69,3193.60),(87,3675.53),(90,3760.0),(94,3874.19),(95,3902.3),(96,3930.85)]
out=[]
for sec,c0 in seed:
 if sec not in sectors:continue
 s=sectors[sec]
 with fits.open(s['source_path'],memmap=False) as h:
  a=h[1].data;t=np.asarray(a['TIME'],float);f=np.asarray(a['SAP_FLUX'],float);q=np.asarray(a['QUALITY'],int)
 good=np.isfinite(t)&np.isfinite(f)&(f>0)&(q==0)&(abs(t-c0)<2.8);t=t[good];f=f[good]
 if len(t)<100:continue
 f=f/np.median(f)
 def model(x):
  c,w,edge,depth,b0,b1=x
  d=np.abs(t-c);e=np.clip((w/2+edge/2-d)/max(edge,1e-6),0,1)
  return b0+b1*(t-c)-depth*e
 x0=[c0,1.4,.2,.03,float(np.median(f)),0]
 lb=[c0-.9,.5,.04,.005,.8,-.05];ub=[c0+.9,3.0,.8,.15,1.2,.05]
 res=least_squares(lambda x:model(x)-f,x0,bounds=(lb,ub),loss='soft_l1',f_scale=.003)
 x=res.x;rmse=float(np.sqrt(np.mean((model(x)-f)**2)))
 out.append(dict(sector=sec,seed_btjd=c0,center_btjd=float(x[0]),full_width_days=float(x[1]),ingress_egress_days=float(x[2]),depth_ppt=float(x[3]*1000),baseline_slope_ppt_per_day=float(x[5]*1000),points=len(t),rmse_ppt=rmse*1000,first_btjd=float(t.min()),last_btjd=float(t.max()),source_sha256=s['source_sha256']))
 print(sec,round(x[0],5),round(x[1],3),round(x[3]*1000,2),round(rmse*1000,2),flush=True)
(B/tic/'lead-trapezoid-fits.json').write_text(json.dumps(out,indent=2)+'\n')

