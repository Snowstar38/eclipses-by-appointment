"""F007 shorter-period alias checks in actually covered raw SAP windows."""
from pathlib import Path
import json,hashlib,math
import numpy as np
from astropy.io import fits
B=Path(__file__).resolve().parent;H=B.parent.parent/'binary-exploration-2026-11-04'/'bulk-results'
bulk=json.loads((H/'238855958.json').read_text());data=[]
for rec in bulk['files']:
 p=Path(rec['path']);assert hashlib.sha256(p.read_bytes()).hexdigest()==rec['sha256']
 with fits.open(p,memmap=False) as hd:
  a=hd[1].data;t=np.asarray(a['TIME'],float);f=np.asarray(a['SAP_FLUX'],float);q=np.asarray(a['QUALITY'],int)
 z=np.isfinite(t)&np.isfinite(f)&(f>0)&(q==0);t=t[z];f=f[z]/np.median(f[z]);data.append((int(rec['sector']),t,f,float(np.median(np.diff(t))),rec['sha256']))
t0=3132.851;P=38.193;trials=[]
for div in (1,2,3,4):
 period=P/div;oc=[]
 for s,t,f,cad,h in data:
  for n in range(math.ceil((t.min()-t0)/period),math.floor((t.max()-t0)/period)+1):
   if n%div==0:continue
   mid=t0+n*period;x=t-mid;core=abs(x)<.13;left=(x>-.8)&(x<-.35);right=(x>.35)&(x<.8)
   if not core.any():continue
   tt=t[core];gap=float(np.diff(tt).max()) if len(tt)>1 else None
   full=bool(len(tt)>10 and tt.min()<mid-.11 and tt.max()>mid+.11 and gap is not None and gap<max(.04,3*cad) and left.sum()>10 and right.sum()>10)
   base=float(np.median(np.r_[f[left],f[right]])) if left.sum()>10 and right.sum()>10 else None
   depth=float((base-np.median(f[core]))/base*1000) if base is not None else None
   side=np.r_[f[left],f[right]];noise=float(1.4826*np.median(abs(side-np.median(side)))/base*1000) if base is not None else None
   oc.append({'sector':s,'subcycle':n,'mid_btjd':mid,'core_n':int(core.sum()),'first_offset_days':float(tt.min()-mid),'last_offset_days':float(tt.max()-mid),'max_gap_days':gap,'left_n':int(left.sum()),'right_n':int(right.sum()),'full':full,'depth_ppt':depth,'side_mad_noise_ppt':noise,'strong_null':bool(full and depth is not None and depth<2),'source_sha256':h})
 trials.append({'period_divisor':div,'period_days':period,'occasions':oc,'strong_null_count':sum(z['strong_null'] for z in oc)})
out={'tic':'238855958','anchor_btjd':t0,'base_period_days_provisional':P,'trials':trials,'caution':'Submultiple checks assume similar same-kind ~7-ppt eclipse every cycle; opposite-kind events may differ. Fully covered core and both baselines required for null.'}
(B/'f007-aliases.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf8')
for x in trials:print(x['period_divisor'],x['strong_null_count'],[(z['sector'],round(z['mid_btjd'],3),round(z['depth_ppt'],1)) for z in x['occasions'] if z['strong_null']][:8])
