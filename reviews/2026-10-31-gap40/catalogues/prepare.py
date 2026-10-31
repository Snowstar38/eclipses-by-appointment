import json,csv,hashlib
from pathlib import Path
p=Path('[local path omitted]'); old=Path('[local path omitted]'); src=Path('[local path omitted] 5/made/sb1-scale/targets.json'); targets=json.loads(src.read_text()); q=list(csv.DictReader(open(p.parent/'queue.csv'))); t={r['tic']:targets[r['tic']] for r in q}; assert len(t)==40 and all(x['gaia']['source_id'] for x in t.values()); (p/'targets-selected.json').write_text(json.dumps(t,indent=2)); (p/'identity-provenance.json').write_text(json.dumps({'source':str(src),'sha256':hashlib.sha256(src.read_bytes()).hexdigest(),'scope':'exact 40 queue; TIC source GAIA historically DR2; nested gaia.source_id exact DR3 NSS identity; coordinates retained','queue_sha256':hashlib.sha256((p.parent/'queue.csv').read_bytes()).hexdigest()},indent=2))
for name in ['vsx70.py','asassn.py','eb-battery.py','gaia-vari.py','simbad-targets.py','controls.py','cone-controls.py','assemble.py']:
 s=(old/name).read_text().replace(str(old).replace('\\','/'),str(p).replace('\\','/')).replace('len(rows)==23','len(rows)==40'); (p/name).write_text(s)

