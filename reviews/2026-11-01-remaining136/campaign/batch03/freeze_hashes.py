from pathlib import Path
import json,csv,hashlib,os
B=Path(__file__).parent.resolve();H={}
def add(p):
 p=Path(p).resolve();H[Path(os.path.relpath(p,B)).as_posix()]=hashlib.sha256(p.read_bytes()).hexdigest()
for p in json.load(open(B/'source-hashes.json')):add(p)
for p in [B.parent/'targets-selected.json',B.parent/'shared-catalogues/gaia-nss-full.csv',B.parent/'shared-catalogues/coverage-matrix.csv',Path('local-source/Fable 5/made/sb1-scale/search.jsonl'),Path('local-source/Fable 5/made/sb1-scale/c7-sapdepth.json'),B/'methods-read-snapshot.html']:add(p)
for p in B.rglob('*'):
 if p.is_file() and p.name not in ['SHA256SUMS.json','root-verification.json','final-hash-verification.json'] and '__pycache__' not in str(p):add(p)
(B/'SHA256SUMS.json').write_text(json.dumps(dict(sorted(H.items())),indent=2)+'\n',encoding='utf8');print(len(H))

