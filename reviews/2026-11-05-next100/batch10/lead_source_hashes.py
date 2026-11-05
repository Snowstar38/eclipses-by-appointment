import csv,json,hashlib
from pathlib import Path
B=Path(__file__).resolve().parent; W=B.parent
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
rows=list(csv.DictReader((B/'queue.csv').open(encoding='utf8'))); out={}
for r in rows:
 tic=r['tic']; packet=W/'source-packets'/tic/'sources.json'; d=json.loads(packet.read_text(encoding='utf8')); paths=[packet,Path(d['bulk_result'])]+[Path(x['path']) for x in d['verified_files']]+[W/'tap-recovery'/('vsx-'+r['sample_id']+'.json')]
 out[r['sample_id']]={str(p):sha(p) for p in paths}
(B/'LEAD-SOURCE-HASHES.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf8')
