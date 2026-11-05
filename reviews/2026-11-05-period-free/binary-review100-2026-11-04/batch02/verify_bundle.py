"""Validate sealed queue/source receipts and freeze batch02 artifact hashes."""
import csv, hashlib, json
from pathlib import Path

B=Path(__file__).resolve().parent
digest=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
seal=json.loads((B.parent/'queue-seal.json').read_text(encoding='utf-8'))
if digest(B/'queue.csv') != seal['batch_sha256']['batch02']:
    raise RuntimeError('queue seal mismatch')
rows=list(csv.DictReader((B/'queue.csv').open(newline='',encoding='utf-8')))
results=list(csv.DictReader((B/'RESULTS.csv').open(newline='',encoding='utf-8')))
if len(rows)!=10 or [r['tic'] for r in rows] != [r['tic'] for r in results]:
    raise RuntimeError('queue/results mismatch')
verified=[]
cutout_receipts=json.loads((B.parent/'missing-coverage'/'cutout-receipts.json').read_text(encoding='utf-8'))
cutout_verified=[]
for receipt in cutout_receipts:
    if receipt.get('status')=='ok' and receipt.get('tic') in {'231694897','323818250'}:
        fp=Path(receipt['path'])
        if digest(fp)!=receipt['sha256']:
            raise RuntimeError('cutout receipt mismatch '+str(fp))
        cutout_verified.append({'tic':receipt['tic'],'sector':receipt['sector'],
                                'path':str(fp),'sha256':receipt['sha256']})
for row in rows:
    tic=row['tic']; packet=B.parent/'source-packets'/tic/'sources.json'
    src=json.loads(packet.read_text(encoding='utf-8'))
    if src['queue_row']['sample_id'] != row['sample_id']:
        raise RuntimeError('packet ID mismatch '+tic)
    bulk=Path(src['bulk_result'])
    if digest(bulk) != src['bulk_result_sha256']:
        raise RuntimeError('bulk receipt mismatch '+tic)
    fold=src.get('fold_result')
    if fold and digest(Path(fold)) != src['fold_result_sha256']:
        raise RuntimeError('fold receipt mismatch '+tic)
    raw=json.loads((B/tic/'raw-inspection.json').read_text())
    for entry in src['target']['files']:
        fp=Path(entry['path'])
        actual=digest(fp)
        if actual != entry['sha256']:
            raise RuntimeError('FITS receipt mismatch '+str(fp))
    verified.append({'sample_id':row['sample_id'],'tic':tic,'packet':str(packet),
                     'packet_sha256':digest(packet),'bulk_sha256':digest(bulk),
                     'fold_sha256':digest(Path(fold)) if fold else None,
                     'fits_count':len(src['target']['files']),
                     'raw_inspection_bulk_sha256':raw['bulk_json_sha256']})
    if raw['bulk_json_sha256'] != src['bulk_result_sha256']:
        raise RuntimeError('raw/bulk receipt mismatch '+tic)
(B/'source-verification.json').write_text(json.dumps({'queue_sha256':digest(B/'queue.csv'),
    'targets':verified,'fits_verified':sum(x['fits_count'] for x in verified),
    'missing_sector_cutouts_verified':cutout_verified},indent=2)+'\n',encoding='utf-8')
hashes={str(p.relative_to(B)).replace('\\','/'):digest(p) for p in sorted(B.rglob('*'))
        if p.is_file() and p.name!='SHA256SUMS.json'}
(B/'SHA256SUMS.json').write_text(json.dumps({'algorithm':'SHA-256','files':hashes},indent=2)+'\n',encoding='utf-8')
print('targets',len(verified),'FITS',sum(x['fits_count'] for x in verified),
      'extra cutouts',len(cutout_verified),'artifacts',len(hashes))
