import csv,hashlib,json
from pathlib import Path
B=Path(__file__).resolve().parent
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
for r in csv.DictReader((B/'queue.csv').open(newline='',encoding='utf-8')):
 tic=r['tic'];p=B.parent/'source-packets'/tic/'sources.json';s=json.loads(p.read_text(encoding='utf-8'))
 records=[{'path':str(p),'sha256':sha(p),'role':'packet'}]
 for key in ('bulk_result','fold_result'):
  path=Path(s[key]);actual=sha(path);assert actual==s[key+'_sha256']
  records.append({'path':str(path),'sha256':actual,'role':key})
 for f in s['target']['files']:
  path=Path(f['path']);actual=sha(path);assert actual==f['sha256']
  records.append({'path':str(path),'sha256':actual,'role':'QLP FITS'})
 (B/tic/'source-hashes.json').write_text(json.dumps({'sample_id':r['sample_id'],'tic':tic,'verified':records},indent=2)+'\n',encoding='utf-8')
 print(r['sample_id'],len(records),flush=True)
