import csv,json,math,hashlib
from pathlib import Path
import numpy as np
B=Path(__file__).resolve().parent;p=B.parent/'shared-catalogues/gaia_nss.csv';rows={r['source_id']:r for r in csv.DictReader(p.open())};pre=json.loads((B/'lead-gaia-geometry.json').read_text());out=[]
def conj(v,k):
 P,e,w,tp=v;nu=(math.pi/2 if k==0 else 3*math.pi/2)-w;E=2*math.atan2(math.sqrt(1-e)*math.sin(nu/2),math.sqrt(1+e)*math.cos(nu/2));return tp+((E-e*math.sin(E))%(2*math.pi))/(2*math.pi)*P
for x in pre:
 s=json.loads((B.parent/'source-packets'/x['tic']/'sources.json').read_text());g=s['target']['gaia'];r=rows[g['source_id']];assert r['nss_solution_type']==g['nss_solution_type'] and abs(float(r['period'])-float(g['period']))<1e-8
 P=float(r['period']);e=float(r['eccentricity']);w=math.radians(float(r['arg_periastron']));tp=389+float(r['t_periastron']);v=np.array([P,e,w,tp]);sig=np.array([float(r['period_error']),float(r['eccentricity_error']),math.radians(float(r['arg_periastron_error'])),float(r['t_periastron_error'])]);nt=6 if r['nss_solution_type'] in ('SB1','SB1C') else 7;cv=[float(z) for z in r['corr_vec'].strip('{}').split(',')];assert len(cv)==nt*(nt-1)//2
 cor=np.eye(nt);z=0
 for i in range(1,nt):
  for j in range(i):cor[i,j]=cor[j,i]=cv[z];z+=1
 inds=[0,3,4,5] if nt==6 else [0,4,5,6];sub=cor[np.ix_(inds,inds)];epoch={'T026':3331.75814}.get(x['sample_id'],x['screen_time_not_fitted']);cc=[]
 for k in (0,1):
  c=conj(v,k);cyc=round((epoch-c)/P);pred=c+cyc*P;der=[]
  for j in range(4):
   step=max(sig[j]*.0001,1e-8);a=v.copy();b=v.copy();a[j]+=step;b[j]-=step;der.append(((conj(a,k)+cyc*a[0])-(conj(b,k)+cyc*b[0]))/(2*step)*sig[j])
  uncertainty=math.sqrt(max(0,np.array(der)@sub@np.array(der)));cc.append({'kind':k,'cycle':cyc,'pred_btjd':pred,'offset_days':epoch-pred,'linear_sigma_days':uncertainty,'offset_in_sigma':(epoch-pred)/uncertainty})
 out.append({'sample_id':x['sample_id'],'tic':x['tic'],'source_id':g['source_id'],'evaluation_epoch_btjd':epoch,'conjunctions':cc,'closest':min(cc,key=lambda a:abs(a['offset_days'])),'corr_min_eigenvalue':float(np.linalg.eigvalsh(cor).min()),'source_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'note':'Edge-on conjunction; linear Gaia covariance; evaluation epoch is measured where supplied, otherwise a screening prediction; systematic or nonlinear uncertainty not included.'});print(x['sample_id'],round(out[-1]['closest']['offset_days'],3),round(out[-1]['closest']['linear_sigma_days'],3))
(B/'lead-gaia-covariance.json').write_text(json.dumps(out,indent=2))


