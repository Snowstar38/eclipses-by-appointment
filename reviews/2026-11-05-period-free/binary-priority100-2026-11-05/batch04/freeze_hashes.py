"""Freeze batch03 source and output SHA-256 receipts, excluding self-reference."""
import csv,json,hashlib
from pathlib import Path
B=Path(__file__).resolve().parent;ROOT=B.parent
def digest(p):
    h=hashlib.sha256()
    with p.open('rb') as f:
        for block in iter(lambda:f.read(1<<20),b''):h.update(block)
    return h.hexdigest()
sources=[]
for r in csv.DictReader((B/'queue.csv').open(newline='',encoding='utf-8')):
    sid=r['sample_id'];tic=r['tic'];sp=ROOT/'source-packets'/tic/'sources.json';bp=ROOT.parent/'binary-exploration-2026-11-04'/'bulk-results'/f'{tic}.json'
    sources.extend([dict(sample_id=sid,role='source_packet',path=str(sp),sha256=digest(sp)),dict(sample_id=sid,role='bulk_windows',path=str(bp),sha256=digest(bp))])
    m=json.loads((B/tic/'lead-numeric.json').read_text())
    for q in m['sources']:
        p=Path(q['path']);actual=digest(p);assert actual==q['sha256'],p
        sources.append(dict(sample_id=sid,role='qlp_raw',sector=q['sector'],path=str(p),sha256=actual))
for p in (ROOT/'shared-catalogues/gaia-neighbors.json',ROOT/'shared-catalogues/gaia_nss.csv',ROOT/'shared-catalogues/TARGET-STATUS.csv',B/'queue.csv'):
    sources.append(dict(role='shared_or_queue',path=str(p),sha256=digest(p)))
(B/'SOURCE-HASHES.json').write_text(json.dumps(dict(scope='batch04 T031-T040 only',verified_sources=sources),indent=2)+'\n')
manifest={}
for p in sorted(B.rglob('*')):
    if p.is_file() and p.name!='SHA256SUMS.json':manifest[str(p.relative_to(B)).replace('\\','/')]=digest(p)
(B/'SHA256SUMS.json').write_text(json.dumps(dict(scope='batch04',algorithm='SHA-256',files=manifest),indent=2)+'\n')
print('sources',len(sources),'batch files',len(manifest))

