from pathlib import Path
import csv,json,hashlib
W=Path(__file__).resolve().parent;S=W/'next256';O=W/'review9';O.mkdir(exist_ok=True)
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
queue=list(csv.DictReader((S/'triage/full-review-queue.csv').open(encoding='utf-8')))
targets=json.loads((S/'pilot.json').read_text())['targets']
screen={r['tic']:r for r in map(json.loads,(S/'screening.jsonl').read_text().splitlines())}
assert len(queue)==len({r['tic'] for r in queue})==9
expected=['159060569','387268955','342060048','184398115','64701575','284613090','128720791','95623701','56912737']
assert [r['tic'] for r in queue]==expected
accepted=list(csv.DictReader((W/'accounting/accepted-proposal-ledger.csv').open()))
assert not {r['tic'] for r in queue}&{r['tic'] for r in accepted}
snapshot={}
for i,r in enumerate(queue):
 tic=r['tic'];t=targets[tic];assert t['gaia']['source_id']==r['gaia_dr3'] and screen[tic]['flag'] and not t['control']
 r['review_id']=f'R{689+i}';r['batch']='review9';r['novelty_status']='unknown: incomplete query'
 snapshot[tic]=dict(target=t,screen=screen[tic])
assert not (O/'queue.csv').exists()
with (O/'queue.csv').open('w',encoding='utf-8',newline='') as f:
 writer=csv.DictWriter(f,fieldnames=queue[0]);writer.writeheader();writer.writerows(queue)
(O/'SOURCE-SNAPSHOT.json').write_text(json.dumps(snapshot,indent=2)+'\n',encoding='utf-8')
sources={str(p.relative_to(W)):sha(p) for p in [S/'pilot.json',S/'screening.jsonl',S/'triage/full-review-queue.csv',S/'triage/REPORT.md',S/'shared-catalogues/coverage-matrix.csv',W/'accounting/accepted-proposal-ledger.csv']}
(O/'queue-seal.json').write_text(json.dumps(dict(count=9,tics=expected,sha256=sha(O/'queue.csv'),snapshot_sha256=sha(O/'SOURCE-SNAPSHOT.json'),source_hashes=sources,reservation='R688 reserved for independent review412; R689-R697 exact9 in triage priority order, not acceptance'),indent=2)+'\n',encoding='utf-8')
print('sealed9',sha(O/'queue.csv'))
