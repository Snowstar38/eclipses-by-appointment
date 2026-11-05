"""Verify the sealed queue, source and raw remote receipt hashes, and ten statuses."""
import csv, hashlib, json
from pathlib import Path
H=Path(__file__).resolve().parent; B=H.parent
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
seal=json.loads((B/'queue-seal.json').read_text())
assert sha(B/'queue.csv')==seal['queue_sha256']
q=list(csv.DictReader((B/'queue.csv').open(encoding='utf-8-sig',newline='')))
ev=json.loads((H/'target-evidence.json').read_text())
status=list(csv.DictReader((H/'TARGET-STATUS.csv').open(encoding='utf-8-sig',newline='')))
assert len(q)==len(ev['targets'])==len(status)==10
assert [x['sample_id'] for x in q]==[x['sample_id'] for x in ev['targets']]==[x['sample_id'] for x in status]
assert [x['tic'] for x in q]==[x['tic'] for x in ev['targets']]==[x['tic'] for x in status]
assert ev['queue_sha256']==seal['queue_sha256']
for label,s in ev['source_hashes'].items():assert sha(Path(s['path']))==s['sha256'],label
hb=json.loads((H/'heartbeat-overlaps.json').read_text())
for s in hb['sources']:assert sha(Path(s['path']))==s['sha256'],s['paper']
ch=json.loads((H/'chopard-overlaps.json').read_text())
for s in ch['sources']:assert sha(Path(s['path']))==s['sha256']
tm=json.loads((H/'tarrants-mendes-overlaps.json').read_text())
assert sha(Path(tm['source']['path']))==tm['source']['sha256']
assert sha(Path(tm['primary_html_exact_gaia_check']['path']))==tm['primary_html_exact_gaia_check']['sha256']
remote=json.loads((H/'remote-receipts.json').read_text())
for label,r in remote.items():
    assert r['queue_sha256']==seal['queue_sha256']
    if r['status']=='success':assert sha(Path(r['raw']))==r['sha256'],label
controls=json.loads((H/'vizier-controls.json').read_text())
for r in controls:
    assert r['queue_sha256']==seal['queue_sha256']
    if r['status']=='success':assert sha(Path(r['raw']))==r['sha256']
nrec=json.loads((H/'gaia-neighbors.receipt.json').read_text())
neighbors=json.loads((H/'gaia-neighbors.json').read_text())
assert nrec['queue_sha256']==neighbors['queue_sha256']==seal['queue_sha256']
assert nrec['status']=='success' and sha(Path(nrec['raw']))==nrec['raw_sha256']
assert set(neighbors['targets'])=={x['sample_id'] for x in q}
assert all(x['vsx_asassn_kostov_gates'].startswith('UNKNOWN') for x in status)
assert status[5]['tic']=='318209162' and 'Tarrants' in status[5]['prior_alerts']
print('PASS: sealed N001-N010, source hashes, raw remote receipts, neighbor scope, statuses')
