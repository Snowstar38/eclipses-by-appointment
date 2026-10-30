from pathlib import Path
import json,numpy as np
from astropy.io import fits
from scipy.optimize import least_squares
root=Path(__file__).parent; records=json.load(open(root/'search-receipts.json')); results={}
for rec in records:
 tic=str(rec['tic']); sr=rec['P']; P=sr['P'];t0=sr['t0'];D=sr['dur']; events=[]
 for f in sorted((root/tic).glob('qlp*.fits')):
  with fits.open(f) as h:
   a=h[1].data;t=np.array(a['TIME'],float);y=np.array(a['SAP_FLUX'],float);q=np.array(a['QUALITY']); m=np.isfinite(t)&np.isfinite(y)&(y>0)&(q==0);t=t[m];y=y[m]; y/=np.median(y)
  if not len(t):continue
  cyc=np.arange(np.ceil((t.min()-t0)/P),np.floor((t.max()-t0)/P)+1,dtype=int)
  # at most two separate representative events in each selected sector
  chosen=cyc if len(cyc)<=2 else cyc[[0,-1]]
  for n in chosen:
   center=t0+n*P;w=min(.3*P,max(.45,4*D));m=abs(t-center)<w;x=t[m]-center;z=y[m]
   if len(x)<20 or sum(abs(x)<D/2)<3 or sum(x<-D)<5 or sum(x>D)<5:continue
   def shape(c,width,frac):return np.clip((width/2-abs(x-c))/(width*frac),0,1)
   def residual(a):return a[0]+a[1]*x+a[2]*x*x-a[3]*shape(a[4],a[5],a[6])-z
   bounds=([.5,-1,-1,0,-D,.35*D,.05],[1.5,1,1,.8,D,3*D,.5]);initial=[1,0,0,max(.001,1-np.percentile(z,5)),0,D,.25]
   try:
    fit=least_squares(residual,initial,bounds=bounds,max_nfev=1500);a=fit.x; r=residual(a);err=np.std(r);events.append(dict(sector=int(f.stem[-3:]),cycle=int(n),tc=float(center+a[4]),nominal_tc=float(center),depth=float(a[3]),duration_d=float(a[5]),ingress_fraction=float(a[6]),residual_rms=float(err),n_points=len(x),n_in=int(sum(abs(x-a[4])<a[5]/2)),edge=bool(abs(a[4])>.95*D or a[5]>.99*3*D)))
   except Exception as e:events.append(dict(sector=int(f.stem[-3:]),cycle=int(n),error=str(e)))
 good=[x for x in events if 'tc' in x and not x['edge'] and x['depth']>3*x['residual_rms']]
 ep=None
 if len(good)>=2 and len(set(x['cycle'] for x in good))>1:
  x=np.array([a['cycle'] for a in good]);y=np.array([a['tc'] for a in good]); p=np.polyfit(x,y,1);ep=dict(period_d=float(p[0]),epoch_btjd=float(p[1]),n_events=len(good),residual_rms_min=float(np.std(y-np.polyval(p,x))*1440),note='unweighted representative events, conditional on original search cycle counts; no uncertainty inferred')
 results[tic]=dict(search_period=P,search_epoch=t0,events=events,representative_ephemeris=ep,method='QLP SAP_FLUX, QUALITY=0; quadratic local baseline plus trapezoid, max two events per selected sector; native cadence, no exposure integration; unweighted errors not estimated')
 print(tic,len(events),ep,flush=True)
json.dump(results,open(root/'raw-events.json','w'),indent=2)
