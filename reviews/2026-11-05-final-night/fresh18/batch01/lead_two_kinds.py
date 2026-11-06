import json,numpy as np
from pathlib import Path
b=Path('[workspace]/Astra/made/final-night-2026-11-05/fresh18/batch01');out={}
for tic,trial in [('22559994',47.1225),('156747165',37.88714)]:
 e=json.loads((b/tic/'lead-timing.json').read_text());tracks={k:sorted([x for x in e if x['kind']==k and x['fit_usable']],key=lambda v:v['center_btjd']) for k in ['deep','shallow']};spans={k:v[-1]['center_btjd']-v[0]['center_btjd'] for k,v in tracks.items()};tests=[]
 for n in range(1,int(spans['deep']/5)+1):
  p=spans['deep']/n
  if p>100:continue
  m=round(spans['shallow']/p);res=spans['shallow']-m*p
  tests.append(dict(deep_cycles=n,period_d=p,shallow_cycles=m,shallow_span_residual_d=res,compatible_0p04d=abs(res)<.04))
 n0=round(spans['deep']/trial);period=spans['deep']/n0;shorts=[x for x in tests if x['compatible_0p04d']]
 out[tic]=dict(tracks={k:[dict(sector=x['sector'],center_btjd=x['center_btjd'],depth_ppt=x['depth_ppt']) for x in v] for k,v in tracks.items()},spans_d=spans,cycle_trial_d=trial,neighbor_integer_tests=[x for x in tests if abs(x['deep_cycles']-n0)<=2],compatible_5to100d=shorts,deep_to_following_shallow_d=(tracks['shallow'][0]['center_btjd']-tracks['deep'][0]['center_btjd'])%period,interpretation='Kinds each recur across distinct sectors; opposite kinds do not count as same-kind recurrence. Cycle-family candidates selected by both spans; covered-window audit tests short submultiples. No exhaustive ephemeris posterior.')
 print(tic,'spans',spans,'compatible',[(x['period_d'],x['deep_cycles'],x['shallow_span_residual_d']) for x in shorts])
(b/'lead-two-kind-aliases.json').write_text(json.dumps(out,indent=2))
