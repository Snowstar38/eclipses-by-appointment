"""Freeze SHA256 receipt for every batch03 leaf file except this manifest and root acceptance."""
from pathlib import Path
import hashlib,json
B=Path(__file__).resolve().parent
files={}
for p in sorted(B.rglob('*')):
    if not p.is_file() or p.name in {'SHA256SUMS.json','ROOT-ACCEPTANCE.json'}:continue
    files[str(p.relative_to(B)).replace('\\','/')]=hashlib.sha256(p.read_bytes()).hexdigest()
(B/'SHA256SUMS.json').write_text(json.dumps(dict(files=files),indent=2)+'\n',encoding='utf8')
print(len(files),'hashed files')
