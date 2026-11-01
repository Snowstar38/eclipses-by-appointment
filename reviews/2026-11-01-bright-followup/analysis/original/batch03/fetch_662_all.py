"""Fetch every archived QLP sector for the sparse-repeat exception."""
import json,hashlib,requests
from pathlib import Path
from astropy.io import fits
B=Path(__file__).parent;R=B.parent
tic='66281997';target=json.loads((R/'targets-selected.json').read_text())[tic]
recs=json.loads((B/'download-receipts.json').read_text())
for sector,uri in target['qlp']:
    if any(r['tic']==tic and r['sector']==sector for r in recs):continue
    p=R/'shared-qlp'/f'{tic}_s{sector:03d}.fits'
    rec=dict(tic=tic,sector=sector,uri=uri,file=str(p))
    try:
        if not p.exists():
            response=requests.get('http[local path omitted]',params={'uri':uri},timeout=120)
            response.raise_for_status();p.write_bytes(response.content)
        with fits.open(p) as h:
            rec['rows']=len(h[1].data);rec['columns']=h[1].columns.names
        rec.update(status='ok',bytes=p.stat().st_size,sha256=hashlib.sha256(p.read_bytes()).hexdigest())
    except Exception as exc:rec.update(status='error',error=str(exc))
    recs.append(rec);print(sector,rec['status'],flush=True)
(B/'download-receipts.json').write_text(json.dumps(recs,indent=2))
