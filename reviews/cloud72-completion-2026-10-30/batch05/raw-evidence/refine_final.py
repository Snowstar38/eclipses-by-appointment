import json,numpy as np
from pathlib import Path
from astropy.io import fits
from scipy.optimize import least_squares
r=Path(__file__).parent;old=json.load(open(r/'raw-events.json'));(r/'raw-events-original-alias.json').write_text(json.dumps(old,indent=2));out=old.copy()
centers={'431762229':[(18,1794.0367),(18,1795.9950),(18,1797.9326),(58,2884.4179),(58,2886.3508)],'9396327':[(80,3481.3363),(80,3483.7529),(80,3495.9588),(80,3498.424),(80,3500.8637),(80,3503.2989)],'222498305':[(12,1634.9536),(12,1650.4743),(39,2365.1964),(39,2380.7449)],'183994341':[(91,3781.9447),(91,3796.6032),(92,3811.2707),(92,3825.9356)]}
for tic,cs in centers.items():
 ev=[]
 for sec,tc in cs:
  with fits.open(r/tic/f'qlp_s{sec:03d}.fits') as h:
   a=h[1].data;t=np.array(a['TIME']);y=np.array(a['SAP_FLUX']);m=np.isfinite(t)&np.isfinite(y)&(y>0)&(a['QUALITY']==0)&(abs(t-tc)<.6);x=t[m]-tc;y=y[m];y/=np.median(y)
  def resid(v):
   b,s,d,c,w,f=v;return b+s*x-d*np.clip((w/2-abs(x-c))/(w*f),0,1)-y
  fit=least_squares(resid,[1,0,max(.01,1-min(y)),0,.18,.25],bounds=([.5,-1,0,-.2,.02,.05],[1.5,1,.9,.2,1.2,.5]));b,s,d,c,w,f=fit.x
  ev.append(dict(sector=sec,tc=float(tc+c),depth=float(d),duration_d=float(w),ingress_fraction=float(f),residual_rms=float(np.std(resid(fit.x))),edge=False,n_points=len(x),cycle=0))
 # consecutive first sector event interval directly, not cross-sector catalogue cycles
 p=ev[1]['tc']-ev[0]['tc'];epoch=ev[0]['tc'];
 if tic=='9396327':
  cyc=np.array([round((e['tc']-epoch)/p) for e in ev]);p,epoch=np.polyfit(cyc,[e['tc'] for e in ev],1)
 if tic=='183994341':
  p,epoch=np.polyfit(np.arange(4),[e['tc'] for e in ev],1)
 for e in ev:e['cycle']=round((e['tc']-epoch)/p)
 out[tic]=dict(search_period=p,search_epoch=epoch,events=ev,representative_ephemeris=dict(period_d=p,epoch_btjd=epoch,n_events=len(ev),note='Representative local event timing regression for939/183; direct consecutive event interval for431/222; no formal period error.'),method='Manual raw minima seed, local linear baseline + trapezoid on QUALITY=0 QLP SAP; representative consecutive events; supersedes original search alias')
 print(tic,p,[(e['sector'],round(e['tc'],5),round(e['depth'],3),round(e['duration_d'],3)) for e in ev])
(r/'raw-events.json').write_text(json.dumps(out,indent=2))
