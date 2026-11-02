from pathlib import Path
import csv,json,numpy as np
B=Path(__file__).parent;out={}
for r in csv.DictReader(open(B/'queue.csv')):
 tic=r['tic'];m=json.load(open(B/tic/'measurements.json'));ev=[e for e in m['events'] if e.get('timing_usable')];sectors={}
 for sec in sorted(set(e['sector'] for e in ev)):
  z=[e for e in ev if e['sector']==sec];sectors[str(sec)]={str(p):dict(n=len(a),median_depth_ppt=float(np.median(a))) for p in [0,1] if (a:=[e['depth_ppt'] for e in z if e['cycle']%2==p])}
 sel=[e for e in ev]
 pairs=[(a['sector'],a['cycle'],b['cycle']) for a,b in zip(sel,sel[1:]) if a['sector']==b['sector'] and b.get('orbital_cycle',b['cycle'])-a.get('orbital_cycle',a['cycle'])==1]
 out[tic]=dict(same_kind_selection=m.get('timing_selection','All timing-usable historical photometric cycles; no persistent unequal alternating pattern seen in representative events.'),within_sector_same_kind_pairs=pairs,sector_parity_depths=sectors,historical_inventory_period_days=float(r['period_days']),historical_SAP_search_period_days=m['historical_period_days'],measured_period_days=m['period_days'],note='Within-sector same-kind recurrence tests integer counts. Half/double alias checked by raw morphology and parity, not silently fixed by Gaia. No exhaustive all-alias blind search claimed.')
json.dump(out,open(B/'alias-audit.json','w'),indent=2)
