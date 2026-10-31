import csv,json,numpy as np,math
from pathlib import Path
b=Path('[local path omitted]'); tg=json.load(open(b.parent/'targets-selected.json')); ns={r['source_id']:r for r in csv.DictReader(open(b.parent/'shared-catalogues/gaia-nss-full.csv'))};g=json.load(open(b/'gaia-geometry.json'));res=[]
for tic,z in g.items():
 n=ns[tg[tic]['gaia']['source_id']];corr=list(map(float,n['corr_vec'].strip('{}[]()').split(',')));C=np.eye(6);k=0
 for i in range(1,6):
  for j in range(i):C[i,j]=C[j,i]=corr[k];k+=1
 P=float(n['period']);e=float(n['eccentricity']);amp=float(n['semi_amplitude_primary']);fm=1.036149e-7*P*amp**3*(1-e*e)**1.5;m1=z['assumed_m1_solar'];m2=z['minimum_m2_solar'];res.append({'tic':tic,'min_correlation_eigenvalue':float(np.linalg.eigvalsh(C).min()),'mass_function_delta':fm-z['mass_function_solar'],'mass_inverse_delta':m2**3/(m1+m2)**2-fm,'photometric_period_delta':json.load(open(b/tic/'measurements.json'))['period_days']-z['photometric_period_days']})
(b/'helper/geometry-audit.json').write_text(json.dumps(res,indent=2));print(json.dumps(res,indent=2))
