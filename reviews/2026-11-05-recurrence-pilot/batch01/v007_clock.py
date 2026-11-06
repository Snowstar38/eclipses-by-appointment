"""V007 measured-event clock and bounded shorter-cycle coverage diagnostics."""
from pathlib import Path
import json,hashlib
import numpy as np
from astropy.io import fits
B=Path(__file__).resolve().parent
tic='147413927'
H=B.parent.parent/'binary-exploration-2026-11-04'/'bulk-results'
bulk=json.loads((H/f'{tic}.json').read_text())
events=np.array([1546.413,1590.499,2317.923,3023.369,3750.813,3772.869,4081.434])
cycles=np.rint((events-events[0])/22.04).astype(int)
p=np.polyfit(cycles,events,1)
res=events-np.polyval(p,cycles)
out={'event_centers_btjd':events.tolist(),'cycle_numbers':cycles.tolist(),'linear_period_days':float(p[0]),'linear_epoch_btjd':float(p[1]),'residual_days':res.tolist(),'note':'Event centers are provisional local fits, not independent precision timing errors.'}
rec=next(x for x in bulk['files'] if x['sector']==90)
path=Path(rec['path']);assert hashlib.sha256(path.read_bytes()).hexdigest()==rec['sha256']
with fits.open(path,memmap=False) as h:
 assert str(int(h[0].header['TICID']))==tic
 a=h[1].data;t=np.asarray(a['TIME'],float);f=np.asarray(a['SAP_FLUX'],float);q=np.asarray(a['QUALITY'],int)
ok=np.isfinite(t)&np.isfinite(f)&(f>0)&(q==0);t=t[ok];f=f[ok]
cad=float(np.median(np.diff(t)));out['s90_source_sha256']=rec['sha256'];out['s90_cadence_days']=cad
checks=[]
for divisor in [2,3,4]:
 step=p[0]/divisor
 for j in range(1,divisor):
  for anchor in [3750.813,3772.869]:
   c=anchor+j*step
   if c>t.max():continue
   core=abs(t-c)<.12;side=(abs(t-c)>.3)&(abs(t-c)<.8)
   ct=t[core];st=t[side]
   core_gap=float(np.max(np.diff(ct))) if len(ct)>1 else None
   left=np.sum((t>c-.8)&(t<c-.3));right=np.sum((t>c+.3)&(t<c+.8))
   depth=float((np.median(f[side])-np.median(f[core]))/np.median(f[side])) if len(ct)>3 and left>10 and right>10 else None
   checks.append({'divisor':divisor,'anchor_btjd':anchor,'predicted_btjd':float(c),'core_n':int(len(ct)),'core_first':float(ct.min()) if len(ct) else None,'core_last':float(ct.max()) if len(ct) else None,'core_max_gap_days':core_gap,'side_left_n':int(left),'side_right_n':int(right),'sap_depth_fraction':depth,'sensitive_core':bool(len(ct)>=.7*(.24/cad) and core_gap is not None and core_gap<3*cad and left>10 and right>10)})
out['shorter_cycle_checks']=checks
(B/'v007-clock.json').write_text(json.dumps(out,indent=2)+'\n')
print('period',p,'residual',res,'checks',[(x['divisor'],round(x['predicted_btjd'],3),x['sensitive_core'],x['sap_depth_fraction']) for x in checks])
