import json,hashlib
from pathlib import Path
B=Path(__file__).resolve().parent;out={}
for name in ('source-verification.json','external-source-verification.json'):
 d=json.loads((B/name).read_text());bad=[]
 for x in d['checks']:
  p=Path(x['path']); h=hashlib.sha256(p.read_bytes()).hexdigest() if p.exists() else None
  if h!=x['sha256']:bad.append(str(p))
 out[name]={'count':len(d['checks']),'mismatches':bad,'receipt_sha256':hashlib.sha256((B/name).read_bytes()).hexdigest()}
(B/'helper-source-receipts-audit.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));assert all(not x['mismatches'] for x in out.values())
