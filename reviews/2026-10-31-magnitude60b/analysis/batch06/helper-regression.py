import json,glob,numpy as np,hashlib,pathlib
B=pathlib.Path('[local path omitted]')
rows=[]
for p in sorted(B.glob('*/measurements.json')):
 m=json.loads(p.read_text()); es=[e for e in m['events'] if e.get('timing_usable')]; x=np.array([e.get('orbital_cycle',e['cycle']) for e in es],float); y=np.array([e['mid_btjd'] for e in es]); s=np.array([e['timing_error_days'] for e in es]); x-=x.min(); w=1/s**2; xm=np.sum(w*x)/sum(w); ym=np.sum(w*y)/sum(w); slope=sum(w*(x-xm)*(y-ym))/sum(w*(x-xm)**2); intercept=ym-slope*xm; red=sum(((y-intercept-slope*x)/s)**2)/max(1,len(x)-2); err=(1/sum(w*(x-xm)**2))**.5*max(1,red)**.5
 rows.append(dict(tic=m['tic'],n=len(es),period=slope,error=err,epoch=intercept,delta_period=slope-m['period_days'],delta_error=err-m['period_error_days'],delta_epoch=intercept-m['primary_epoch_btjd'],sha256=hashlib.sha256(p.read_bytes()).hexdigest()))
assert all(abs(r['delta_period'])<1e-9 and abs(r['delta_error'])<1e-9 and abs(r['delta_epoch'])<1e-7 for r in rows)
(B/'helper-regression.json').write_text(json.dumps(rows,indent=2))
for r in rows: print(r['tic'],r['n'],f"{r['period']:.10f}",f"{r['error']:.10g}",f"{r['epoch']:.8f}")
