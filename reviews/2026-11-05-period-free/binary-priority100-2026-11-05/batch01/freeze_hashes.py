"""Validate fixed batch identities and freeze checksums after all lead/helper edits."""
import csv,hashlib,json
from pathlib import Path
B=Path(__file__).resolve().parent; R=B.parent
def h(p):
    z=hashlib.sha256()
    with p.open('rb') as f:
        for block in iter(lambda:f.read(4*1024*1024),b''):z.update(block)
    return z.hexdigest()
q=list(csv.DictReader((B/'queue.csv').open(newline='',encoding='utf-8')))
r=list(csv.DictReader((B/'RESULTS.csv').open(newline='',encoding='utf-8')))
assert len(q)==len(r)==10
assert [(x['sample_id'],x['tic'],x['sample_stratum']) for x in q]==[(x['sample_id'],x['tic'],x['sample_stratum']) for x in r]
seal=json.loads((R/'queue-seal.json').read_text())
assert h(B/'queue.csv')==seal['batch_sha256']['batch01']
for x in r:
    p=Path(x['report']);assert p.is_file() and p.parent==B/x['tic']
    assert (p.parent/'lead-numeric.json').is_file() and (p.parent/'lead-timing.json').is_file()
    assert x['novelty_status']=='UNKNOWN' and x['full_review_completion']=='COMPLETE'
    assert x['physical_verdict'] in {'CONFIRMED','PROBABLE','PLAUSIBLE','REFUTED'}
files={p.relative_to(B).as_posix():h(p) for p in sorted(B.rglob('*')) if p.is_file() and p.name!='SHA256SUMS.json'}
for x in q:
    p=R/'source-packets'/x['tic']/'sources.json';files['../source-packets/'+x['tic']+'/sources.json']=h(p)
for name in ['queue-seal.json','shared-catalogues/gaia_nss.csv','shared-catalogues/gaia-neighbors.json','shared-catalogues/TARGET-STATUS.csv']:
    files['../'+name]=h(R/name)
output=dict(batch='batch01',sample_ids=[x['sample_id'] for x in q],queue_sha256=files['queue.csv'],algorithm='SHA-256',files=files,note='Paths are relative to batch01. SOURCE-SHA256 receipts inside source packets bind bulk and FITS files; source packets and shared Gaia/catalogue inputs are also frozen here. This file does not hash itself.')
(B/'SHA256SUMS.json').write_text(json.dumps(output,indent=2)+'\n',encoding='utf-8')
print(len(files),'files hashed; verdicts', {v:sum(x['physical_verdict']==v for x in r) for v in sorted({x['physical_verdict'] for x in r})})
