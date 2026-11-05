import hashlib,json
from pathlib import Path
B=Path(__file__).resolve().parent
files=sorted([p for p in B.rglob('helper*') if p.is_file()]+[p for p in (B/'helper-pixels').rglob('*') if p.is_file()])
files=list(dict.fromkeys(files));d={str(p.relative_to(B)).replace('\\','/'):hashlib.sha256(p.read_bytes()).hexdigest() for p in files if p.name!='helper-hashes.json'}
(B/'helper-hashes.json').write_text(json.dumps(d,indent=2)+'\n');print('hashed',len(d))
