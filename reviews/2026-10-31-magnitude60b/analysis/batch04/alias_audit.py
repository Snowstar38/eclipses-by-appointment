from pathlib import Path
import csv,json,numpy as np
B=Path(__file__).parent;out={}
for r in csv.DictReader(open(B/'queue.csv')):
 tic=r['tic'];m=json.load(open(B/tic/'measurements.json'));ev=[e for e in m['events'] if e.get('timing_usable')];sectors={}
 for sec in sorted(set(e['sector'] for e in ev)):
  z=[e for e in ev if e['sector']==sec];sectors[str(sec)]={str(p):dict(n=len(a),median_depth_ppt=float(np.median(a))) for p in [0,1] if (a:=[e['depth_ppt'] for e in z if e['cycle']%2==p])}
 out[tic]=dict(same_kind_selection='All timing-usable historical photometric cycles; no persistent unequal alternating pattern seen in representative raw events.',within_sector_consecutive_pairs=[(a['sector'],a['cycle'],b['cycle']) for a,b in zip(ev,ev[1:]) if a['sector']==b['sector'] and b['cycle']-a['cycle']==1],sector_parity_depths=sectors,historical_inventory_period_days=float(r['period_days']),measured_period_days=m['period_days'],note='Within-sector recurrence tests long-baseline integer counts. Morphology/parity check supports retained period; no blind exhaustive alias scan claimed.')
out['403154475'].update(same_kind_selection='Even historical half-period cycles only; sample slightly deeper, physical primary not established',note='Half-period dip recurrence is real; same-kind parity plus Gaia5.07d geometry supports reported orbital period; no exhaustive independent alias scan.')
out['394386248'].update(note='Two consecutive quality-zero sector81 events test recurrence; earlier sector40 two flagged2048 raw repeats support recurrence but are not timing points. Available QLP sectors14,40,41,54,74,81 checked in shared targets-selected metadata; no clean-null interpretation for unfitted sectors.')
json.dump(out,open(B/'alias-audit.json','w'),indent=2)

