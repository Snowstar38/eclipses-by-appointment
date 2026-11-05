import hashlib,json
from pathlib import Path
b=Path(__file__).resolve().parent
files={str(p.relative_to(b)).replace('\\','/'):hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(b.rglob('*')) if p.is_file() and p.name not in ('SHA256SUMS.json','ROOT-ACCEPTANCE.json')}
(b/'SHA256SUMS.json').write_text(json.dumps({'files':files},indent=2)+'\n',encoding='utf8')
