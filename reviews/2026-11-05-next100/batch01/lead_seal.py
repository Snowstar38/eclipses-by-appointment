"""Hash batch01 deliverables, excluding root acceptance and this manifest."""
from pathlib import Path
import hashlib,json
B=Path(__file__).resolve().parent
files={}
for p in sorted(B.rglob('*')):
 if not p.is_file() or '__pycache__' in p.parts or p.name in ('SHA256SUMS.json','ROOT-ACCEPTANCE.json'):continue
 files[p.relative_to(B).as_posix()]=hashlib.sha256(p.read_bytes()).hexdigest()
(B/'SHA256SUMS.json').write_text(json.dumps({'files':files},indent=2)+'\n',encoding='utf-8')
for rel,sha in files.items():assert hashlib.sha256((B/rel).read_bytes()).hexdigest()==sha
print(len(files),'batch01 artifacts sealed')

