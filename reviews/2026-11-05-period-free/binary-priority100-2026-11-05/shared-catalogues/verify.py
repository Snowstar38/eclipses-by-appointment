"""Verify the fixed queue, cached-source scope, remote receipts, and target coverage."""
import csv,hashlib,json
from pathlib import Path
H=Path(__file__).resolve().parent
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
q=H.parent/'queue.csv';seal=json.loads((H.parent/'queue-seal.json').read_text())
assert sha(q)==seal['queue_sha256']
queue=list(csv.DictReader(q.open(encoding='utf-8-sig',newline='')))
ev=json.loads((H/'target-evidence.json').read_text(encoding='utf-8'))
status=list(csv.DictReader((H/'TARGET-STATUS.csv').open(encoding='utf-8-sig',newline='')))
assert len(queue)==len(ev['targets'])==len(status)==100
assert [(x['sample_id'],x['tic'],x['gaia_dr3']) for x in ev['targets']]==[(x['sample_id'],x['tic'],x['gaia_dr3']) for x in queue]
assert [(x['sample_id'],x['tic'],x['gaia_dr3']) for x in status]==[(x['sample_id'],x['tic'],x['gaia_dr3']) for x in queue]
for src in ev['sources'].values():
    assert sha(src['path'])==src['sha256'],src['path']
for cat in ('heartbeat','chopard','tarrants'):
    obj=json.loads(Path(ev['sources'][cat]['path']).read_text(encoding='utf-8'))
    for src in obj.get('sources',[]):assert sha(src['path'])==src['sha256'],src['path']
    for key in ('source','primary_html_exact_gaia_check'):
        src=obj.get(key)
        if src: assert sha(src['path'])==src['sha256'],src['path']
bulk=json.loads((H/'bulk-remote-receipts.json').read_text())
assert set(bulk)=={'gaia_eb','gaia_summary','gaia_nss','simbad'}
for rec in bulk.values():assert rec['status']=='success' and rec['queue_sha256']==sha(q) and sha(rec['raw'])==rec['sha256']
neighbor=json.loads((H/'gaia-neighbors.json').read_text())
assert neighbor['queue_sha256']==sha(q) and set(neighbor['targets'])=={x['sample_id'] for x in queue}
for rp in neighbor['receipts']:
    rec=json.loads(Path(rp).read_text())
    assert rec['status']=='success' and rec['queue_sha256']==sha(q) and rec['radius_arcsec']==120 and sha(rec['raw'])==rec['raw_sha256']
for x in ev['targets']:
    assert len(x['gate_status'])==10
    assert all(x['gate_status'][g].startswith('unknown:') for g in ('vsx','asassn','kostov2025_table3','kostov2025_table4'))
    assert x['gaia_neighbors_120arcsec']==neighbor['targets'][x['sample_id']]
    for rec in x['verified_historical_cone_receipts'].values():
        assert sha(rec['receipt'])==rec['receipt_sha256'] and sha(rec['raw'])==rec['raw_sha256']
alerts=[x for x in ev['targets'] if x['novelty_status'].startswith('prior association alert')]
assert {x['sample_id'] for x in alerts}=={'T074','T083','T085','T086','T091'}
out={'queue_sha256':sha(q),'targets':100,'four_vizier_gates_unknown_per_target':True,'prior_association_alerts':[x['sample_id'] for x in alerts], 'bulk_success':list(bulk),'neighbor_receipts_success':2,'verified':True}
(H/'verification.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out))
