import json,hashlib
from pathlib import Path
import numpy as np
from astropy.io import fits
B=Path(__file__).resolve().parent;H=B.parent.parent/'binary-exploration-2026-11-04'; tic='339023379'; bulk=json.loads((H/'bulk-results'/f'{tic}.json').read_text()); out=[]
for rec in bulk['files']:
 p=Path(rec['path']);assert hashlib.sha256(p.read_bytes()).hexdigest()==rec['sha256']
 with fits.open(p) as h:t=np.array(h[1].data['TIME'],float);f=np.array(h[1].data['SAP_FLUX'],float);q=np.array(h[1].data['QUALITY'],int)
 good=np.isfinite(t)&np.isfinite(f)&(f>0)&(q==0);t=t[good];f=f[good];o={'sector':rec['sector'],'range':[float(min(t)),float(max(t))],'windows':[],'source_sha256':rec['sha256']}
 # shallow pair differences, approximate centers, no clock precision implied
 for k in [14,15,16]:
  P=(3121.0-2371.095)/k
  for n in range(-100,101):
   x=2371.095+n*P
   if min(t)-1<x<max(t)+1:
    core=t[(abs(t-x)<=.25)];left=t[(t>=x-.9)&(t<=x-.45)];right=t[(t>=x+.45)&(t<=x+.9)];dt=np.median(np.diff(t));
    def cov(a,lo,hi):
     return {'n':len(a),'left_gap':float(a[0]-lo) if len(a) else None,'right_gap':float(hi-a[-1]) if len(a) else None,'max_internal_gap':float(max(np.diff(a))) if len(a)>1 else None}
    v={'k':k,'period':P,'n':n,'predicted':x,'cadence':float(dt),'core':cov(core,x-.25,x+.25),'left':cov(left,x-.9,x-.45),'right':cov(right,x+.45,x+.9)}
    if len(core)>1 and len(left)>1 and len(right)>1:
     baseline=.5*(np.median(f[(t>=x-.9)&(t<=x-.45)])+np.median(f[(t>=x+.45)&(t<=x+.9)]));v['depth_ppt']=float(1000*(1-np.median(f[abs(t-x)<=.25])/baseline))
    o['windows'].append(v)
 out.append(o)
(B/'helper-F008-coverage.json').write_text(json.dumps(out,indent=2));
for o in out:
 for v in o['windows']:
  c=v['core'];l=v['left'];r=v['right'];
  if all(z['n']>3 and z['left_gap'] is not None and z['right_gap'] is not None and z['max_internal_gap'] is not None and max(z['left_gap'],z['right_gap'],z['max_internal_gap'])<.08 for z in [c,l,r]): print(o['sector'],v['k'],round(v['predicted'],3),round(v.get('depth_ppt',0),2))
