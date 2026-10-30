import json,csv,hashlib,collections
from pathlib import Path
B=Path('.');D=B.parent
rows=list(csv.DictReader((B/'RESULTS.csv').open()));assert len(rows)==10
assert [r['tic'] for r in rows]==[r['tic'] for r in csv.DictReader((D/'queue.csv').open()) if r['batch']=='2']
R=json.loads((B/'raw-evidence/raw-events.json').read_text());Q=json.loads((B/'raw-evidence/qlp-results.json').read_text())
for r in rows:
 t=r['tic'];assert Path(r['report']).is_file();assert all(r[k] for k in ['physical_verdict','full_review_completion','novelty_status','report','next_check']);assert r['catalogue_coverage_complete']=='yes'
 for path,sha in [(R[t]['source_cutout'],R[t]['source_sha256']),(R[t]['gaia_cache'],R[t]['gaia_sha256']),(R[t]['seed_receipt'],R[t]['seed_sha256'])]:assert hashlib.sha256(Path(path).read_bytes()).hexdigest()==sha
 assert hashlib.sha256((B/'raw-evidence'/t/f"qlp_s{R[t]['sector']:03d}.fits").read_bytes()).hexdigest()==Q[t]['sha256']
 assert Q[t]['header_TICID']==t;assert Q[t]['header_SECTOR']==R[t]['sector'];assert Q[t]['representative_ephemeris']['n_events']>=2
assert (B/'helper/HELPER-AUDIT.md').exists()
files=[p for p in B.rglob('*') if p.is_file() and p.name not in ['manifest.json','validation.json']]
manifest={str(p.relative_to(B)):hashlib.sha256(p.read_bytes()).hexdigest() for p in files}
for f in ['gaia-nss_two_body_orbit.csv','coverage-matrix.csv']:manifest['../shared-catalogues/'+f]=hashlib.sha256((D/'shared-catalogues'/f).read_bytes()).hexdigest()
(B/'manifest.json').write_text(json.dumps(manifest,indent=2))
(B/'validation.json').write_text(json.dumps(dict(rows=10,reports=10,counts=dict(collections.Counter(r['physical_verdict'] for r in rows)),all_scoped_coverage_complete=True,source_hashes_verified=True,execution_incomplete=0,manifest_files=len(manifest)),indent=2))
print('validated',len(manifest),'hashes')
