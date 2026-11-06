from pathlib import Path
import json,csv,hashlib,collections,datetime
b=Path(__file__).resolve().parent
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
q=list(csv.DictReader((b/'queue.csv').open()));r=list(csv.DictReader((b/'RESULTS.csv').open()));assert [x['tic'] for x in q]==[x['tic'] for x in r];assert len(q)==8;assert all(x['completion']=='complete' for x in r);assert all((b/x['report']).exists() for x in r)
files=[p for p in b.rglob('*') if p.is_file() and p.name!='BATCH-SEAL.json']
seal=dict(utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),queue_sha256=sha(b/'queue.csv'),results_sha256=sha(b/'RESULTS.csv'),exact_tics=[x['tic'] for x in q],completion_count=8,tier_counts=dict(collections.Counter(x['tier'] for x in r)),eligible_tics=[x['tic'] for x in r if x['publication_eligible']=='true'],shared_catalogue_seal=dict(path=str(b.parent/'shared-catalogues/ROOT-CATALOGUE-SEAL.json'),sha256=sha(b.parent/'shared-catalogues/ROOT-CATALOGUE-SEAL.json')),helper_audit_sha256=sha(b/'helper-independent-audit.md'),helper_hash_manifest_sha256=sha(b/'helper-final-artifact-hashes.json'),file_count=len(files),total_bytes=sum(p.stat().st_size for p in files),files=[dict(path=str(p.relative_to(b)),bytes=p.stat().st_size,sha256=sha(p)) for p in sorted(files)],status='lead-complete-awaiting-root-acceptance',no_public_or_ledger_edits=True)
(b/'BATCH-SEAL.json').write_text(json.dumps(seal,indent=2));print(json.dumps({k:v for k,v in seal.items() if k!='files'},indent=2));print('seal_sha256',sha(b/'BATCH-SEAL.json'))
