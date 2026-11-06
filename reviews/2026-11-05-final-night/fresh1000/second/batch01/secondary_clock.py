import json,numpy as np
from pathlib import Path
b=Path(__file__).resolve().parent;t='272726082';ev=json.loads((b/t/'lead-timing.json').read_text());sec=[e for e in ev if e.get('fit_usable') and 8<e['depth_ppt']<20];x=np.array([e['center_btjd'] for e in sec]);p=45.01584602;n=np.round((x-x[0])/p);v=np.polyfit(n,x,1);o={'same_kind':'shallow opposite conjunction','times_btjd':x.tolist(),'cycles':n.tolist(),'period_d':float(v[0]),'epoch_btjd':float(v[1]),'residuals_d':(x-n*v[0]-v[1]).tolist(),'note':'S84 andS85 are consecutive same-kind shallow eclipses. This is a separate clock from deep primaries; it does not treat opposite conjunction as same-kind recurrence.'};al=json.loads((b/'lead-alias-covered-windows.json').read_text());o['alias_secondary_timing_tests']=[]
for r in al[t]:
 if not r['timing_compatible'] or r['nulls']:continue
 pp=r['period_d'];res=(x-x[0])-np.round((x-x[0])/pp)*pp;o['alias_secondary_timing_tests'].append({'label':r['label'],'period_d':pp,'secondary_residuals_d':res.tolist(),'secondary_timing_compatible':bool(max(abs(res))<.04)})
(b/t/'lead-secondary-clock.json').write_text(json.dumps(o,indent=2));print(json.dumps(o,indent=2))
