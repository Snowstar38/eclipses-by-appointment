import json,hashlib
from pathlib import Path
D=Path(__file__).resolve().parent.parent;R=D.parent;M=json.loads((D/'applied-manifest.json').read_text()); bad=[]
for m in M:
 p=R/m['path']; h=hashlib.sha256(p.read_bytes()).hexdigest()
 if h!=m['after_sha256']:bad.append(m['path'])
print('applied files',len(M),'mismatches',bad)
(D/'terra'/'applied-check.json').write_text(json.dumps({'files':len(M),'mismatches':bad},indent=2)+'\n')
