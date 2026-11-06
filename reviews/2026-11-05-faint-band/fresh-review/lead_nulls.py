import json
from pathlib import Path
import numpy as np
from astropy.io import fits
B=Path(__file__).resolve().parent
jobs=[('343187602',1970.10303,50.60814658605716,.12),('371856921',1951.95793,23.128222192838756,.16)]
out={}
for tic,t0,p,dur in jobs:
 c=json.loads((B/tic/'lead-context.json').read_text());res=[]
 for src in c['source']:
  with fits.open(src['path']) as h:
   a=h[1].data;t=np.asarray(a['TIME'],float);f=np.asarray(a['SAP_FLUX'],float);q=np.asarray(a['QUALITY'],int)
  good=np.isfinite(t)&np.isfinite(f)&(f>0)&(q==0);t=t[good];f=f[good]
  if len(t)<10:continue
  for n in range(round((t.min()-t0)/p)-1,round((t.max()-t0)/p)+2):
   pred=t0+n*p
   if pred<t.min()-.5 or pred>t.max()+.5:continue
   core=np.abs(t-pred)<dur/2;left=(t>=pred-.4)&(t<pred-.15);right=(t>pred+.15)&(t<=pred+.4)
   base=left|right
   d=dict(sector=src['sector'],cycle=n,predicted_btjd=pred,first_btjd=float(t.min()),last_btjd=float(t.max()),core_n=int(core.sum()),left_n=int(left.sum()),right_n=int(right.sum()),source_sha256=src['sha256'])
   if core.sum()>0 and base.sum()>8:
    cadence=np.median(np.diff(t));expected=max(1,round(dur/cadence));d.update(core_fraction=float(core.sum()/expected),depth_ppt=float((1-np.median(f[core])/np.median(f[base]))*1000),max_core_gap_d=float(np.max(np.diff(t[core]))) if core.sum()>1 else None,baseline_scatter_ppt=float(1.4826*np.median(np.abs(f[base]/np.median(f[base])-1))*1000))
   res.append(d)
 out[tic]=res
 print(tic,[(x['sector'],x['cycle'],round(x['predicted_btjd'],3),x['core_n'],x.get('depth_ppt')) for x in res])
(B/'lead-null-coverage.json').write_text(json.dumps(out,indent=2),encoding='utf8')
