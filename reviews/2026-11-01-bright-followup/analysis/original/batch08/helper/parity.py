import json,numpy as np
from astropy.io import fits
p='[local path omitted]'
m=json.load(open(p));p0=m['historical_period_days'];t0=m['historical_epoch_btjd']
for s in m['sources']:
 with fits.open(s['path']) as h:
  d=h[1].data;t=d['TIME'];f=d['SAP_FLUX'];q=d['QUALITY'];ok=np.isfinite(t)&np.isfinite(f)&(f>0)&(q==0);t=t[ok];f=f[ok]
 for n in range(int(np.ceil((t.min()-t0)/p0)),int(np.floor((t.max()-t0)/p0))+1):
  z=t-(t0+n*p0); inn=abs(z)<.1; out=(abs(z)>.2)&(abs(z)<.5)
  print(s['sector'],n,'in',sum(inn),'out',sum(out),'depth',round(1000*(1-np.median(f[inn])/np.median(f[out])),1) if sum(inn)>2 and sum(out)>3 else None)
