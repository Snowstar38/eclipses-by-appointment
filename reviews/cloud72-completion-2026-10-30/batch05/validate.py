from pathlib import Path
import csv,json,hashlib
B=Path(__file__).parent;D=B.parent;rows=list(csv.DictReader((B/'RESULTS.csv').open()));expected=[r['tic'] for r in csv.DictReader((D/'queue.csv').open()) if r['batch']=='batch05'];assert [r['tic'] for r in rows]==expected;assert len(rows)==10
for r in rows:
 assert r['full_review_completion']=='complete' and r['remaining_full_review']=='false';p=D/r['report'];assert p.is_file() and p.stat().st_size>1000
ident=json.load(open(B/'raw-evidence/identity-checks.json'));assert len(ident)==26 and all(x['tic_matches'] and x['sector_matches'] for x in ident)
dl=json.load(open(B/'raw-evidence/tesscut-downloads.json'));assert len(dl)==18 and all('members' in x for x in dl)
counts={s:sum(r['physical_verdict']==s for r in rows) for s in set(r['physical_verdict'] for r in rows)};(B/'validation.json').write_text(json.dumps(dict(assigned=10,results=10,reports=10,qlp_identity_matches=26,fresh_cutouts=18,tier_counts=counts,credits='Automated GPT-6.1 Sol plus fresh GPT-6.1 Terra, supervised by Astra; anonymous coordinator'),indent=2))
files=[dict(path=p.relative_to(B).as_posix(),bytes=p.stat().st_size,sha256=hashlib.sha256(p.read_bytes()).hexdigest()) for p in B.rglob('*') if p.is_file() and p.name!='manifest.json'];(B/'manifest.json').write_text(json.dumps(dict(batch='batch05',files=files),indent=2));print(counts,len(files),'hashed files')
