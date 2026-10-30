import json,csv
from pathlib import Path
B=Path(__file__).parent;D=B.parent;ids=list(json.load(open(B/'targets-selected.json')));C={r['tic']:r for r in csv.DictReader((D/'shared-catalogues/coverage-matrix.csv').open())};(B/'catalogue-scope.json').write_text(json.dumps({t:C[t] for t in ids},indent=2));print([(t,C[t]['scoped_prior_eb_status']) for t in ids])
