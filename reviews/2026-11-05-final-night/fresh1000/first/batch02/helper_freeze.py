import csv,json,hashlib
from pathlib import Path
B=Path(__file__).resolve().parent
rows=list(csv.DictReader((B/'queue.csv').open()))
out={}
for row in rows:
 d=B/row['tic']; j=json.loads((d/'helper-localization.json').read_text()); n=json.loads((d/'helper-gaia-neighbors.json').read_text()); files=sorted(d.glob('helper-*'))
 out[row['sample_id']]={'tic':row['tic'],'localization':j,'neighbors':n,'files_sha256':{str(p.relative_to(B)):hashlib.sha256(p.read_bytes()).hexdigest() for p in files if p.is_file()}}
(B/'helper-numeric-audit.json').write_text(json.dumps(out,indent=2),encoding='utf8')
