import json,csv,pathlib,numpy as np
b=pathlib.Path(__file__).resolve().parent.parent
rows={r['tic']:r for r in csv.DictReader(open(b/'RESULTS.csv'))}
out={}
for t,r in rows.items():
 m=json.load(open(b/t/'measurements.json')); ev=[e for e in m['events'] if e.get('timing_usable')]; x=np.array([e['cycle']-m['epoch_cycle'] for e in ev],float); y=np.array([e['mid_btjd'] for e in ev]); s=np.array([e['timing_error_days'] for e in ev]); X=np.column_stack((np.ones(len(x)),x)); A=X/s[:,None]; z=y/s; v=np.linalg.inv(A.T@A); beta=np.linalg.solve(A.T@A,A.T@z); chi=float(np.sum(((y-X@beta)/s)**2)/(len(x)-2)); err=float(np.sqrt(v[1,1]*max(1,chi)))
 assert abs(beta[1]-float(r['period_days']))<1e-9 and abs(err-float(r['period_error_days']))<1e-9 and abs(beta[0]-float(r['primary_epoch_btjd']))<1e-7
 assert abs(np.median([e['depth_ppt'] for e in ev])-float(r['depth_ppt']))<1e-9
 assert all(abs(e['timing_error_days']-max(e['formal_timing_error_days'],e['cadence_days']/2))<1e-9 for e in ev)
 out[t]={'events':len(m['events']),'usable':len(ev),'period_days':float(beta[1]),'error_days':err,'epoch_btjd':float(beta[0]),'reduced_chi_square':chi,'median_used_depth_ppt':float(np.median([e['depth_ppt'] for e in ev])),'excluded':[(e['sector'],e['cycle']) for e in m['events'] if not e.get('timing_usable')]}
print(json.dumps(out,indent=2))
