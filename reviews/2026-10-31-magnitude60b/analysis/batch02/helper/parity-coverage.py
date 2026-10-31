import numpy as np,json
from astropy.io import fits
from pathlib import Path
b=Path('[local path omitted]');out=[]
for tic,sector,cycles,p,t0 in [('141811748',37,[144,145,146],6.8389345006482305,1327.1896),('267094867',67,[519,520,521,522,523],3.4708258458646104,1328.4798)]:
 with fits.open(b/'shared-qlp'/f'{tic}_s{sector:03}.fits') as h:
  a=h[1].data;t=np.array(a['TIME']);f=np.array(a['SAP_FLUX']);q=np.array(a['QUALITY']);
  for cycle in cycles:
   c=t0+cycle*p;v=np.isfinite(t)&np.isfinite(f)&(q==0);i=v&(abs(t-c)<.05);o=v&(abs(t-c)>.13)&(abs(t-c)<.3);out.append(dict(tic=tic,sector=sector,cycle=cycle,n_in=int(sum(i)),n_out=int(sum(o)),depth_ppt=float((1-np.median(f[i])/np.median(f[o]))*1000) if sum(i)>0 and sum(o)>0 else None))
print(json.dumps(out,indent=2));(b/'batch02/helper/parity-coverage.json').write_text(json.dumps(out,indent=2))
