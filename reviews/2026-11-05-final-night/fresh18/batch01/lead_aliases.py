import json,numpy as np
from pathlib import Path
from astropy.io import fits
b=Path('[workspace]/Astra/made/final-night-2026-11-05/fresh18/batch01');cl=json.loads((b/'lead-clocks.json').read_text());out=[]
for tic,c in cl.items():
 d=json.loads((b/tic/'lead-context.json').read_text());p=c['period_d'];t0=c['epoch_btjd'];dur=.55 if tic=='22559994' else .25
 for src in d['source']:
  with fits.open(src['path']) as h:
   a=h[1].data;t=np.asarray(a['TIME'],float);y=np.asarray(a['SAP_FLUX'],float);q=np.asarray(a['QUALITY'],int)
  ok=np.isfinite(t)&np.isfinite(y)&(y>0)&(q==0);t=t[ok];y=y[ok]
  for div in [2,3,4,5,6]:
   pp=p/div
   for n in range(int(np.ceil((t.min()-t0)/pp)),int(np.floor((t.max()-t0)/pp))+1):
    if n%div==0:continue
    pred=t0+n*pp;core=abs(t-pred)<dur/2;outer=1.15 if tic=='22559994' else 2;inner=.65 if tic=='22559994' else .8;left=(t>pred-dur*outer)&(t<pred-dur*inner);right=(t>pred+dur*inner)&(t<pred+dur*outer)
    if min(core.sum(),left.sum(),right.sum())<5:continue
    tc=t[core];cad=np.median(np.diff(t));cover=len(tc)*cad/dur
    if cover<.75 or np.max(np.diff(tc))>max(cad*3,dur*.25):continue
    tl=np.median(t[left]);tr=np.median(t[right]);fl=np.median(y[left]);fr=np.median(y[right]);base=fl+(fr-fl)*(t-tl)/(tr-tl);z=y/base;noise=1.4826*np.median(abs(z[left|right]-np.median(z[left|right])))
    out.append(dict(tic=tic,sector=src['sector'],alias_divisor=div,predicted_btjd=float(pred),core_n=int(core.sum()),coverage_fraction=float(cover),core_gap_d=float(np.max(np.diff(tc))),depth_ppt=float((1-np.median(z[core]))*1000),noise_ppt=float(noise*1000),source_sha256=src['sha256']))
(b/'lead-alias-covered-windows.json').write_text(json.dumps(out,indent=2))
for tic in cl:
 print(tic,[(n,len([e for e in out if e['tic']==tic and e['alias_divisor']==n]),round(min([abs(e['depth_ppt']) for e in out if e['tic']==tic and e['alias_divisor']==n] or [999]),2)) for n in [2,3,4,5,6]])

