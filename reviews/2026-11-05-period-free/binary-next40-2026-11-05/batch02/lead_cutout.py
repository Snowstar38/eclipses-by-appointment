"""Fetch small TESSCut WCS cubes for source attribution of F014."""
import hashlib, json, requests
from pathlib import Path
B=Path(__file__).resolve().parent
O=B/'236223193'/'cutouts';O.mkdir(parents=True,exist_ok=True)
items=[]
for sector in (41,55,75):
    url='https://mast.stsci.edu/tesscut/api/v0.1/astrocut'
    args=dict(ra=313.71484129,dec=35.42214602,x=11,y=11,sector=sector)
    r=requests.get(url,params=args,timeout=90);r.raise_for_status()
    if r.headers.get('Content-Type','').split(';')[0]!='application/zip':raise RuntimeError((sector,r.status_code,r.text[:300]))
    p=O/f's{sector:03d}.zip';p.write_bytes(r.content)
    items.append(dict(sector=sector,url=r.url,sha256=hashlib.sha256(r.content).hexdigest(),size=len(r.content)))
    print(sector,len(r.content),flush=True)
(O/'receipts.json').write_text(json.dumps(items,indent=2)+'\n',encoding='utf-8')
