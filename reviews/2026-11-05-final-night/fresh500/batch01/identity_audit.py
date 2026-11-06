import csv,json,hashlib
from pathlib import Path
b=Path(__file__).resolve().parent;q=list(csv.DictReader((b/'queue.csv').open()));p=json.loads((b.parent.parent/'fresh-band-extra500/population.json').read_text())['targets'];audit=[]
for r in q:
 t=r['tic'];d=json.loads((b/t/'lead-context.json').read_text());g=p[t]['gaia'];assert g['source_id']==r['gaia_dr3'];assert all(str(s['header']['TICID'])==t for s in d['sectors']);assert abs(float(g['period'])-float(r['gaia_period']))<1e-9;audit.append(dict(tic=t,gaia_dr3=r['gaia_dr3'],identity='pass',source_headers=[s['header'] for s in d['sectors']]))
(b/'identity-audit.json').write_text(json.dumps(audit,indent=2))
