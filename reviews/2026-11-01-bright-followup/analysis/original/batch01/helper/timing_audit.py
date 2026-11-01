import json,csv,hashlib
from pathlib import Path
import numpy as np
B=Path(__file__).parent.parent;out={}
for row in csv.DictReader(open(B/'queue.csv')):
 t=row['tic'];p=B/t/'measurements.json';d=json.load(open(p));e=[z for z in d['events'] if z.get('timing_usable')];x=np.array([z.get('orbital_cycle',z['cycle']) for z in e],float);y=np.array([z['mid_btjd'] for z in e]);w=1/np.array([z['timing_error_days'] for z in e])**2;xm=np.average(x,weights=w);ym=np.average(y,weights=w);s=np.sum(w*(x-xm)*(y-ym))/np.sum(w*(x-xm)**2);res=y-(ym+s*(x-xm));chi=sum(w*res**2)/max(len(x)-2,1);err=np.sqrt(max(1,chi)/np.sum(w*(x-xm)**2));epoch=ym+s*(d['epoch_cycle']-xm);out[t]=dict(n=len(e),cycles=x.tolist(),period=s,error=err,epoch=epoch,period_diff=s-d['period_days'],error_diff=err-d['period_error_days'],epoch_diff=epoch-d['primary_epoch_btjd'],measure_sha256=hashlib.sha256(p.read_bytes()).hexdigest());print(t, len(e),s,err,'diff',out[t]['period_diff'],out[t]['error_diff'],out[t]['epoch_diff'])
json.dump(out,open(B/'helper'/'timing-audit.json','w'),indent=2)
