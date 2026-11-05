"""Verify the sealed forty, source and raw remote receipt hashes, and statuses."""
import csv, hashlib, json
from pathlib import Path
H=Path(__file__).resolve().parent; B=H.parent
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
seal=json.loads((B/'queue-seal.json').read_text())
assert sha(B/'queue.csv')==seal['queue_sha256']
q=list(csv.DictReader((B/'queue.csv').open(encoding='utf-8-sig',newline='')))
ev=json.loads((H/'target-evidence.json').read_text())
status=list(csv.DictReader((H/'TARGET-STATUS.csv').open(encoding='utf-8-sig',newline='')))
assert len(q)==len(ev['targets'])==len(status)==40
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
vr=json.loads((H/'vizier-gate-receipts.json').read_text())
vg=json.loads((H/'vizier-gate-results.json').read_text())
assert vg['queue_sha256']==seal['queue_sha256'] and len(vr)==160
assert set(vg['targets'])=={x['sample_id'] for x in q}
for k,r in vr.items():
    assert r['queue_sha256']==seal['queue_sha256']
    if r['status']=='success':assert sha(Path(r['raw']))==r['sha256'],k
controls=json.loads((H/'kostov-controls.json').read_text())
for k,r in controls.items():
    assert r['queue_sha256']==seal['queue_sha256']
    if r['status']=='success':assert sha(Path(r['raw']))==r['sha256'],k
known={'F008','F022','F023','F035','F038'}
assert {x['sample_id'] for x in status if x['novelty_status'].startswith('KNOWN_PUBLISHED_EB_ALERT')}==known
assert all(x['novelty_status'].startswith('SCOPED_NONMATCH') for x in status if x['sample_id'] not in known)
assert status[22]['tic']=='286094277' and 'Tarrants' in status[22]['published_eb_alerts']
assert status[10]['tic']=='17238861' and status[10]['local_prior_candidate_alerts']
manifest=json.loads((H/'SHA256SUMS.json').read_text())
for name,digest in manifest.items():assert sha(H/name)==digest,name
assert set(manifest)=={p.relative_to(H).as_posix() for p in H.rglob('*') if p.is_file() and p.name!='SHA256SUMS.json' and '__pycache__' not in p.parts}
print('PASS: sealed F001-F040, source hashes, 160 raw VizieR receipts, neighbor scope, statuses, artifact manifest')
