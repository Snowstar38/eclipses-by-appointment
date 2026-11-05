import hashlib,json
from pathlib import Path
ps=[p for p in Path('.').glob('helper-*') if p.is_file() and p.name!='helper-SHA256SUMS.json']+list(Path('helper-tesscut').glob('*'))
Path('helper-SHA256SUMS.json').write_text(json.dumps({str(p):hashlib.sha256(p.read_bytes()).hexdigest() for p in ps},indent=2)+'\n')
