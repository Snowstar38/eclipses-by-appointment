import csv,json,math,numpy as np
from pathlib import Path
D=Path('[local working path omitted]');B=D/'batch04';T=json.loads((D/'targets-selected.json').read_text());R=json.loads((B/'raw-evidence/raw-events.json').read_text());NS={r['source_id']:r for r in csv.DictReader((D/'shared-catalogues/gaia-nss_two_body_orbit.csv').open())};out={}
def conj(v,k):
 P,e,w,tp=v;nu=(math.pi/2 if k=='A' else 3*math.pi/2)-w;E=2*math.atan2(math.sqrt(1-e)*math.sin(nu/2),math.sqrt(1+e)*math.cos(nu/2));return tp+((E-e*math.sin(E))%(2*math.pi))/(2*math.pi)*P
for tic,r in R.items():
 t=T[tic];n=NS[t['gaia']['source_id']];v=np.array([float(n['period']),float(n['eccentricity']),math.radians(float(n['arg_periastron'])),float(n['t_periastron'])+389]);errs=np.array([float(n['period_error']),float(n['eccentricity_error']),math.radians(float(n['arg_periastron_error'])),float(n['t_periastron_error'])]);ep=r['representative_ephemeris'];epoch=r['events'][0]['tc'];pred={}
 for k in ['A','B']:
  c=conj(v,k);cyc=round((epoch-c)/v[0]);offset=epoch-c-cyc*v[0];der=[]
  for j in range(4):
   vv=v.copy();step=errs[j]*.001 or 1e-7;vv[j]+=step;der.append((conj(vv,k)+cyc*vv[0]-c-cyc*v[0])/step*errs[j])
  pred[k]={'offset_d':offset,'offset_phase':offset/v[0],'diagonal_linear_error_d':float(np.linalg.norm(der))}
 k=min(pred,key=lambda k:abs(pred[k]['offset_d']));P,e,w,tp=v;m1=t.get('mass') or 1.;fm=1.036149e-7*P*float(n['semi_amplitude_primary'])**3*(1-e*e)**1.5
 lo,hi=.001,10
 for _ in range(60):
  m2=(lo+hi)/2
  if m2**3/(m1+m2)**2>fm:hi=m2
  else:lo=m2
 a=4.208278*(m1+m2)**(1/3)*P**(2/3);rad=t.get('rad') or 1;r2=m2**.8 if m2<1 else m2**.57;dur=P/math.pi*(rad+r2)/a*math.sqrt(1-e*e)/(1+(1 if k=='A' else -1)*e*math.sin(w))*24
 out[tic]={'gaia_source_id':n['source_id'],'solution':n['nss_solution_type'],'gaia_P':P,'gaia_P_error':errs[0],'phot_P':ep['period_d'],'period_difference_gaia_sigma':(ep['period_d']-P)/errs[0],'e':e,'omega_deg':float(n['arg_periastron']),'conjunction':pred,'closest_kind':k,'mass_function':fm,'m1_assumed':m1,'m2_min':m2,'r1_tic':rad,'central_duration_hours_approx':dur,'observed_duration_hours_median':float(np.median([x['duration_d']*24 for x in r['events']])),'note':'Nominal edge-on conjunction with descriptive diagonal linear uncertainty, omits covariance. No sigma veto. Duration uses TIC radius and minimum mass/main-sequence companion radius; feasibility approximation, not a fitted geometry. Same-sector photometric periods have no formal errors.'}
 print(tic,n['nss_solution_type'],'phase',round(pred[k]['offset_phase'],5),'Pdelta',round(out[tic]['period_difference_gaia_sigma'],2),'dur',round(out[tic]['observed_duration_hours_median'],2),round(dur,2))
(B/'gaia-geometry.json').write_text(json.dumps(out,indent=2))

