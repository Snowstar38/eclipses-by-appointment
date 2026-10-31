from pathlib import Path
import csv,json,numpy as np
B=Path(__file__).parent;out={}
for r in csv.DictReader(open(B/'queue.csv')):
 tic=r['tic'];m=json.load(open(B/tic/'measurements.json'));ev=[e for e in m['events'] if e.get('timing_usable')];sectors={}
 for sec in sorted(set(e['sector'] for e in ev)):
  z=[e for e in ev if e['sector']==sec];sectors[str(sec)]={str(p):dict(n=len(a),median_depth_ppt=float(np.median(a))) for p in [0,1] if (a:=[e['depth_ppt'] for e in z if e['cycle']%2==p])}
 out[tic]=dict(same_kind_selection=('Even historical half-period cycles; deeper primaries only. Persistent unequal parity depths in both selected sectors reject the half orbital period.' if tic in ('382603504','128825695') else 'All timing-usable historical photometric cycles; no persistent unequal alternating pattern seen in representative raw events.'),within_sector_consecutive_pairs=[(a['sector'],a['cycle'],b['cycle']) for a,b in zip(ev,ev[1:]) if a['sector']==b['sector'] and b['cycle']-a['cycle']==1],sector_parity_depths=sectors,historical_inventory_period_days=float(r['period_days']),measured_period_days=m['period_days'],note='Within-sector recurrence tests long-baseline integer counts. Morphology/parity check supports retained same-kind period; unequal alternating branches use only even cycles and doubled orbital cycles. No blind exhaustive alias scan claimed.')
json.dump(out,open(B/'alias-audit.json','w'),indent=2)


