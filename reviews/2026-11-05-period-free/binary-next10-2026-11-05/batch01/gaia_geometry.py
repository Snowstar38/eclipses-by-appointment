"""Source-specific Gaia spectroscopic conjunction timing, linear covariance diagnostic."""
import csv,json,math
from pathlib import Path
import numpy as np
B=Path(__file__).resolve().parent
R={r['source_id']:r for r in csv.DictReader((B.parent/'shared-catalogues'/'gaia_nss.csv').open(newline='',encoding='utf8'))}
Q={r['sample_id']:r for r in csv.DictReader((B/'queue.csv').open(newline='',encoding='utf8'))}
E={'N001':1959.089,'N004':2510.814,'N005':2042.157,'N006':1891.863,'N007':2712.682,'N008':2046.070,'N010':1635.896}
def conj(v,kind):
 P,e,w,tp=v;nu=(math.pi/2 if kind=='A' else 3*math.pi/2)-w
 an=2*math.atan2(math.sqrt(1-e)*math.sin(nu/2),math.sqrt(1+e)*math.cos(nu/2))
 return tp+((an-e*math.sin(an))%(2*math.pi))/(2*math.pi)*P
out={}
for sid,epoch in E.items():
 row=Q[sid];rr=R[row['gaia_dr3']];P=float(rr['period']);e=float(rr['eccentricity']);w=math.radians(float(rr['arg_periastron']));tp=389+float(rr['t_periastron']);v=np.array([P,e,w,tp]);sig=np.array([float(rr['period_error']),float(rr['eccentricity_error']),math.radians(float(rr['arg_periastron_error'])),float(rr['t_periastron_error'])]);nt=6 if rr['nss_solution_type']=='SB1' else 7
 cv=[float(x) for x in rr['corr_vec'].strip('{}').split(',')];assert len(cv)==nt*(nt-1)//2
 cor=np.eye(nt);n=0
 for i in range(1,nt):
  for j in range(i):cor[i,j]=cor[j,i]=cv[n];n+=1
 inds=[0,3,4,5] if nt==6 else [0,4,5,6];sub=cor[np.ix_(inds,inds)];cs=[]
 for kind in ['A','B']:
  c=conj(v,kind);cyc=round((epoch-c)/P);pred=c+cyc*P;der=[]
  for j in range(4):
   step=max(sig[j]*.0001,1e-8);a=v.copy();b=v.copy();a[j]+=step;b[j]-=step
   der.append(((conj(a,kind)+cyc*a[0])-(conj(b,kind)+cyc*b[0]))/(2*step)*sig[j])
  unc=math.sqrt(max(0,np.array(der)@sub@np.array(der)))
  cs.append({'kind':kind,'gaia_cycle':cyc,'predicted_btjd':pred,'observed_btjd':epoch,'offset_days':epoch-pred,'offset_phase':(epoch-pred)/P,'linear_covariance_sigma_days':unc,'offset_over_linear_sigma':(epoch-pred)/unc if unc>0 else None})
 out[sid]={'tic':row['tic'],'gaia_source_id':row['gaia_dr3'],'nss_type':rr['nss_solution_type'],'period_days':P,'period_error_days':sig[0],'eccentricity':e,'omega_deg':math.degrees(w),'tp_btjd':tp,'conjunctions':cs,'covariance_order':'P,gamma,K,e,omega,Tp' if nt==6 else 'P,gamma,K1,K2,e,omega,Tp','note':'Linear source-specific Gaia covariance at one observed epoch, not full conjunction uncertainty; approximate edge-on geometry.'}
(B/'gaia-geometry.json').write_text(json.dumps(out,indent=2)+'\n')
for sid,x in out.items():print(sid,[(c['kind'],round(c['offset_phase'],4),round(c['offset_over_linear_sigma'],2)) for c in x['conjunctions']])
