"""Bounded F008 two-kind alias intervals from partial-event timing ranges."""
import json
from pathlib import Path
B=Path(__file__).resolve().parent
deep0=(1645.5,1647.0);deep1=(3846.1,3846.5)
shallow0=(2370.9,2371.3);shallow1=(3120.6,3121.4)
def intervals(a,b,ks):
 return [{'cycles':k,'period_min_days':(b[0]-a[1])/k,'period_max_days':(b[1]-a[0])/k} for k in ks]
d=intervals(deep0,deep1,[43,44,45,86,88,90]);s=intervals(shallow0,shallow1,[14,15,16,28,30,32]);overlap=[]
for x in d:
 for y in s:
  lo=max(x['period_min_days'],y['period_min_days']);hi=min(x['period_max_days'],y['period_max_days'])
  if lo<=hi:overlap.append({'deep_cycles':x['cycles'],'shallow_cycles':y['cycles'],'shared_period_min_days':lo,'shared_period_max_days':hi})
out={'deep_partial_btjd_interval':deep0,'deep_full_btjd_interval':deep1,'shallow_full_btjd_interval':shallow0,'shallow_partial_btjd_interval':shallow1,'deep_aliases':d,'shallow_aliases':s,'intersections':overlap,'interpretation':'Conservative approximate center intervals. Near-50-day k44/k15 intersection is supported. Near-25-day harmonic k88/k30 also intersects numerically; it predicts a deep-kind occurrence at the observed S39 shallow event, so stable distinct eclipse kinds disfavor it. Morphology evolution could weaken this exclusion. External Gaia/VSX clocks are corroboration, not measured cycle counts.'}
(B/'f008-cycle-intersection.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf8')
print(overlap)
