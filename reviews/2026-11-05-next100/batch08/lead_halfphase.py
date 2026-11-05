import json
from pathlib import Path
import numpy as np
from astropy.io import fits
B=Path(__file__).resolve().parent;tic='280051953';ctx=json.loads((B/tic/'lead-context.json').read_text());t0=1379.83394011;p=28.34273608;out=[]
for s in ctx['sectors']:
 with fits.open(s['source_path'],memmap=False) as h:
  a=h[1].data;t=np.array(a['TIME'],float);f=np.array(a['SAP_FLUX'],float);q=np.array(a['QUALITY'],int)
 g=np.isfinite(t)&np.isfinite(f)&(f>0)&(q==0);t=t[g];f=f[g];cad=s['cadence_days']
 for n in range(int(np.floor((t.min()-t0)/p))-1,int(np.ceil((t.max()-t0)/p))+2):
  c=t0+(n+.5)*p
  if c<t.min()-2.4 or c>t.max()+2.4:continue
  core=(abs(t-c)<=.85);left=(t>=c-2.4)&(t<=c-1.4);right=(t>=c+1.4)&(t<=c+2.4);tc=t[core]
  depth=None
  if core.sum()>4 and left.sum()>4 and right.sum()>4:
   base=(np.median(f[left])+np.median(f[right]))/2;depth=float(1000*(1-np.median(f[core])/base))
  out.append(dict(sector=s['sector'],half_cycle_after=n,predicted_btjd=float(c),core_actual=int(core.sum()),core_expected=int(round(1.7/cad))+1,core_first=float(tc.min()) if len(tc) else None,core_last=float(tc.max()) if len(tc) else None,core_max_internal_gap=float(np.max(np.diff(tc))) if len(tc)>1 else None,left_actual=int(left.sum()),right_actual=int(right.sum()),median_core_depth_ppt=depth,source_sha256=s['source_sha256']))
(B/tic/'lead-halfphase-coverage.json').write_text(json.dumps(out,indent=2)+'\n')
print([(x['sector'],round(x['predicted_btjd'],2),x['core_actual'],x['core_expected'],round(x['median_core_depth_ppt'],2) if x['median_core_depth_ppt'] is not None else None) for x in out])
