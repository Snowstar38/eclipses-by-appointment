"""Transparent hand-selected representative raw-event cycle arithmetic; no automated verdicts."""
import json
from pathlib import Path
B=Path(__file__).resolve().parent
cases={
'F001':{'kind':'deep narrow','events':[(1714.419,0),(1753.010,2),(1907.381,10),(1945.973,12),(1965.252,13),(2621.350,47),(2640.644,48),(2659.941,49),(3354.612,85),(3393.204,87)],'caution':'F001 event source favors capable neighbor; these timings describe blended train only.'},
'F002':{'kind':'short eclipse','events':[(1434.925,0),(2153.951,12),(3951.547,42),(4011.467,43)],'caution':'S97 fitted detector window at 3951.547 retained, not nearby spurious 3941.719.'},
'F006':{'kind':'broad possible eclipse','events':[(3057.805,0),(4083.478,26),(4122.905,27)],'caution':'S100/S101 local trapezoid fit centers are affected by sloping baseline; periods are conditional.'},
'F007':{'kind':'narrow eclipse','events':[(1337.722,0),(3132.851,47),(3171.042,48),(3858.534,66),(3896.731,67)],'caution':'S1 formal covariance singular; clock uses multiple recent resolved events.'},
'F008':{'kind':'two eclipse kinds','deep_events':[(1646.0,0),(3846.274,44)],'shallow_events':[(2371.095,0),(3121.0,15)],'caution':'S12/S66 are partial with approximate center bounds; no precision period inferred.'},
'F010':{'kind':'broad eclipse trains','deep_events':[(1649.352,0),(2377.495,22),(3105.497,44),(3833.891,66)],'other_events':[(1632.862,0),(3850.351,67)],'caution':'Broad timing points from provisional fits/predicted centers; assign no formal error or primary kind.'}
}
for sid,x in cases.items():
 for key in ('events','deep_events','shallow_events','other_events'):
  if key in x:
   ev=x[key];x[key+'_pair_periods']=[{'from_btjd':ev[i][0],'to_btjd':ev[j][0],'cycles':ev[j][1]-ev[i][1],'conditional_period_days':(ev[j][0]-ev[i][0])/(ev[j][1]-ev[i][1])} for i in range(len(ev)) for j in range(i+1,len(ev))]
(B/'review-clocks.json').write_text(json.dumps(cases,indent=2)+'\n',encoding='utf8')
for sid,x in cases.items():
 print(sid,[(k,round(v[0]['conditional_period_days'],5)) for k,v in x.items() if k.endswith('_pair_periods')])
