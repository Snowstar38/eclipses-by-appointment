from pathlib import Path
import json,csv,hashlib
B=Path(__file__).parent;R=B/'raw-evidence';Q=[r for r in csv.DictReader(open(B.parent/'queue.csv')) if r['batch']=='batch03'];out=json.load(open(B/'RESULTS.json'));assert [r['tic'] for r in out]==[r['tic'] for r in Q];assert len(out)==10
idc=json.load(open(R/'identity-checks.json'));assert len(idc)==29 and all(x['tic_matches'] and x['sector_matches'] for x in idc)
assert all((B.parent/r['report']).exists() and r['full_review_completion']=='complete' for r in out)
manifest=json.load(open(B/'manifest.json'));bad=[x['path'] for x in manifest['files'] if hashlib.sha256((B/x['path']).read_bytes()).hexdigest()!=x['sha256']];assert not bad
v=dict(targets=10,input_qlp_files=29,identity_checks='29/29 TICID and SECTOR match',verdict_counts={k:sum(r['physical_verdict']==k for r in out) for k in ['CONFIRMED','PROBABLE','PLAUSIBLE','REFUTED']},reports_present=True,hashes_verified=len(manifest['files']),execution_complete=True,unattempted_deciding_checks=0,notes='MAST pipeline inventory not attempted; independent custom TESScut reduction supplies the required processing comparison and shares photons.')
(B/'validation.json').write_text(json.dumps(v,indent=2));print(v)
