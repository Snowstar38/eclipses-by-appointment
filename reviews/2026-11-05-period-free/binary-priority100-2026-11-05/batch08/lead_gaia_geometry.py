import json,csv,math,hashlib
from pathlib import Path
B=Path(__file__).resolve().parent;rows=list(csv.DictReader((B/'queue.csv').open()));out=[]
timing={x['sample_id']:x for x in json.loads((B/'lead-timing.json').read_text())}
for r in rows:
 p=B.parent/'source-packets'/r['tic']/'sources.json';s=json.loads(p.read_text());g=s['target']['gaia'];P=float(g['period']);e=float(g['eccentricity']);w=math.radians(float(g['arg_periastron']));tp=389+float(g['t_periastron']);epoch=timing[r['sample_id']].get('epoch_btjd',float(r['best_window_btjd']));con=[]
 for k in (0,1):
  nu=(math.pi/2 if k==0 else 3*math.pi/2)-w;E=2*math.atan2(math.sqrt(1-e)*math.sin(nu/2),math.sqrt(1+e)*math.cos(nu/2));base=tp+((E-e*math.sin(E))%(2*math.pi))/(2*math.pi)*P;cycle=round((epoch-base)/P);pred=base+cycle*P;con.append({'kind':k,'cycle':cycle,'pred_btjd':pred,'screen_minus_pred_days':epoch-pred,'screen_minus_pred_phase':(epoch-pred)/P})
 out.append({'sample_id':r['sample_id'],'tic':r['tic'],'screen_time_not_fitted':epoch,'gaia_period_days':P,'eccentricity':e,'omega_deg':math.degrees(w),'periastron_btjd':tp,'conjunctions':con,'closest':min(con,key=lambda c:abs(c['screen_minus_pred_days'])),'uncertainty':'unknown: covariance not present in packet; screen time not a fitted center; edge-on approximation','source_packet_sha256':hashlib.sha256(p.read_bytes()).hexdigest()});print(r['sample_id'],round(out[-1]['closest']['screen_minus_pred_days'],3),round(out[-1]['closest']['screen_minus_pred_phase'],4))
(B/'lead-gaia-geometry.json').write_text(json.dumps(out,indent=2))

