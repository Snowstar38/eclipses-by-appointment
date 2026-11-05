"""Verify fixed input identities and seal all batch-owned artifacts."""
import csv,hashlib,json
from pathlib import Path
B=Path(__file__).resolve().parent;R=B.parent
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
q=list(csv.DictReader((B/'queue.csv').open(newline='',encoding='utf-8')))
assert [r['sample_id'] for r in q]==[f'T{i:03d}' for i in range(11,21)]
source={'queue':{'path':str(B/'queue.csv'),'sha256':sha(B/'queue.csv')},'targets':{}}
for r in q:
    tic=r['tic'];packet=R/'source-packets'/tic/'sources.json';p=json.loads(packet.read_text());n=json.loads((B/tic/'lead-numeric.json').read_text());
    assert p['queue_row']['sample_id']==r['sample_id'] and p['queue_row']['tic']==tic
    original={Path(x['path']).resolve():x['sha256'] for x in p['target']['files']}
    used={Path(x['path']).resolve():x['sha256'] for x in n['sources']}
    assert original==used
    assert all(sha(fp)==digest for fp,digest in used.items())
    bulk=Path(p['bulk_result']);fold=Path(p['fold_result'])
    assert sha(bulk)==p['bulk_result_sha256'] and sha(fold)==p['fold_result_sha256']
    source['targets'][r['sample_id']]={'tic':tic,'source_packet':{'path':str(packet),'sha256':sha(packet)},'bulk_result':{'path':str(bulk),'sha256':sha(bulk)},'fold_result':{'path':str(fold),'sha256':sha(fold)},'fits':[{'path':str(fp),'sha256':digest} for fp,digest in used.items()]}
source['additional_cutouts']=[]
for receipt_file in ('helper-fetch.json','lead-s105-fetch.json','lead-exception-fetch.json'):
    receipt_path=B/receipt_file
    if not receipt_path.exists():continue
    for entry in json.loads(receipt_path.read_text(encoding='utf-8')):
        if entry.get('error'):continue
        fp=Path(entry.get('fits_path') or B/f"helper-{entry['tic']}-s{entry['sector']}.fits")
        digest=entry.get('fits_sha256') or entry.get('sha256')
        assert sha(fp)==digest,(fp,digest)
        source['additional_cutouts'].append({'receipt':receipt_file,'path':str(fp),'sha256':digest,'url':entry.get('url')})
(B/'SOURCE-HASHES.json').write_text(json.dumps(source,indent=2)+'\n',encoding='utf-8')
manifest={str(p.relative_to(B)).replace('\\','/'):sha(p) for p in B.rglob('*') if p.is_file() and p.name!='SHA256SUMS.json'}
(B/'SHA256SUMS.json').write_text(json.dumps({'algorithm':'SHA256','files':manifest},indent=2)+'\n',encoding='utf-8')
print('sealed',len(q),'targets',sum(len(v['fits']) for v in source['targets'].values()),'FITS',len(manifest),'batch files')
