import json,hashlib
from pathlib import Path
B=Path(__file__).parent;files={}
for p in B.rglob('*'):
 if p.is_file() and p.name not in ['SHA256SUMS.json','root-verification.json','final-validation.json'] and '__pycache__' not in p.parts:files[p.relative_to(B).as_posix()]=hashlib.sha256(p.read_bytes()).hexdigest()
for r in json.load(open(B/'measurement-source-receipts.json')):
 p=Path(r['path']);files[Path(__import__('os').path.relpath(p,B)).as_posix()]=hashlib.sha256(p.read_bytes()).hexdigest()
for p,h in json.load(open(B/'source-hashes.json')).items():
 p=Path(p);assert hashlib.sha256(p.read_bytes()).hexdigest()==h;files[Path(__import__('os').path.relpath(p,B)).as_posix()]=h
for p in [B.parent/'targets-selected.json', B.parent/'shared-catalogues/gaia-nss-full.csv',Path('local-source/Fable 5/made/sb1-scale/search.jsonl'),Path('local-source/Fable 5/made/sb1-scale/c7-sapdepth.json')]:
 files[Path(__import__('os').path.relpath(p,B)).as_posix()]=hashlib.sha256(p.read_bytes()).hexdigest()
(B/'SHA256SUMS.json').write_text(json.dumps(dict(sorted(files.items())),indent=2)+'\n');print(len(files))
