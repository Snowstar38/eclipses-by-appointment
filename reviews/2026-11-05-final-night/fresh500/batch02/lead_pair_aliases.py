import json,numpy as np
from pathlib import Path
from astropy.io import fits
b=Path(__file__).resolve().parent;tic='372172730';d=json.loads((b/tic/'lead-context.json').read_text());t0=1669.9473844469494;delta=2056.9016622032736-t0;dur=.162;series=[]
for src in d['source']:
 with fits.open(src['path']) as h:a=h[1].data;t=np.asarray(a['TIME'],float);f=np.asarray(a['SAP_FLUX'],float);q=np.asarray(a['QUALITY'],int)
 ok=np.isfinite(t)&np.isfinite(f)&(f>0)&(q==0);series.append((src,t[ok],f[ok]))
out=[]
for n in range(4,78):
 p=delta/n;windows=[]
 for src,t,f in series:
  cad=np.median(np.diff(t))
  for cyc in range(int(np.ceil((min(t)-t0)/p)),int(np.floor((max(t)-t0)/p))+1):
   pred=t0+cyc*p;core=abs(t-pred)<dur*.35;left=(t>pred-dur*1.6)&(t<pred-dur*.75);right=(t>pred+dur*.75)&(t<pred+dur*1.6)
   if min(core.sum(),left.sum(),right.sum())<3:continue
   if core.sum()*cad/(dur*.7)<.75 or np.max(np.diff(t[core]))>max(cad*3,dur*.2):continue
   tl=np.median(t[left]);tr=np.median(t[right]);fl=np.median(f[left]);fr=np.median(f[right]);base=fl+(fr-fl)*(t-tl)/(tr-tl);z=f/base;noise=1.4826*np.median(abs(z[left|right]-np.median(z[left|right])))*1000;depth=(1-np.median(z[core]))*1000;null=depth<max(7.7*.15,noise*4/np.sqrt(core.sum()));windows.append(dict(sector=src['sector'],predicted_btjd=pred,depth_ppt=depth,noise_ppt=noise,core_n=int(core.sum()),null=bool(null),source_sha256=src['sha256']))
 out.append(dict(cycles_between_clean_events=n,period_d=p,covered_windows=windows,null_count=sum(w['null'] for w in windows)))
(b/'lead-E018-pair-aliases.json').write_text(json.dumps(out,indent=2));print('pair aliases without covered nulls',[(a['cycles_between_clean_events'],a['period_d'],len(a['covered_windows'])) for a in out if not a['null_count']])
