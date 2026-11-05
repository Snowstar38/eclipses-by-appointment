"""Hash all batch-local review artifacts except this manifest."""
import hashlib,json
from pathlib import Path
B=Path(__file__).resolve().parent
items={str(p.relative_to(B)).replace('\\','/'):hashlib.sha256(p.read_bytes()).hexdigest() for p in B.rglob('*') if p.is_file() and p.name!='SHA256SUMS.json'}
(B/'SHA256SUMS.json').write_text(json.dumps({'algorithm':'sha256','files':dict(sorted(items.items()))},indent=2)+'\n',encoding='utf-8')
print(len(items),'batch files hashed')
