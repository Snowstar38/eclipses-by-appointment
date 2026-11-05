import csv,hashlib,json
from pathlib import Path
H=Path(__file__).resolve().parent;Q=H.parent/'queue.csv';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
seal=json.loads((H.parent/'queue-seal.json').read_text());assert sha(Q)==seal['queue_sha256']
ev=json.loads((H/'target-evidence.json').read_text(encoding='utf-8'))
q=list(csv.DictReader(Q.open(encoding='utf-8-sig')));rows=list(csv.DictReader((H/'TARGET-STATUS.csv').open(encoding='utf-8-sig')))
assert len(ev['targets'])==len(rows)==len(q)==100
assert [(x['sample_id'],x['tic'],x['gaia_dr3']) for x in ev['targets']]==[(x['sample_id'],x['tic'],x['gaia_dr3']) for x in q]
assert [(x['sample_id'],x['tic']) for x in rows]==[(x['sample_id'],x['tic']) for x in q]
for s in ev['sources'].values():
    if 'path' in s: assert sha(Path(s['path']))==s['sha256']
bulk=json.loads((H/'bulk-remote-receipts.json').read_text());assert all(x['status']=='success' and sha(Path(x['raw']))==x['sha256'] for x in bulk.values())
for x in ev['targets']:
    assert x['novelty_status'].startswith('novelty unknown')
    assert not x['primary_prsa_exact_rows'] and not x['primary_ijspeert_exact_rows']
    assert not x['primary_prsa_5arcsec_rows'] and not x['primary_ijspeert_5arcsec_rows']
    assert not x['prior_review_or_register'] and not x['gaia_eb_rows']
    assert not any(x['local_prior'].values())
    assert not any(z['otype'] in ('EB*','Al*','bL*','WU*') for z in x['simbad_rows'])
    assert len(x['gate_status'])==10 and sum(v.startswith('unknown:') for v in x['gate_status'].values())==4
    for rec in x['verified_historical_cone_receipts'].values():
        assert sha(Path(rec['receipt']))==rec['receipt_sha256'] and sha(Path(rec['raw']))==rec['raw_sha256']
out={'queue_sha256':sha(Q),'targets':100,'novelty_unknown':100,'known_prior_associations':0,'primary_exact_matches':0,'primary_5arcsec_matches':0,'remote_vizier_gates_unqueried_per_target':4,'successful_bulk':list(bulk),'verified':True}
(H/'verification.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8');print(json.dumps(out))
