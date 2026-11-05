"""Bounded same-kind timing fits to selected raw SAP local events.

Selections are explicit and visually checked; omitted retained windows include
opposite eclipse kinds, stellar structure, gaps, and shallow false detections.
"""
import csv, json
from pathlib import Path
import numpy as np

B=Path(__file__).resolve().parent
spec={
 'T073':('B',24.592,[1374.089,3931.673,4202.187]),
 'T074':('A',22.4506,[1783.059,2860.689,3601.559]),
 'T075':('A',30.092,[2182.435,2212.527,3687.036]),
 'T076':('A',26.46,[1346.121,1663.633,3145.362,3833.307,3859.767,3886.226]),
 'T077':('A',14.2915,[2469.622,2855.489,2869.781]),
 'T078':('A',44.9244,[2020.308,2604.324,3323.115]),
 'T079':('A',44.3838,[1355.245,1488.395,1577.163,1621.546,2065.382,2109.765,2198.533,2287.300,2331.684,2997.438,3041.821,3130.589,3707.576,3751.959,3885.110,3929.493]),
 'T080':('A',43.142,[2881.158,1975.170,3398.852]),
}
out=[]
for row in csv.DictReader((B/'queue.csv').open()):
 sid=row['sample_id']; tic=row['tic']; m=json.loads((B/tic/'lead-numeric.json').read_text())
 if sid not in spec:
  out.append(dict(sample_id=sid,tic=tic,status='no reliable repeated same-kind centers selected'))
  continue
 kind,trial,seeds=spec[sid]; events=[]
 for seed in seeds:
  matches=sorted(m['events'],key=lambda e:abs(e.get('fit_mid_btjd',0)-seed))
  e=matches[0]; assert abs(e['fit_mid_btjd']-seed)<.003,(sid,seed,e['fit_mid_btjd'])
  events.append(e)
 t=np.array([e['fit_mid_btjd'] for e in events]); cycles=np.rint((t-t[0])/trial).astype(int)
 assert len(set(cycles))==len(cycles),(sid,cycles)
 # Trapezoid covariance is optimistic when ingress is noisy or partly gapped.
 # Floor by half the data cadence and inflate for observed timing scatter.
 cad={s['sector']:s['cadence_days'] for s in m['coverage']}
 sig=np.array([max(e.get('fit_mid_formal_error_days') or 0,cad[e['sector']]/2) for e in events])
 X=np.array([np.ones(len(t)),cycles]).T
 w=1/sig**2; cov=np.linalg.inv(X.T@(w[:,None]*X)); beta=cov@(X.T@(w*t));res=t-X@beta
 chi=float(np.sum((res/sig)**2)); dof=len(t)-2; inflation=max(1,np.sqrt(chi/dof)) if dof else 1
 rec=dict(sample_id=sid,tic=tic,kind=kind,trial_period_days=trial,epoch_btjd=float(beta[0]),period_days=float(beta[1]),conditional_formal_period_error_days=float(np.sqrt(cov[1,1])*inflation),chi2=chi,dof=dof,scatter_inflation=float(inflation),events=[dict(sector=e['sector'],mid_btjd=float(mid),cycle=int(cyc),timing_floor_days=float(s),residual_days=float(rr),fit_depth_ppt=e['fit_depth_ppt'],quality0_core_n=e['quality0_core_n']) for e,mid,cyc,s,rr in zip(events,t,cycles,sig,res)],caution='Conditional selected-event linear fit; cycle numbers and eclipse kind chosen by visually checked raw profiles and Gaia-near trial. Formal error plus scatter inflation is not calibrated systematics or exhaustive aliases.')
 out.append(rec);print(sid,kind,round(rec['period_days'],7),round(rec['conditional_formal_period_error_days'],7),round(max(abs(res)),4),cycles.tolist(),flush=True)
(B/'lead-timing.json').write_text(json.dumps(out,indent=2)+'\n')
