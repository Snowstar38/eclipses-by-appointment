import json,csv
from pathlib import Path
b=Path('[workspace]/Astra/made/final-night-2026-11-05/fresh1000/first/batch04');cat=b.parent/'shared-catalogues';ids={r['tic'] for r in csv.DictReader((b/'queue.csv').open())};out={}
for name in ['target-results.json','literature-adjudication.json','kebc-toi-matches.json','local-table-matches-60arcsec.json']:
 d=json.loads((cat/name).read_text());out[name]=[x for x in d if isinstance(x,dict) and str(x.get('tic','')) in ids] if isinstance(d,list) else d
(b/'lead-catalogue-scope.json').write_text(json.dumps(out,indent=2));print(json.dumps(out['target-results.json'][-1],indent=2))
