from pathlib import Path
import json,hashlib
B=Path(__file__).parent
old=json.load(open(B/'SHA256SUMS.json'))
h={p:hashlib.sha256(Path(p).read_bytes()).hexdigest() for p in old if not Path(p).is_relative_to(B)}
for r in json.load(open(B/'download-receipts.json')):h[r['path']]=hashlib.sha256(Path(r['path']).read_bytes()).hexdigest()
for p in B.rglob('*'):
 if p.is_file() and p.name not in ('SHA256SUMS.json','root-verification.json'):h[str(p)]=hashlib.sha256(p.read_bytes()).hexdigest()
assert (B/'helper-audit.md').exists()
json.dump(h,open(B/'SHA256SUMS.json','w'),indent=2)
print(len(h))
