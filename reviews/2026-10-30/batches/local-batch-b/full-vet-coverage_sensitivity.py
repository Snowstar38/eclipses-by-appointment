import pathlib,json,numpy as np
r=pathlib.Path(__file__).parent
for path in r.glob('*_measurements.json'):
 d=json.loads(path.read_text());ev=[e for e in d['events'] if e['coverage_ok'] and e['depth']/e['depth_error']>4];strict=[e for e in ev if e['max_in_event_gap_d'] is not None and e['max_in_event_gap_d'] <= 2.1*e['cadence_d'] and e['in_count']*e['cadence_d']/e['T14_d']>=.6];out={'original_n':len(ev),'strict_n':len(strict)}
 if len(strict)>2:
  k=np.array([e['cycle'] for e in strict]);t=np.array([e['tc'] for e in strict]);s=np.array([e['tc_error_d'] for e in strict]);mid=int(np.median(k));X=np.column_stack([np.ones(len(k)),k-mid]);W=1/s**2;cov=np.linalg.inv(X.T@(W[:,None]*X));b=cov@(X.T@(W*t));out.update(P=float(b[1]),T0=float(b[0]),cycle=mid)
 for e in d['events']:
  e['width_profile_grid_limited']= e['T14_profile_d'][0]==e['T14_profile_d'][1];e['contact_profile_boundary']=e['T12_profile_d'][0]<=.15*e['T14_d']+.001 or e['T12_profile_d'][1]>=.5*e['T14_d']-.001
 (r/(d['tic']+'_coverage_sensitivity.json')).write_text(json.dumps(out,indent=2));path.write_text(json.dumps(d,indent=2));print(d['tic'],out)
