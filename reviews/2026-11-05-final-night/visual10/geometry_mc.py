import json,math,numpy as np
from pathlib import Path
B=Path(__file__).resolve().parent;D=json.loads((B/'lead-deciding-checks.json').read_text());C=json.loads((B/'lead-clocks.json').read_text());out={};rng=np.random.default_rng(2026110507)
for tic,r in D.items():
 g=r['gaia_row'];keys=['period','center_of_mass_velocity','semi_amplitude_primary','eccentricity','arg_periastron','t_periastron'];mu=np.array([float(g[k]) for k in keys]);sig=np.array([float(g[k+'_error']) for k in keys]);corr=np.eye(6);z=0;vals=[float(x) for x in g['corr_vec'].strip('{}').split(',')]
 for i in range(1,6):
  for j in range(i):corr[i,j]=corr[j,i]=vals[z];z+=1
 cov=corr*sig[:,None]*sig[None,:];samples=rng.multivariate_normal(mu,cov,20000);valid=(samples[:,0]>0)&(samples[:,3]>=0)&(samples[:,3]<1);samples=samples[valid];epoch=C[tic]['epoch_btjd'];vv=[]
 for k in [0,1]:
  pp=samples[:,0];e=samples[:,3];w=np.deg2rad(samples[:,4]);tp=samples[:,5]+389;nu=(math.pi/2 if k==0 else 3*math.pi/2)-w;E=2*np.arctan2(np.sqrt(1-e)*np.sin(nu/2),np.sqrt(1+e)*np.cos(nu/2));tc=tp+((E-e*np.sin(E))%(2*math.pi))*pp/(2*math.pi);offset=(epoch-tc+pp/2)%pp-pp/2;vv.append(dict(kind=k,offset_quantiles_d=np.quantile(offset,[.025,.16,.5,.84,.975]).tolist(),fraction_abs_offset_lt_1day=float(np.mean(abs(offset)<1))))
 out[tic]=dict(seed=2026110507,requested_draws=20000,valid_draws=len(samples),sb1_order=keys,covariance_eigenvalues=np.linalg.eigvalsh(cov).tolist(),conjunctions=vv,note='Full published SB1 correlation vector, edge-on conjunction approximation; invalid e draws rejected. Near-circular omega/Tp correlation retained. Event timing systematic not included.')
 print(tic,vv)
(B/'lead-gaia-covariance.json').write_text(json.dumps(out,indent=2))
