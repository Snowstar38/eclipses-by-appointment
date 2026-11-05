"""Seal batch-10 artifacts except manifest and root acceptance."""
import hashlib,json
from pathlib import Path
B=Path(__file__).resolve().parent
files={str(p.relative_to(B)):hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(B.rglob('*')) if p.is_file() and p.name not in ('SHA256SUMS.json','ROOT-ACCEPTANCE.json','ROOT-ACCEPTANCE.md')}
(B/'SHA256SUMS.json').write_text(json.dumps({'files':files},indent=2)+'\n',encoding='utf-8')
print(len(files),'files sealed')
