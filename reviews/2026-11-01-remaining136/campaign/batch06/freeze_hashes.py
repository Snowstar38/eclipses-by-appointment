from pathlib import Path
import json,os,hashlib
B=Path(__file__).parent
H={}
def add(p):
 p=Path(p);H[Path(os.path.relpath(p,B)).as_posix()]=hashlib.sha256(p.read_bytes()).hexdigest()
for path,h in json.load(open(B/'source-hashes.json')).items():
 p=Path(path);assert hashlib.sha256(p.read_bytes()).hexdigest()==h;add(p)
for p in [B.parent/'shared-catalogues/coverage-matrix.csv',B.parent/'shared-catalogues/all-nearby-eb-identity-audit.json',B.parent/'BRIEF.txt',B.parent/'SESSION-SCOPE.txt',Path('local-source/Fable 5/made/sb1-scale/diffimg/diffstack.py')]:add(p)
for p in B.rglob('*'):
 if p.is_file() and p.name not in ('SHA256SUMS.json','root-verification.json','helper-final-verification.json') and '__pycache__' not in str(p):add(p)
(B/'SHA256SUMS.json').write_text(json.dumps(dict(sorted(H.items())),indent=2)+'\n');print(len(H))
