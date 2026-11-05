"""Check integer-cycle aliases between sector-89 B eclipses in raw SAP."""
import json,hashlib
from pathlib import Path
import numpy as np
from astropy.io import fits
B=Path(__file__).resolve().parent;m=json.loads((B/'271053559'/'lead-numeric.json').read_text())
e=sorted([x for x in m['events'] if x['sector']==89 and abs(x['fit_mid_btjd']-3721.493)<.003 or x['sector']==89 and abs(x['fit_mid_btjd']-3746.148)<.003],key=lambda x:x['fit_mid_btjd'])
assert len(e)==2
s=next(x for x in m['sources'] if x['sector']==89);p=Path(s['path']);assert hashlib.sha256(p.read_bytes()).hexdigest()==s['sha256']
with fits.open(p) as h:
 d=h[1].data;t=np.asarray(d['TIME'],float);f=np.asarray(d['SAP_FLUX'],float);q=np.asarray(d['QUALITY'],int)
ok=np.isfinite(t)&np.isfinite(f)&(f>0)&(q==0);t=t[ok];f=f[ok];cad=np.median(np.diff(t));out=[]
for n in range(2,6):
 P=(e[1]['fit_mid_btjd']-e[0]['fit_mid_btjd'])/n;mid=[]
 for k in range(1,n):
  pred=e[0]['fit_mid_btjd']+k*P;core=np.abs(t-pred)<.18;base=((t>pred-.9)&(t<pred-.36))|((t>pred+.36)&(t<pred+.9))
  mid.append(dict(pred_btjd=float(pred),core_n=int(core.sum()),expected_n=int(round(.36/cad)),core_first=float(t[core].min()) if core.any() else None,core_last=float(t[core].max()) if core.any() else None,max_gap=float(np.diff(t[core]).max()) if core.sum()>1 else None,baseline_n=int(base.sum()),core_deficit_ppt=float(1000*(1-np.median(f[core])/np.median(f[base]))) if core.sum()>2 and base.sum()>5 else None))
 out.append(dict(cycles_between_B=n,conditional_period_days=P,intermediate_B_predictions=mid))
 print(n,round(P,6),[(round(x['pred_btjd'],3),x['core_n'],round(x['core_deficit_ppt'],1) if x['core_deficit_ppt'] is not None else None) for x in mid])
(B/'lead-alias-t083.json').write_text(json.dumps(out,indent=2)+'\n')
