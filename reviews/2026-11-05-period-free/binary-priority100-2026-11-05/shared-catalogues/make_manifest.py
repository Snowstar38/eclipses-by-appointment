"""Write SHA256 for this directory's reproducible audit artifacts."""
import hashlib,json
from pathlib import Path
H=Path(__file__).resolve().parent
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
files=sorted(p for p in H.iterdir() if p.is_file() and p.name!='SHA256SUMS.json')
(H/'SHA256SUMS.json').write_text(json.dumps({'files':{p.name:sha(p) for p in files}},indent=2)+'\n',encoding='utf-8')
