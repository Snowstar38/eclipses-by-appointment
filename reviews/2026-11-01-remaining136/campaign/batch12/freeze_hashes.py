from pathlib import Path
import json,hashlib,os
B=Path(__file__).parent.resolve();H={}
def add(p):
 p=Path(p).resolve();H[Path(os.path.relpath(p,B)).as_posix()]=hashlib.sha256(p.read_bytes()).hexdigest()
for p,h in json.load(open(B/'source-hashes.json')).items():
 assert hashlib.sha256(Path(p).read_bytes()).hexdigest()==h,p
 add(p)
for p in [B.parent/'shared-catalogues/coverage-matrix.csv',B.parent/'shared-catalogues/AUDIT.md']:add(p)
for p in B.rglob('*'):
 if p.is_file() and p.name!='SHA256SUMS.json' and not p.name.startswith(('root-','helper-final','helper-frozen')) and '__pycache__' not in str(p):add(p)
(B/'SHA256SUMS.json').write_text(json.dumps(dict(sorted(H.items())),indent=2)+'\n',encoding='utf8')
print('Frozen',len(H),'artifacts; generators stop now')
