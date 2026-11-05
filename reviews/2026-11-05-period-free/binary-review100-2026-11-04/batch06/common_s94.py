import json,hashlib
from pathlib import Path
import numpy as np
from astropy.io import fits
B=Path(__file__).resolve().parent
T=['318649725','278081787','129543547']
bins=[(3862,3864),(3865,3867),(3867,3869),(3870,3872),(3873,3874),(3874,3875),(3875,3876),(3876,3877),(3878,3880)]
out={'note':'Same-time binned raw SAP comparison among widely separated targets; per-target sector median normalization is descriptive, not a common-mode mechanism fit.','targets':{}}
for tic in T:
 s=next(x for x in json.loads((B/tic/'raw-inspection.json').read_text())['sectors'] if x['sector']==94)
 p=Path(s['path']);assert hashlib.sha256(p.read_bytes()).hexdigest()==s['sha256']
 with fits.open(p,memmap=False) as h:
  a=h[1].data;t=np.asarray(a['TIME'],float);f=np.asarray(a['SAP_FLUX'],float);q=np.asarray(a['QUALITY'],int)
 ok=np.isfinite(t)&np.isfinite(f)&(f>0)&(q==0);base=np.median(f[ok&(t>=3862)&(t<3864)])
 rec=[]
 for lo,hi in bins:
  m=ok&(t>=lo)&(t<hi);rec.append({'start':lo,'end':hi,'n':int(m.sum()),'median_relative_ppt':float(1000*(np.median(f[m])/base-1)) if m.any() else None})
 out['targets'][tic]={'fits_sha256':s['sha256'],'bins':rec}
(B/'common-s94.json').write_text(json.dumps(out,indent=2)+'\n')
for tic,x in out['targets'].items():print(tic,[(v['start'],v['n'],round(v['median_relative_ppt'],1) if v['median_relative_ppt'] is not None else None) for v in x['bins']])
