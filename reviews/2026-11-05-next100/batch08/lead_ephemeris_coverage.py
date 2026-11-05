import json,hashlib
from pathlib import Path
import numpy as np
from astropy.io import fits
B=Path(__file__).resolve().parent;tic='280051953';ctx=json.loads((B/tic/'lead-context.json').read_text())
t0=1663.26804363;p=28.34254477;out=[]
for s in ctx['sectors']:
 with fits.open(s['source_path'],memmap=False) as h:
  a=h[1].data;t=np.asarray(a['TIME'],float);f=np.asarray(a['SAP_FLUX'],float);q=np.asarray(a['QUALITY'],int)
 g=np.isfinite(t)&np.isfinite(f)&(f>0)&(q==0);t=t[g];f=f[g]
 for n in range(int(np.floor((t.min()-t0)/p))-1,int(np.ceil((t.max()-t0)/p))+2):
  c=t0+n*p
  if c<t.min()-2.4 or c>t.max()+2.4:continue
  core=(np.abs(t-c)<=.85);left=(t>=c-2.4)&(t<=c-1.4);right=(t>=c+1.4)&(t<=c+2.4)
  tc=t[core];fc=f[core];fl=f[left];fr=f[right];expected=int(round(1.7/s['cadence_days']))+1
  depth=None
  if len(fc)>4 and len(fl)>4 and len(fr)>4:
   baseline=(np.median(fl)+np.median(fr))/2;depth=float((1-np.median(fc)/baseline)*1000)
  out.append(dict(sector=s['sector'],cycle=n,predicted_center_btjd=float(c),core_start=float(c-.85),core_end=float(c+.85),core_actual=int(len(tc)),core_expected=expected,core_first=float(tc.min()) if len(tc) else None,core_last=float(tc.max()) if len(tc) else None,core_max_internal_gap_days=float(np.max(np.diff(tc))) if len(tc)>1 else None,left_baseline_actual=int(len(fl)),right_baseline_actual=int(len(fr)),median_core_depth_ppt=depth,source_sha256=s['source_sha256']))
(B/tic/'lead-ephemeris-coverage.json').write_text(json.dumps(dict(measured_ephemeris=dict(t0=t0,p=p,width_days=1.7),windows=out),indent=2)+'\n')
print([(x['sector'],x['cycle'],round(x['predicted_center_btjd'],2),x['core_actual'],x['core_expected'],round(x['median_core_depth_ppt'],1) if x['median_core_depth_ppt'] is not None else None) for x in out])
