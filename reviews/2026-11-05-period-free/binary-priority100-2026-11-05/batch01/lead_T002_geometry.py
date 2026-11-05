"""Re-evaluate source-specific Gaia covariance at the newly measured T002 eclipse."""
import csv,hashlib,json,math
from pathlib import Path
import numpy as np
B=Path(__file__).resolve().parent;src=B.parent/'shared-catalogues/gaia_nss.csv';packet=json.loads((B.parent/'source-packets/92234103/sources.json').read_text());g=packet['target']['gaia'];r=next(x for x in csv.DictReader(src.open()) if x['source_id']==g['source_id'] and x['nss_solution_type']==g['nss_solution_type'] and abs(float(x['period'])-float(g['period']))<1e-8)
def conj(v,k):
 P,e,w,tp=v;nu=(math.pi/2 if k==0 else 3*math.pi/2)-w;E=2*math.atan2(math.sqrt(1-e)*math.sin(nu/2),math.sqrt(1+e)*math.cos(nu/2));return tp+((E-e*math.sin(E))%(2*math.pi))/(2*math.pi)*P
v=np.array([float(r['period']),float(r['eccentricity']),math.radians(float(r['arg_periastron'])),389+float(r['t_periastron'])]);sig=np.array([float(r['period_error']),float(r['eccentricity_error']),math.radians(float(r['arg_periastron_error'])),float(r['t_periastron_error'])]);cv=[float(z) for z in r['corr_vec'].strip('{}').split(',')];cor=np.eye(6);z=0
for i in range(1,6):
 for j in range(i):cor[i,j]=cor[j,i]=cv[z];z+=1
sub=cor[np.ix_([0,3,4,5],[0,3,4,5])];epoch=json.loads((B/'92234103/lead-new-timing.json').read_text())['events'][-1]['center_btjd'];cc=[]
for kind in (0,1):
 c=conj(v,kind);cyc=round((epoch-c)/v[0]);pred=c+cyc*v[0];der=[]
 for j in range(4):
  step=max(sig[j]*.0001,1e-8);a=v.copy();b=v.copy();a[j]+=step;b[j]-=step;der.append(((conj(a,kind)+cyc*a[0])-(conj(b,kind)+cyc*b[0]))/(2*step)*sig[j])
 sd=math.sqrt(max(0,np.array(der)@sub@np.array(der)));cc.append(dict(kind=kind,gaia_cycle=cyc,pred_btjd=pred,offset_days=epoch-pred,linear_sigma_days=sd,offset_in_sigma=(epoch-pred)/sd))
o=dict(tic='92234103',evaluation_epoch_btjd=epoch,source_id=g['source_id'],source_sha256=hashlib.sha256(src.read_bytes()).hexdigest(),closest=min(cc,key=lambda x:abs(x['offset_days'])),conjunctions=cc,method='Edge-on conjunction, correlated Gaia DR3 NSS covariance, first-order propagation. No pipeline timing systematic or nonlinear extrapolation allowance.')
(B/'92234103/lead-new-geometry.json').write_text(json.dumps(o,indent=2)+'\n');print(o)
