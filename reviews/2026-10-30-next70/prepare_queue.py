import csv,json,hashlib,os
from pathlib import Path
D=Path(__file__).parent
S=Path('[local working path omitted; see provenance receipts] 5.1/made/paper/tables/batch_candidates.csv')
B=Path('[local working path omitted; see provenance receipts]')
exclude={r['tic'] for r in csv.DictReader((B/'FULL-RESULTS.csv').open())}
for p in B.rglob('RESULTS.csv'):
 try: exclude.update(r['tic'] for r in csv.DictReader(p.open()) if r.get('tic'))
 except Exception: pass
for base in [Path('[local working path omitted; see provenance receipts] 5/made/sb1-scale/pervet'),Path('[local working path omitted; see provenance receipts] 5.1/made/sb1-scale/pervet')]:
 if base.exists():exclude.update(p.name.removeprefix('vet') for p in base.iterdir() if p.is_dir())
for table,key in [(Path('[local working path omitted; see provenance receipts] 5.1/made/paper/tables/returned_review_2026-10-30.csv'),'tic'),(Path('[local working path omitted; see provenance receipts] 5.1/made/paper/tables/objects.csv'),'TIC')]:
 exclude.update(r[key] for r in csv.DictReader(table.open(encoding='utf-8-sig')))
rows=sorted((r for r in csv.DictReader(S.open()) if r['status']=='candidate' and r['tic'] not in exclude),key=lambda r:(float(r['depth_ppt']),int(r['tic'])))[:70]
assert len(rows)==70 and len({r['tic'] for r in rows})==70
assert not ({r['tic'] for r in rows}&exclude)
with (D/'queue.csv').open('w',newline='') as f:
 w=csv.DictWriter(f,['position','batch']+list(rows[0]));w.writeheader();w.writerows(dict(position=i+1,batch=i//10+1,**r) for i,r in enumerate(rows))
tp=Path(os.environ['TEMP'])/'hunt-sb1-scale/targets.json'
t=json.loads(tp.read_text());selected={r['tic']:t[r['tic']] for r in rows}
(D/'targets-selected.json').write_text(json.dumps(selected,indent=2))
(D/'queue-provenance.json').write_text(json.dumps(dict(source=str(S),source_sha256=hashlib.sha256(S.read_bytes()).hexdigest(),excluded_ids=sorted(exclude),selection='candidate, absent prior review results and pervet; depth_ppt ascending then TIC; first70',count=70,queue_sha256=hashlib.sha256((D/'queue.csv').read_bytes()).hexdigest()),indent=2))
print([r['tic'] for r in rows[:10]])
