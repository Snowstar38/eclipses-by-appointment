"""Seal all batch-owned outputs; external frozen sources retain their own receipts."""
import hashlib,json
from pathlib import Path
B=Path(__file__).resolve().parent
files={}
for p in sorted(B.rglob('*')):
 if p.is_file() and p.name!='SHA256SUMS.json':
  files[p.relative_to(B).as_posix()]=hashlib.sha256(p.read_bytes()).hexdigest()
(B/'SHA256SUMS.json').write_text(json.dumps(files,indent=2)+'\n',encoding='utf-8')
print(len(files))
