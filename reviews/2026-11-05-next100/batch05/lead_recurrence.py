"""Audit all covered predicted occasions of the proposed photometric clocks."""
import hashlib,json,math
from pathlib import Path
import numpy as np
from astropy.io import fits
B=Path(__file__).resolve().parent
CFG={'398073873':(1811.26020146,22.42906598,.045),
     '143497778':(1520.09707851,23.40062282,.14)}
for tic,(epoch,period,w) in CFG.items():
 d=B/tic;ctx=json.loads((d/'lead-context.json').read_text());rows=[]
 for s in ctx['sectors']:
  fp=Path(s['source_path']);assert hashlib.sha256(fp.read_bytes()).hexdigest()==s['source_sha256']
  with fits.open(fp,memmap=False) as h:
   a=h[1].data;t=np.asarray(a['TIME'],float);f=np.asarray(a['SAP_FLUX'],float);q=np.asarray(a['QUALITY'],int)
  good=np.isfinite(t)&np.isfinite(f)&(f>0)&(q==0);t=t[good];f=f[good];cad=s['cadence_days']
  lo=math.ceil((t.min()-epoch)/period);hi=math.floor((t.max()-epoch)/period)
  for n in range(lo,hi+1):
   c=epoch+n*period;core=(t>=c-w)&(t<=c+w);left=(t>=c-5*w)&(t<c-2*w);right=(t>c+2*w)&(t<=c+5*w)
   ct=t[core];expected=2*w/cad
   coreok=bool(len(ct)>=.75*expected and len(ct)>2 and ct[0]<=c-w+2*cad and ct[-1]>=c+w-2*cad and np.max(np.diff(ct))<=3*cad)
   sideok=bool(left.sum()>=5 and right.sum()>=5)
   rec=dict(sector=s['sector'],cycle=n,predicted_btjd=float(c),core_count=int(core.sum()),core_expected=float(expected),core_first_btjd=float(ct[0]) if len(ct) else None,core_last_btjd=float(ct[-1]) if len(ct) else None,core_max_gap_days=float(np.max(np.diff(ct))) if len(ct)>1 else None,left_count=int(left.sum()),right_count=int(right.sum()),sensitive=coreok and sideok,source_sha256=s['source_sha256'])
   if rec['sensitive']:
    st=np.r_[t[left],t[right]];sf=np.r_[f[left],f[right]];trend=np.polyfit(st-c,sf,1)
    rec['local_depth_ppt']=float((1-np.median(f[core]/np.polyval(trend,ct-c)))*1000)
    rec['side_mad_ppt']=float(1.4826*np.median(np.abs(sf/np.polyval(trend,st-c)-1))*1000)
   rows.append(rec)
 (d/'lead-recurrence.json').write_text(json.dumps(dict(epoch_btjd=epoch,conditional_period_days=period,half_core_days=w,occasions=rows),indent=2)+'\n')
 print(tic,[(x['sector'],x['cycle'],round(x['local_depth_ppt'],2)) for x in rows if x['sensitive']])
