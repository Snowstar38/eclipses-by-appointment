import json,numpy as np
from pathlib import Path
from astropy.io import fits
b=Path(r'[workspace]/Astra\made\final-night-2026-11-05\fresh18\batch02');tic='162437782';cl=json.loads((b/'lead-clocks.json').read_text())[tic];times=np.array(cl['event_btjd']);t0=times[0];span=times[-1]-t0;ctx=json.loads((b/tic/'lead-context.json').read_text());curves=[]
for src in ctx['source']:
 with fits.open(src['path']) as h:
  a=h[1].data;t=np.array(a['TIME']);y=np.array(a['SAP_FLUX']);q=np.array(a['QUALITY']);o=(q==0)&np.isfinite(t)&np.isfinite(y)&(y>0);curves.append((src,t[o],y[o]))
out=[]
for n in range(int(np.ceil(span/100)),int(span/.5)+1):
 p=span/n;cycles=np.rint((times-t0)/p);res=times-t0-cycles*p
 if max(abs(res))>.06:continue
 nulls=[]
 for src,t,y in curves:
  for k in range(int(np.ceil((t.min()-t0)/p)),int(np.floor((t.max()-t0)/p))+1):
   pred=t0+k*p
   if min(abs(times-pred))<.1:continue
   core=abs(t-pred)<.12;side=(abs(t-pred)>.3)&(abs(t-pred)<.55);left=(t<pred-.3)&(t>pred-.55);right=(t>pred+.3)&(t<pred+.55)
   if min(core.sum(),left.sum(),right.sum())<5:continue
   cad=np.median(np.diff(t));tc=t[core]
   if np.max(np.diff(tc))>max(cad*3,.06) or core.sum()*cad/.24<.75:continue
   base=np.polyval(np.polyfit(t[side]-pred,y[side],1),t-pred);z=y/base;depth=(1-np.median(z[core]))*1000;noise=np.std(z[side])*1000
   if abs(depth)<6 and noise<6:nulls.append(dict(sector=src['sector'],btjd=float(pred),depth_ppt=float(depth),noise_ppt=float(noise),n_core=int(core.sum()),source_sha256=src['sha256']))
   if len(nulls)>=2:break
  if len(nulls)>=2:break
 out.append(dict(period_d=p,cycles=cycles.astype(int).tolist(),max_residual_d=float(max(abs(res))),clean_nulls=nulls,rejected=bool(nulls)))
(b/'lead-y011-integer-alias-audit.json').write_text(json.dumps(dict(scope='same-kind constant periods0.5-100d anchored first and last events; intermediate center tolerance0.06d; clean core coverage>=75%, max gap3cadence or.06d; null |depth|<6ppt and side scatter<6ppt against23ppt eclipse',candidates=out),indent=2));print('aliases',len(out),'survive',[(r['period_d'],r['cycles']) for r in out if not r['rejected']])
