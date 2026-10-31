from pathlib import Path
import json,csv,hashlib
B=Path(__file__).parent;SB=Path('[local path omitted]')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
paths=[B.parent/'targets-selected.json',B.parent/'shared-catalogues/gaia-nss-full.csv',SB/'search.jsonl',SB/'c5-sapdepth.json',SB/'diffstack.py',SB/'c3_sapdepth.py']
for r in csv.DictReader(open(B/'queue.csv')):
 t=r['tic'];p=json.load(open(B/'pixel-audit.json'))[t];src=Path(p['difference_path']);paths.extend([src,src.with_suffix('.png'),src.parent/'gaia.json',Path(p['cutout_path'])])
 paths.extend(Path(x['path']) for x in json.load(open(B/t/'measurements.json'))['sources'])
json.dump({str(p):sha(p) for p in paths if p.is_file()},open(B/'source-hashes.json','w'),indent=2)
manifest={p.relative_to(B).as_posix():sha(p) for p in sorted(B.rglob('*')) if p.is_file() and p.name!='SHA256SUMS.json'}
json.dump(manifest,open(B/'SHA256SUMS.json','w'),indent=2)
