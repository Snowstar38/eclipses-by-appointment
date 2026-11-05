"""Selected same-kind raw SAP timing, with explicit event cycles."""
import csv, json
from pathlib import Path
import numpy as np

B=Path(__file__).resolve().parent
spec={
 'T081':('short-period A',10.518,[1474.787,1485.304,2211.063,2221.582,3673.099]),
 'T082':('short-period A',16.204,[1577.438,1593.642,2322.823,2339.027,2355.231,3052.003,4089.059,4105.262,4121.465]),
 'T083':('B',24.655,[3721.493,3746.148]),
 'T084':('A',32.807,[2521.286,3243.049]),
 'T086':('A',58.732,[1666.212,2370.990,3134.499,3839.277]),
 'T087':('A',26.535,[2135.654,2162.187,3939.892,3966.425]),
 'T089':('A',29.749,[1663.769,2050.508,3151.224,3865.202,4103.193,4162.691]),
 'T090':('short-period A',3.209,[1843.974,1847.183,1853.601,1860.041,2582.021,2585.230,2588.439,2601.274,2941.418,2944.627,2947.836,3291.188,3297.605,3307.233,3310.441,3320.068,3323.276,3326.485]),
}
out=[]
for row in csv.DictReader((B/'queue.csv').open()):
 sid=row['sample_id']; tic=row['tic']; m=json.loads((B/tic/'lead-numeric.json').read_text())
 if sid not in spec:
  out.append(dict(sample_id=sid,tic=tic,status='no Gaia-near reliable repeated same-kind centers selected'))
  continue
 kind,trial,seeds=spec[sid]; events=[]
 for seed in seeds:
  matches=sorted(m['events'],key=lambda e:abs(e.get('fit_mid_btjd',0)-seed));e=matches[0]
  assert abs(e['fit_mid_btjd']-seed)<.003,(sid,seed,e['fit_mid_btjd'])
  events.append(e)
 t=np.array([e['fit_mid_btjd'] for e in events]);cycles=np.rint((t-t[0])/trial).astype(int)
 assert len(set(cycles))==len(cycles)
 cad={s['sector']:s['cadence_days'] for s in m['coverage']}
 sig=np.array([max(e.get('fit_mid_formal_error_days') or 0,cad[e['sector']]/2) for e in events])
 X=np.array([np.ones(len(t)),cycles]).T;w=1/sig**2
 cov=np.linalg.inv(X.T@(w[:,None]*X));beta=cov@(X.T@(w*t));res=t-X@beta
 chi=float(np.sum((res/sig)**2));dof=len(t)-2; inflation=max(1,np.sqrt(chi/dof)) if dof else 1
 rec=dict(sample_id=sid,tic=tic,kind=kind,trial_period_days=trial,epoch_btjd=float(beta[0]),period_days=float(beta[1]),conditional_formal_period_error_days=float(np.sqrt(cov[1,1])*inflation),chi2=chi,dof=dof,scatter_inflation=float(inflation),events=[dict(sector=e['sector'],mid_btjd=float(mid),cycle=int(cyc),timing_floor_days=float(s),residual_days=float(rr),fit_depth_ppt=e['fit_depth_ppt']) for e,mid,cyc,s,rr in zip(events,t,cycles,sig,res)],caution='Conditional selected-event fit. Two-event periods require alias tests. Source-specific fit errors are not universal acceptance cuts.')
 out.append(rec)
 print(sid,round(rec['period_days'],7),round(rec['conditional_formal_period_error_days'],7),round(max(abs(res)),4),cycles.tolist(),flush=True)
(B/'lead-timing.json').write_text(json.dumps(out,indent=2)+'\n')
