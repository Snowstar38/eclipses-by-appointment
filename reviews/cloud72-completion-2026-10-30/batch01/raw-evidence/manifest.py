from pathlib import Path
import json,hashlib
r=Path(__file__).parent;out=[]
for p in sorted(r.rglob('*')):
 if p.is_file() and p.name!='receipt-manifest.json':
  out.append(dict(path=str(p.relative_to(r)).replace('\\','/'),bytes=p.stat().st_size,sha256=hashlib.sha256(p.read_bytes()).hexdigest()))
json.dump(out,open(r/'receipt-manifest.json','w'),indent=2)
print(len(out))
