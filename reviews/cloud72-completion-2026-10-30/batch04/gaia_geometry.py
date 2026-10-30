import json,math,csv,numpy as np
from pathlib import Path
D=Path('[local working path omitted]');B=D/'batch04';T=json.loads((D/'targets-selected.json').read_text());R=json.loads((B/'raw-evidence/raw-events.json').read_text());ns={r['source_id']:r for r in csv.DictReader((D/'shared-catalogues/gaia-nss_two_body_orbit.csv').open())};out={}
def c(v,kind):
 P,e,w,tp=v;nu=(math.pi/2 if kind=='A' else 3*math.pi/2)-w;E=2*math.atan2(math.sqrt(1-e)*math.sin(nu/2),math.sqrt(1+e)*math.cos(nu/2));return tp+((E-e*math.sin(E))%(2*math.pi))/(2*math.pi)*P
for tic,r in R.items():
 t=T[tic];n=ns[t['gaia']['source_id']];v=np.array([float(n['period']),float(n['eccentricity']),math.radians(float(n['arg_periastron'])),float(n['t_periastron'])+389]);err=np.array([float(n['period_error']),float(n['eccentricity_error']),math.radians(float(n['arg_periastron_error'])),float(n['t_periastron_error'])]);ep=r['representative_ephemeris'];pred={}
 if ep is not None and 'period_d' not in ep:ep={**ep,'period_d':ep['candidate_binary_period_d']}
 if ep is None:
  out[tic]=dict(status='unresolved',reason='No representative eclipse ephemeris measured; cannot perform eclipse conjunction check',gaia_source_id=n['source_id'],gaia_P=float(v[0]),gaia_P_error=float(err[0]),e=float(v[1]),omega_deg=float(n['arg_periastron']));continue
 for kind in ['A','B']:
  nominal=c(v,kind);cyc=round((ep['epoch_btjd']-nominal)/v[0]);dd=(ep['epoch_btjd']-(nominal+cyc*v[0])+v[0]/2)%v[0]-v[0]/2
  deriv=[]
  for j in range(4):
   vv=v.copy();step=err[j]*.001 or 1e-7;vv[j]+=step;deriv.append((((c(vv,kind)+cyc*vv[0])-(nominal+cyc*v[0]))/step)*err[j])
  C=np.eye(6);vals=[float(x) for x in n['corr_vec'].strip('{}[]()').split(',')];z=0
  for ii in range(1,6):
   for jj in range(ii):C[ii,jj]=C[jj,ii]=vals[z];z+=1
  sub=C[np.ix_([0,3,4,5],[0,3,4,5])];cov_err=float(np.sqrt(max(0,np.asarray(deriv)@sub@np.asarray(deriv))))
  pred[kind]=dict(covariance_linear_error_d=cov_err,offset_d=dd,diagonal_error_d=float(np.linalg.norm(deriv)),conservative_sum_error_d=sum(abs(x) for x in deriv))
 primary=min(pred,key=lambda k:abs(pred[k]['offset_d']));P,e,w,tp=v
 fm=1.036149e-7*P*float(n['semi_amplitude_primary'])**3*(1-e*e)**1.5;m1=t.get('mass') or 1.;lo,hi=.001,10
 for _ in range(60):
  m2=(lo+hi)/2
  if m2**3/(m1+m2)**2>fm:hi=m2
  else:lo=m2
 a=4.208278*(m1+m2)**(1/3)*P**(2/3);r1=t.get('rad');r2=m2**.8 if m2<1 else m2**.57
 duration=P/math.pi*((r1 or 1)+r2)/a*math.sqrt(1-e*e)/(1+(1 if primary=='A' else -1)*e*math.sin(w))*24
 diffs=[]
 for p in (B/'raw-evidence').glob(f'{tic}*'):pass
 out[tic]=dict(gaia_source_id=n['source_id'],gaia_P=P,gaia_P_error=err[0],phot_P=ep['period_d'],period_difference_gaia_sigma=(ep['period_d']-P)/err[0],conjunction=pred,closest_kind=primary,e=e,omega_deg=float(n['arg_periastron']),mass_function=fm,m1_assumed=m1,m2_min=m2,r1_tic=r1,companion_radius_MS_approx=r2,central_duration_hours_approx=duration,observed_duration_hours_median=float(np.median([x['duration_d']*24 for x in r['events'] if 'duration_d' in x])),note='Linear covariance error uses full SB1 lower-triangle correlations in P,gamma,K1,e,omega,Tp order; diagonal error ignores correlations; sum absolute parameter contributions is conservative under unknown correlations. Radius/main-sequence companion approximation is feasibility only, not a fitted geometry.')
 print(tic,'Pdelta',round(out[tic]['period_difference_gaia_sigma'],2),'conj',primary,pred[primary], 'dur',round(out[tic]['observed_duration_hours_median'],2),round(duration,2))
(B/'gaia-geometry.json').write_text(json.dumps(out,indent=2))



