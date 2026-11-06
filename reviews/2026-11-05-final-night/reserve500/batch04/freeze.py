"""Validate exact coverage, source receipts and freeze bounded review artifacts."""
import csv,json,hashlib
from pathlib import Path
from datetime import datetime,timezone
B=Path(__file__).resolve().parent
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
q=list(csv.DictReader((B/'queue.csv').open()));r=list(csv.DictReader((B/'RESULTS.csv').open()))
assert len(q)==len(r)==2 and [x['tic'] for x in q]==[x['tic'] for x in r]
assert [(x['sample_id'],x['gaia_dr3']) for x in q]==[(x['sample_id'],x['gaia_dr3']) for x in r]
assert all(x['completion']=='complete' and x['publication_eligible']=='false' for x in r)
assert [x['tier'] for x in r]==['PLAUSIBLE','REFUTED']
for x in r:
 assert (B/x['report']).is_file()
 d=json.loads((B/x['tic']/'lead-context.json').read_text())
 for src in d['source']:assert sha(Path(src['path']))==src['sha256']
 c=json.loads((B/x['tic']/'lead-central-catalogue-receipts.json').read_text())
 for name,h in c['source_sha256'].items():assert sha(Path(c['central_path'])/name)==h
 for p in (B/x['tic']).glob('lead-localization-*.json'):
  d=json.loads(p.read_text());sec=d['event']['sector'];assert sha(p.parent/f'lead-tesscut-{sec}.fits')==d['fits_sha256']
catalogue=B.parent/'shared-catalogues';cs=json.loads((catalogue/'ROOT-CATALOGUE-SEAL.json').read_text())
for name,h in cs['files'].items():assert sha(catalogue/name)==h
assert (B/'HELPER-NOTE.md').is_file()
files={str(p.relative_to(B)).replace('\\','/'):sha(p) for p in sorted(B.rglob('*')) if p.is_file() and p.name not in ('SEAL.json','helper-final-seal-audit.json')}
out={'utc':datetime.now(timezone.utc).isoformat(),'queue_sha256':sha(B/'queue.csv'),'exact_n':2,'outcomes':{'PLAUSIBLE':1,'REFUTED':1},'accepted_claims':0,'checks':'exact queue identities; source hashes; cutout hashes; shared catalogue seal and copied receipts; completion and report coverage','files':files}
(B/'SEAL.json').write_text(json.dumps(out,indent=2))
print(json.dumps({k:v for k,v in out.items() if k!='files'},indent=2));print('sealed',len(files),'files')
