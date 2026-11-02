from pathlib import Path
import json,numpy as np
from astropy.io import fits
b=Path('Astra/made/remaining136-2026-11-01/batch01');out={}
for tic in ['123220066']:
 m=json.load(open(b/tic/'measurements.json'));ev=[e for e in m['events'] if e.get('timing_usable')];epoch=m['primary_epoch_btjd'];P=m['period_days'];dur=m['search_duration_days'];data=[]
 for r in m['sources']:
  with fits.open(r['path']) as h:
   a=h[1].data;t=np.array(a['TIME']);f=np.array(a['SAP_FLUX']);q=np.array(a['QUALITY']);ok=np.isfinite(t)&np.isfinite(f)&(f>0);data.append((r['sector'],t[ok],f[ok],q[ok]))
 def check(p):
  records=[]
  for sec,t,f,q in data:
   for n in range(int(np.ceil((min(t)-epoch)/p)),int(np.floor((max(t)-epoch)/p))+1):
    c=epoch+n*p;x=t-c;core=(abs(x)<dur*.25)&(q==0);left=(x>-2*dur)&(x<-dur)&(q==0);right=(x>dur)&(x<2*dur)&(q==0)
    if min(core.sum(),left.sum(),right.sum())<4:continue
    base=np.median(f[left|right]);dep=1-np.median(f[core])/base;noise=1.4826*np.median(abs(f[left|right]/base-1));records.append(dict(sector=sec,center=c,depth_ppt=dep*1000,scatter_ppt=noise*1000,clean_null=bool(dep<.003 and noise<.004),n_core=int(core.sum())))
  return records
 # Finite integer-cycle aliases from first/last measured centers, allowing .04d interior timing residuals.
 tt=np.array([e['mid_btjd'] for e in ev]);cand=[]
 for n in range(int((tt[-1]-tt[0])/40),int((tt[-1]-tt[0])/.8)+1):
  p=(tt[-1]-tt[0])/n
  if max(abs((tt-tt[0])/p-np.round((tt-tt[0])/p)))*p>.04:continue
  rec=check(p);cand.append(dict(period_days=p,clean_null_count=sum(r['clean_null'] for r in rec),covered_predictions=len(rec)))
 out[tic]=dict(note='Bounded integer-alias test 0.8-40d from first/last measured centers; 0.04d interior tolerance is heuristic, not confidence coverage. Clean null requires quality-zero core and both sides, shallow deficit <3ppt and side scatter<4ppt.',aliases=cand,half_period_predictions=check(P/2),full_period_predictions=check(P))
json.dump(out,open(b/'sparse-alias-coverage.json','w'),indent=2,default=float)
print([(round(c['period_days'],7),c['clean_null_count']) for c in cand])



