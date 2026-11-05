"""Inspect F032 44/43-cycle alias and its later-sector predicted null."""
from pathlib import Path
import json, hashlib
import numpy as np
from astropy.io import fits
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

B=Path(__file__).resolve().parent
D=json.loads((B/'51321183'/'lead-measurements.json').read_text())
E=D['screen_flagged_dips']
t1,t2,t3=[E[i]['measured_center_btjd'] for i in (0,1,2)]
p1=(t2-t1)/44
p2=(t3-t2)/43
p=(t3-t1)/87
pred=t3+21*p
src=next(x for x in D['source_receipts'] if x['sector']==99)
fp=Path(src['path']);assert hashlib.sha256(fp.read_bytes()).hexdigest()==src['sha256']
with fits.open(fp,memmap=False) as h:
 a=h[1].data;t=np.array(a['TIME'],float);f=np.array(a['SAP_FLUX'],float);q=np.array(a['QUALITY'],int)
ok=np.isfinite(t)&np.isfinite(f)&(f>0)&(q==0);t=t[ok];f=f[ok]
fig,ax=plt.subplots(figsize=(10,4));sel=abs(t-pred)<2
ax.plot(t[sel]-pred,f[sel]/np.median(f[sel]),'.',ms=2)
ax.axvspan(-.1,.1,color='red',alpha=.15);ax.set_title(f'F032 S99 predicted eclipse {pred:.4f}; P {p:.6f} d')
fig.tight_layout();fig.savefig(B/'51321183'/'lead-alias-null.png',dpi=150)
edge=sel&(abs(t-pred)>.25)
core=abs(t-pred)<.09
out=dict(timing_btjd=[t1,t2,t3],cycle_counts=[44,43],pair_periods_days=[p1,p2],long_span_period_days=p,predicted_s99_btjd=pred,source_sha256=src['sha256'],s99_core_n=int(core.sum()),s99_core_minmax=[float(t[core].min()),float(t[core].max())] if core.any() else None,s99_core_relative_median=float(np.median(f[core])/np.median(f[edge])-1) if core.any() and edge.any() else None,s99_gaps_over_0p2=D['coverage'][-1]['gaps_over_0p2_days'])
(B/'51321183'/'lead-alias-null.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
aliases=[]
for k in range(1,6):
 period=p/k; checks=[]
 for rec in D['source_receipts']:
  sec=rec['sector']; fpath=Path(rec['path']);assert hashlib.sha256(fpath.read_bytes()).hexdigest()==rec['sha256']
  with fits.open(fpath,memmap=False) as h:
   a=h[1].data;time=np.array(a['TIME'],float);flux=np.array(a['SAP_FLUX'],float);quality=np.array(a['QUALITY'],int)
  good=np.isfinite(time)&np.isfinite(flux)&(flux>0)&(quality==0);time=time[good];flux=flux[good]
  for n in range(-100,200):
   center=t1+n*period
   if center<time.min()+.5 or center>time.max()-.5:continue
   core=abs(time-center)<.06; shoulders=(abs(time-center)>.16)&(abs(time-center)<.35)
   if core.sum()<6 or shoulders.sum()<15:continue
   baseline=np.median(flux[shoulders]);depth=(1-np.median(flux[core])/baseline)*1000
   checks.append(dict(sector=sec,n=n,center_btjd=float(center),core_n=int(core.sum()),core_first_last=[float(time[core].min()),float(time[core].max())],depth_ppt=float(depth)))
 aliases.append(dict(divisor=k,period_days=float(period),checks=checks))
(B/'51321183'/'lead-alias-grid.json').write_text(json.dumps(aliases,indent=2)+'\n')
print('aliases:',[(a['divisor'],[(x['sector'],round(x['center_btjd'],3),round(x['depth_ppt'],2)) for x in a['checks']]) for a in aliases])
adjacent=[]
for n1 in range(40,49):
 for n2 in range(39,48):
  q1=(t2-t1)/n1;q2=(t3-t2)/n2
  adjacent.append(dict(cycles=[n1,n2],periods_days=[float(q1),float(q2)],difference_days=float(q1-q2)))
adjacent.sort(key=lambda x:abs(x['difference_days']))
(B/'51321183'/'lead-adjacent-cycle-check.json').write_text(json.dumps(adjacent,indent=2)+'\n')
print('best adjacent:',adjacent[:8])
