import json,numpy as np
from pathlib import Path
from astropy.io import fits
b=Path(__file__).resolve().parent;out={}
for p in b.glob('*/lead-context.json'):
 d=json.loads(p.read_text());evs=[]
 for e in json.loads((p.parent/'lead-timing.json').read_text()):
  if not e.get('fit_usable'):continue
  src=next(z for z in d['source'] if z['sector']==e['sector']);a=fits.getdata(src['path'],1);t=np.asarray(a['TIME']);f=np.asarray(a['SAP_FLUX']);q=np.asarray(a['QUALITY']);ok=np.isfinite(t)&np.isfinite(f)&(f>0);c=e['center_btjd'];dur=e['duration_d'];core=ok&(abs(t-c)<dur*.5);side=ok&(abs(t-c)>dur*.7)&(abs(t-c)<dur*1.5);base=np.median(f[side&(q==0)]) if (side&(q==0)).sum()>3 else np.nan
  evs.append({'sector':e['sector'],'center_btjd':c,'core_quality_zero_n':int((core&(q==0)).sum()),'core_flagged_n':int((core&(q!=0)).sum()),'all_finite_core_median_depth_ppt':float((1-np.median(f[core])/base)*1000) if core.any() else None,'flagged_core_minimum_btjd':float(t[core&(q!=0)][np.argmin(f[core&(q!=0)])]) if (core&(q!=0)).any() else None,'flag_values':np.unique(q[core&(q!=0)]).astype(int).tolist(),'source_sha256':src['sha256']})
 out[d['tic']]=evs
(b/'lead-flagged-raw-audit.json').write_text(json.dumps(out,indent=2));print('flagged representative core audit',sum(len(x) for x in out.values()))
