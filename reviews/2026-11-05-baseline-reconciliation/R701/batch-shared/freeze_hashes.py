"""Write a flat per-file SHA-256 manifest after all review artifacts are final."""
import hashlib, json
from pathlib import Path

B=Path(__file__).resolve().parent
out={}
for p in sorted(B.rglob('*')):
    if p.is_file() and p.name!='SHA256SUMS.json' and '__pycache__' not in p.parts:
        out[p.relative_to(B).as_posix()]=hashlib.sha256(p.read_bytes()).hexdigest()
(B/'SHA256SUMS.json').write_text(json.dumps(dict(root='review_cached10',algorithm='sha256',files=out),indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
print(len(out),'files')
