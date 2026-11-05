"""Seal review deliverables; leaf manifests also bind locally cached binary data."""
from pathlib import Path
import json,hashlib
W=Path(__file__).resolve().parent
assert json.loads((W/'FINAL-VERIFICATION.json').read_text())['status']=='PASS'
extensions={'.md','.txt','.py','.json','.csv','.png','.tsv','.xml','.html'}
files={}
for p in sorted(W.rglob('*')):
 if not p.is_file() or p.name=='FINAL-SHA256SUMS.json' or '__pycache__' in p.parts:continue
 if p.suffix.lower() not in extensions and p.name!='.gitignore':continue
 files[p.relative_to(W).as_posix()]=hashlib.sha256(p.read_bytes()).hexdigest()
out={'scope':'Review text, source receipts, scripts, tables and figures. FITS/archive bytes are local caches bound by leaf manifests and download receipts; this root manifest excludes itself.','files':files}
p=W/'FINAL-SHA256SUMS.json';p.write_text(json.dumps(out,indent=2)+'\n',encoding='utf8')
for name,h in files.items():assert hashlib.sha256((W/name).read_bytes()).hexdigest()==h
print(len(files),'final artifacts sealed and rechecked')
