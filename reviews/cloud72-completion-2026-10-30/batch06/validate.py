from pathlib import Path
import csv,json,hashlib
B=Path(__file__).parent;D=B.parent;rows=list(csv.DictReader((B/'RESULTS.csv').open()));expected=[r['tic'] for r in csv.DictReader((D/'queue.csv').open()) if r['batch']=='batch06'];assert [r['tic'] for r in rows]==expected and len(rows)==5
for r in rows:
 assert r['full_review_completion']=='complete' and r['remaining_full_review']=='false';p=D/r['report'];assert p.is_file() and p.stat().st_size>1000;assert 'GPT-6.1 Sol' in p.read_text() and 'GPT-6.1 Terra' in p.read_text()
ident=json.load(open(B/'raw-evidence/identity-checks.json'));assert len(ident)==15 and all(x['tic_matches'] and x['sector_matches'] for x in ident)
dl=json.load(open(B/'raw-evidence/tesscut-downloads.json'));assert len(dl)==10 and all('members' in x for x in dl)
ci=json.load(open(B/'raw-evidence/cutout-identity.json'));assert len(ci)==10 and all(x['sector_matches'] and x['target_in_central3x3'] for x in ci)
assert (B/'HELPER.md').is_file()
counts={s:sum(r['physical_verdict']==s for r in rows) for s in set(r['physical_verdict'] for r in rows)};(B/'validation.json').write_text(json.dumps(dict(assigned=5,results=5,reports=5,queue_positions=[51,52,53,54,55],qlp_identity_matches=15,fresh_cutouts=10,cutout_identities=10,tier_counts=counts,credits='Automated GPT-6.1 Sol plus fresh GPT-6.1 Terra, supervised by Astra; anonymous coordinator'),indent=2))
files=[dict(path=p.relative_to(B).as_posix(),bytes=p.stat().st_size,sha256=hashlib.sha256(p.read_bytes()).hexdigest()) for p in B.rglob('*') if p.is_file() and p.name!='manifest.json'];(B/'manifest.json').write_text(json.dumps(dict(batch='batch06',files=files),indent=2));print(counts,len(files),'hashed files')
