"""Freeze hashes of all batch02 leaves except acceptance and manifest itself."""
import hashlib,json
from pathlib import Path
B=Path(__file__).resolve().parent
files={}
for p in sorted(B.rglob('*')):
    if not p.is_file() or p.name in ('SHA256SUMS.json','ROOT-ACCEPTANCE.json') or '__pycache__' in p.parts:continue
    h=hashlib.sha256()
    with p.open('rb') as f:
        for block in iter(lambda:f.read(1024*1024),b''):h.update(block)
    files[p.relative_to(B).as_posix()]=h.hexdigest()
(B/'SHA256SUMS.json').write_text(json.dumps(dict(files=files,acceptance_excluded=True),indent=2)+'\n',encoding='utf-8')
print(len(files))
