import json,hashlib
from pathlib import Path
B=Path(__file__).resolve().parent
paths=sorted(p for p in B.rglob('*') if p.is_file() and (p.name.startswith('helper') or 'helper-pixels' in p.parts) and p.name!='helper-hashes.json')
(B/'helper-hashes.json').write_text(json.dumps({str(p.relative_to(B)):hashlib.sha256(p.read_bytes()).hexdigest() for p in paths},indent=2)+'\n')
