import hashlib,json,requests
from pathlib import Path
from astropy.io import fits

B=Path(__file__).parent; R=B.parent
tic='382581210'; target=json.loads((R/'targets-selected.json').read_text())[tic]
rows=[]
for sec,uri in target['qlp']:
 p=R/'shared-qlp'/f'{tic}_s{sec:03}.fits'
 if not p.exists():
  r=requests.get('http[local path omitted]',params={'uri':uri},timeout=120)
  r.raise_for_status(); p.write_bytes(r.content)
 with fits.open(p) as h:
  assert str(h[0].header.get('TICID'))==tic
  n=len(h[1].data); assert n>0
 rec=dict(tic=tic,sector=sec,uri=uri,file=str(p),rows=n,status='ok',bytes=p.stat().st_size,sha256=hashlib.sha256(p.read_bytes()).hexdigest())
 rows.append(rec); print(sec,n,rec['bytes'],flush=True)
(B/'sparse-sector-receipts.json').write_text(json.dumps(rows,indent=2)+'\n')
