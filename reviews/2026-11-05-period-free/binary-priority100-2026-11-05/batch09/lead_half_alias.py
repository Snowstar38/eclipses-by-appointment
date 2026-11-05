"""Test half-period opposite-kind predictions against actual QLP SAP coverage."""
import json,hashlib
from pathlib import Path
import numpy as np
from astropy.io import fits
B=Path(__file__).resolve().parent
tim={x['sample_id']:x for x in json.loads((B/'lead-timing.json').read_text())}
out=[]
for sid,tic in [('T086','398402989'),('T087','200743349'),('T089','410314066')]:
 m=json.loads((B/tic/'lead-numeric.json').read_text());P=tim[sid]['period_days'];epoch=tim[sid]['epoch_btjd'];rows=[]
 for s in m['sources']:
  p=Path(s['path']);assert hashlib.sha256(p.read_bytes()).hexdigest()==s['sha256']
  with fits.open(p) as h:
   d=h[1].data;t=np.asarray(d['TIME'],float);f=np.asarray(d['SAP_FLUX'],float);q=np.asarray(d['QUALITY'],int)
  ok=np.isfinite(t)&np.isfinite(f)&(f>0)&(q==0);t=t[ok];f=f[ok]
  if len(t)<10:continue
  cad=np.median(np.diff(t));half=.18
  for n in range(int(np.floor((t.min()-epoch)/(P/2)))-1,int(np.ceil((t.max()-epoch)/(P/2)))+2):
   if n%2==0:continue
   pred=epoch+n*P/2
   if pred<t.min()-half or pred>t.max()+half:continue
   core=np.abs(t-pred)<half;left=(t>pred-.9)&(t<pred-.36);right=(t>pred+.36)&(t<pred+.9);base=left|right
   expected=round(2*half/cad);coverage=core.sum()/expected
   rec=dict(sector=s['sector'],half_cycle=n,pred_btjd=float(pred),core_n=int(core.sum()),expected_n=int(expected),core_coverage=float(coverage),first_core=float(t[core].min()) if core.any() else None,last_core=float(t[core].max()) if core.any() else None,max_gap=float(np.diff(t[core]).max()) if core.sum()>1 else None,baseline_n=int(base.sum()),core_deficit_ppt=float(1000*(1-np.median(f[core])/np.median(f[base]))) if core.sum()>2 and base.sum()>5 else None)
   rows.append(rec)
 out.append(dict(sample_id=sid,tic=tic,period_days=P,half_period_days=P/2,core_half_width_days=.18,records=rows))
 print(sid,[(x['sector'],round(x['pred_btjd'],3),round(x['core_coverage'],2),round(x['core_deficit_ppt'],1) if x['core_deficit_ppt'] is not None else None) for x in rows])
(B/'lead-half-alias.json').write_text(json.dumps(out,indent=2)+'\n')
