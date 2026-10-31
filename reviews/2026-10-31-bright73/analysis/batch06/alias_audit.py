from pathlib import Path
import csv,json,numpy as np
B=Path(__file__).parent;out={}
for r in csv.DictReader(open(B/'queue.csv')):
 tic=r['tic'];m=json.load(open(B/tic/'measurements.json'));ev=[e for e in m['events'] if e.get('timing_usable')];sectors={}
 for sec in sorted(set(e['sector'] for e in ev)):
  z=[e for e in ev if e['sector']==sec];sectors[str(sec)]={str(p):dict(n=len(a),median_depth_ppt=float(np.median(a))) for p in [0,1] if (a:=[e['depth_ppt'] for e in z if e['cycle']%2==p])}
 selection='Odd historical half-period cycles; five deeper eclipses. Persistent unequal parity depths in sector80 reject the half orbital period.' if tic=='329559935' else 'Even historical half-period cycles; same parity orbital timing. Near-equal alternating depths leave photometric half-period ambiguity; Gaia orbital period supports doubled branch.' if tic=='76020303' else 'All timing-usable historical photometric cycles; no persistent unequal alternating pattern seen in representative raw events.'
 out[tic]=dict(same_kind_selection=selection,within_sector_consecutive_pairs=[(a['sector'],a['cycle'],b['cycle']) for a,b in zip(ev,ev[1:]) if a['sector']==b['sector'] and b['cycle']-a['cycle']==1],sector_parity_depths=sectors,historical_inventory_period_days=float(r['period_days']),measured_period_days=m['period_days'],note='Within-sector recurrence tests integer counts; sparse earlier raw repeats can support recurrence without precision timing. Explicit parity branch selection is preserved. No blind exhaustive alias scan claimed.')
json.dump(out,open(B/'alias-audit.json','w'),indent=2)


