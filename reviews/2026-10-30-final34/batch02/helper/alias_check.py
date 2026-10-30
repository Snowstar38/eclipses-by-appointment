import json,numpy as np
from pathlib import Path
from astropy.io import fits
base=Path('../raw-evidence'); R=json.loads((base/'raw-events.json').read_text())
for tic in ['424878861','47719859','162234490']:
 r=R[tic]; sec=r['sector']; d=r['events'][0]['duration_d']; p=r['representative_ephemeris']['period_d']; t0=r['events'][0]['tc']
 with fits.open(base/tic/f'qlp_s{sec:03d}.fits') as h:
  a=h[1].data;t=np.array(a['TIME'],float);f=np.array(a['SAP_FLUX'],float);q=np.array(a['QUALITY']);m=np.isfinite(t)&np.isfinite(f)&(q==0);t=t[m];f=f[m]
 print(tic,'range',t.min(),t.max())
 for n in range(-4,6):
  tc=t0+(n+.5)*p; x=t-tc; inner=np.abs(x)<d*.3; outer=(np.abs(x)>d*.75)&(np.abs(x)<d*1.75)
  if inner.sum() and outer.sum():print(' midpoint',round(tc,4),'N',inner.sum(),outer.sum(),'loss',round(1-np.median(f[inner])/np.median(f[outer]),4))
