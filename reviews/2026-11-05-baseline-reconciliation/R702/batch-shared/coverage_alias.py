"""Sample clean/flagged predicted main and half-period windows, without interpreting predictions as timings."""
import json,math
from pathlib import Path
import numpy as np
from astropy.io import fits
B=Path(__file__).resolve().parent;D=json.loads((B/'SOURCE-SNAPSHOT.json').read_text(encoding='utf-8'));out={}
for tic,src in D.items():
 m=json.loads((B/tic/'measurements.json').read_text(encoding='utf-8'));P=m['period_days'];epoch=m['reference_epoch_btjd'];dur=float(m['screen_duration_days']);windows=[]
 for r in src['target']['file_receipts']:
  with fits.open(r['path'],memmap=False) as h:
   a=h[1].data;t=np.asarray(a['TIME'],float);f=np.asarray(a['SAP_FLUX'],float);q=np.asarray(a['QUALITY'],int)
  valid=np.isfinite(t)&np.isfinite(f)&(f>0);t=t[valid];f=f[valid];q=q[valid]
  if not len(t):continue
  for kind in ('same','half'):
   shift=0 if kind=='same' else .5
   for n in range(math.ceil((t.min()-epoch)/P-shift),math.floor((t.max()-epoch)/P-shift)+1):
    pred=epoch+(n+shift)*P;delta=t-pred;full=np.abs(delta)<max(dur*.5,.06);side=(np.abs(delta)>max(dur*1.3,.18))&(np.abs(delta)<max(dur*2.5,.4));bilat=bool(sum(side&(delta<0)&(q==0))>=3 and sum(side&(delta>0)&(q==0))>=3);clean=full&(q==0);oot=side&(q==0);rec=dict(sector=r['sector'],kind=kind,cycle=n,predicted_btjd=pred,n_core_quality0=int(sum(clean)),n_core_flagged=int(sum(full&(q!=0))),bilateral_sidebands=bilat)
    if sum(clean)>=2 and sum(oot)>=6 and bilat:
     base=np.median(f[oot]);rec['core_median_deficit_ppt']=float((1-np.median(f[clean])/base)*1000);rec['core_low_third_deficit_ppt']=float((1-np.median(np.sort(f[clean])[:max(2,sum(clean)//3)])/base)*1000);rec['oot_scatter_ppt']=float(1.4826*np.median(abs(f[oot]/base-1))*1000);rec['status']='measured_clean_window'
    else:rec['status']='incomplete_or_flagged_window'
    windows.append(rec)
 out[tic]=dict(tic=tic,period_days=P,epoch_btjd=epoch,window_note='Predictions only. Clean requires >=2 quality-zero core samples and bilateral sidebands; status is coverage, not eclipse classification. Main and opposite half-phase windows sampled.',windows=windows)
 print(tic,'same',[(w['sector'],w['cycle'],round(w.get('core_median_deficit_ppt',0),1),w['status']) for w in windows if w['kind']=='same'],'half_clean',sum(w['status']=='measured_clean_window' for w in windows if w['kind']=='half'))
(B/'coverage-alias.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
