"""Validate lead review deliverables and freeze this batch's leaf files."""
import csv,hashlib,json
from pathlib import Path
B=Path(__file__).resolve().parent
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
rows=list(csv.DictReader((B/'RESULTS.csv').open(encoding='utf8',newline='')))
assert len(rows)==9 and [r['sample_id'] for r in rows]==[f'U{i:03d}' for i in range(1,10)]
assert len({r['tic'] for r in rows})==9
for r in rows:
 assert r['full_review_completion']=='COMPLETE'
 assert Path(r['report']).exists()
 assert (B/r['tic']/'lead-context.json').exists() and (B/r['tic']/'lead-timing.json').exists()
 c=json.loads((B/r['tic']/'lead-context.json').read_text())
 assert c['tic']==r['tic'] and c['sample_id']==r['sample_id']
 assert sha(Path(c['bulk_result']))==c['bulk_sha256']
 for s in c['source']:assert sha(Path(s['path']))==s['sha256']
receipts=json.loads((B/'lead-extra-sector-receipts.json').read_text())
for x in receipts:
 if 'fits_path' in x:assert sha(Path(x['fits_path']))==x['fits_sha256']
cut=json.loads((B/'helper-cuts-receipts.json').read_text())
for x in cut:
 if 'sha256' in x:
  p=B/x['tic']/f"helper-cut-s{x['sector']}.fits"
  assert p.exists() and sha(p)==x['sha256']
files=[p for p in B.rglob('*') if p.is_file() and 'shared-catalogues' not in p.parts and p.name!='SHA256SUMS.json']
manifest={'scope':'fresh-review leaf files excluding shared-catalogues and this manifest','file_count':len(files),'files':{p.relative_to(B).as_posix():sha(p) for p in sorted(files)}}
(B/'SHA256SUMS.json').write_text(json.dumps(manifest,indent=2)+'\n',encoding='utf8')
print(len(rows),'rows',len(files),'manifest files',sum(len(json.loads((B/r['tic']/'lead-context.json').read_text())['source']) for r in rows),'verified QLP FITS')
