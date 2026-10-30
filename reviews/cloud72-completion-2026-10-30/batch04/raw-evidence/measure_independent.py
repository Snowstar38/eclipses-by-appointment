import json,numpy as np,pathlib
r=pathlib.Path(__file__).parent;raw=json.load(open(r/'raw-events.json'));rows=json.load(open(r/'independent-extraction.json'));out=[]
for row in rows:
 tic=row['tic'];sec=row['sector'];a=np.load(r/row['file']);t=a['time'];y=a['flux'];events=[]
 for e in raw[tic]['events']:
  if e.get('sector')!=sec or 'tc' not in e or e.get('edge'):continue
  D=e['duration_d'];x=t-e['tc'];m=abs(x)<max(.4,3*D);x=x[m];z=y[m];ins=abs(x)<D/2
  if len(x)<12 or sum(ins)<2 or sum(x<-D*.65)<3 or sum(x>D*.65)<3:continue
  z=z/np.median(z);shape=np.clip((D/2-abs(x))/(D*max(.05,e.get('ingress_fraction',.25))),0,1);A=np.column_stack((np.ones(len(x)),x,x*x,-shape));c=np.linalg.lstsq(A,z,rcond=None)[0];res=z-A@c;err=np.sqrt(np.linalg.pinv(A.T@A)[-1,-1]*sum(res*res)/max(1,len(x)-4));events.append(dict(tc=e['tc'],depth=float(c[-1]),formal_error=float(err),n_in=int(sum(ins))))
 out.append(dict(tic=tic,sector=sec,events=events,note='Same-FFI custom aperture; QLP-shaped fixed-event regression with quadratic baseline, formal error ignores correlated noise. Empty means no usable selected events, not no variability.'))
json.dump(out,open(r/'independent-results.json','w'),indent=2)
for o in out:
 if o['events']:print(o['tic'],o['sector'],[(round(x['tc'],3),round(x['depth'],4),round(x['formal_error'],4)) for x in o['events'][:5]])
