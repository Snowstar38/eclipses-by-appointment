"""Inventory every batch-local deliverable except this self-referential manifest."""
import hashlib,json
from pathlib import Path
B=Path(__file__).resolve().parent
files={}
for p in sorted(B.rglob('*')):
    if p.is_file() and p.name!='SHA256SUMS.json' and p.name!='batch-validation.json':
        files[p.relative_to(B).as_posix()]=hashlib.sha256(p.read_bytes()).hexdigest()
(B/'SHA256SUMS.json').write_text(json.dumps(dict(scope='Batch05 local artifacts; external source packets, cached QLP FITS and shared catalogue receipts are verified in source-verification.json and per-TIC numeric artifacts.',files=files),indent=2)+'\n',encoding='utf-8')
print(len(files))
