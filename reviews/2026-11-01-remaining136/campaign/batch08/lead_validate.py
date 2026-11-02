from pathlib import Path
import csv,json,hashlib,numpy as np
B=Path(__file__).parent;res=list(csv.DictReader(open(B/'RESULTS.csv')));tg=json.load(open(B.parent/'targets-selected.json'));ns={r['source_id']:r for r in csv.DictReader(open(B.parent/'shared-catalogues/gaia-nss-full.csv'))};receipts=[];checks=[]
for r in res:
 tic=r['tic'];m=json.load(open(B/tic/'measurements.json'));ev=[e for e in m['events'] if e.get('timing_usable')];n=np.array([e['cycle'] for e in ev]);tt=np.array([e['mid_btjd'] for e in ev]);er=np.array([e['timing_error_days'] for e in ev]);X=np.array([np.ones(len(n)),n-n.min()]).T;co=np.linalg.inv((X/er[:,None]).T@(X/er[:,None]));beta=co@((X/er[:,None]).T@(tt/er));red=sum(((tt-X@beta)/er)**2)/(len(tt)-2) if len(tt)>2 else None;co*=max(red or 1,1)
 assert abs(beta[0]-m['primary_epoch_btjd'])<1e-8 and abs(beta[1]-m['period_days'])<1e-9
 for key in ['period_days','period_error_days','primary_epoch_btjd','depth_ppt']:assert float(r[key])==m[key]
 z=ns[str(tg[tic]['gaia']['source_id'])];C=np.eye(6);vv=list(map(float,z['corr_vec'].strip('{}[]()').split(',')));k=0
 for i in range(1,6):
  for j in range(i):C[i,j]=C[j,i]=vv[k];k+=1
 eig=np.linalg.eigvalsh(C);assert min(eig)>0
 checks.append(dict(tic=tic,independent_ephemeris_recompute=True,gaia_correlation_minimum_eigenvalue=float(min(eig)),events=len(ev),same_sector_consecutive_cycle=bool(any(a['sector']==b['sector'] and b['cycle']-a['cycle']==1 for a,b in zip(ev,ev[1:])))))
 receipts+=m['sources']
json.dump(receipts,open(B/'measurement-source-receipts.json','w'),indent=2);json.dump(checks,open(B/'lead-numeric-check.json','w'),indent=2)
H=json.load(open(B/'source-hashes.json'))
for p in [B/'diffstack-primitive.py',B/'methods-snapshot.html',B.parent/'shared-catalogues/297956126-mast-availability.json']:H[str(p)]=hashlib.sha256(p.read_bytes()).hexdigest()
json.dump(H,open(B/'source-hashes.json','w'),indent=2)
