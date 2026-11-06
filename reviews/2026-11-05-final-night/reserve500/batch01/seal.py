from pathlib import Path
import json,csv,hashlib,datetime
b=Path(__file__).resolve().parent
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
q=list(csv.DictReader((b/'queue.csv').open()));r=list(csv.DictReader((b/'RESULTS.csv').open()));assert [x['tic'] for x in q]==[x['tic'] for x in r] and len(r)==8
assert all(x['completion']=='complete' for x in r)
assert sum(x['publication_eligible']=='true' for x in r)==5
files={str(p.relative_to(b)).replace('\\','/'):sha(p) for p in sorted(b.rglob('*')) if p.is_file() and p.name not in ['BATCH-SEAL.json','helper-final-freeze-audit.json'] and '__pycache__' not in p.parts}
shared=b.parent/'shared-catalogues/ROOT-CATALOGUE-SEAL.json';sc=json.loads(shared.read_text());root=shared.parent
assert all(sha(root/p)==v for p,v in sc['files'].items())
sources=json.loads((b/'lead-source-hashes.json').read_text());n=0
for tic,d in sources.items():
 for s in d['source']:
  assert sha(Path(s['path']))==s['sha256'];n+=1
out={'frozen_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'queue_n':8,'completed':8,'outcomes':{k:sum(x['tier']==k for x in r) for k in ['CONFIRMED','PROBABLE','PLAUSIBLE','REFUTED']},'eligible_n':5,'files':files,'raw_source_files_verified':n,'shared_catalogue_seal':str(shared),'shared_catalogue_seal_sha256':sha(shared),'shared_catalogue_files_verified':len(sc['files']),'scope':'Exact queue no substitutions; current final reserve500 raw data; no ledger/public edits; frozen after helper independent report/numeric audit. Freeze audit excluded to avoid self-reference.'}
(b/'BATCH-SEAL.json').write_text(json.dumps(out,indent=2));print(json.dumps({k:v for k,v in out.items() if k!='files'},indent=2))
