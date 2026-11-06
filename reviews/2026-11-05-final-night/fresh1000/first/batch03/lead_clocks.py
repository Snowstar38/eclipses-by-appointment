import json,numpy as np
from pathlib import Path
b=Path(__file__).resolve().parent
ev=json.loads((b/'25073050/lead-timing.json').read_text());s=[e for e in ev if e['kind']=='shallow'];t=np.array([e['center_btjd'] for e in s]);err=np.array([max(e['center_formal_error_d'],e['cadence_d']/2,.002) for e in s]);p=t[1]-t[0]
out={'25073050':dict(period_d=p,epoch_btjd=t[0],formal_period_error_d=float(np.hypot(*err)),cycles=[0,1],times=t.tolist(),residuals=[0,0],duration_d=float(np.mean([e['duration_d'] for e in s])),depth_ppt=float(np.mean([e['depth_ppt'] for e in s])),gaia_period_d=24.285909256317957,deep_event_btjd=ev[1]['center_btjd'],deep_phase=float((ev[1]['center_btjd']-t[0])/p),note='One same-kind interval between two shallow eclipses. Deep event is opposite conjunction, not a third same-kind timing. Formal difference error has a 0.002d event floor; no O-C scatter or precision long baseline inferred. Sector80 common timing offset cancels in same-sector interval; shape/baseline systematic allowance 0.02d is heuristic, not calibrated.')}
(b/'lead-clocks.json').write_text(json.dumps(out,indent=2));print(out)
