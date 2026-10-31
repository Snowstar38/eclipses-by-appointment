import json,csv,hashlib
from pathlib import Path
import numpy as np
B=Path(__file__).resolve().parent.parent
out={}
for row in csv.DictReader(open(B/'queue.csv')):
 t=row['tic']; m=json.load(open(B/t/'measurements.json')); ev=[e for e in m['events'] if 'mid_btjd' in e]
 if t=='343926224': ev=[e for e in ev if e['cycle'] not in (154,176)]
 if t in ('397178704','7446763'): ev=[e for e in ev if e['cycle']%2==1]
 n=np.array([e.get('orbital_cycle',e['cycle']) for e in ev],float); y=np.array([e['mid_btjd'] for e in ev]); s=np.array([e['timing_error_days'] for e in ev]); x=n-n.min(); w=1/s**2; p=np.sum(w*(x-np.average(x,weights=w))*(y-np.average(y,weights=w)))/np.sum(w*(x-np.average(x,weights=w))**2); a=np.average(y-p*x,weights=w); chi=np.sum(((y-a-p*x)/s)**2)/max(len(y)-2,1); err=np.sqrt(max(chi,1)/np.sum(w*(x-np.average(x,weights=w))**2))
 d=json.load(open(next((B/t/'historical').glob('diff_*.json')))); cand=[z for z in d['neighbours_60'] if z['possible']]; out[t]={'n':len(ev),'period':p,'period_error':err,'epoch':a,'difference':p-m['period_days'],'chi2_reduced':chi,'capable':len(cand),'neighbor_ids':[z['source_id'] for z in cand]}
files=[B/'review_measure.py',B/'314041837/harmonic-test.png',B/'314041837/harmonic-test.json',B/'343926224/raw-events.png',B/'62940616/historical/diff_s46.json',B/'62940616/historical/diff_s46.png',Path('[local path omitted]')]
result={'checks':out,'sha256':{str(p):hashlib.sha256(p.read_bytes()).hexdigest() for p in files}}
(B/'helper'/'audit-numeric.json').write_text(json.dumps(result,indent=2))
print(json.dumps(result,indent=2))
