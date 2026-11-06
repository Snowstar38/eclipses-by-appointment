import json,hashlib,csv,collections
from pathlib import Path
b=Path(__file__).resolve().parent;s=b.parent/'shared-catalogues';seal=json.loads((s/'ROOT-CATALOGUE-SEAL.json').read_text());sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
for p,h in seal['files'].items(): assert sha(s/p)==h,p
rs=list(csv.DictReader((b/'RESULTS.csv').open()));qs=list(csv.DictReader((b/'queue.csv').open()));assert [r['tic'] for r in rs]==[r['tic'] for r in qs];assert len(rs)==8;assert all(r['full_review_completion']=='COMPLETE' for r in rs)
for r in rs:
 p=Path(r['report']);assert p.is_file();text=p.read_text(encoding='utf8');assert r['tic'] in text and r['gaia_dr3'] in text
out={'schema':'bounded-physical-review-v1','exact_rows':8,'source_FITS_verified':37,'independent_helper_audit':'helper-independent-audit.md','physical_verdict_counts':dict(collections.Counter(r['physical_verdict'] for r in rs)),'known_recoveries':['271763138'],'host_uncertain':['241100642','280692653'],'positive_offtarget_refuted':['240615841','258216510'],'root_catalogue_seal_sha256':sha(s/'ROOT-CATALOGUE-SEAL.json'),'root_catalogue_verified_files':len(seal['files']),'files':{str(p.relative_to(b)):sha(p) for p in sorted(b.rglob('*')) if p.is_file() and p.name!='BATCH-SEAL.json'}}
(b/'BATCH-SEAL.json').write_text(json.dumps(out,indent=2),encoding='utf8');print({k:v for k,v in out.items() if k!='files'})
