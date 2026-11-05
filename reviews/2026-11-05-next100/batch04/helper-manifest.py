"""Record SHA256 of every helper artifact, excluding the self-referential manifest."""
import hashlib
import json
from pathlib import Path
B=Path(__file__).resolve().parent
entries={p.name:{'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'bytes':p.stat().st_size}
         for p in sorted(B.glob('helper-*')) if p.name!='helper-SHA256SUMS.json' and p.is_file()}
(B/'helper-SHA256SUMS.json').write_text(json.dumps(entries,indent=2)+'\n',encoding='utf8')
print(len(entries),'helper files sealed')
