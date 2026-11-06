import csv,json,math,hashlib
from pathlib import Path
import numpy as np
from astropy.io import fits
b=Path(__file__).resolve().parent;rng=np.random.default_rng(50701); ns={r['source_id']:r for r in csv.DictReader((b.parent/'shared-catalogues/gaia_nss-pending.csv').open())};out={}
for row in csv.DictReader((b/'queue.csv').open()):
 tic=row['tic'];r=ns[row['gaia_dr3']];v=np.array([float(r[x]) for x in ['period','eccentricity','arg_periastron','t_periastron']]);sig=np.array([float(r[x]) for x in ['period_error','eccentricity_error','arg_periastron_error','t_periastron_error']]);cv=[float(x) for x in r['corr_vec'].strip('{}').split(',')];cor=np.eye(6);i,j=np.tril_indices(6,-1);cor[i,j]=cv;cor[j,i]=cv;sub=cor[np.ix_([0,3,4,5],[0,3,4,5])];draw=rng.multivariate_normal(v,sig[:,None]*sub*sig[None,:],100000);draw=draw[(draw[:,1]>=0)&(draw[:,1]<1)&(draw[:,0]>0)];events=[]
 for ev in json.loads((b/tic/'lead-timing.json').read_text()):
  if not ev.get('fit_usable'):continue
  obs=ev['center_btjd'];conjs=[]
  for k in (0,1):
   nu=(np.pi/2 if k==0 else 3*np.pi/2)-np.radians(draw[:,2]);E=2*np.arctan2(np.sqrt(1-draw[:,1])*np.sin(nu/2),np.sqrt(1+draw[:,1])*np.cos(nu/2));c=389+draw[:,3]+np.mod(E-draw[:,1]*np.sin(E),2*np.pi)*draw[:,0]/(2*np.pi);nomnu=(np.pi/2 if k==0 else 3*np.pi/2)-np.radians(v[2]);nomE=2*np.arctan2(np.sqrt(1-v[1])*np.sin(nomnu/2),np.sqrt(1+v[1])*np.cos(nomnu/2));nomc=389+v[3]+np.mod(nomE-v[1]*np.sin(nomE),2*np.pi)*v[0]/(2*np.pi);cycle=round((obs-nomc)/v[0]);pred=c+cycle*draw[:,0];res=obs-pred;conjs.append(dict(kind=k,offset_quantiles_d=np.quantile(res,[.00135,.025,.5,.975,.99865]).tolist(),two_sided_tail=float(2*min(np.mean(res<0),np.mean(res>0)))))
  events.append(dict(sector=ev['sector'],center_btjd=obs,conjunctions=conjs))
 out[tic]=dict(seed=50701,n_valid=len(draw),events=events)
(b/'helper-nonlinear-gaia.json').write_text(json.dumps(out,indent=2));print(json.dumps(out['149847663'],indent=2))
