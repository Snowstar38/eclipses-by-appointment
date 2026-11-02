"""Measure the other event kind identified in lead raw-sector plots."""
import json
from pathlib import Path
import numpy as np
from scipy.optimize import curve_fit
from astropy.io import fits
B=Path(__file__).parent;out={}
def model(t,b,s,d,c,w,k):return b+s*t-d*np.clip((w/2-abs(t-c))/max(k,1e-5),0,1)
for tic,phase in {'300339443':-.43,'260765760':-.4669,'17033860':.2712,'464680877':.48}.items():
 m=json.load(open(B/tic/'measurements.json'));p=m['period_days'];ep=m['primary_epoch_btjd'];dur=np.median([e['duration_days'] for e in m['events'] if e.get('timing_usable')]);events=[]
 for src in m['sources']:
  with fits.open(src['path']) as h:a=h[1].data;t=np.array(a['TIME'],float);f=np.array(a['SAP_FLUX'],float);q=np.array(a['QUALITY'])
  ok=np.isfinite(t)&np.isfinite(f)&(f>0)&(q==0);t=t[ok];f=f[ok];cad=np.median(np.diff(t))
  for n in range(int(np.ceil((t.min()-ep)/p-phase)),int(np.floor((t.max()-ep)/p-phase))+1):
   pred=ep+(n+phase)*p;sel=abs(t-pred)<3*dur;x=t[sel]-pred;y=f[sel];oot=abs(x)>dur
   if min(sum(oot&(x<0)),sum(oot&(x>0)),sum(abs(x)<dur/2))<4:continue
   y=y/np.median(y[oot]);noise=max(1.4826*np.median(abs(y[oot]-np.median(y[oot]))),1e-6)
   try:
    v,c=curve_fit(model,x,y,p0=[1,0,max(1-y.min(),.001),0,dur,dur*.2],bounds=([.7,-1,0,-dur,.2*dur,.01*dur],[1.3,1,1,dur,3*dur,dur]),sigma=np.full(len(x),noise),absolute_sigma=True,maxfev=20000)
    err=np.sqrt(c[3,3]);
    if not 0<err<dur:continue
    mid=pred+v[3];events.append(dict(sector=src['sector'],cycle=n,mid_btjd=mid,timing_error_days=max(err,cad/2),formal_timing_error_days=err,phase_relative_selected=((mid-ep)/p+.5)%1-.5,depth_ppt=1000*v[2],duration_days=v[4]))
   except Exception:pass
 out[tic]=dict(events=events,phase_seed_from_visual_fold=phase,interpretation='Actual free-center fits of other eclipse kind. Two event kinds recur at unequal separation; P/2 does not preserve morphology/timing. Generic exactly-half-phase baseline estimates can overlap this secondary and are not valid eclipse depths for these targets. Selected reference epoch names the selected kind;300339443 depth ordering is not established uniformly across sectors.')
 (B/tic/'secondary-timing.json').write_text(json.dumps(out[tic],indent=2));print(tic,[(e['sector'],round(e['phase_relative_selected'],4),round(e['depth_ppt'],1)) for e in events])
(B/'secondary-audit.json').write_text(json.dumps(out,indent=2))

