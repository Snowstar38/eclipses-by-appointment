"""Freeze exact batch outputs and verify every used cached source again."""
from pathlib import Path
import csv,hashlib,json
B=Path(__file__).resolve().parent
W=B.parent
H=W.parent/'binary-exploration-2026-11-04'/'bulk-results'
def digest(p): return hashlib.sha256(p.read_bytes()).hexdigest()
out={}
for p in sorted(B.rglob('*')):
 if p.is_file() and p.name not in ('SHA256SUMS.json','ROOT-ACCEPTANCE.json'):
  out[str(p.relative_to(B)).replace('\\','/')]=digest(p)
external=[W/'pilot-seal.json',W/'novelty-audit'/'live'/'gaia_nss-pilot.csv']
for q in csv.DictReader((B/'queue.csv').open(newline='',encoding='utf8')):
 tic=q['tic'];bulk_path=H/f'{tic}.json';bulk=json.loads(bulk_path.read_text(encoding='utf8'))
 assert bulk['tic']==tic
 external.append(bulk_path)
 for r in bulk['files']:
  p=Path(r['path']);sha=digest(p)
  assert sha==r['sha256'],p
  external.append(p)
for p in external:
 assert p.is_file(),p
 out[str(p)]=digest(p)
(B/'SHA256SUMS.json').write_text(json.dumps({'files':out,'scope':'Exact batch V001-V010 outputs, queue seal, used Gaia row source, ten bulk JSON and every cached FITS; excludes ROOT-ACCEPTANCE.'},indent=2)+'\n',encoding='utf8')
print('manifest entries',len(out))
