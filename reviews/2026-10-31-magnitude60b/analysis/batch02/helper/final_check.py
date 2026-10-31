import json,csv,pathlib,hashlib,math
p=pathlib.Path(__file__).resolve().parent.parent;q=list(csv.DictReader(open(p/'queue.csv')));r=list(csv.DictReader(open(p/'RESULTS.csv')));by={x['tic']:x for x in r};g=json.load(open(p/'gaia-geometry.json'));issues=[];hashes={}
if len(q)!=10 or set(x['tic'] for x in q)!=set(by) or len(r)!=10:issues.append('queue coverage')
for x in q:
 t=x['tic'];m=json.load(open(p/t/'measurements.json'));s=(p/t/'REPORT.md').read_text(encoding='utf8');row=by[t]
 for k in ['period_days','period_error_days','primary_epoch_btjd','depth_ppt']:
  if float(row[k])!=m[k]:issues.append([t,k,'row'])
 for e in m['events']:
  if f"{e['mid_btjd']:.7f}" not in s and f"{e['mid_btjd']:.8f}" not in s:issues.append([t,e['cycle'],'missing event'])
 if t not in s or row['physical_verdict'] not in s:issues.append([t,'identity or verdict'])
 if abs(g[t]['photometric_period_days']-m['period_days'])>1e-12:issues.append([t,'geometry period'])
 for f in (p/t).rglob('*'):
  if f.is_file():hashes[str(f.relative_to(p))]=hashlib.sha256(f.read_bytes()).hexdigest()
for f in [p/'queue.csv',p/'RESULTS.csv',p/'gaia-geometry.json',p/'geometry.py',p/'download-receipts.json',p/'review_measure.py',p/'ingest156.py',p/'report156.py',p/'write_reports.py']:
 if f.exists():hashes[str(f.relative_to(p))]=hashlib.sha256(f.read_bytes()).hexdigest()
(p/'helper/final-audited-hashes.json').write_text(json.dumps(hashes,indent=2));print('issues',issues,'hashed',len(hashes))
