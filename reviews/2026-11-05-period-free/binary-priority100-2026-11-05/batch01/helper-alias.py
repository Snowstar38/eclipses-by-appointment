import json,math,hashlib
from pathlib import Path
import numpy as np
from astropy.io import fits
B=Path(__file__).resolve().parent
out=[]
for tic,t0,t1 in [('92234103',1435.0295,2149.0344),('46744354',2183.239,2226.301)]:
 lead=json.loads((B/tic/'lead-numeric.json').read_text());src=[]
 for s in lead['sources']:
  p=Path(s['path']);assert hashlib.sha256(p.read_bytes()).hexdigest()==s['sha256']
  with fits.open(p,memmap=False) as h:
   d=h[1].data;t=np.asarray(d['TIME'],float);f=np.asarray(d['SAP_FLUX'],float);q=np.asarray(d['QUALITY'],int);good=np.isfinite(t)&np.isfinite(f)&(q==0)&(f>0);t=t[good];f=f[good];src.append((s['sector'],t,f,float(np.median(np.diff(t)))))
 delta=t1-t0; cases=[]
 for n in range(math.ceil(delta/60),math.floor(delta/10)+1):
  P=delta/n; tests=[]
  for sector,t,f,cad in src:
   for k in range(math.ceil((t.min()-t0)/P),math.floor((t.max()-t0)/P)+1):
    if k in [0,n]:continue
    tm=t0+k*P;x=t-tm;core=abs(x)<.12;left=(x>-.5)&(x<-.2);right=(x>.2)&(x<.5)
    cov=[]
    for a,b,mask in [(-.12,.12,core),(-.5,-.2,left),(.2,.5,right)]:
     tt=t[mask];cov.append({'n':len(tt),'edge_and_internal_max_gap':float(np.max(np.diff(np.r_[tm+a,tt,tm+b])))})
    sensitive=all(v['edge_and_internal_max_gap']<max(3*cad,.04) for v in cov)
    depth=float(1000*(1-np.median(f[core])/(.5*(np.median(f[left])+np.median(f[right]))))) if all(z['n']>=2 for z in cov) else None
    tests.append({'sector':sector,'cycle':k,'time':tm,'coverage':cov,'sensitive':sensitive,'depth_ppt':depth})
  cases.append({'integer_cycles':n,'period_days':P,'tests':tests})
 out.append({'tic':tic,'centers_approx':[t0,t1],'assumption':'same kind; range 10-60 d; single-point estimates ignore timing uncertainty; window .24 d with .3 d flanks; test only predictions in file time ranges, do not extrapolate sensitive null to gapped edges','cases':cases});print(tic,'cases',len(cases),'with sensitive tests',sum(any(x['sensitive'] for x in c['tests']) for c in cases))
(B/'helper-alias.json').write_text(json.dumps(out,indent=2))

