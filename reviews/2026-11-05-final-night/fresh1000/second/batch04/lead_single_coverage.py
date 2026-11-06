"""Covered windows conditional on the selection Gaia period; never a period measurement."""
import json,csv,numpy as np
from pathlib import Path
from astropy.io import fits
b=Path(__file__).resolve().parent;out={}
for r in csv.DictReader((b/'queue.csv').open()):
 tic=r['tic'];d=json.loads((b/tic/'lead-context.json').read_text());ev=json.loads((b/tic/'lead-timing.json').read_text());e=ev[0];c=e.get('center_btjd',e['screen_btjd']);dur=e.get('duration_d',.5);dur=min(max(dur,.1),1.6);p=float(r['gaia_period']);tests=[]
 for src in d['source']:
  with fits.open(src['path']) as h:a=h[1].data;t=np.array(a['TIME']);f=np.array(a['SAP_FLUX']);q=np.array(a['QUALITY'])
  k=np.isfinite(t)&np.isfinite(f)&(f>0)&(q==0);t=t[k];f=f[k];cad=np.median(np.diff(t))
  for n in range(int(np.ceil((t.min()-c)/p)),int(np.floor((t.max()-c)/p))+1):
   pred=c+n*p;core=abs(t-pred)<dur*.35;left=(t>pred-dur*1.6)&(t<pred-dur*.75);right=(t>pred+dur*.75)&(t<pred+dur*1.6)
   z=dict(sector=src['sector'],cycle=n,pred_btjd=pred,core_n=int(core.sum()),left_n=int(left.sum()),right_n=int(right.sum()),source_sha256=src['sha256'])
   if min(core.sum(),left.sum(),right.sum())>=3:
    z['core_fraction']=float(core.sum()*cad/(dur*.7));z['max_core_gap_d']=float(np.max(np.diff(t[core])));base=np.median(f[left|right]);z['depth_ppt']=float((1-np.median(f[core])/base)*1000);z['side_scatter_ppt']=float(1.4826*np.median(abs(f[left|right]-np.median(f[left|right])))/base*1000);z['coverage_adequate']=bool(z['core_fraction']>=.75 and z['max_core_gap_d']<max(3*cad,dur*.2))
   else:z['coverage_adequate']=False
   tests.append(z)
 out[tic]=dict(assumed_period_d=p,proxy_epoch_btjd=c,assumed_duration_d=dur,tests=tests,note='Conditional Gaia-period recurrence anchored to representative event; not a measured eclipse period. No blanket null verdict: long-baseline ephemeris drift, uncertain event kind and noise can invalidate exact predicted windows. Missing/flagged windows are not nulls.')
(b/'lead-single-conditional-coverage.json').write_text(json.dumps(out,indent=2));print('recorded',len(out))
