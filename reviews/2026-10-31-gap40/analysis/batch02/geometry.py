import csv,json,math
from pathlib import Path
import numpy as np
B=Path(__file__).parent
TG=json.load(open(B.parent/'shared-catalogues/targets-selected.json'))
NS={r['source_id']:r for r in csv.DictReader(open(B.parent/'shared-catalogues/gaia-nss-full.csv'))}
def conj(v,k):
 p,e,w,tp=v;nu=(math.pi/2 if k==0 else 3*math.pi/2)-w;E=2*math.atan2(math.sqrt(1-e)*math.sin(nu/2),math.sqrt(1+e)*math.cos(nu/2));return tp+(E-e*math.sin(E))%(2*math.pi)/(2*math.pi)*p
out={}
for row in csv.DictReader(open(B/'queue.csv')):
 tic=row['tic'];m=json.load(open(B/tic/'measurements.json'));t=TG[tic];n=NS[t['gaia']['source_id']]
 v=np.array([float(n['period']),float(n['eccentricity']),math.radians(float(n['arg_periastron'])),float(n['t_periastron'])+389]);err=np.array([float(n['period_error']),float(n['eccentricity_error']),math.radians(float(n['arg_periastron_error'])),float(n['t_periastron_error'])]);C=np.eye(6);vals=[float(x) for x in n['corr_vec'].strip('{}[]()').split(',')];z=0
 for i in range(1,6):
  for j in range(i):C[i,j]=C[j,i]=vals[z];z+=1
 sub=C[np.ix_([0,3,4,5],[0,3,4,5])];epoch=m['primary_epoch_btjd'];pred=[]
 for k in (0,1):
  c=conj(v,k);cyc=round((epoch-c)/v[0]);delta=epoch-c-cyc*v[0];der=[]
  for j in range(4):
   step=max(err[j]*.0001,1e-8);a=v.copy();b=v.copy();a[j]+=step;b[j]-=step
   if j==1 and b[j]<0:b[j]=v[j]
   derivative=(conj(a,k)+cyc*a[0]-conj(b,k)-cyc*b[0])/(a[j]-b[j]);der.append(derivative*err[j])
  sigma=float(np.sqrt(max(np.array(der)@sub@np.array(der),0)));pred.append(dict(kind=k,offset_days=delta,offset_phase=delta/v[0],gaia_covariance_linear_error_days=sigma))
 best=min(pred,key=lambda x:abs(x['offset_days']));P,e,w,tp=v
 backcycle=round((389-epoch)/m['period_days']);near_epoch=epoch+backcycle*m['period_days'];c=conj(v,best['kind']);near_cycle=round((near_epoch-c)/P);near_delta=near_epoch-c-near_cycle*P
 near=dict(projected_photometric_epoch_btjd=near_epoch,offset_days=near_delta,period_projection_allowance_days=abs(backcycle)*m['period_error_days'],note='Photometric fit projected toward Gaia2016 reference; ephemeris period error allowance only, ignores covariance and model systematics; compare to actual-epoch covariance above.')
 fm=1.036149e-7*P*float(n['semi_amplitude_primary'])**3*(1-e*e)**1.5;m1=t.get('mass') or 1.;lo,hi=.001,10
 for _ in range(70):
  m2=(lo+hi)/2
  if m2**3/(m1+m2)**2>fm:hi=m2
  else:lo=m2
 a=4.208278*(m1+m2)**(1/3)*P**(2/3);r1=t.get('rad') or 1;r2=m2**.8 if m2<1 else m2**.57;duration=P/math.pi*(r1+r2)/a*math.sqrt(1-e*e)/(1+(1 if best['kind']==0 else -1)*e*math.sin(w))*24
 out[tic]=dict(gaia_source_id=n['source_id'],period_days=P,period_error_days=err[0],eccentricity=e,omega_deg=float(n['arg_periastron']),t_periastron_btjd=tp,photometric_period_days=m['period_days'],period_difference_days=m['period_days']-P,conjunction=pred,closest=best,near_reference=near,mass_function_solar=fm,assumed_m1_solar=m1,minimum_m2_solar=m2,tic_radius_solar=r1,central_duration_hours_approx=duration,observed_duration_hours=float(np.median([e['duration_days'] for e in m['events'] if 'duration_days' in e])*24),note='Edge-on conjunction; full SB1 correlation lower triangle order P,gamma,K,e,omega,Tp, subindices0,3,4,5. Linear propagated uncertainty is descriptive, not sigma veto. Approximate duration assumes TIC radius and main-sequence minimum-mass companion; not fitted geometry.')
 print(tic,round(best['offset_phase'],5),round(best['gaia_covariance_linear_error_days'],4),'dur',round(out[tic]['observed_duration_hours'],2),round(duration,2))
json.dump(out,open(B/'gaia-geometry.json','w'),indent=2)
