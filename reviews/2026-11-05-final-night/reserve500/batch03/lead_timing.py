import json,numpy as np
from pathlib import Path
from astropy.io import fits
from scipy.optimize import curve_fit
B=Path(__file__).resolve().parent
def trap(x,b,s,d,c,w,ing):
 z=np.abs(x-c);return b+s*x-d*np.clip((w/2-z)/(w*ing),0,1)
for fp in B.glob('*/lead-context.json'):
 d=json.loads(fp.read_text());events=d['flag_events'];out=[]
 if d['tic']=='408996985':events=events+[dict(sector=73,screen_btjd=3288.68,screen_duration_d=1.6)]
 if d['tic']=='467864145':events=events+[dict(sector=73,screen_btjd=3287.85,screen_duration_d=1.4),dict(sector=73,screen_btjd=3306.08,screen_duration_d=1.4)]
 if d['tic']=='132999153':events=[dict(sector=54,screen_btjd=2792.2166,screen_duration_d=.1)]
 for ev in events:
  sec=ev['sector'];pred=ev['screen_btjd'];dur=ev['screen_duration_d'];span=max(.5,dur*3)
  src=next(s for s in d['source'] if s['sector']==sec)
  with fits.open(src['path']) as h:a=h[1].data;t=np.array(a['TIME']);f=np.array(a['SAP_FLUX']);q=np.array(a['QUALITY'])
  ok=np.isfinite(t)&np.isfinite(f)&(f>0)&(q==0)&(abs(t-pred)<span);x=t[ok]-pred;y=f[ok];base=abs(x)>max(dur*.8,.2)
  if base.sum()<5 or len(x)<12:continue
  scale=np.median(y[base]);y=y/scale;noise=max(1.4826*np.median(abs(y[base]-np.median(y[base]))),.0003)
  try:
   p,cov=curve_fit(trap,x,y,p0=[1,0,min(max(1-y.min(),.005),.95),0,dur*1.5,.2],bounds=([.7,-.3,0,-max(.15,dur),.02,.03],[1.3,.3,1.2,max(.15,dur),span*1.2,.49]),sigma=np.full(len(x),noise),absolute_sigma=True,maxfev=30000)
   err=float(np.sqrt(max(cov[3,3],0)));fit=dict(center_btjd=float(pred+p[3]),center_formal_error_d=err,depth_ppt=float(p[2]*1000),duration_d=float(p[4]),ingress_d=float(p[4]*p[5]),residual_rms_ppt=float(np.std(y-trap(x,*p))*1000),fit_usable=bool(np.isfinite(err) and err>0 and err<max(.1,dur*.2) and abs(p[3])<max(.14,dur*.95) and p[2]>.002))
  except Exception as e:fit=dict(fit_error=str(e))
  out.append(dict(sector=sec,screen_btjd=pred,kind='candidate',n=len(x),cadence_d=float(np.median(np.diff(t[ok]))),noise_ppt=float(noise*1000),source_sha256=src['sha256'],**fit))
 (fp.parent/'lead-timing.json').write_text(json.dumps(out,indent=2));print(d['tic'],[(e['sector'],round(e.get('center_btjd',0),5),round(e.get('depth_ppt',0),1),round(e.get('duration_d',0),3),e.get('fit_usable')) for e in out])

