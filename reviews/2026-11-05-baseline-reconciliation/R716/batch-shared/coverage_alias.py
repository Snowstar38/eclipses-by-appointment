"""Actual quality-zero coverage and integer-cycle aliases; predictions are never timings."""
import json,math
from pathlib import Path
import numpy as np
from astropy.io import fits
B=Path(__file__).resolve().parent;D=json.loads((B/'SOURCE-SNAPSHOT.json').read_text());out={}
for tic,src in D.items():
 m=json.loads((B/tic/'measurements.json').read_text()); es=[e for e in m['events'] if e.get('timing_usable') or (tic=='349527829' and e.get('mid_btjd'))];es.sort(key=lambda e:e['mid_btjd'])
 P=m['period_days'];epoch=m['reference_epoch_btjd'];dur=float(np.median([e['duration_days'] for e in es]));dep=float(np.median([e['depth_ppt'] for e in es]));series=[]
 for r in src['target']['file_receipts']:
  with fits.open(r['path'],memmap=False) as h:
   a=h[1].data;t=np.asarray(a['TIME'],float);f=np.asarray(a['SAP_FLUX'],float);q=np.asarray(a['QUALITY'],int)
  v=np.isfinite(t)&np.isfinite(f)&(f>0);t=t[v];f=f[v];q=q[v];series.append((r['sector'],t,f,q,float(np.median(np.diff(t)))))
 def windows(per,phase=0):
  ws=[]
  for sec,t,f,q,cad in series:
   for n in range(math.ceil((t.min()-epoch)/per-phase),math.floor((t.max()-epoch)/per-phase)+1):
    pred=epoch+(n+phase)*per;x=t-pred;core=abs(x)<dur*.3;side=(abs(x)>dur*.8)&(abs(x)<max(dur*1.8,.5));clean=core&(q==0);oot=side&(q==0);left=sum(oot&(x<0));right=sum(oot&(x>0));frac=sum(clean)/max(1,dur*.6/cad)
    r=dict(sector=sec,cycle=n,predicted_btjd=float(pred),n_core_quality0=int(sum(clean)),n_core_flagged=int(sum(core&(q!=0))),core_cadence_fraction=float(frac),bilateral_sidebands=bool(left>=4 and right>=4),status='incomplete_or_flagged')
    if frac>=.75 and sum(clean)>=3 and left>=4 and right>=4:
     base=np.median(f[oot]);noise=1.4826*np.median(abs(f[oot]/base-1))*1000;loss=(1-np.median(f[clean])/base)*1000;inconsistent=bool(loss+5*noise/np.sqrt(max(1,sum(clean)))<dep*.4 and noise<dep*.25);r.update(status='clean_measured_window',median_deficit_ppt=float(loss),scatter_ppt=float(noise),depth_inconsistent_window=inconsistent,sensitive_null=bool(inconsistent and loss<max(dep*.1,3*noise/np.sqrt(max(1,sum(clean))))))
    ws.append(r)
  return ws
 candidates=[];span=es[-1]['mid_btjd']-es[0]['mid_btjd'];N=round(span/P)
 vals=[('selected',P),('half',P/2),('third',P/3),('double',P*2)]
 if N>2: vals +=[(f'integer_{j}',span/j) for j in range(max(1,N-2),N+3) if j!=N]
 for label,per in vals:
  ws=windows(per);res=[abs(((e['mid_btjd']-epoch+per/2)%per)-per/2) for e in es];tol=max(.03,dur*.15);nulls=[w for w in ws if w.get('sensitive_null')]
  candidates.append(dict(label=label,period_days=per,timing_max_residual_days=max(res),timing_test_tolerance_days=tol,timing_rejected=max(res)>tol,sensitive_null_count=len(nulls),sensitive_nulls=nulls,depth_inconsistent_count=sum(w.get('depth_inconsistent_window',False) for w in ws),windows=ws))
 out[tic]=dict(tic=tic,epoch_btjd=epoch,adopted_period_days=P,duration_days=dur,central_depth_ppt=dep,aliases=candidates,opposite_half_phase_windows=windows(P,.5),note='Raw SAP quality0 coverage. Sensitive null requires >=75% central cadence coverage, >=3 core points, >=4 each sideband, scatter <1/4 event depth, and median deficit +5*scatter/sqrt(N)<0.4 event depth. Timing tests use actual centers; other-kind eclipses may reject a half period only when unequal morphology establishes kinds. Alternative integer aliases locally N±2 are tested; no exhaustive alias claim.')
 print(tic,[(a['label'],a['timing_rejected'],a['sensitive_null_count']) for a in candidates])
(B/'coverage-alias.json').write_text(json.dumps(out,indent=2)+'\n')
