import csv,json,hashlib
from pathlib import Path
out={}
for r in csv.DictReader(open('queue.csv',encoding='utf8')):
 c=json.loads(Path(r['tic'],'lead-context.json').read_text()); checks=[]
 for s in c['sectors']:
  p=Path(s['source_path']); h=hashlib.sha256(p.read_bytes()).hexdigest(); checks.append({'sector':s['sector'],'path':str(p),'sha256':h,'matches':h==s['source_sha256']})
 out[r['sample_id']]=checks
Path('helper-source-checks.json').write_text(json.dumps(out,indent=2)+'\n');print('checked',sum(map(len,out.values())),'all matches',all(z['matches'] for a in out.values() for z in a))
