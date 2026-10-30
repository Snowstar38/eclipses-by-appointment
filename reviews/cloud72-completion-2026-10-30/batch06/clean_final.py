from pathlib import Path
import json
B=Path(__file__).parent;p=B/'decisions.json';d=json.load(open(p))
for tic in ['275022619','257575960']:
 d[tic]['limitations']=d[tic]['limitations'].replace('Refutation applies to the submitted eclipse interpretation, not to binarity or all possible shallow eclipses. ','No secure eclipse identification or exclusion of all possible shallow eclipses follows. ')
p.write_text(json.dumps(d,indent=2))
