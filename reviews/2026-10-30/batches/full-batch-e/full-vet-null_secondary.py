import json,numpy as np
import fit_batch as f
F=f.ROOT
def conj(P,e,w,tp,kind):
 nu=(np.pi/2 if kind=='A' else 3*np.pi/2)-w;E=2*np.arctan2(np.sqrt(1-e)*np.sin(nu/2),np.sqrt(1+e)*np.cos(nu/2));return tp+((E-e*np.sin(E))%(2*np.pi))/(2*np.pi)*P
for tic in ['194609413','370251176','82620363']:
 d=F/tic;r=json.load(open(d/'fit-results.json'));o=json.load(open(d/'orbit-gates.json'));n=json.load(open(d/'gaia-nss.json'));ep=r['ephemeris'];secs=f.read(tic);f.P=ep['P']
 C=np.eye(6);c=[float(x) for x in n['corr_vec'].strip('{}[]()').split(',')];k=0
 for i in range(1,6):
  for j in range(i):C[i,j]=C[j,i]=c[k];k+=1
 ix=[0,3,4,5];err=np.array([float(n[x]) for x in ['period_error','eccentricity_error','arg_periastron_error','t_periastron_error']]);err[2]*=np.pi/180
 mu=np.array([float(n['period']),float(n['eccentricity']),np.deg2rad(float(n['arg_periastron'])),float(n['t_periastron'])+389]);cov=C[np.ix_(ix,ix)]*np.outer(err,err);draw=np.random.default_rng(584).multivariate_normal(mu,cov,20000);draw=draw[(draw[:,1]>=0)&(draw[:,1]<1)]
 pri=o['primary_conjunction'];other='B' if pri=='A' else 'A';ph=((conj(*draw.T,other)-conj(*draw.T,pri))/draw[:,0])%1;phase=o['predicted_secondary_phase'];ph=phase+(ph-phase+.5)%1-.5;sig=float(np.std(ph));widths=[r['shape']['T14']*.6,r['shape']['T14'],r['shape']['T14']*1.7,.5,.76];tests=[]
 for T in widths:
  for p in np.linspace(phase-2*sig,phase+2*sig,9):
   rows=[]
   for s in secs:
    for cyc in range(int(np.ceil((min(s['t'])-ep['T0'])/f.P-p)),int(np.floor((max(s['t'])-ep['T0'])/f.P-p))+1):
     a=f.event(s,ep['T0']+(cyc+p)*f.P,T,.35,scan=False);a['cycle']=cyc;rows.append(a)
   fit=[a for a in rows if a['status']=='fit'];dep=np.array([a['depth'] for a in fit]);er=np.array([a['depth_error'] for a in fit]);w=1/er**2
   if len(fit):
    mean=float(sum(w*dep)/sum(w));e=max(float(1/np.sqrt(sum(w))),float(np.std(dep)/np.sqrt(len(dep))));tests.append(dict(T14=T,phase=float(p),n=len(fit),depth=mean,error=e,upper3sigma=max(0,mean)+3*e,events=rows))
 # Approximate duration chord feasibility under stated radius assumption.
 phys=[]
 for a in o['physics']:
  k=a['r2_approx_rsun']/a['r1_rsun'];ratio=r['shape']['T14']*24/a['central_T14_hours'][pri];b=(1+k)*np.sqrt(max(0,1-ratio**2));es=mu[1]*np.sin(mu[2]);bother=b*(1+es)/(1-es) if pri=='A' else b*(1-es)/(1+es)
  phys.append(dict(radius_ratio_assumption=k,b_primary_duration_approx=b,b_other=bother,contact=1+k,other_misses=bool(bother>1+k),es_gaia=es,note='Central-duration/chord approximation with main-sequence companion radius, not measured component dimensions; establishes feasible missing eclipse, not unique geometry.'))
 out=dict(phase=phase,phase_sigma_covariance=sig,tests=tests,upper_limit_range=[min(x['upper3sigma'] for x in tests),max(x['upper3sigma'] for x in tests)],geometry=phys,note='Pointwise conditional3sigma limits across5widths and9phases spanning2sigma Gaia relative-phase covariance. No detection significance assigned after scanning; coverage exclusions retained; widest events may lack clean local baselines.')
 json.dump(out,open(d/'null-secondary.json','w'),indent=2);print(tic,'sigma phase',sig,'limits',out['upper_limit_range'],'geometry',phys)


