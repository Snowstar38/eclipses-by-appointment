import json,numpy as np
from astropy.io import fits
from astropy.timeseries import BoxLeastSquares
from pathlib import Path
R=Path(__file__).parent; tic='411647453'; T=[];Y=[]
for f in sorted((R/tic).glob('qlp*.fits')):
 with fits.open(f) as h:
  a=h[1].data;t=np.array(a['TIME'],float);y=np.array(a['SAP_FLUX'],float);q=np.array(a['QUALITY']);m=np.isfinite(t)&np.isfinite(y)&(y>0)&(q==0);t=t[m];y=y[m];y=y/np.median(y);T.extend(t);Y.extend(y)
t=np.array(T);y=np.array(Y);p=np.linspace(.6,1.1,50000);z=BoxLeastSquares(t,y).power(p,[.04,.06,.08,.1]); ix=np.argsort(z.power)[-10:][::-1]; out=[dict(period=float(z.period[i]),epoch=float(z.transit_time[i]),duration=float(z.duration[i]),depth=float(z.depth[i]),power=float(z.power[i])) for i in ix];json.dump(out,open(R/'411-period-search.json','w'),indent=2);print(out[:3])
