import json, hashlib
from pathlib import Path
import numpy as np
from astropy.io import fits
B=Path(__file__).resolve().parent; root=B.parent
p=json.loads((root/'source-packets/28059397/sources.json').read_text(encoding='utf-8'))
t0=2835.22350148201;t1=3561.0543768368098; dt=t1-t0
series=[]; hashes=[]
for v in p['verified_files']:
 f=Path(v['path']); h=hashlib.sha256(f.read_bytes()).hexdigest(); assert h==v['sha256']; hashes.append({'path':str(f),'sha256':h})
 with fits.open(f) as hd:
  d=hd[1].data;t=np.asarray(d['TIME'],float);y=np.asarray(d['SAP_FLUX'],float);q=np.asarray(d['QUALITY'],int)
  ok=np.isfinite(t)&np.isfinite(y)&(y>0)&(q==0);t=t[ok];y=y[ok];series.append((int(f.stem.split('_s')[-1]),t,y))
out=[]
for n in range(25,38):
 P=dt/n; windows=[]
 for s,t,y in series:
  for k in range(-5,n+6):
   c=t0+k*P
   if abs(c-t0)<.8 or abs(c-t1)<.8 or c<t.min()-.5 or c>t.max()+.5:continue
   core=(abs(t-c)<.15); base=(abs(t-c)>.45)&(abs(t-c)<.85)
   if not core.any(): continue
   cadence=np.median(np.diff(t)); expected=.30/cadence
   # coverage evaluated by endpoints and largest gap, separately from baseline
   tc=t[core]; coverage={'fraction':min(1,len(tc)/expected),'left_offset':float(tc.min()-c),'right_offset':float(tc.max()-c),'max_gap':float(np.max(np.diff(tc))) if len(tc)>1 else None}
   dep=float((1-np.median(y[core])/np.median(y[base]))*1000) if base.sum()>5 else None
   windows.append({'sector':s,'center':c,'coverage':coverage,'baseline_n':int(base.sum()),'depth_ppt':dep})
 out.append({'N':n,'period':P,'windows':windows})
(B/'28059397/helper-alias.json').write_text(json.dumps({'event_centers':[t0,t1],'note':'Local medians; depths and core coverage are screening only. Off-event baselines may contain events; predicted centers assume exact same-kind period. Partial windows do not automatically reject.','sources':hashes,'aliases':out},indent=2)+'\n',encoding='utf-8')
for a in out:
 print(a['N'],round(a['period'],5),[(w['sector'],round(w['center'],2),round(w['coverage']['fraction'],2),round(w['depth_ppt'],1) if w['depth_ppt'] is not None else None) for w in a['windows']])
