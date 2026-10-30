import json
from pathlib import Path
r=Path('.'); p=r/'independent-results.json'; d=json.load(p.open());
for x in d:
 if x.get('error')=='MAST product inventory timed out': x['error']='No MAST product inventory was supplied; archive pipeline search not attempted.'
json.dump(d,p.open('w'),indent=2)
raw=json.load(open('raw-events.json'))
for k,v in raw.items():
 good=[e for e in v['events'] if 'tc' in e and not e['edge'] and e['depth']>3*e['residual_rms']]
 print(k, [(e['sector'], round(e['depth'],4),round(e['duration_d'],3)) for e in good], v['representative_ephemeris'])
