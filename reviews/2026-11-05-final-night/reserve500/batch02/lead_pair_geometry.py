import json,csv,numpy as np
from pathlib import Path
b=Path(__file__).resolve().parent;r=next(r for r in csv.DictReader((b.parent/'shared-catalogues/gaia_nss-pending.csv').open()) if r['source_id']=='4905403442934128256')
v=np.array([float(r[k]) for k in ('period','eccentricity','arg_periastron','t_periastron')]);s=np.array([float(r[k+'_error']) for k in ('period','eccentricity','arg_periastron','t_periastron')]);co=np.eye(6);i,j=np.tril_indices(6,-1);co[i,j]=[float(x) for x in r['corr_vec'].strip('{}').split(',')];co[j,i]=co[i,j];co=co[np.ix_([0,3,4,5],[0,3,4,5])];rng=np.random.default_rng(50702);x=rng.multivariate_normal(v,s[:,None]*co*s[None,:],200000);x=x[(x[:,1]>=0)&(x[:,1]<1)&(x[:,0]>0)]
cs=[]
for nu0 in (np.pi/2,3*np.pi/2):
 nu=nu0-np.radians(x[:,2]);e=x[:,1];E=2*np.arctan2(np.sqrt(1-e)*np.sin(nu/2),np.sqrt(1+e)*np.cos(nu/2));cs.append(np.mod(E-e*np.sin(E),2*np.pi)*x[:,0]/(2*np.pi))
delta=np.mod(cs[0]-cs[1],x[:,0]);ev=sorted([e['center_btjd'] for e in json.loads((b/'281540788/lead-timing.json').read_text()) if e['sector']==1 and e.get('fit_usable')]);obs=ev[1]-ev[0];res=obs-delta
out={'tic':'281540788','same_orbit_conjunction_pair_test':True,'observed_kindB_to_kindA_d':obs,'predicted_interval_quantiles_d':np.quantile(delta,[.00135,.025,.5,.975,.99865]).tolist(),'two_sided_tail':float(2*min(np.mean(res<0),np.mean(res>0))),'n_valid':len(x),'seed':50702,'note':'Pair interval cancels uncertain epoch and propagation cycle. Full source covariance, truncation0<=e<1. Edge-on conjunction. Observed secondary at1350.03073 is kept separate from same-kind clock.'}
(b/'lead-pair-geometry.json').write_text(json.dumps(out,indent=2));print(out)
