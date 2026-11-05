"""Independent pipeline flux check at selected measured raw events.

KSPSAP is a separately extracted flux column in the cached QLP file and
shares the same TESS observing occasions as SAP.
"""
import csv,json,hashlib
from pathlib import Path
import numpy as np
from astropy.io import fits
B=Path(__file__).resolve().parent;out=[]
for r in csv.DictReader((B/'queue.csv').open()):
 m=json.loads((B/r['tic']/'lead-numeric.json').read_text()); ev=[]
 for src in m['sources']:
  p=Path(src['path']);assert hashlib.sha256(p.read_bytes()).hexdigest()==src['sha256']
  with fits.open(p,memmap=False) as h:
   a=h[1].data;t=np.array(a['TIME'],float);q=np.array(a['QUALITY'],int);f=np.array(a['KSPSAP_FLUX'],float) if 'KSPSAP_FLUX' in a.names else None
  if f is None:continue
  for e in m['events']:
   if e['sector']!=src['sector']:continue
   center=e['fit_mid_btjd'];dur=e['fit_duration_days']
   core=(abs(t-center)<dur*.35)&(q==0)&np.isfinite(f)&(f>0)
   left=(t>center-2*dur)&(t<center-dur)&(q==0)&np.isfinite(f)&(f>0)
   right=(t>center+dur)&(t<center+2*dur)&(q==0)&np.isfinite(f)&(f>0)
   if min(core.sum(),left.sum(),right.sum())<3:depth=None
   else:
    base=(np.median(f[left])+np.median(f[right]))/2
    depth=float(1000*(1-np.median(f[core])/base))
   ev.append(dict(sector=e['sector'],mid_btjd=center,raw_depth_ppt=e['raw_core_median_deficit_ppt'],kspsap_depth_ppt=depth,core_n=int(core.sum()),left_n=int(left.sum()),right_n=int(right.sum()),source_sha256=src['sha256']))
 out.append(dict(sample_id=r['sample_id'],tic=r['tic'],events=ev))
 print(r['sample_id'],[(e['sector'],round(e['mid_btjd'],2),None if e['kspsap_depth_ppt'] is None else round(e['kspsap_depth_ppt'],1)) for e in ev],flush=True)
(B/'lead-alternative.json').write_text(json.dumps(out,indent=2)+'\n')
