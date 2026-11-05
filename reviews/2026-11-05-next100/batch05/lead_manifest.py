"""Seal every batch05 leaf, excluding the manifest and root acceptance file."""
import hashlib,json
from pathlib import Path
B=Path(__file__).resolve().parent
files={p.relative_to(B).as_posix():hashlib.sha256(p.read_bytes()).hexdigest()
       for p in sorted(B.rglob('*')) if p.is_file() and p.name not in ('SHA256SUMS.json','ROOT-ACCEPTANCE.json')}
(B/'SHA256SUMS.json').write_text(json.dumps({'files':files},indent=2,ensure_ascii=False)+'\n',encoding='utf8')
print(len(files),'files sealed')
