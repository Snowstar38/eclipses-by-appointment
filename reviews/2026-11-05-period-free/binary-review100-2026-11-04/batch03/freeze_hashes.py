"""Validate queue/result coverage and seal batch03 local files."""
import csv,hashlib,json,re
from pathlib import Path
B=Path(__file__).resolve().parent
q=list(csv.DictReader((B/'queue.csv').open(newline='',encoding='utf-8')))
r=list(csv.DictReader((B/'RESULTS.csv').open(newline='',encoding='utf-8')))
assert len(q)==len(r)==10
assert [(x['sample_id'],x['tic'],x['sample_stratum']) for x in q]==[(x['sample_id'],x['tic'],x['sample_stratum']) for x in r]
assert all(x['full_review_completion']=='COMPLETE' and x['novelty_status']=='UNKNOWN' for x in r)
for row in r:
 report=Path(row['report']);assert report.is_file() and report==B/row['tic']/'REPORT.md'
 assert (B/row['tic']/'raw-inspection.json').is_file()
 for target in re.findall(r'\]\(([^)]+)\)',report.read_text(encoding='utf-8')):
  if not target.startswith(('http:','https:')):assert (report.parent/target).is_file(),(report,target)
files=sorted(p for p in B.rglob('*') if p.is_file() and p.name!='SHA256SUMS.json')
hashes={p.relative_to(B).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in files}
(B/'SHA256SUMS.json').write_text(json.dumps(hashes,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'queue_rows':len(q),'result_rows':len(r),'sealed_files':len(hashes),'verdicts':{v:sum(x['physical_verdict']==v for x in r) for v in sorted(set(x['physical_verdict'] for x in r))}}))
