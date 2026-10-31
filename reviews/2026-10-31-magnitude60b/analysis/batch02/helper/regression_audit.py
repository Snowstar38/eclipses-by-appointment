import pathlib,json,numpy as np,math,hashlib
p=pathlib.Path(__file__).resolve().parent.parent
rows=[]
for f in sorted(p.glob('*/measurements.json')):
 j=json.loads(f.read_text(encoding='utf-8'));
 if 'period_days' not in j: continue
 es=[e for e in j['events'] if e['timing_usable'] and (not j.get('timing_selection') or 'orbital_cycle' in e)]; ks=np.array([e.get('orbital_cycle',e['cycle']) for e in es],float); y=np.array([e['mid_btjd'] for e in es]); sig=np.array([e['timing_error_days'] for e in es]); a=np.column_stack([np.ones(len(ks)),ks-ks.min()]); w=1/sig**2; cov=np.linalg.inv(a.T@(w[:,None]*a)); beta=cov@(a.T@(w*y)); chi=sum(((y-a@beta)/sig)**2)/max(len(y)-2,1); err=math.sqrt(cov[1,1]*max(1,chi));
 rows.append(dict(tic=j['tic'],sha256=hashlib.sha256(f.read_bytes()).hexdigest(),n=len(es),reported_n=j['timing_event_count'],period_difference_days=beta[1]-j['period_days'],epoch_difference_days=beta[0]-j['primary_epoch_btjd'],error_difference_days=err-j['period_error_days'],reduced_chi=chi,selected_parities=sorted(set(e['cycle']%2 for e in es)),unusable_n=sum(not e['timing_usable'] for e in j['events'])))
(p/'helper'/'regression-audit.json').write_text(json.dumps(rows,indent=2),encoding='utf-8')

