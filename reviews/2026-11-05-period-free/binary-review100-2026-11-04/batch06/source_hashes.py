"""Reverify and record frozen source packet, bulk JSON, and cached FITS bytes."""
import csv,hashlib,json
from pathlib import Path
B=Path(__file__).resolve().parent
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
out={}
for q in csv.DictReader((B/'queue.csv').open(newline='',encoding='utf-8')):
 tic=q['tic'];packet=B.parent/'source-packets'/tic/'sources.json';src=json.loads(packet.read_text(encoding='utf-8'))
 bulk=Path(src['bulk_result']);assert sha(bulk)==src['bulk_result_sha256']
 fits=[]
 for f in src['verified_files']:
  assert sha(f['path'])==f['sha256']
  fits.append({'path':f['path'],'sha256':f['sha256'],'sector':f['sector']})
 out[tic]={'source_packet':str(packet),'source_packet_sha256':sha(packet),'bulk_result':str(bulk),'bulk_result_sha256':src['bulk_result_sha256'],'fits':fits}
(B/'SOURCE-HASHES.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(len(out),sum(len(x['fits']) for x in out.values()))
