import json,csv,hashlib
from pathlib import Path
import numpy as np
from scipy.optimize import least_squares
B=Path('[local path omitted]')
rows=list(csv.DictReader(open(B/'queue.csv'))); out=[]
for row in rows:
 t=row['tic']; m=json.load(open(B/t/'measurements.json')); w=list(csv.DictReader(open(B/t/'raw-windows.csv'))); ev=[e for e in m['events'] if e.get('timing_usable') and (t!='309558046' or e['cycle']%2==0)]; dif=[]
 for e in ev:
  a=[q for q in w if int(q['sector'])==e['sector'] and int(q['cycle'])==e['cycle']]; x=np.array([float(q['btjd'])-e['predicted_btjd'] for q in a]); y=np.array([float(q['normalized_raw_sap']) for q in a]); d=m['search_duration_days']
  def residual(p):
   b,s,depth,c,width,ingress=p; return b+s*x-depth*np.clip((width/2-np.abs(x-c))/ingress,0,1)-y
  res=least_squares(residual,[1,0,e['depth_ppt']/1000,e['fit_shift_days'],e['duration_days'],d*.2],bounds=([.7,-1,0,-d,.3*d,.01*d],[1.3,1,1,d,3*d,1.4*d]),xtol=1e-12,ftol=1e-12,gtol=1e-12,max_nfev=30000)
  dif.append(float(res.x[3]-e['fit_shift_days']))
 n=np.array([e.get('orbital_cycle',e['cycle']) for e in ev],float); tt=np.array([e['mid_btjd'] for e in ev]); er=np.array([e['timing_error_days'] for e in ev]); origin=n.min(); X=np.column_stack((np.ones(len(n)),n-origin)); beta=np.linalg.lstsq(X/er[:,None],tt/er,rcond=None)[0]; cov=np.linalg.inv((X/er[:,None]).T@(X/er[:,None])); chi=float(np.sum(((tt-X@beta)/er)**2)/max(len(n)-2,1)); pe=float(np.sqrt(cov[1,1]*max(chi,1)))
 out.append(dict(tic=t,events=len(ev),period_refit=float(beta[1]),period_delta=float(beta[1]-m['period_days']),error_refit=pe,error_delta=pe-m['period_error_days'],epoch_refit=float(beta[0]),epoch_delta=float(beta[0]-m['primary_epoch_btjd']),max_event_center_refit_delta_days=max(map(abs,dif)),max_timing_error_floor_discrepancy=max(abs(e['timing_error_days']-max(e['formal_timing_error_days'],e['cadence_days']/2)) for e in ev),measurement_sha256=hashlib.sha256((B/t/'measurements.json').read_bytes()).hexdigest(),windows_sha256=hashlib.sha256((B/t/'raw-windows.csv').read_bytes()).hexdigest()))
json.dump(out,open(B/'helper-numerical-audit.json','w'),indent=2)
print(json.dumps(out,indent=2))
