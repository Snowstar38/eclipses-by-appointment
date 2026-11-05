"""Bounded F010 deep-event adjacent cycle aliases against real SAP time coverage."""
from pathlib import Path
import json,math,hashlib
import numpy as np
from astropy.io import fits
B=Path(__file__).resolve().parent;H=B.parent.parent/'binary-exploration-2026-11-04'/'bulk-results'
bulk=json.loads((H/'458324895.json').read_text());data=[]
for rec in bulk['files']:
 p=Path(rec['path']);assert hashlib.sha256(p.read_bytes()).hexdigest()==rec['sha256']
 with fits.open(p,memmap=False) as hd:
  a=hd[1].data;t=np.asarray(a['TIME'],float);f=np.asarray(a['SAP_FLUX'],float);q=np.asarray(a['QUALITY'],int)
 z=np.isfinite(t)&np.isfinite(f)&(f>0)&(q==0);t=t[z];f=f[z]/np.median(f[z]);data.append((int(rec['sector']),t,f,float(np.median(np.diff(t))),rec['sha256']))
t0=1649.352;t1=3833.891;trials=[]
for k in (63,64,65,66,67,68,69,132):
 P=(t1-t0)/k;occasions=[]
 for s,t,f,cad,h in data:
  n0=math.ceil((t.min()-t0)/P);n1=math.floor((t.max()-t0)/P)
  for n in range(n0,n1+1):
   if n in (0,k):continue
   mid=t0+n*P;x=t-mid;core=abs(x)<.5;left=(x>-2.5)&(x<-1.4);right=(x>1.4)&(x<2.5)
   if not core.any():continue
   coret=t[core];span=(float(coret.min()-mid),float(coret.max()-mid));gap=float(np.diff(coret).max()) if len(coret)>1 else None
   full=bool(len(coret)>20 and span[0]<-.4 and span[1]>.4 and gap is not None and gap<max(.06,3*cad) and left.sum()>20 and right.sum()>20)
   if left.sum()>20 and right.sum()>20:
    # Linear baseline from side-window medians, evaluated at mid.
    xb=np.r_[np.median(x[left]),np.median(x[right])];yb=np.r_[np.median(f[left]),np.median(f[right])];base=float(np.interp(0,xb,yb));depth=float((base-np.median(f[core]))/base*1000)
   else:depth=None
   occasions.append({'sector':s,'cycle':n,'predicted_mid_btjd':mid,'core_n':int(core.sum()),'core_first_offset_days':span[0],'core_last_offset_days':span[1],'max_core_gap_days':gap,'left_n':int(left.sum()),'right_n':int(right.sum()),'full_coverage':full,'local_linear_depth_ppt':depth,'strong_null':bool(full and depth is not None and depth<6),'source_sha256':h})
 trials.append({'cycles_between_anchor_deep_events':k,'conditional_period_days':P,'occasions':occasions,'strong_null_count':sum(x['strong_null'] for x in occasions)})
out={'tic':'458324895','anchors_provisional_btjd':[t0,t1],'nominal_deep_core_window_days':1.0,'nominal_deep_depth_ppt':24,'trials':trials,'caution':'Only fully covered, internally continuous core with two outer baselines can be a sensitive null. Baseline variability can mimic weak apparent depth; inspect decisive windows visually. Even a surviving k does not prove all integer/harmonic aliases.'}
(B/'f010-aliases.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf8')
for x in trials:print(x['cycles_between_anchor_deep_events'],round(x['conditional_period_days'],5),x['strong_null_count'],[(z['sector'],z['cycle'],round(z['local_linear_depth_ppt'],1)) for z in x['occasions'] if z['strong_null']][:8])
