import json,math,hashlib
from pathlib import Path
import numpy as np
B=Path(__file__).resolve().parent; G=json.loads((B/'gaia-geometry.json').read_text()); out={}
for tic in G:
 r=json.loads((B/tic/'gaia-nss-row.json').read_text()); g=G[tic]; assert r['source_id']==g['gaia_source_id']; p,e,w,tp=[float(r[k]) for k in ('period','eccentricity','arg_periastron','t_periastron')]; w=math.radians(w); tp+=389
 cor=np.eye(6); v=[float(x) for x in r['corr_vec'].strip('{}').split(',')];assert len(v)==15
 cor[np.tril_indices(6,-1)]=v;cor=cor+cor.T-np.eye(6); ix=[0,3,4,5]; sig=np.array([float(r['period_error']),float(r['eccentricity_error']),math.radians(float(r['arg_periastron_error'])),float(r['t_periastron_error'])]); C=cor[np.ix_(ix,ix)]*np.outer(sig,sig)
 def f(a,k,n):
  P,E,W,T=a;nu=(math.pi/2+k*math.pi-W)%(2*math.pi);ecc=2*math.atan2(math.sqrt(1-E)*math.sin(nu/2),math.sqrt(1+E)*math.cos(nu/2));return T+P*(n+((ecc-E*math.sin(ecc))%(2*math.pi))/(2*math.pi))
 arr=np.array([p,e,w,tp]); vals=[]
 for k,item in enumerate(g['conjunctions']):
  n=item['gaia_cycle']; steps=np.array([1e-5,1e-6,1e-6,1e-4]);J=[]
  for i,h in enumerate(steps):
   d=np.zeros(4);d[i]=h;J.append((f(arr+d,k,n)-f(arr-d,k,n))/(2*h))
  sd=math.sqrt(np.array(J)@C@np.array(J));vals.append({'sigma_days':sd,'difference_from_lead':sd-item['gaia_linear_covariance_error_days']})
 out[tic]={'gaia_source_id':r['source_id'],'row_sha256':hashlib.sha256((B/tic/'gaia-nss-row.json').read_bytes()).hexdigest(),'min_correlation_eigenvalue':float(np.linalg.eigvalsh(cor).min()),'conjunctions':vals}
(B/'helper-covariance-audit.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
