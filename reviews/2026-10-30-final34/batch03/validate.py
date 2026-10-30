import csv,json,hashlib,collections
from pathlib import Path
B=Path(__file__).parent;D=B.parent
rows=list(csv.DictReader((B/'RESULTS.csv').open()));expected=list(csv.DictReader((D/'queue.csv').open()))[20:30]
assert len(rows)==10 and {r['tic'] for r in rows}=={r['tic'] for r in expected}
raw=json.loads((B/'raw-evidence/raw-events.json').read_text());qlp=json.loads((B/'raw-evidence/qlp-results.json').read_text())
for r in rows:
 t=r['tic'];assert Path(r['report']).is_file();assert r['physical_verdict'] in ['CONFIRMED','PROBABLE','PLAUSIBLE','REFUTED'];assert all(r[k] for k in ['full_review_completion','novelty_status','report','next_check']);assert r['catalogue_coverage_complete']=='yes'
 assert qlp[t]['header_TICID']==t and int(qlp[t]['header_SECTOR'])==raw[t]['sector'];assert len(raw[t]['events'])>=2 and len(qlp[t]['events'])>=2
 for k,h in [('source_cutout','source_sha256'),('gaia_cache','gaia_sha256'),('seed_receipt','seed_sha256')]:assert hashlib.sha256(Path(raw[t][k]).read_bytes()).hexdigest()==raw[t][h]
 assert hashlib.sha256((B/f"raw-evidence/{t}/qlp_s{raw[t]['sector']:03d}.fits").read_bytes()).hexdigest()==qlp[t]['sha256']
manifest={str(p.relative_to(B)):hashlib.sha256(p.read_bytes()).hexdigest() for p in B.rglob('*') if p.is_file() and p.name not in ['manifest.json','validation.json']}
for name in ['gaia-nss_two_body_orbit.csv','coverage-matrix.csv']:manifest['../shared-catalogues/'+name]=hashlib.sha256((D/'shared-catalogues'/name).read_bytes()).hexdigest()
(B/'manifest.json').write_text(json.dumps(manifest,indent=2));(B/'validation.json').write_text(json.dumps(dict(rows=10,reports=10,counts=dict(collections.Counter(r['physical_verdict'] for r in rows)),known_prior_eb=sum(r['novelty_status']=='known prior EB' for r in rows),all_scoped_coverage_complete=True,source_hashes_verified=True,execution_incomplete=0),indent=2));print('Validated10, original source and QLP identity/hash checks passed')
