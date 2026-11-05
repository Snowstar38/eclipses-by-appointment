"""Hash all finished shared-catalogue artifacts, excluding the manifest itself."""
import hashlib,json
from pathlib import Path
h=Path(__file__).resolve().parent
files={p.relative_to(h).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(h.rglob('*')) if p.is_file() and p.name!='SHA256SUMS.json' and '__pycache__' not in p.parts}
(h/'SHA256SUMS.json').write_text(json.dumps(files,indent=2)+'\n',encoding='utf-8')
print(len(files),'artifact hashes')
