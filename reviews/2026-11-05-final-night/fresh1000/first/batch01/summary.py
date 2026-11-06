import json
from pathlib import Path
b=Path(__file__).resolve().parent;g=json.loads((b/'lead-gaia-covariance.json').read_text());a=json.loads((b/'lead-alias-covered-windows.json').read_text())
for t,x in g.items():print(t,'Gaia',x['gaia_period_d'],x['gaia_period_error_d'],'e',x['eccentricity'])
print('Z005 survivors times+null:',[(r['label'],r['period_d']) for r in a['92872537'] if r['timing_compatible'] and not r['nulls']])
