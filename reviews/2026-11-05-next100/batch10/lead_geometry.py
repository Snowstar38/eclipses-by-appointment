import csv,json,numpy as np
from pathlib import Path
b=Path(__file__).parent; r=next(x for x in csv.DictReader((b.parent/'shared-catalogues/gaia_nss.csv').open()) if x['source_id']=='5430344035305587584')
p=float(r['period']);e=float(r['eccentricity']);w=np.deg2rad(float(r['arg_periastron']));tau=1389+float(r['t_periastron']);t=1528.141014132959;out=[]
for angle in [90,270]:
 nu=np.deg2rad(angle)-w; E=2*np.arctan2(np.sqrt(1-e)*np.sin(nu/2),np.sqrt(1+e)*np.cos(nu/2)); M=(E-e*np.sin(E))%(2*np.pi); t0=tau+p*M/(2*np.pi);k=round((t-t0)/p); pred=t0+k*p;out.append({'conjunction_angle_deg':angle,'reference_btjd':t0,'cycle':k,'predicted_btjd':pred,'measured_btjd':t,'difference_days':t-pred,'difference_phase':(t-pred)/p})
print(json.dumps({'tau_btjd':tau,'period':p,'eccentricity':e,'omega_deg':float(r['arg_periastron']),'results':out,'note':'edge-on approximation, no full covariance uncertainty; no association claimed'},indent=2));(b/'3299934'/'lead-gaia-geometry.json').write_text(json.dumps({'tau_btjd':tau,'period':p,'eccentricity':e,'omega_deg':float(r['arg_periastron']),'results':out,'note':'edge-on approximation, no full covariance uncertainty; no association claimed'},indent=2))
