import json,csv,hashlib
from pathlib import Path
import numpy as np
B=Path(__file__).parent.parent; G=json.load(open(B/'gaia-geometry.json')); out={}
for row in csv.DictReader(open(B/'queue.csv')):
 t=row['tic']; p=B/t/'measurements.json'; d=json.load(open(p)); e=[x for x in d['events'] if x.get('timing_usable') and (t not in ('48752905','351335839') or x['cycle']%2==0)]; x=np.array([z.get('orbital_cycle',z['cycle']) for z in e],float); y=np.array([z['mid_btjd'] for z in e]); w=1/np.array([z['timing_error_days'] for z in e])**2; xm=np.average(x,weights=w); ym=np.average(y,weights=w); slope=np.sum(w*(x-xm)*(y-ym))/np.sum(w*(x-xm)**2); resid=y-(ym+slope*(x-xm)); rchi=sum(w*resid**2)/max(len(x)-2,1); err=np.sqrt(max(1,rchi)/np.sum(w*(x-xm)**2)); epoch=ym+slope*(min(x)-xm); gd=G[t]; out[t]=dict(n=len(e),period=slope,period_error=err,epoch=epoch,period_diff=slope-d['period_days'],error_diff=err-d['period_error_days'],epoch_diff=epoch-d['primary_epoch_btjd'],geometry_period_diff=gd['photometric_period_days']-d['period_days'],selected_cycles=x.tolist(),measure_sha256=hashlib.sha256(p.read_bytes()).hexdigest());print(t,len(e),slope,err,epoch,'diff',out[t]['period_diff'])
json.dump(out,open(B/'helper'/'timing-audit.json','w'),indent=2)
