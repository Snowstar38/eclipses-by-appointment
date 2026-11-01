"""Enumerate adjacent integer-cycle assignments for the three measured events."""
import json
from pathlib import Path
B=Path(__file__).parent
m=json.loads((B/'34759144'/'measurements.json').read_text())
ev=sorted([x for x in m['events'] if x.get('timing_usable')],key=lambda x:x['mid_btjd'])
assert len(ev)==3
t=[e['mid_btjd'] for e in ev]
hist=m['historical_period_days']
out=[]
for n1 in range(50,66):
 for n2 in range(32,44):
  p1=(t[1]-t[0])/n1;p2=(t[2]-t[1])/n2
  if .85*hist < p1 < 1.15*hist and .85*hist < p2 < 1.15*hist:
   out.append(dict(cycles_first_gap=n1,cycles_second_gap=n2,period_first_days=p1,period_second_days=p2,period_disagreement_days=abs(p1-p2)))
out.sort(key=lambda x:x['period_disagreement_days'])
result=dict(tic='34759144',measured_btjd=t,historical_search_period_days=hist,enumerated_cycle_ranges=[[50,65],[32,43]],tested_period_range='0.85–1.15 of historical period in both gaps',aliases=out)
(B/'34759144-alias-enumeration.json').write_text(json.dumps(result,indent=2)+'\n')
print(out[:5])
