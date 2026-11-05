import csv,json,math,hashlib
from pathlib import Path
B=Path(__file__).parent; rows=list(csv.DictReader((B/'queue.csv').open()));nss={r['source_id']:r for r in csv.DictReader((B.parent/'shared-catalogues/gaia_nss.csv').open())};out=[]
for r in rows:
 a=nss.get(r['gaia_dr3']);d=json.loads((B/r['tic']/'lead-numeric.json').read_text());
 if not a or not all(a.get(k) for k in ['eccentricity','arg_periastron','t_periastron','period']):continue
 e=float(a['eccentricity']);omega=math.radians(float(a['arg_periastron']));P=float(a['period']); tp=389+float(a['t_periastron']);con=[]
 for f in [math.pi/2-omega,3*math.pi/2-omega]:
  E=2*math.atan2(math.sqrt(1-e)*math.sin(f/2),math.sqrt(1+e)*math.cos(f/2));M=(E-e*math.sin(E))%(2*math.pi);con.append((M/(2*math.pi))%1)
 events=[]
 for ev in d['events']:
  if 'fit_mid_btjd' not in ev:continue
  phase=((ev['fit_mid_btjd']-tp)/P)%1;dist=min(abs((phase-p+.5)%1-.5) for p in con);events.append(dict(sector=ev['sector'],mid=ev['fit_mid_btjd'],nearest_conjunction_delta_days=dist*P))
 out.append(dict(sample_id=r['sample_id'],eccentricity=e,omega_deg=float(a['arg_periastron']),gaia_period=P,tperiastron_btjd=tp,edge_on_conjunction_phases=con,events=events,warning='nominal spectroscopic orbit only; omega convention selects conjunction labels; no covariance, uncertainties or precision geometry; source attribution remains separate'))
(B/'helper-geometry.json').write_text(json.dumps(out,indent=2));print([(x['sample_id'],round(min((v['nearest_conjunction_delta_days'] for v in x['events']),default=-1),2)) for x in out]);print('nss sha256',hashlib.sha256((B.parent/'shared-catalogues/gaia_nss.csv').read_bytes()).hexdigest())

