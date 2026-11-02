from pathlib import Path
import json,csv,hashlib,numpy as np
b=Path(__file__).parent;rows=list(csv.DictReader(open(b/'RESULTS.csv')));out=[]
for r in rows:
 tic=r['tic'];m=json.load(open(b/tic/'measurements.json'));d=json.load(open(b/tic/'fresh-pixels/diff_fresh.json'));ev=[e for e in m['events'] if e.get('timing_usable')];n=np.array([e.get('orbital_cycle',e['cycle']) for e in ev]);x=n-n.min();t=np.array([e['mid_btjd'] for e in ev]);err=np.array([e['timing_error_days'] for e in ev]);X=np.column_stack((np.ones(len(x)),x));beta=np.linalg.lstsq(X/err[:,None],t/err,rcond=None)[0];cov=np.linalg.inv((X/err[:,None]).T@(X/err[:,None]));red=float(sum(((t-X@beta)/err)**2)/(len(t)-2)) if len(t)>2 else None;perr=np.sqrt(cov[1,1]*max(red or 1,1))
 assert abs(beta[1]-m['period_days'])<1e-9 and abs(beta[0]-m['primary_epoch_btjd'])<1e-8
 assert np.isclose(perr,m['period_error_days'],rtol=1e-6)
 for e in ev:assert np.isclose(e['depth_ppt'],e['extrapolated_amplitude_ppt']*min(1,e['duration_days']/(2*e['ingress_parameter_days'])))
 assert np.isclose(np.median([e['depth_ppt'] for e in ev]),m['depth_ppt'])
 for k in ['period_days','period_error_days','primary_epoch_btjd','depth_ppt']:assert float(r[k])==m[k]
 for nb in d['neighbours_60']:
  f=10**(-.4*(nb['G']-d['target_G']));need=m['depth_ppt']/1000*(1+f)/f;assert np.isclose(need,nb['depth_needed'])
 for s in m['sources']:assert hashlib.sha256(Path(s['path']).read_bytes()).hexdigest()==s['sha256']
 out.append(dict(tic=tic,n_timings=len(ev),period_recomputed_days=float(beta[1]),period_error_recomputed_days=float(perr),realized_depth_and_neighbour_thresholds_verified=True))
(b/'lead-numeric-check.json').write_text(json.dumps(out,indent=2))
print('Verified',len(out),'targets')
