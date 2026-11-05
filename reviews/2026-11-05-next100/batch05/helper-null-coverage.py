import json,hashlib
from pathlib import Path
import numpy as np
from astropy.io import fits
B=Path(__file__).resolve().parent
cases=[('398073873',18,1800.04557078,.045),('398073873',18,1796.3066,.045),('398073873',58,2899.0701,.045),('143497778',61,2982.636,.14),('143497778',61,2978.736,.14),('143497778',88,3708.055,.14)]
out=[]
for tic,sec,c,w in cases:
 s=next(x for x in json.loads((B/tic/'lead-context.json').read_text())['sectors'] if x['sector']==sec);p=Path(s['source_path']);sha=hashlib.sha256(p.read_bytes()).hexdigest()
 with fits.open(p,memmap=False) as h:
  d=h[1].data;t=np.array(d['TIME'],float); f=np.array(d['SAP_FLUX'],float);q=np.array(d['QUALITY'],int)
 good=np.isfinite(t)&np.isfinite(f)&(f>0)&(q==0); t=t[good];f=f[good]; masks={'core':(t>=c-w)&(t<=c+w),'left':(t>=c-5*w)&(t<c-2*w),'right':(t>c+2*w)&(t<=c+5*w)}; row=dict(tic=tic,sector=sec,center=c,halfcore=w,source_sha256=sha,expected_cadence_days=s['cadence_days']);
 for name,mask in masks.items():
  a=t[mask];row[name]=dict(count=len(a),first=float(a.min()) if len(a) else None,last=float(a.max()) if len(a) else None,max_internal_gap=float(np.diff(a).max()) if len(a)>1 else None,expected_start=float(c+{'left':-5,'core':-1,'right':2}[name]*w),expected_end=float(c+{'left':-2,'core':1,'right':5}[name]*w))
 out.append(row)
(B/'helper-null-coverage.json').write_text(json.dumps(out,indent=2)+'\n')
for x in out: print(x['tic'],x['sector'],x['center'],[(k,x[k]['count'],round(x[k]['first']-x[k]['expected_start'],4),round(x[k]['expected_end']-x[k]['last'],4),round(x[k]['max_internal_gap'],4)) for k in ('left','core','right')])
