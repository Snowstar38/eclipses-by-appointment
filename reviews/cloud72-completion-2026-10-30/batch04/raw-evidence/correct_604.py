import json,numpy as np
from pathlib import Path
from scipy.optimize import least_squares
from astropy.io import fits
r=Path(__file__).parent; raw=json.load(open(r/'raw-events.json'));mins=json.load(open(r/'local-minima.json'))['60443793']; events=[]
for sec in mins:
 f=r/'60443793'/('qlp_s%03d.fits'%sec['sector'])
 with fits.open(f) as h:
  a=h[1].data;t=np.asarray(a['TIME'],float);y=np.asarray(a['SAP_FLUX'],float);q=np.asarray(a['QUALITY']);good=np.isfinite(t)&np.isfinite(y)&(q==0)&(y>0);t=t[good];y=y[good]/np.median(y[good])
 for tc in sec['times']:
  m=abs(t-tc)<.32;x=t[m]-tc;z=y[m]
  if len(x)<12:continue
  def model(a):return a[0]+a[1]*x+a[2]*x*x-a[3]*np.clip((a[5]/2-abs(x-a[4]))/(a[5]*.25),0,1)
  try:
   fit=least_squares(lambda a:model(a)-z,[1,0,0,.05,0,.16],bounds=([.5,-1,-3,0,-.06,.06],[1.5,1,3,.8,.06,.35]));a=fit.x;res=np.std(model(a)-z)
   if a[3]>3*res:events.append(dict(sector=sec['sector'],tc=float(tc+a[4]),depth=float(a[3]),duration_d=float(a[5]),ingress_fraction=.25,residual_rms=float(res),edge=False,n_points=len(x),n_in=int(sum(abs(x-a[4])<a[5]/2))))
  except ValueError:pass
# Estimate spacing with long-baseline integer cycle assignment; alternating minima imply twice spacing.
t=np.array([e['tc'] for e in events]);n=np.round((t-1658.35)/1.297).astype(int);fit=np.polyfit(n,t,1)
for e,i in zip(events,n):e['cycle']=int(i)
raw['60443793']['events']=events;raw['60443793']['representative_ephemeris']=dict(minimum_spacing_d=float(fit[0]),candidate_binary_period_d=float(2*fit[0]),epoch_btjd=float(fit[1]),residual_rms_min=float(np.std(t-np.polyval(fit,n))*1440),n_events=len(t),note='Cycle count conditional on approximate 1.297 d spacing; alternating depths suggest double spacing as binary period. No uncertainty or secure alias test.')
raw['60443793']['method']='QLP QUALITY=0 local quadratic plus trapezoid fitted around independently identified minima.'
json.dump(raw,open(r/'raw-events.json','w'),indent=2);print(raw['60443793']['representative_ephemeris'])
