import csv,json,numpy as np
from pathlib import Path
rows=list(csv.DictReader(open('RESULTS.csv')));out={}
for r in rows:
 m=json.load(open(Path(r['tic'])/'measurements.json')); good=[e for e in m['events'] if e.get('timing_usable') and (r['tic'] not in ('254723054','388052602') or e['cycle']%2 == (0 if r['tic']=='254723054' else 1))]; n=np.array([e.get('orbital_cycle',e['cycle']) for e in good]);t=np.array([e['mid_btjd'] for e in good]);s=np.array([e['timing_error_days'] for e in good]); x=np.column_stack([np.ones(len(n)),n-min(n)]);b=np.linalg.lstsq(x/s[:,None],t/s,rcond=None)[0];cov=np.linalg.inv((x/s[:,None]).T@(x/s[:,None]));red=np.sum(((t-x@b)/s)**2)/max(len(n)-2,1);error=np.sqrt(cov[1,1]*max(1,red));calc=[b[1],error,b[0],np.median([e['depth_ppt'] for e in good])]; vals=[float(r[k]) for k in ('period_days','period_error_days','primary_epoch_btjd','depth_ppt')];out[r['tic']]={'n':len(good),'max_abs_difference':max(abs(np.array(calc)-vals)),'deltas':(np.array(calc)-vals).tolist(),'calculated':list(map(float,calc)),'selected_cycles':list(map(int,n))}
json.dump(out,open('helper/numeric-audit.json','w'),indent=2);print(json.dumps(out,indent=2))
