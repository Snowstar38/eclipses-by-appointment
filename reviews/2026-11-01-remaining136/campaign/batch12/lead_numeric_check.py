from pathlib import Path
import json,csv,hashlib,numpy as np
b=Path(__file__).parent;out=[]
rows=list(csv.DictReader(open(b/'RESULTS.csv')));assert [r['tic'] for r in rows]==[r['tic'] for r in csv.DictReader(open(b/'queue.csv'))]
for r in rows:
 t=r['tic'];m=json.load(open(b/t/'measurements.json'));ev=[e for e in m['events'] if e.get('timing_usable')];n=np.array([e.get('orbital_cycle',e['cycle']) for e in ev]);er=np.array([e['timing_error_days'] for e in ev]);tt=np.array([e['mid_btjd'] for e in ev]);X=np.column_stack([np.ones(len(n)),n-n.min()]);C=np.linalg.inv((X/er[:,None]).T@(X/er[:,None]));beta=C@((X/er[:,None]).T@(tt/er));res=tt-X@beta;chi=float(sum((res/er)**2)/(len(n)-2)) if len(n)>2 else None;C*=max(chi or 1,1)
 for k,v in [('period_days',beta[1]),('primary_epoch_btjd',beta[0]),('period_error_days',np.sqrt(C[1,1])),('epoch_error_days',np.sqrt(C[0,0])),('depth_ppt',np.median([e['depth_ppt'] for e in ev]))]:assert np.isclose(m[k],v,rtol=1e-11,atol=1e-12),(t,k,m[k],v)
 for e in ev:assert np.isclose(e['depth_ppt'],e['extrapolated_amplitude_ppt']*min(1,e['duration_days']/(2*e['ingress_parameter_days'])))
 for k in ['period_days','period_error_days','primary_epoch_btjd','depth_ppt']:assert float(r[k])==m[k]
 assert (chi is None and m['reduced_chi_square'] is None) or np.isclose(m['reduced_chi_square'],chi,rtol=1e-10)
 d=json.load(open(b/t/'fresh-pixels/diff_fresh.json'));g=json.load(open(b/t/'fresh-pixels/gaia.json'));target=g['src'][0];
 for nb in d['neighbours_60']:
  expected=m['depth_ppt']/1000*(1+10**(.4*(nb['G']-float(target['phot_g_mean_mag']))))
  assert np.isclose(nb['depth_needed'],expected,rtol=1e-8),(t,nb['source_id'])
 out.append(dict(tic=t,timings=len(ev),chi_square_dof=len(ev)-2,ephemeris_recomputed=True,realized_depth_checked=True,neighbor_thresholds_checked=True))
json.dump(out,open(b/'lead-numeric-check.json','w'),indent=2)
print('Verified',len(out))
