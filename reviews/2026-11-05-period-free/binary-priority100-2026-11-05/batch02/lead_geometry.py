"""Edge-on conjunction phase diagnostic from the selected Gaia NSS orbit."""
import csv,json,math,hashlib
from pathlib import Path
B=Path(__file__).resolve().parent
for r in csv.DictReader((B/'queue.csv').open(newline='',encoding='utf-8')):
    tic=r['tic'];packet_path=B.parent/'source-packets'/tic/'sources.json';g=json.loads(packet_path.read_text())['target']['gaia']
    P=float(g['period']);e=float(g['eccentricity']);w=math.radians(float(g['arg_periastron']));tp=389+float(g['t_periastron'])
    d=json.loads((B/tic/'lead-timing.json').read_text()); events=[]
    for kind,clock in d['kinds'].items():
        for t in clock['mid_btjd']:
            conjunctions=[]
            for k,nu in enumerate((math.pi/2-w,3*math.pi/2-w)):
                E=2*math.atan2(math.sqrt(1-e)*math.sin(nu/2),math.sqrt(1+e)*math.cos(nu/2))
                base=tp+((E-e*math.sin(E))%(2*math.pi))/(2*math.pi)*P
                n=round((t-base)/P);pred=base+n*P
                conjunctions.append({'conjunction':k,'cycle':n,'pred_btjd':pred,'observed_minus_pred_days':t-pred,'phase_offset':(t-pred)/P})
            events.append({'kind':kind,'mid_btjd':t,'conjunctions':conjunctions,'nearest':min(conjunctions,key=lambda c:abs(c['observed_minus_pred_days']))})
    out={'sample_id':r['sample_id'],'tic':tic,'gaia_period_days':P,'eccentricity':e,'omega_degrees':math.degrees(w),'periastron_btjd':tp,'events':events,'model':'edge-on Kepler conjunction approximation; Gaia period can drift over multi-year TESS baseline; not an eclipse-period estimate','source_packet_sha256':hashlib.sha256(packet_path.read_bytes()).hexdigest()}
    (B/tic/'lead-geometry.json').write_text(json.dumps(out,indent=2)+'\n')
    print(r['sample_id'],[(round(x['mid_btjd'],3),round(x['nearest']['phase_offset'],4)) for x in events])
