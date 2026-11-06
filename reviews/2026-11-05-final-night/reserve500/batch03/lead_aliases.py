import json,numpy as np
from pathlib import Path
from astropy.io import fits
b=Path(__file__).resolve().parent;cl=json.loads((b/'lead-clocks.json').read_text());out={}
for tic,c in cl.items():
 d=json.loads((b/tic/'lead-context.json').read_text());series=[]
 for src in d['source']:
  with fits.open(src['path']) as h:
   a=h[1].data;t=np.asarray(a['TIME'],float);y=np.asarray(a['SAP_FLUX'],float);q=np.asarray(a['QUALITY'],int)
  ok=np.isfinite(t)&np.isfinite(y)&(y>0)&(q==0);series.append((src,t[ok],y[ok]))
 dur=c['duration_d'];t0=c['epoch_btjd'];periods=[('measured',c['period_d'])]+[(f'divisor{n}',c['period_d']/n) for n in range(2,7)]
 if tic in cl:
  delta=max(c['times'])-min(c['times']);periods += [(f'integer{n}',delta/n) for n in range(max(1,int(delta/100)),int(delta/5)+1)]
 tests=[]
 for label,p in periods:
  nulls=[];dips=[];covered=0
  timing_residuals=[float((tt-t0)-round((tt-t0)/p)*p) for tt in c['times']]
  timing_compatible=max(abs(x) for x in timing_residuals)<max(.04,dur*.1)
  for src,t,y in series:
   cad=np.median(np.diff(t))
   for n in range(int(np.ceil((t.min()-t0)/p)),int(np.floor((t.max()-t0)/p))+1):
    pred=t0+n*p;core=abs(t-pred)<dur*.35;left=(t>pred-dur*1.6)&(t<pred-dur*.75);right=(t>pred+dur*.75)&(t<pred+dur*1.6)
    if min(core.sum(),left.sum(),right.sum())<3:continue
    tc=t[core];cover=len(tc)*cad/(dur*.7)
    if cover<.75 or np.max(np.diff(tc))>max(cad*3,dur*.2):continue
    tl=np.median(t[left]);tr=np.median(t[right]);fl=np.median(y[left]);fr=np.median(y[right]);base=fl+(fr-fl)*(t-tl)/(tr-tl);z=y/base;noise=1.4826*np.median(abs(z[left|right]-np.median(z[left|right])))*1000;depth=(1-np.median(z[core]))*1000
    e=dict(sector=src['sector'],predicted_btjd=pred,depth_ppt=depth,noise_ppt=noise,core_n=int(core.sum()),coverage_fraction=cover,max_core_gap_d=float(np.max(np.diff(tc))),source_sha256=src['sha256']);covered+=1
    if depth<max(c['depth_ppt']*.15,noise*4/np.sqrt(core.sum())):nulls.append(e)
    else:dips.append(e)
  tests.append(dict(label=label,period_d=p,timing_residuals_d=timing_residuals,timing_compatible=timing_compatible,covered=covered,nulls=nulls,dips=dips))
 out[tic]=tests
 print(tic,[(r['label'],round(r['period_d'],6),r['covered'],len(r['nulls'])) for r in tests[:6]],'integer survivors',[(r['label'],round(r['period_d'],5),r['covered']) for r in tests[6:] if not r['nulls']])
(b/'lead-alias-covered-windows.json').write_text(json.dumps(out,indent=2))




