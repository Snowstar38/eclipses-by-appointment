import json,hashlib,csv,py_compile
from pathlib import Path
b=Path(r'[workspace]/Astra\made\final-night-2026-11-05\fresh18\batch02')
for p in b.glob('*.py'):py_compile.compile(str(p),cfile=str(b/'__pycache__'/f'{p.stem}.pyc'),doraise=True)
rows=list(csv.DictReader((b/'RESULTS.csv').open()));q=list(csv.DictReader((b/'queue.csv').open()));assert [(r['sample_id'],r['tic']) for r in rows]==[(r['sample_id'],r['tic']) for r in q];assert all((b/r['report']).exists() for r in rows)
files=[p for p in b.rglob('*') if p.is_file() and p.name!='SHA256SUMS.json' and '__pycache__' not in p.parts];out={str(p.relative_to(b)).replace('\\','/'):hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(files)};(b/'SHA256SUMS.json').write_text(json.dumps(out,indent=2),encoding='utf8');assert all(hashlib.sha256((b/p).read_bytes()).hexdigest()==h for p,h in out.items());print(len(rows),'rows,',len(out),'files hashed and verified')
