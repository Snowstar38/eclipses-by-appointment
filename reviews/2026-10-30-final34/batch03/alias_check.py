import json,numpy as np
from pathlib import Path
B=Path(__file__).parent;Q=json.loads((B/'raw-evidence/qlp-results.json').read_text());R=json.loads((B/'raw-evidence/raw-events.json').read_text());out={}
for tic in ['407991939','407220461']:
 out[tic]={}
 for name,data in [('qlp',Q),('custom',R)]:
  out[tic][name]={}
  for parity in [0,1]:
   events=[e for e in data[tic]['events'] if e['cycle']%2==parity and not (tic=='407220461' and e['cycle']==336)]
   period=float(np.polyfit([e['cycle']/2 for e in events],[e['tc'] for e in events],1)[0])
   out[tic][name][str(parity)]={'period_d':period,'events':[{k:e[k] for k in ['cycle','tc','depth']} for e in events]}
(B/'alias-check.json').write_text(json.dumps(out,indent=2))
