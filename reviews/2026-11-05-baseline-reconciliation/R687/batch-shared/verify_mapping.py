"""Exact fixed-queue and final-row/source-receipt integrity gate."""
import csv, hashlib, json
from pathlib import Path
W=Path(__file__).resolve().parent
S=W.parent/'search256'
q=list(csv.DictReader((W/'queue.csv').open(newline='',encoding='utf-8')))
r=list(csv.DictReader((W/'RESULTS.csv').open(newline='',encoding='utf-8')))
snap=json.loads((W/'SOURCE-SNAPSHOT.json').read_text(encoding='utf-8'))
assert [x['tic'] for x in q]==['167197264','155346713']==[x['tic'] for x in r]
assert len(set(x['gaia_dr3_source_id'] for x in q))==2
assert all(x['gaia_dr3_source_id']==y['gaia_dr3_source_id']==snap['targets'][x['tic']]['gaia_source_id'] for x,y in zip(q,r))
assert all(y['full_review_completion']=='COMPLETE_LEAD_HELPER_ROOT_CATALOGUE_PENDING' and y['count_eligible_now']=='false' for y in r)
assert r[0]['physical_verdict']=='probable' and r[1]['physical_verdict']=='plausible'
assert r[1]['period_days']=='' and r[1]['gaia_period_days']!=''
for p,h in snap['source_sha256'].items():
    assert hashlib.sha256(Path(p).read_bytes()).hexdigest()==h,p
for x in q:
    target=snap['targets'][x['tic']]
    for item in target['raw_fits']:
        assert hashlib.sha256(Path(item['path']).read_bytes()).hexdigest()==item['sha256'],item['path']
    assert hashlib.sha256(Path(target['screen_plot']['path']).read_bytes()).hexdigest()==target['screen_plot']['sha256']
    assert (W/r[int(x['queue_index'])-1]['report']).exists()
old167=json.loads((W/'helper-downloads-167197264.json').read_text())['products']
old155=json.loads((S/'followups'/'downloads-155346713.json').read_text())['products']
for item in old167+old155:
    assert item['status']=='ok' and hashlib.sha256(Path(item['path']).read_bytes()).hexdigest()==item['sha256']
for receipt in [W/'pixel-155-s88-download.json',W/'helper-pixel-download-167197264.json']:
    v=json.loads(receipt.read_text());assert v['status']=='ok'
    key='fits_sha256' if 'fits_sha256' in v else 'tesscut_fits_sha256'
    assert hashlib.sha256(Path(v['fits_path']).read_bytes()).hexdigest()==v[key]
out={'queue_order':[x['tic'] for x in q],'row_count':len(r),'source_hashes_checked':len(snap['source_sha256']),
     'frozen_fits_checked':sum(len(snap['targets'][x['tic']]['raw_fits']) for x in q),
     'older_fits_checked':len(old167+old155),'pixel_fits_checked':2,
     'status':'pass','scope':'local source identities, hashes and exact result mapping; not catalogue clearance'}
(W/'verify-result-mapping.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
print(json.dumps(out,indent=2))
