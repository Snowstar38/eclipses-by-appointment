import json,numpy as np
from pathlib import Path
b=Path(__file__).resolve().parent
aliases=json.loads((b/'lead-alias-covered-windows.json').read_text());out={}
for tic,tests in aliases.items():
 btimes=[]
 if tic=='165828134':
  ev=json.loads((b/tic/'lead-timing.json').read_text());btimes=[next(e['center_btjd'] for e in ev if e['sector']==11),next(e['center_btjd'] for e in ev if e['sector']==37 and e['kind']=='kindB')]
 for e in tests:
  e['second_kind_residual_d']=abs((btimes[1]-btimes[0])-round((btimes[1]-btimes[0])/e['period_d'])*e['period_d']) if btimes else None
  e['joint_timing_compatible']=e['timing_compatible'] and (not btimes or e['second_kind_residual_d']<.04)
 survivors=[e for e in tests if e['joint_timing_compatible'] and not e['nulls']]
 out[tic]={'survivors':[{k:e[k] for k in ['label','period_d','covered','timing_compatible','second_kind_residual_d']} for e in survivors],'second_kind_times_btjd':btimes,'note':'Integer families scanned from5 to~100d plus divisors2-6. A survivor requires every same-kind time and separately the second-kind interval where available; opposite conjunctions are not pooled. Coverage null criteria in lead_aliases.py. Scope is bounded, not exhaustive arbitrary-period search.'}
print(json.dumps(out,indent=2));(b/'lead-alias-summary.json').write_text(json.dumps(out,indent=2))
