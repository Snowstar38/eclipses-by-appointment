from pathlib import Path
import csv,hashlib,json
W=Path(__file__).resolve().parent;S=W/'remaining_cached'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
read=lambda p:list(csv.DictReader(p.open(encoding='utf-8-sig')))
for path,digest in json.loads((S/'triage/output-hashes.json').read_text()).items():
    p=Path(path);p=p if p.is_absolute() else S/'triage'/p
    assert sha(p)==digest,str(p)
proposal=read(S/'triage/full-review-proposal.csv');assert len(proposal)==15
targets=json.loads((S/'pilot.json').read_text())['targets']
screen={r['tic']:r for r in map(json.loads,(S/'screening.jsonl').read_text().splitlines())}
ledger=W/'accounting/accepted-proposal-ledger.csv';prior=read(ledger)
assert not {x['tic'] for x in proposal}&{x['tic'] for x in prior}
assert len({x['tic'] for x in proposal})==15
for batch,name,start in [('1','review_cached10',698),('2','review_cached5',708)]:
    O=W/name;O.mkdir(exist_ok=True);assert not (O/'queue.csv').exists()
    rows=[r for r in proposal if r['batch']==batch];snapshot={}
    for i,r in enumerate(rows):
        tic=r['tic'];t=targets[tic]
        assert t['gaia']['source_id']==r['gaia_dr3'] and screen[tic]['flag'] and not t['control']
        r['review_id']=f'R{start+i}';r['gaia_dr3_source_id']=r['gaia_dr3'];r['novelty_status']='unknown: unavailable catalogue scopes'
        snapshot[tic]=dict(target=t,screen=screen[tic])
    with (O/'queue.csv').open('w',encoding='utf-8',newline='') as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
    (O/'SOURCE-SNAPSHOT.json').write_text(json.dumps(snapshot,indent=2)+'\n',encoding='utf-8')
    (O/'selection-time-ledger.csv').write_bytes(ledger.read_bytes())
    paths=[S/'pilot.json',S/'screening.jsonl',S/'triage/full-review-proposal.csv',S/'triage/REPORT.md',S/'shared-catalogues/coverage-matrix.csv',O/'selection-time-ledger.csv',Path(__file__)]
    seal=dict(count=len(rows),tics=[r['tic'] for r in rows],sha256=sha(O/'queue.csv'),snapshot_sha256=sha(O/'SOURCE-SNAPSHOT.json'),source_hashes={str(p.relative_to(W)):sha(p) for p in paths},reservation=f'R{start}-R{start+len(rows)-1}; root acceptance required, no new claim inferred')
    (O/'queue-seal.json').write_text(json.dumps(seal,indent=2)+'\n',encoding='utf-8')
    print(name,len(rows),seal['sha256'])
