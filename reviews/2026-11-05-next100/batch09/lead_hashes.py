"""Verify sealed source receipts and hash batch outputs."""
import csv, hashlib, json
from pathlib import Path

B=Path(__file__).resolve().parent;W=B.parent
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
source={}
for q in csv.DictReader((B/'queue.csv').open(newline='',encoding='utf8')):
 tic=q['tic'];packet=W/'source-packets'/tic/'sources.json';p=json.loads(packet.read_text(encoding='utf8'))
 assert p['queue_row']['sample_id']==q['sample_id']
 assert sha(packet)==json.loads((W/'source-packet-index.json').read_text(encoding='utf8'))['targets'][tic]['sha256']
 bulk=Path(p['bulk_result']);assert sha(bulk)==p['bulk_result_sha256']
 source[str(packet)]=sha(packet);source[str(bulk)]=sha(bulk)
 ctx=json.loads((B/tic/'lead-context.json').read_text(encoding='utf8'))
 for s in ctx['sectors']:
  fp=Path(s['source_path']);assert sha(fp)==s['source_sha256']
  source[str(fp)]=s['source_sha256']
(B/'LEAD-SOURCE-HASHES.json').write_text(json.dumps(dict(files=source,count=len(source)),indent=2)+'\n',encoding='utf8')
files={str(p.relative_to(B)).replace('\\','/'):sha(p) for p in sorted(B.rglob('*')) if p.is_file() and p.name not in ('SHA256SUMS.json','ROOT-ACCEPTANCE.json')}
(B/'SHA256SUMS.json').write_text(json.dumps(dict(files=files),indent=2)+'\n',encoding='utf8')
print('source files',len(source),'batch files',len(files))
