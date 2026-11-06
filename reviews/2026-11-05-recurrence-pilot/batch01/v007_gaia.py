"""Fixed-cycle Gaia SB1 edge-on conjunction diagnostic for V007."""
from pathlib import Path
import csv,json,hashlib,math
import numpy as np
B=Path(__file__).resolve().parent
PTH=B.parent/'novelty-audit'/'live'/'gaia_nss-pilot.csv'
sha=hashlib.sha256(PTH.read_bytes()).hexdigest()
sid='5363294922888372608'
row=next(r for r in csv.DictReader(PTH.open(newline='',encoding='utf8')) if r['source_id']==sid)
assert row['nss_solution_type']=='SB1'
v=np.array([float(row['period']),float(row['eccentricity']),math.radians(float(row['arg_periastron'])),389+float(row['t_periastron'])])
sig=np.array([float(row['period_error']),float(row['eccentricity_error']),math.radians(float(row['arg_periastron_error'])),float(row['t_periastron_error'])])
cv=np.array([float(x) for x in row['corr_vec'].strip('{}').split(',')]);assert len(cv)==15
cor=np.eye(6);n=0
for i in range(1,6):
 for j in range(i):cor[i,j]=cor[j,i]=cv[n];n+=1
sub=cor[np.ix_([0,3,4,5],[0,3,4,5])]
def conjunction(z,kind):
 P,e,w,tp=z
 nu=(math.pi/2 if kind=='A' else 3*math.pi/2)-w
 E=2*math.atan2(math.sqrt(1-e)*math.sin(nu/2),math.sqrt(1+e)*math.cos(nu/2))
 return tp+((E-e*math.sin(E))%(2*math.pi))/(2*math.pi)*P
out={'source_id':sid,'gaia_csv_sha256':sha,'gaia_values':{'period_days':v[0],'period_error_days':sig[0],'eccentricity':v[1],'omega_deg':math.degrees(v[2]),'tp_btjd':v[3]},'events':[],'caveat':'Gaia spectroscopic orientation yields two edge-on candidate conjunctions. Fixed integer cycles and linear covariance are local diagnostics, not full ephemeris uncertainty; inclination is not measured by this SB1 row.'}
for event in [2317.923,3023.369,3750.813,3772.869]:
 for kind in ['A','B']:
  c=conjunction(v,kind);cyc=round((event-c)/v[0]);pred=c+cyc*v[0]
  deriv=[]
  for j in range(4):
   step=max(1e-8,sig[j]*.0001);a=v.copy();b=v.copy();a[j]+=step;b[j]-=step
   deriv.append(((conjunction(a,kind)+cyc*a[0])-(conjunction(b,kind)+cyc*b[0]))/(2*step)*sig[j])
  uncertainty=float(np.sqrt(max(0,np.array(deriv)@sub@np.array(deriv))))
  out['events'].append({'observed_btjd':event,'kind':kind,'fixed_cycle':cyc,'predicted_btjd':pred,'offset_days':event-pred,'offset_phase':(event-pred)/v[0],'linear_covariance_sigma_days':uncertainty})
(B/'v007-gaia.json').write_text(json.dumps(out,indent=2)+'\n')
print('Gaia source',sid,'P',v[0],[(x['observed_btjd'],x['kind'],round(x['offset_days'],3),round(x['linear_covariance_sigma_days'],3)) for x in out['events']])
