from pathlib import Path
import csv,json,numpy as np
from scipy.ndimage import median_filter
D=Path(__file__).resolve().parent;z=np.load(D/'cadences/187261476-59.npz');t=z['t'];f=z['pdc'];mask=np.isfinite(f)&(f>0);t=t[mask];f=f[mask]/np.median(f[mask])
def read(p,e,ph=0):
 result=[]
 for k in range(-2,26):
  tc=e+(k+ph)*p
  if 2916.9<tc<2918.6:continue
  dt=t-tc;left=(dt>-.18)&(dt<-.10);right=(dt>.10)&(dt<.18);inner=abs(dt)<.095
  if min(left.sum(),right.sum())<6 or inner.sum()<30:continue
  b=np.interp(dt[inner],[np.median(dt[left]),np.median(dt[right])],[np.median(f[left]),np.median(f[right])]);res=(1-f[inner]/b)*1000
  dep=np.percentile(res,96);wt=np.maximum(0,res-dep*.25)
  if wt.sum()==0:continue
  center=np.average(t[inner],weights=wt);width=np.ptp(t[inner][res>dep*.50])*24
  result.append(dict(cycle=k,center_btjd=float(center),depth_ppt=float(dep),width_h=float(width)))
 return result
p=1.180;e=2912.2142
for _ in range(4):
 pri=read(p,e);p,e=np.polyfit([r['cycle'] for r in pri],[r['center_btjd'] for r in pri],1)
sec=read(p,e,.5)
print(p,e,len(pri),'median width',np.median([r['width_h'] for r in pri]),'depth',np.median([r['depth_ppt'] for r in pri]),'r90',np.percentile([abs(r['center_btjd']-e-r['cycle']*p)*1440 for r in pri],90))
print('secondary',[(round(r['depth_ppt'],1),round((r['center_btjd']-e)/p-r['cycle'],3)) for r in sec])
out=dict(tic='187261476',sector=59,ephemeris='recurrence of deep marks on short cycle',epoch_btjd=e,period_days=p,primaries=pri,opposite_phase_extractions=sec)
(D/'187261476-clock.json').write_text(json.dumps(out,indent=1))
