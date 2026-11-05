"""Verify frozen inputs and seal batch09 outputs, excluding the manifest itself."""
import csv,hashlib,json
from pathlib import Path
B=Path(__file__).resolve().parent;W=B.parent
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
q=list(csv.DictReader((B/'queue.csv').open(newline='')))
expected=json.loads((W/'queue-seal.json').read_text())['batch_sha256']['batch09']
assert sha(B/'queue.csv')==expected
sources={}
for r in q:
 tic=r['tic'];p=W/'source-packets'/tic/'sources.json';packet=json.loads(p.read_text());inputs=[p,Path(packet['bulk_result'])]
 if packet.get('fold_result'):inputs.append(Path(packet['fold_result']))
 for entry in packet['target']['files']:inputs.append(Path(entry['path']))
 assert sha(Path(packet['bulk_result']))==packet['bulk_result_sha256']
 if packet.get('fold_result'):assert sha(Path(packet['fold_result']))==packet['fold_result_sha256']
 for entry in packet['target']['files']:assert sha(Path(entry['path']))==entry['sha256']
 sources[tic]={str(x):sha(x) for x in inputs}
(B/'SOURCE-HASHES.json').write_text(json.dumps({'queue_sha256':expected,'targets':sources},indent=2)+'\n',encoding='utf8')
files={str(p.relative_to(B)):sha(p) for p in sorted(B.rglob('*')) if p.is_file() and p.name not in ('SHA256SUMS.json','ROOT-ACCEPTANCE.json')}
(B/'SHA256SUMS.json').write_text(json.dumps({'files':files},indent=2)+'\n',encoding='utf8')
print(len(q),'targets',sum(len(v) for v in sources.values()),'source files',len(files),'sealed files')
