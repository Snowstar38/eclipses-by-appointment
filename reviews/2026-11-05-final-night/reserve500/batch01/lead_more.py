from pathlib import Path
import json,numpy as np
from astropy.io import fits
b=Path(__file__).resolve().parent
for tic,sec in [('165828134',37),('165828134',64),('15527953',101),('97279198',7)]:
 d=json.loads((b/tic/'lead-context.json').read_text());s=next(x for x in d['source'] if x['sector']==sec)
 with fits.open(s['path']) as h:
  a=h[1].data;t=np.array(a['TIME']);y=np.array(a['SAP_FLUX']);q=np.array(a['QUALITY'])
 ok=np.isfinite(t)&np.isfinite(y)&(y>0)&(q==0);t=t[ok];y=y[ok]
 if tic=='165828134':
  m=(t>2330) if sec==37 else (t>3054)&(t<3057)
  print(tic,sec,t[m][np.argmin(y[m])])
