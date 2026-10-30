import json,numpy as np
import fit_batch as f
F=f.ROOT
def conj(P,e,w,tp,kind):
 nu=(np.pi/2 if kind=='A' else 3*np.pi/2)-w;E=2*np.arctan2(np.sqrt(1-e)*np.sin(nu/2),np.sqrt(1+e)*np.cos(nu/2));return tp+((E-e*np.sin(E))%(2*np.pi))/(2*np.pi)*P
diag=json.load(open(F/'review-diagnostics.json'));out={}
for tic in f.targets:
 d=F/tic;n=json.load(open(d/'gaia-nss.json'));o=json.load(open(d/'orbit-gates.json'));C=np.eye(6);c=[float(x) for x in n['corr_vec'].strip('{}[]()').split(',')];k=0
 for i in range(1,6):
  for j in range(i):C[i,j]=C[j,i]=c[k];k+=1
 ix=[0,3,4,5];err=np.array([float(n[x]) for x in ['period_error','eccentricity_error','arg_periastron_error','t_periastron_error']]);err[2]*=np.pi/180;mu=np.array([float(n['period']),float(n['eccentricity']),np.deg2rad(float(n['arg_periastron'])),float(n['t_periastron'])+389]);draw=np.random.default_rng(584).multivariate_normal(mu,C[np.ix_(ix,ix)]*np.outer(err,err),40000);draw=draw[(draw[:,1]>=0)&(draw[:,1]<1)];pri=o['primary_conjunction'];other='B' if pri=='A' else 'A';ph=((conj(*draw.T,other)-conj(*draw.T,pri))/draw[:,0])%1;phase=o['predicted_secondary_phase'];ph=phase+(ph-phase+.5)%1-.5;ec=draw[:,1]*np.cos(draw[:,2]);es=draw[:,1]*np.sin(draw[:,2]);a=dict(predicted_phase=phase,phase_error=float(np.std(ph)),gaia_ecos=float(mu[1]*np.cos(mu[2])),gaia_ecos_error=float(np.std(ec)),gaia_esin=float(mu[1]*np.sin(mu[2])),gaia_esin_error=float(np.std(es)))
 if diag[tic]['timing']:
  t=diag[tic]['timing'];a['phase_difference_sigma']=(t['phase_at_primary_Tref']-phase)/np.hypot(t['phase_error_conservative'],a['phase_error']);a['measured_phase']=t['phase_at_primary_Tref'];a['measured_phase_error']=t['phase_error_conservative']
 out[tic]=a;print(tic,a)
json.dump(out,open(F/'timing-covariance.json','w'),indent=2)
