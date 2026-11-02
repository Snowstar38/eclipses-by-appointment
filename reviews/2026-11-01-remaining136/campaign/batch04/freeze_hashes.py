from pathlib import Path
import json,hashlib,os,csv
B=Path(__file__).parent.resolve();SB=Path('local-source/Fable 5/made/sb1-scale');H={};sources={}
def add(p,source=False):
 p=Path(p).resolve();h=hashlib.sha256(p.read_bytes()).hexdigest();H[Path(os.path.relpath(p,B)).as_posix()]=h
 if source:sources[str(p)]=h
for rec in json.load(open(B/'measurement-source-receipts.json')):add(rec['path'],True)
for rec in json.load(open(B/'terra-pixel-audit.json')):add(rec['cutout'],True)
for t in [r['tic'] for r in csv.DictReader(open(B/'queue.csv'))]:
 for p in (SB/'diffimg'/t).glob('*'):
  if p.is_file() and (p.name=='gaia.json' or p.name.startswith('diff_s')):add(p,True)
for p in [B.parent/'targets-selected.json',B.parent/'shared-catalogues/gaia-nss-full.csv',B.parent/'shared-catalogues/coverage-matrix.csv',SB/'search.jsonl',SB/'c7-sapdepth.json',SB/'diffimg/diffstack.py']:add(p,True)
(B/'source-hashes.json').write_text(json.dumps(sources,indent=2)+'\n')
for p in B.rglob('*'):
 if p.is_file() and p.name not in ['SHA256SUMS.json','root-verification.json','root-numeric-verification.json','final-hash-verification.json'] and '__pycache__' not in str(p):add(p)
(B/'SHA256SUMS.json').write_text(json.dumps(dict(sorted(H.items())),indent=2)+'\n');print(len(H))
