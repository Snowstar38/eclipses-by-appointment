import json, pathlib, numpy as np
from astropy.io import fits
B=pathlib.Path(r'[local-path-redacted]'); rec=json.load(open(B/'helper-source-hashes.json')); out=[]
for r in rec:
 with fits.open(r['file'],memmap=False) as h:
  d=h[1].data; t=np.array(d['TIME']); q=np.array(d['QUALITY']); f=np.array(d['SAP_FLUX'],float); x=r['time']; dur=r['duration']; m=np.isfinite(t)&np.isfinite(f)&(abs(t-x)<=dur/2); g=m&(q==0); tg=np.sort(t[g]); cadence=np.nanmedian(np.diff(np.sort(t[np.isfinite(t)]))); out.append({**r,'finite_core':int(m.sum()),'quality0_core':int(g.sum()),'nominal_expected':round(dur/cadence,1),'quality0_max_internal_gap_days':float(np.max(np.diff(tg))) if len(tg)>1 else None,'quality0_first':float(tg[0]) if len(tg) else None,'quality0_last':float(tg[-1]) if len(tg) else None})
json.dump(out,open(B/'helper-coverage.json','w'),indent=2)
