import csv,json,hashlib
from pathlib import Path
B=Path('[local-path-redacted]');R=B.parent;out=[]
for r in csv.DictReader((B/'queue.csv').open(encoding='utf8',newline='')):
 tic=r['tic'];p=R/'source-packets'/tic/'sources.json';q=json.loads(p.read_text());
 for v in q['verified_files']:
  fp=Path(v['path']);actual=hashlib.sha256(fp.read_bytes()).hexdigest();assert actual==v['sha256'];out.append(dict(sample_id=r['sample_id'],tic=tic,path=str(fp),sha256=actual,sector=v['sector']))
 out.append(dict(sample_id=r['sample_id'],tic=tic,path=str(p),sha256=hashlib.sha256(p.read_bytes()).hexdigest(),source_kind='packet'))
 fp=Path(q['bulk_result']);actual=hashlib.sha256(fp.read_bytes()).hexdigest();assert actual==q['bulk_result_sha256'];out.append(dict(sample_id=r['sample_id'],tic=tic,path=str(fp),sha256=actual,source_kind='bulk_detector'))
(B/'LEAD-SOURCE-HASHES.json').write_text(json.dumps(out,indent=2)+'\n');print(len(out),'hashes')
