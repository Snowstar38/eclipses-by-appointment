import json,csv,numpy as np
from pathlib import Path
from astropy.io import fits
from scipy.optimize import curve_fit
B=Path(__file__).parent
def model(t,b,s,d,c,w,k):
 z=np.abs(t-c);shape=np.clip((w/2-z)/max(k,1e-5),0,1)
 return b+s*t-d*shape

phases={'165779351':.72,'91614687':.508,'66503432':.475,'152876230':.712}
out={}
for tic,phase in phases.items():
 m=json.load(open(B/tic/'measurements.json'));P=m['period_days'];T=m['primary_epoch_btjd'];dur=m['search_duration_days'];events=[]
 for rec in m['sources']:
  with fits.open(rec['path']) as h:
   a=h[1].data;ok=(a['QUALITY']==0)&np.isfinite(a['SAP_FLUX'])&(a['SAP_FLUX']>0);t=np.array(a['TIME'][ok],float);f=np.array(a['SAP_FLUX'][ok],float)
  cad=np.median(np.diff(t))
  for n in range(int(np.ceil((t.min()-T)/P-phase)),int(np.floor((t.max()-T)/P-phase))+1):
   pred=T+(n+phase)*P;ix=abs(t-pred)<2*dur;x=t[ix]-pred;y=f[ix];oot=abs(x)>dur
   if len(x)<15 or sum(oot&(x<0))<3 or sum(oot&(x>0))<3 or sum(abs(x)<dur/3)<3:continue
   y=y/np.median(y[oot]);noise=max(1.4826*np.median(abs(y[oot]-np.median(y[oot]))),1e-6)
   try:
    pars,cov=curve_fit(model,x,y,p0=[1,0,max(1-min(y),.001),0,dur,.2*dur],bounds=([.7,-1,0,-dur,.2*dur,.01*dur],[1.3,1,1,dur,3*dur,dur]),sigma=np.full(len(x),noise),absolute_sigma=True,maxfev=20000)
    err=float(np.sqrt(max(cov[3,3],0)));events.append(dict(sector=rec['sector'],cycle=n,mid_btjd=pred+pars[3],phase_relative_to_selected=((pred+pars[3]-T)/P)%1,depth_ppt=pars[2]*1000,formal_error_days=err,timing_allowance_days=max(err,cad/2),usable=bool(0<err<dur and pars[2]>3*noise)))
   except Exception:pass
 out[tic]=dict(events=events,note='Free-center secondary-candidate trapezoids; usable is heuristic >3 local-scatter amplitude plus finite covariance, not calibrated significance. Events and recurring morphology were inspected before interpreting secondary.')
(B/'secondary-measurements.json').write_text(json.dumps(out,indent=2))
for tic,z in out.items():
 a=[e for e in z['events'] if e['usable']];print(tic,len(a),'phase',np.median([e['phase_relative_to_selected'] for e in a]) if a else None,'depth',np.median([e['depth_ppt'] for e in a]) if a else None)
