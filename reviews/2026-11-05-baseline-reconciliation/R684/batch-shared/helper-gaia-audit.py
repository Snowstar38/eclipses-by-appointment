import csv,json,math
from pathlib import Path
p=Path(__file__).parent
rows={r['source_id']:r for r in csv.DictReader((p.parent/'coverage-study/gaia-nss.csv').open())}; out={}
for q in csv.DictReader((p/'queue.csv').open()):
 r=rows[q['gaia_dr3_source_id']]; d=json.loads((p/q['tic']/'measurements.json').read_text()); P=float(r['period']); e=float(r['eccentricity']); w=math.radians(float(r['arg_periastron'])); tp=float(r['t_periastron'])+389; K=float(r['semi_amplitude_primary']); f=1.036149e-7*K**3*P*(1-e*e)**1.5
 es=[]
 for ev in d['events']:
  if not ev.get('timing_usable'):continue
  nu=(math.pi/2 if ev['kind']=='A' else 3*math.pi/2)-w; E=2*math.atan2(math.sqrt(1-e)*math.sin(nu/2),math.sqrt(1+e)*math.cos(nu/2)); M=(E-e*math.sin(E))%(2*math.pi); t=tp+M*P/(2*math.pi); t+=round((ev['mid_btjd']-t)/P)*P
  es.append({'kind':ev['kind'],'sector':ev['sector'],'mid':ev['mid_btjd'],'conjunction':t,'days_offset':ev['mid_btjd']-t,'screen_prediction_difference':t-ev['predicted_btjd'],'screen_sigma':ev['predicted_sigma_days'],'abs_z':abs(ev['mid_btjd']-t)/ev['predicted_sigma_days']})
 out[q['tic']]={'source_id':q['gaia_dr3_source_id'],'period':P,'eccentricity':e,'omega_deg':float(r['arg_periastron']),'mass_function_solar':f,'events':es}
(p/'helper-gaia-audit.json').write_text(json.dumps(out,indent=2));print(json.dumps(out,indent=2))
