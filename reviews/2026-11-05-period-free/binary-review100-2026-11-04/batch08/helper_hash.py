from pathlib import Path
import json,hashlib
B=Path(__file__).resolve().parent
paths=sorted(p for p in B.rglob('helper*') if p.is_file() and p.name!='helper-SHA256SUMS.json')
(B/'helper-SHA256SUMS.json').write_text(json.dumps({str(p.relative_to(B)):hashlib.sha256(p.read_bytes()).hexdigest() for p in paths},indent=2)+'\n')
