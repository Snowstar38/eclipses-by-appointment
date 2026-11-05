import csv,json,math,hashlib
from pathlib import Path
import numpy as np
B=Path(__file__).parent;p=B.parent/'shared-catalogues/gaia_nss.csv';r=next(r for r in csv.DictReader(p.open()) if r['source_id']=='5811265337623194752')
def conj(v,k):
 P,e,w,tp=v;nu=(math.pi/2 if k==0 else 3*math.pi/2)-w;E=2*math.atan2(math.sqrt(1-e)*math.sin(nu/2),math.sqrt(1+e)*math.cos(nu/2));return tp+((E-e*math.sin(E))%(2*math.pi))/(2*math.pi)*P
P=float(r['period']);v=np.array([P,float(r['eccentricity']),math.radians(float(r['arg_periastron'])),389+float(r['t_periastron'])]);sig=np.array([float(r['period_error']),float(r['eccentricity_error']),math.radians(float(r['arg_periastron_error'])),float(r['t_periastron_error'])]);cv=[float(z) for z in r['corr_vec'].strip('{}').split(',')];cor=np.eye(6);z=0
for i in range(1,6):
 for j in range(i):cor[i,j]=cor[j,i]=cv[z];z+=1
sub=cor[np.ix_([0,3,4,5],[0,3,4,5])];epoch=3100.2737469;out=[]
for k in (0,1):
 c=conj(v,k);cyc=round((epoch-c)/P);pred=c+cyc*P;der=[]
 for j in range(4):
  step=max(sig[j]*.0001,1e-8);a=v.copy();b=v.copy();a[j]+=step;b[j]-=step;der.append(((conj(a,k)+cyc*a[0])-(conj(b,k)+cyc*b[0]))/(2*step)*sig[j])
 unc=math.sqrt(max(0,np.array(der)@sub@np.array(der)));out.append(dict(conjunction=k,pred_btjd=pred,offset_days=epoch-pred,linear_sigma_days=unc,offset_sigma=(epoch-pred)/unc))
res=dict(source_sha256=hashlib.sha256(p.read_bytes()).hexdigest(),epoch_btjd=epoch,conjunctions=out,min_eigenvalue=float(np.linalg.eigvalsh(cor).min()),note='Linear Gaia covariance, edge-on conjunctions; excludes nonlinear and systematic errors.')
(B/'helper-T042-geometry.json').write_text(json.dumps(res,indent=2));print(json.dumps(res,indent=2))
