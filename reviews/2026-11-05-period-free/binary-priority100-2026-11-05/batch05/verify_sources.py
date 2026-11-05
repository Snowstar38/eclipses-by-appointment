"""Check fixed identity and all per-target source receipts used by batch05."""
import csv,hashlib,json
from pathlib import Path
B=Path(__file__).resolve().parent;R=B.parent
rows=list(csv.DictReader((B/'queue.csv').open(encoding='utf-8',newline='')))
out=[]
for r in rows:
    tic=r['tic'];p=R/'source-packets'/tic/'sources.json';d=json.loads(p.read_text(encoding='utf-8'))
    assert d['queue_row']['sample_id']==r['sample_id'] and d['queue_row']['gaia_dr3']==r['gaia_dr3']
    br=Path(d['bulk_result']);fr=Path(d['fold_result'])
    assert hashlib.sha256(br.read_bytes()).hexdigest()==d['bulk_result_sha256']
    assert hashlib.sha256(fr.read_bytes()).hexdigest()==d['fold_result_sha256']
    m=json.loads((B/tic/'lead-numeric.json').read_text(encoding='utf-8'))
    for s in m['sources']:
        assert hashlib.sha256(Path(s['path']).read_bytes()).hexdigest()==s['sha256']
    out.append(dict(sample_id=r['sample_id'],tic=tic,source_packet_sha256=hashlib.sha256(p.read_bytes()).hexdigest(),bulk_sha256=d['bulk_result_sha256'],fold_sha256=d['fold_result_sha256'],verified_fits=len(m['sources'])))
(B/'source-verification.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print('verified',len(out),'targets,',sum(x['verified_fits'] for x in out),'FITS files')
