import numpy as np,json
from astropy.io import fits
p='[local-path-redacted]'; c=2912.3112348088957
with fits.open(p) as h:
 a=h[1].data;t=np.asarray(a['TIME'],float);f=np.asarray(a['SAP_FLUX'],float);q=np.asarray(a['QUALITY']);m=np.isfinite(t)&(abs(t-c)<.8)
 for ti,fi,qi in zip(t[m],f[m],q[m]):
  if abs(ti-c)<.12: print(round(ti,6),round(fi,2),qi)
 print('range',np.nanmin(t[m]),np.nanmax(t[m]),'zero_or_negative',int(np.sum(m & (f<=0))),'q0',int(np.sum(m &(q==0))), 'minimum',np.nanmin(f[m]))
