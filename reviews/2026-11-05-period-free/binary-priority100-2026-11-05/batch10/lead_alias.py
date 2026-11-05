"""Bounded integer-cycle alias test on actual raw SAP cadence coverage."""
import json, csv, hashlib
from pathlib import Path
import numpy as np
from astropy.io import fits
B=Path(__file__).resolve().parent
spec={
 'T091':(2001.0008,2729.0102,0.27,0.05,[15,30,45]),
 'T093':(2312.9773,3044.2421,2.44,0.083,range(8,81)),
 'T094':(2478.7621,3215.7910,0.79,0.045,range(12,36)),
 'T097':(1559.4177,2275.4556,1.50,0.22,range(8,73)),
 'T095':(1921.7669,2611.8693,1.80,0.08,range(14,101)),
 'T096':(2478.5706,3228.9576,0.34,0.03,[22,44,66]),
 'T098':(1795.4125,2908.5573,1.14,0.03,[32,64,96]),
 'T099':(1822.7651,2916.8088,2.10,0.09,[38,76,114]),
 'T092':(3512.5162,3531.9648,0.65,0.12,range(1,8)),
}
rows={r['sample_id']:r for r in csv.DictReader((B/'queue.csv').open())}
out={}
for sid,(t0,t1,dur,depth,cycles) in spec.items():
 tic=rows[sid]['tic'];bulk=json.loads(Path('[local-path-redacted]',tic+'.json').read_text())
 files=[]
 for f in bulk['files']:
  if f['status']!='ok':continue
  p=Path(f['path']);assert hashlib.sha256(p.read_bytes()).hexdigest()==f['sha256']
  with fits.open(p,memmap=False) as h:
   a=h[1].data;t=np.array(a['TIME'],float);v=np.array(a['SAP_FLUX'],float);q=np.array(a['QUALITY'],int)
  good=np.isfinite(t)&np.isfinite(v)&(v>0)&(q==0);t=t[good];v=v[good]
  files.append((f['sector'],t,v,float(np.median(np.diff(t)))))
 trials=[]
 for n in cycles:
  P=(t1-t0)/n;checks=[]
  for sector,t,v,cad in files:
   lo=int(np.ceil((t.min()-t0)/P));hi=int(np.floor((t.max()-t0)/P))
   for k in range(lo,hi+1):
    c=t0+k*P
    if abs(c-t0)<dur or abs(c-t1)<dur:continue
    core=(t>=c-dur/2)&(t<=c+dur/2)
    left=(t>=c-2*dur)&(t<=c-dur)
    right=(t>=c+dur)&(t<=c+2*dur)
    def cov(mask,span):
     z=t[mask]
     return dict(n=int(len(z)),fraction=min(1.,len(z)*cad/span),first=float(z.min()) if len(z) else None,last=float(z.max()) if len(z) else None,max_gap=float(np.max(np.diff(z))) if len(z)>1 else None)
    cc=cov(core,dur);lc=cov(left,dur);rc=cov(right,dur)
    sensitive=all(x['fraction']>.75 and x['max_gap'] is not None and x['max_gap']<.25*dur for x in (cc,lc,rc))
    if sensitive:
     base=(np.median(v[left])+np.median(v[right]))/2
     obs=float(1-np.median(v[core])/base)
    else:obs=None
    checks.append(dict(sector=sector,cycle=k,center=round(c,4),core=cc,left=lc,right=rc,sensitive=sensitive,observed_depth=obs))
  nulls=[x for x in checks if x['sensitive'] and x['observed_depth'] is not None and x['observed_depth']<depth*.35]
  trials.append(dict(cycles_between=n,period_days=P,covered_windows=sum(x['sensitive'] for x in checks),deep_nulls=len(nulls),null_examples=[dict(sector=x['sector'],center=x['center'],observed_depth=x['observed_depth']) for x in nulls[:6]],checks=checks))
 out[sid]=dict(tic=tic,anchor_midpoints=[t0,t1],assumed_duration_days=dur,assumed_depth=depth,method='Prediction-only same-kind aliases. Null requires >75% actual quality-zero cadence in core and both separated side bands, with max internal gap < duration/4; observed core median <35% of anchor depth. These are bounded screens, not image-vetted physical nulls.',caution='T092 has unequal events likely of opposite eclipse kinds; its listed same-kind aliases are hypothetical and do not exclude an unknown binary clock.' if sid=='T092' else 'A sensitive numeric null requires visual validation if it decides a verdict.',trials=trials)
 print(sid,[(x['cycles_between'],round(x['period_days'],4),x['covered_windows'],x['deep_nulls']) for x in trials],flush=True)
(B/'lead-alias.json').write_text(json.dumps(out,indent=2)+'\n')
