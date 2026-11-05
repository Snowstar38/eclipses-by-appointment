import json,numpy as np
from pathlib import Path
from astropy.io import fits
B=Path(__file__).parent;D=B/'3299934';ctx=json.loads((D/'lead-context.json').read_text());ev=json.loads((D/'lead-timing.json').read_text()); t=np.array([x['center_btjd'] for x in ev]); n=np.array([0,1,70,105]); P,epoch=np.polyfit(n,t,1); out={'period_fit_d':P,'epoch_btjd':epoch,'residual_days':(t-(epoch+n*P)).tolist(),'aliases':{}}
for k in range(1,5):
 p=P/k;wins=[]
 for s in ctx['sectors']:
  with fits.open(s['source_path']) as h:
   a=h[1].data;tt=np.asarray(a['TIME'],float);ff=np.asarray(a['SAP_FLUX'],float);q=np.asarray(a['QUALITY'],int);g=np.isfinite(tt)&np.isfinite(ff)&(ff>0)&(q==0);tt=tt[g];ff=ff[g]
  for j in range(int(np.floor((tt.min()-epoch)/p)),int(np.ceil((tt.max()-epoch)/p))+1):
   c=epoch+j*p
   if c-.45<tt.min() or c+.45>tt.max():continue
   core=(abs(tt-c)<.20);left=(tt>c-.45)&(tt<c-.30);right=(tt>c+.30)&(tt<c+.45)
   if core.sum()<3 or left.sum()<3 or right.sum()<3:continue
   cad=s['cadence_days']; maxgap=max(np.diff(tt[(tt>c-.45)&(tt<c+.45)]),default=99)
   if maxgap>3*cad:continue
   depth=(1-np.median(ff[core])/np.median(ff[left|right]))*1000
   wins.append({'sector':s['sector'],'center':c,'depth_ppt':depth,'core_n':int(core.sum()),'left_n':int(left.sum()),'right_n':int(right.sum()),'max_gap_d':float(maxgap),'near_observed_event':bool(min(abs(t-c))<.1)})
 out['aliases'][str(k)]={'period_d':p,'windows':wins}
(D/'lead-alias.json').write_text(json.dumps(out,indent=2));print(json.dumps(out,indent=2))
