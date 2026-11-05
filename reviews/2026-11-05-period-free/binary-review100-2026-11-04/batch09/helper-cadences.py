import json,hashlib
from pathlib import Path
import numpy as np
from astropy.io import fits
B=Path(__file__).resolve().parent
cases=[('H086','146516744',32,2199.85),('H087','433693445',17,1783.6384936),('H088','146169279',90,3759.385),('H084','43868028',98,3996.034)]
out=[]
for sample,tic,sec,c in cases:
 p=Path(f'[local-path-redacted]')
 with fits.open(p) as h:
  a=h[1].data;t=np.array(a['TIME']);q=np.array(a['QUALITY']); f=np.array(a['SAP_FLUX']);sel=(abs(t-c)<.16)&np.isfinite(f)
  rows=[{k:float(a[k][i]) for k in ('TIME','SAP_FLUX','KSPSAP_FLUX','SAP_BKG','SAP_X','SAP_Y','QUALITY') if k in a.names} for i in np.where(sel)[0]]
  out.append(dict(sample=sample,path=str(p),sha256=hashlib.sha256(p.read_bytes()).hexdigest(),center=c,rows=rows))
(B/'helper-cadences.json').write_text(json.dumps(out,indent=2)+'\n')
