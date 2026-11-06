import json,csv,hashlib,math,numpy as np
from pathlib import Path
b=Path('[workspace]/Astra/made/final-night-2026-11-05/fresh1000/second/batch03');p=b.parent/'shared-catalogues/gaia_nss-pending.csv';ns={r['source_id']:r for r in csv.DictReader(p.open())};queue=list(csv.DictReader((b/'queue.csv').open()));out={}
def conj(v,k):
 P,e,w,tp=v;nu=(math.pi/2 if k==0 else 3*math.pi/2)-w;E=2*math.atan2(math.sqrt(1-e)*math.sin(nu/2),math.sqrt(1+e)*math.cos(nu/2));return tp+((E-e*math.sin(E))%(2*math.pi))*P/(2*math.pi)
for row in queue:
 tic=row['tic'];r=ns[row['gaia_dr3']];
 if r['nss_solution_type']!='SB1' or int(r['bit_index'])!=127:
  out[tic]={'solution_type':r['nss_solution_type'],'note':'Non-SB1 covariance requires different source parameter mapping; not evaluated by SB1 primitive'};continue
 v=np.array([float(r['period']),float(r['eccentricity']),math.radians(float(r['arg_periastron'])),389+float(r['t_periastron'])]);sig=np.array([float(r['period_error']),float(r['eccentricity_error']),math.radians(float(r['arg_periastron_error'])),float(r['t_periastron_error'])]);cv=[float(x) for x in r['corr_vec'].strip('{}').split(',')];assert len(cv)==15;cor=np.eye(6);n=0
 for i in range(1,6):
  for j in range(i):cor[i,j]=cor[j,i]=cv[n];n+=1
 sub=cor[np.ix_([0,3,4,5],[0,3,4,5])];events=[]
 for ev in json.loads((b/tic/'lead-timing.json').read_text()):
  if not ev.get('fit_usable'):continue
  t=ev['center_btjd'];preds=[]
  for k in (0,1):
   c=conj(v,k);cyc=round((t-c)/v[0]);pred=c+cyc*v[0];der=[]
   for j in range(4):
    step=max(1e-8,sig[j]*.0001);a=v.copy();z=v.copy();a[j]+=step;z[j]-=step;der.append(((conj(a,k)+cyc*a[0])-(conj(z,k)+cyc*z[0]))/(2*step)*sig[j])
   error=float(np.sqrt(max(0,np.array(der)@sub@np.array(der))));preds.append(dict(kind=k,cycle=cyc,predicted_btjd=pred,offset_d=t-pred,phase_offset=(t-pred)/v[0],linear_covariance_sigma_d=error))
  events.append(dict(sector=ev['sector'],event_kind=ev['kind'],observed_btjd=t,conjunctions=preds))
 fm=1.036149e-7*v[0]*float(r['semi_amplitude_primary'])**3*(1-v[1]**2)**1.5
 out[tic]=dict(source_id=row['gaia_dr3'],gaia_nss_sha256=hashlib.sha256(p.read_bytes()).hexdigest(),gaia_period_d=v[0],gaia_period_error_d=sig[0],eccentricity=v[1],omega_deg=math.degrees(v[2]),tp_btjd=v[3],mass_function_solar=fm,events=events,note='Fixed-cycle local linear covariance; SB1 lower triangle P,gamma,K,e,omega,Tp; subindices0,3,4,5. Edge-on conjunction assumptions; no inclination measurement or full nonlinear posterior. This tests source-specific orbital consistency, not solely period matching.')
 print(tic,[(e['sector'],round(min(e['conjunctions'],key=lambda x:abs(x['offset_d']))['offset_d'],3),round(min(e['conjunctions'],key=lambda x:abs(x['offset_d']))['linear_covariance_sigma_d'],3)) for e in events])
(b/'lead-gaia-covariance.json').write_text(json.dumps(out,indent=2))



