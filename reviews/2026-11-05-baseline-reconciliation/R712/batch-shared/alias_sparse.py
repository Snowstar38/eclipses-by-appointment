import json,math
from pathlib import Path
import numpy as np
from astropy.io import fits
B=Path(__file__).resolve().parent;D=json.loads((B/'SOURCE-SNAPSHOT.json').read_text());out={}
for tic in ('188908998','280950412'):
 s=D[tic];m=json.loads((B/tic/'measurements.json').read_text());
 if tic=='188908998':e1,e2=[e['mid_btjd'] for e in m['events']];n0=32;depth=18;duration=.6
 else:e1,e2=1603.6078424135983,3061.5060888802295;n0=64;depth=1.;duration=.3
 sectors=[]
 for r in s['target']['file_receipts']:
  with fits.open(r['path']) as h:
   a=h[1].data;t=np.asarray(a['TIME'],float);f=np.asarray(a['SAP_FLUX'],float);q=np.asarray(a['QUALITY'],int)
  ok=np.isfinite(t)&np.isfinite(f)&(f>0);sectors.append((r['sector'],t[ok],f[ok],q[ok]))
 aliases=[]
 for ncycle in range(max(1,n0-10),n0+11):
  p=(e2-e1)/ncycle; wins=[]
  for sector,t,f,q in sectors:
   for n in range(math.ceil((t.min()-e1)/p),math.floor((t.max()-e1)/p)+1):
    pred=e1+n*p
    if min(abs(pred-e1),abs(pred-e2))<duration:continue
    x=t-pred; core=(abs(x)<duration*.30)&(q==0);left=(x<-.75*duration)&(x>-1.5*duration)&(q==0);right=(x>.75*duration)&(x<1.5*duration)&(q==0)
    if sum(core)>=4 and sum(left)>=4 and sum(right)>=4:
     base=np.median(f[left|right]); deficit=(1-np.median(f[core])/base)*1000; noise=1.4826*np.median(abs(f[left|right]/base-1))*1000
     sensitive=bool(noise<depth/3)
     wins.append(dict(sector=sector,cycle=n,btjd=pred,deficit_ppt=deficit,noise_ppt=noise,sensitive_to_nominal_depth=sensitive,clean_null=bool(sensitive and deficit<depth*.4)))
  aliases.append(dict(cycles_between=ncycle,period_days=p,clean_nulls=sum(w['clean_null'] for w in wins),covered_predictions=len(wins),windows=wins))
 out[tic]=dict(event_centers_btjd=[e1,e2],candidate_aliases=aliases,criterion='Measured quality-zero central/sideband windows; clean_null requires local robust scatter <nominal depth/3 and measured deficit <0.4 nominal depth. This simple aperture-noise sensitivity screen is descriptive only; weak-case dips are not secure.')
 print(tic,[(a['cycles_between'],round(a['period_days'],4),a['covered_predictions'],a['clean_nulls']) for a in aliases])
(B/'sparse-aliases.json').write_text(json.dumps(out,indent=2)+'\n')
