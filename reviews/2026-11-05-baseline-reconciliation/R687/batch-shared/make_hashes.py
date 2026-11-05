"""Freeze all batch03 lead/helper physical evidence, excluding root's mutable catalogues."""
import hashlib,json
from pathlib import Path
W=Path(__file__).resolve().parent
paths=sorted(p for p in W.rglob('*') if p.is_file() and 'shared-catalogues' not in p.parts and p.name!='SHA256SUMS.json')
out={p.relative_to(W).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in paths}
assert len(out)==len(paths)
(W/'SHA256SUMS.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
print(len(out),'flat physical-evidence SHA-256 receipts')
