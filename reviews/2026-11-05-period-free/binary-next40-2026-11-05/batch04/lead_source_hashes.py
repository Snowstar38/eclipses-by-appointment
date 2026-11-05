"""Bind all used raw observations and original detector packets by SHA256."""
from pathlib import Path
import csv,hashlib,json
B=Path(__file__).resolve().parent
R=B.parent
out={}
for row in csv.DictReader((B/'queue.csv').open(encoding='utf-8',newline='')):
 tic=row['tic'];packet_path=R/'source-packets'/tic/'sources.json';packet=json.loads(packet_path.read_text(encoding='utf-8'))
 def check(p,want):
  got=hashlib.sha256(Path(p).read_bytes()).hexdigest();assert got==want,(p,got,want);return got
 sources=[dict(path=x['path'],sector=x['sector'],sha256=check(x['path'],x['sha256'])) for x in packet['verified_files']]
 out[row['sample_id']]=dict(tic=tic,source_packet=str(packet_path),source_packet_sha256=hashlib.sha256(packet_path.read_bytes()).hexdigest(),bulk_result=packet['bulk_result'],bulk_result_sha256=check(packet['bulk_result'],packet['bulk_result_sha256']),fits=sources)
(B/'LEAD-SOURCE-HASHES.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print('verified',len(out),'targets and',sum(len(x['fits']) for x in out.values()),'FITS')
