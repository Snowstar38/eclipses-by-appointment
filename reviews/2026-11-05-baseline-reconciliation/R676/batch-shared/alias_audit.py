import csv,json
from pathlib import Path
import numpy as np
B=Path(__file__).resolve().parent;out={}
for r in csv.DictReader((B/'queue.csv').open()):
    tic=r['tic'];m=json.loads((B/tic/'measurements.json').read_text());e=[z for z in m['events'] if z.get('timing_usable')];sectors={}
    for sec in sorted({z['sector'] for z in e}):
        sectors[str(sec)]={str(p):dict(n=len(a),median_depth_ppt=float(np.median(a))) for p in (0,1) if (a:=[z['depth_ppt'] for z in e if z['sector']==sec and z['cycle']%2==p])}
    pairs=[dict(sector=a['sector'],cycle_a=a['cycle'],cycle_b=b['cycle'],delta_days=b['mid_btjd']-a['mid_btjd']) for a,b in zip(e,e[1:]) if a['sector']==b['sector'] and b['cycle']-a['cycle']==1]
    out[tic]=dict(sector_parity_depths=sectors,adjacent_cycle_pairs=pairs,adopted_period_days=m['period_days'],search_period_days=m['historical_period_days'],note=('Two nearly equal-depth dips per Gaia orbit; adopted same-kind even-cycle period, with half-period photometric alias retained.' if tic=='54054420' else 'Representative same-kind recurrence and phase/parity inspected; no exhaustive blind alias search.'))
(B/'alias-audit.json').write_text(json.dumps(out,indent=2))
