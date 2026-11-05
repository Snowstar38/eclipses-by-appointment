import csv,json,numpy as np
from pathlib import Path
p=Path(__file__).parent; N={r['source_id']:r for r in csv.DictReader((p.parent/'coverage-study/gaia-nss.csv').open())}; out={}; rng=np.random.default_rng(810023)
for q in csv.DictReader((p/'queue.csv').open()):
 r=N[q['gaia_dr3_source_id']]; keys=['period','eccentricity','arg_periastron','t_periastron']; mu=np.array([float(r[k]) for k in keys]); sd=np.array([float(r[k+'_error']) for k in keys]); v=list(map(float,r['corr_vec'].strip('{}').split(','))); C=np.eye(6); z=0
 assert int(r['bit_index'])==127 and len(v)==15
 for i in range(1,6):
  for j in range(i): C[i,j]=C[j,i]=v[z];z+=1
 C=C[np.ix_([0,3,4,5],[0,3,4,5])]*np.outer(sd,sd); sam=rng.multivariate_normal(mu,C,100000,check_valid='raise'); sam=sam[(sam[:,0]>0)&(sam[:,1]>=0)&(sam[:,1]<1)]; P,e,w,tp=sam.T; w=np.deg2rad(w); evs=[]
 for x in json.loads((p/q['tic']/'measurements.json').read_text())['events']:
  if not x.get('timing_usable'):continue
  nu=(np.pi/2 if x['kind']=='A' else 3*np.pi/2)-w; E=2*np.arctan2(np.sqrt(1-e)*np.sin(nu/2),np.sqrt(1+e)*np.cos(nu/2)); base=tp+389+(E-e*np.sin(E))%(2*np.pi)*P/(2*np.pi); cycle=round((x['mid_btjd']-np.median(base))/mu[0]); ts=base+cycle*P; lo,med,hi=np.percentile(ts,[15.8655,50,84.1345]); evs.append({'sector':x['sector'],'kind':x['kind'],'median':med,'half_68_interval':(hi-lo)/2,'observed':x['mid_btjd'],'offset_in_68_halfwidth':(x['mid_btjd']-med)/((hi-lo)/2)})
 out[q['tic']]={'source_id':q['gaia_dr3_source_id'],'draws_kept':len(sam),'events':evs}
(p/'helper-gaia-covariance.json').write_text(json.dumps(out,indent=2)); print(json.dumps(out,indent=2))
