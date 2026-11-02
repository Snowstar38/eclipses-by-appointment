from pathlib import Path
import json,csv,hashlib,os
B=Path(__file__).parent.resolve();H={}
def add(p):
 p=Path(p).resolve();H[Path(os.path.relpath(p,B)).as_posix()]=hashlib.sha256(p.read_bytes()).hexdigest()
for r in json.load(open(B/'measurement-source-receipts.json')):add(r['path'])
for p in [B.parent/'targets-selected.json',B.parent/'shared-catalogues/gaia-nss-full.csv',B.parent/'shared-catalogues/sha256-manifest.csv',B.parent/'shared-catalogues/coverage-matrix.csv',Path('local-source/Fable 5/made/sb1-scale/search.jsonl'),Path('local-source/Fable 5/made/sb1-scale/c7-sapdepth.json')]:add(p)
for r in csv.DictReader(open(B/'queue.csv')):
 d=json.load(open(B/r['tic']/'fresh-pixels/diff_fresh.json'));add(Path('local-source/sky/data/sb1-scale-c3')/('vet'+r['tic'])/f"tesscut_s{d['sector']:03d}.fits")
for p in B.rglob('*'):
 if p.is_file() and p.name not in ['SHA256SUMS.json','root-verification.json','root-numeric-verification.json','final-hash-verification.json'] and '__pycache__' not in str(p):add(p)
(B/'SHA256SUMS.json').write_text(json.dumps(dict(sorted(H.items())),indent=2)+'\n')
print(len(H))
