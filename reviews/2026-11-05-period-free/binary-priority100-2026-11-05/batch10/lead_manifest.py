"""Freeze SHA256 of batch artifacts and reviewed source inputs."""
import csv,json,hashlib
from pathlib import Path
B=Path(__file__).resolve().parent
def sha(p):
 h=hashlib.sha256()
 with p.open('rb') as f:
  for block in iter(lambda:f.read(1024*1024),b''):h.update(block)
 return h.hexdigest()
files={str(p.relative_to(B)).replace('\\','/'):sha(p) for p in sorted(B.rglob('*')) if p.is_file() and p.name not in ('SHA256SUMS.json','ROOT-ACCEPTANCE.json') and '__pycache__' not in p.parts}
sources={}
for r in csv.DictReader((B/'queue.csv').open()):
 tic=r['tic'];m=json.loads((B/tic/'lead-numeric.json').read_text())
 for x in m['sources']:
  p=Path(x['path']);v=sha(p);assert v==x['sha256'];sources[str(p)]=v
 p=B.parent/'source-packets'/tic/'sources.json';sources[str(p)]=sha(p)
for name in ('target-evidence.json','gaia-neighbors.json','REPORT.md','TARGET-STATUS.csv'):
 p=B.parent/'shared-catalogues'/name;sources[str(p)]=sha(p)
out=dict(batch='batch10',files=files,reviewed_sources=sources)
(B/'SHA256SUMS.json').write_text(json.dumps(out,indent=2)+'\n')
print(len(files),'batch files',len(sources),'source files')
