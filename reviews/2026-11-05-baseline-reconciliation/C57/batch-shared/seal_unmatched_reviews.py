from pathlib import Path
import csv,json,hashlib
W=Path(__file__).resolve().parent;S=W/'unmatched512';T=S/'triage'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
read=lambda p:list(csv.DictReader(p.open(encoding='utf-8-sig')))
for p,d in json.loads((T/'output-hashes.json').read_text()).items():assert sha(T/p)==d,p
proposal=read(T/'full-review-queue.csv');assert len(proposal)==12 and len({r['tic'] for r in proposal})==12
targets=json.loads((S/'pilot.json').read_text())['targets'];screen={r['tic']:r for r in map(json.loads,(S/'screening.jsonl').read_text().splitlines())}
ledger=W/'accounting/accepted-proposal-ledger.csv';prior=read(ledger)
assert not {r['tic'] for r in proposal}&{r['tic'] for r in prior}
for batch,name,start in [('1','review_unmatched10',713),('2','review_unmatched2',723)]:
 O=W/name;O.mkdir(exist_ok=True);assert not (O/'queue.csv').exists()
 rows=[r for r in proposal if r['batch']==batch];snapshot={}
 for i,r in enumerate(rows):
  tic=r['tic'];t=targets[tic];assert screen[tic]['flag'] and not t['control']
  r['review_id']=f'R{start+i}';r['gaia_dr3_source_id']=t['gaia']['source_id'];snapshot[tic]=dict(target=t,screen=screen[tic])
 with (O/'queue.csv').open('w',encoding='utf-8',newline='') as f:
  w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
 (O/'SOURCE-SNAPSHOT.json').write_text(json.dumps(snapshot,indent=2)+'\n',encoding='utf-8')
 (O/'selection-time-ledger.csv').write_bytes(ledger.read_bytes())
 paths=[S/'pilot.json',S/'screening.jsonl',T/'full-review-queue.csv',T/'REPORT.md',T/'output-hashes.json',O/'selection-time-ledger.csv',Path(__file__)]
 seal=dict(count=len(rows),tics=[r['tic'] for r in rows],sha256=sha(O/'queue.csv'),snapshot_sha256=sha(O/'SOURCE-SNAPSHOT.json'),source_hashes={str(p.relative_to(W)):sha(p) for p in paths},reservation=f'R{start}-R{start+len(rows)-1}; root acceptance required; catalogue work pending')
 (O/'queue-seal.json').write_text(json.dumps(seal,indent=2)+'\n',encoding='utf-8');print(name,seal['sha256'])
