import json,numpy as np
from pathlib import Path
D=Path(__file__).parent
def conj(P,e,w,tp,k):
 nu=(np.pi/2 if k=='A' else 3*np.pi/2)-w
 E=2*np.arctan2(np.sqrt(1-e)*np.sin(nu/2),np.sqrt(1+e)*np.cos(nu/2))
 return tp+((E-e*np.sin(E))%(2*np.pi))/(2*np.pi)*P
out={}
for d in D.iterdir():
 if not (d/'gaia-nss.json').exists():continue
 n=json.load(open(d/'gaia-nss.json'));o=json.load(open(d/'orbit-gates.json'));s=json.load(open(d/'secondary-fit.json'));r=json.load(open(d/'fit-results.json'))
 size=6 if n['nss_solution_type']=='SB1' else 7; assert (n['nss_solution_type'],int(n['bit_index'])) in [('SB1',127),('SB2',255)]
 c=[float(x) for x in n['corr_vec'].strip('{}[]()').split(',')];assert len(c)==size*(size-1)//2
 C=np.eye(size);z=0
 for i in range(1,size):
  for j in range(i): C[i,j]=C[j,i]=c[z];z+=1
 ix=[0,3,4,5] if size==6 else [0,4,5,6]
 err=np.array([float(n[x]) for x in ['period_error','eccentricity_error','arg_periastron_error','t_periastron_error']]);err[2]*=np.pi/180
 mu=np.array([float(n['period']),float(n['eccentricity']),np.deg2rad(float(n['arg_periastron'])),float(n['t_periastron'])+389]);cov=C[np.ix_(ix,ix)]*np.outer(err,err)
 draw=np.random.default_rng(594).multivariate_normal(mu,cov,100000);draw=draw[(draw[:,1]>=0)&(draw[:,1]<1)]
 pri=o['primary_conjunction'];other='B' if pri=='A' else 'A'; ph=((conj(*draw.T,other)-conj(*draw.T,pri))/draw[:,0])%1;nom=o['predicted_secondary_phase'];ph=nom+(ph-nom+.5)%1-.5
 q=lambda a:[float(x) for x in np.quantile(a,[.16,.5,.84])]
 geom=json.load(open(d/'geometry.json')) if (d/'geometry.json').exists() else {}
 detection=s['statistic'].get('n_individual_gt3sigma',0)>=3
 phot=s['profile_phase'] if detection else None
 # Formula assumes A primary; when B is primary reverse sign.
 sign=1 if pri=='A' else -1
 out[d.name]=dict(bit_index=int(n['bit_index']),gaia_primary=pri,gaia_relative_phase_nominal=nom,gaia_relative_phase_quantiles_16_50_84=q(ph),gaia_relative_phase_sigma=float(np.std(ph)),gaia_e_cos_omega_quantiles=q(draw[:,1]*np.cos(draw[:,2])),gaia_e_sin_omega_quantiles=q(draw[:,1]*np.sin(draw[:,2])),photometric_phase=phot,photometric_e_cos_omega_first_order=float(sign*np.pi/2*(phot-.5)) if phot is not None else None,photometric_note='First-order small-e approximation; fitted profile phase is optimized and conditional on eclipse shape, with no calibrated uncertainty. Omitted without three individual secondary detections.',geometry_status=geom.get('status'),geometry_e_sin_omega_conditional_range=geom.get('profile_interval_approx_95',{}).get('e_sin_omega'),geometry_note='Coarse conditional feasibility range, fixed TIC properties and simplified limb-darkened shape; not a calibrated posterior. Check chi2 and grid boundaries in geometry.json.')
json.dump(out,open(D/'covariance-geometry-comparison.json','w'),indent=2)
print(len(out))
