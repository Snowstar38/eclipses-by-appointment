"""Bounded integer-alias coverage from T033's s80 center and s91 partial return."""
import json,hashlib
from pathlib import Path
import numpy as np
from astropy.io import fits
B=Path(__file__).resolve().parent;tic='362778566'
m=json.loads((B/tic/'lead-numeric.json').read_text())
epoch=m['events'][0]['fit_mid_btjd'];delta=5*m['gaia_period_days']
sectors=[]
for s in m['sources']:
 p=Path(s['path']);assert hashlib.sha256(p.read_bytes()).hexdigest()==s['sha256']
 with fits.open(p,memmap=False) as h:
  d=h[1].data;t=np.asarray(d['TIME'],float);f=np.asarray(d['SAP_FLUX'],float);q=np.asarray(d['QUALITY'],int)
 ok=np.isfinite(t)&np.isfinite(f)&(f>0)&(q==0);sectors.append((s['sector'],t[ok],f[ok]))
out=[]
for cycles in range(3,11):
 period=delta/cycles;windows=[]
 for number in range(-2,cycles+3):
  pred=epoch+number*period
  for sec,t,f in sectors:
   if pred<t.min()-1.5 or pred>t.max()+1.5:continue
   core=np.abs(t-pred)<0.6;side=(np.abs(t-pred)>1.2)&(np.abs(t-pred)<2.5)
   d=dict(number=number,sector=sec,pred_btjd=float(pred),core_n=int(sum(core)),side_n=int(sum(side)),core_start=float(t[core].min()) if any(core) else None,core_end=float(t[core].max()) if any(core) else None,max_core_gap=float(np.diff(t[core]).max()) if sum(core)>1 else None)
   if sum(core)>20 and sum(side)>20:d['core_minus_side_ppt']=float(1000*(np.median(f[core])/np.median(f[side])-1))
   windows.append(d)
 out.append(dict(cycles=cycles,conditional_period_days=period,windows=windows))
(B/tic/'lead-aliases.json').write_text(json.dumps(out,indent=2)+'\n')
for a in out:
 print(a['cycles'],round(a['conditional_period_days'],3),[(x['sector'],x['number'],round(x['pred_btjd'],2),x['core_n'],round(x.get('core_minus_side_ppt',float('nan')),1)) for x in a['windows']])
