import json
from pathlib import Path
import numpy as np
from astropy.io import fits
B=Path(__file__).parent
for tic,sector,cycles in [('30770290',66,[174,175,176,177,178]),('30770290',104,[305,306,307]),('306980055',93,[131,132,133,134])]:
 m=json.loads((B/tic/'measurements.json').read_text());p=m['historical_period_days'];t0=m['historical_epoch_btjd']
 fp=B.parent/'shared-qlp'/f'{tic}_s{sector:03}.fits'
 with fits.open(fp) as h:
  a=h[1].data;t=np.array(a['TIME'],float);f=np.array(a['SAP_FLUX'],float);q=np.array(a['QUALITY'],int)
 print(tic,sector)
 for cy in cycles:
  pred=t0+cy*p;idx=np.isfinite(t)&np.isfinite(f)&(abs(t-pred)<.2);clean=idx&(q==0)
  if clean.any():
   outer=clean&(abs(t-pred)>.08)
   med=np.median(f[outer]) if outer.any() else np.median(f[clean])
   dep=(1-np.min(f[clean])/med)*1000
  else:dep=None
  print(cy,round(pred,5),'all',int(idx.sum()),'clean',int(clean.sum()),'min_drop_ppt',None if dep is None else round(dep,1))
