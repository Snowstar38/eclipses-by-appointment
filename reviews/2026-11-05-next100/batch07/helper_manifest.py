import hashlib,json
from pathlib import Path
B=Path(__file__).resolve().parent
out={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(B.glob('helper*')) if p.is_file() and p.name!='helper-manifest.json'}
(B/'helper-manifest.json').write_text(json.dumps(out,indent=2)+'\n')
