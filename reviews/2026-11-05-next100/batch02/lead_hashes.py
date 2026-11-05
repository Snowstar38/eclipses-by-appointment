"""Verify all used source receipts and freeze a leaf SHA256 manifest."""
import csv,hashlib,json
from pathlib import Path
B=Path(__file__).resolve().parent;ROOT=B.parent
rows=list(csv.DictReader((B/'queue.csv').open(encoding='utf-8',newline='')))
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
sources=[]
for row in rows:
    tic=row['tic'];pktpath=ROOT/'source-packets'/tic/'sources.json'
    pkt=json.loads(pktpath.read_text(encoding='utf-8'))
    assert sha(pkt['bulk_result'])==pkt['bulk_result_sha256']
    target=dict(sample_id=row['sample_id'],tic=tic,source_packet_path=str(pktpath),source_packet_sha256=sha(pktpath),bulk_result_path=pkt['bulk_result'],bulk_result_sha256=pkt['bulk_result_sha256'],fits=[])
    inv=json.loads((B/tic/'lead-inventory.json').read_text(encoding='utf-8'))
    used={s['sector'] for s in inv['sectors']}
    for rec in pkt['verified_files']:
        if int(rec['sector']) not in used:continue
        assert sha(rec['path'])==rec['sha256']
        target['fits'].append(dict(sector=rec['sector'],path=rec['path'],sha256=rec['sha256']))
    if (B/tic/'cutouts'/'receipts.json').exists():
        target['tesscut']=[]
        for rec in json.loads((B/tic/'cutouts'/'receipts.json').read_text(encoding='utf-8')):
            assert sha(rec['path'])==rec['sha256']
            target['tesscut'].append(rec)
    sources.append(target)
(B/'lead-source-hashes.json').write_text(json.dumps(sources,indent=2)+'\n',encoding='utf-8')
files={p.relative_to(B).as_posix():sha(p) for p in B.rglob('*') if p.is_file() and p.name not in {'SHA256SUMS.json','ROOT-ACCEPTANCE.json'} and '__pycache__' not in p.parts}
(B/'SHA256SUMS.json').write_text(json.dumps({'files':dict(sorted(files.items()))},indent=2)+'\n',encoding='utf-8')
print('verified',len(sources),'targets',sum(len(x['fits']) for x in sources),'FITS',len(files),'batch leaves')
