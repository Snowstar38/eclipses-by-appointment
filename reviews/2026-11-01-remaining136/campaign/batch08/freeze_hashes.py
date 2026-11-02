from pathlib import Path
import json,hashlib,os
B=Path(__file__).parent;H={}
def add(p):
 p=Path(p).resolve();H[Path(os.path.relpath(p,B)).as_posix()]=hashlib.sha256(p.read_bytes()).hexdigest()
for p in json.load(open(B/'source-hashes.json')):add(p)
for p in B.rglob('*'):
 if p.is_file() and p.name!='SHA256SUMS.json' and not p.name.startswith('root-') and 'helper-final' not in p.name and '__pycache__' not in str(p):add(p)
(B/'SHA256SUMS.json').write_text(json.dumps(dict(sorted(H.items())),indent=2)+'\n',encoding='utf8')
print(len(H))
