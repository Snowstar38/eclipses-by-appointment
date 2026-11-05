"""Conditional selected-event clocks by eclipse kind, with explicit cycles."""
import csv,json
from pathlib import Path
import numpy as np
B=Path(__file__).resolve().parent
spec={
 'T091':('deep',48.54,[2001.0008,2729.0102,3311.4182,3457.0186]),
 'T093':('deep',56.25,[2312.9773,3044.2421]),
 'T096':('deep',34.11,[1455.3169,2478.5706,3228.9576]),
 'T098':('deep',34.78,[1795.4125,2908.5573]),
 'T099':('deep',28.79,[1822.7651,2916.8088,3291.0574]),
 'T100':('narrow',0.6793,[2231.2842,2236.0406,2237.3993,2248.2674,2977.0231,2979.0604,2981.0976,3706.4598,3713.2529,3716.6494]),
}
out=[]
for row in csv.DictReader((B/'queue.csv').open()):
 sid=row['sample_id'];tic=row['tic'];m=json.loads((B/tic/'lead-numeric.json').read_text())
 if sid not in spec:
  out.append(dict(sample_id=sid,tic=tic,status='No reliable three-or-more same-kind timing set selected; see alias audit.'))
  continue
 kind,trial,seeds=spec[sid];events=[]
 for seed in seeds:
  e=min(m['events'],key=lambda x:abs(x['fit_mid_btjd']-seed));assert abs(e['fit_mid_btjd']-seed)<.004,(sid,seed,e['fit_mid_btjd']);events.append(e)
 t=np.array([e['fit_mid_btjd'] for e in events]);cycles=np.rint((t-t[0])/trial).astype(int)
 assert len(set(cycles))==len(cycles)
 cad={s['sector']:s['cadence_days'] for s in m['coverage']}
 sig=np.array([max(e.get('fit_mid_formal_error_days') or 0,cad[e['sector']]/2) for e in events])
 X=np.array([np.ones(len(t)),cycles]).T;w=1/sig**2
 cov=np.linalg.inv(X.T@(w[:,None]*X));beta=cov@(X.T@(w*t));res=t-X@beta
 chi=float(np.sum((res/sig)**2));dof=len(t)-2;inflation=max(1,np.sqrt(chi/dof)) if dof else 1
 rec=dict(sample_id=sid,tic=tic,kind=kind,trial_period_days=trial,epoch_btjd=float(beta[0]),period_days=float(beta[1]),conditional_formal_period_error_days=float(np.sqrt(cov[1,1])*inflation),chi2=chi,dof=dof,scatter_inflation=float(inflation),events=[dict(sector=e['sector'],mid_btjd=float(mid),cycle=int(cyc),timing_floor_days=float(s),residual_days=float(rr),fit_depth_ppt=e['fit_depth_ppt']) for e,mid,cyc,s,rr in zip(events,t,cycles,sig,res)],caution='Conditional selected-event fit. Alias coverage and morphology separately assessed. Formal errors do not include cycle ambiguity or extraction systematics.')
 out.append(rec);print(sid,rec['period_days'],rec['conditional_formal_period_error_days'],max(abs(res)),cycles.tolist(),flush=True)
(B/'lead-timing.json').write_text(json.dumps(out,indent=2)+'\n')
