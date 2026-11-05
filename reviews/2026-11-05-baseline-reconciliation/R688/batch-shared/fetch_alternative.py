"""Fetch two bounded TESS-SPOC same-photon reductions for cross-check."""
import hashlib,json,requests
from pathlib import Path
H=Path(__file__).parent
rows=json.load(open(H/'mast-availability.json'))['response']['data']
out=[]
for sec in (56,84):
    x=next(z for z in rows if z['sequence_number']==sec and z['provenance_name']=='TESS-SPOC')
    path=H/f'tess-spoc-s{sec:03d}.fits'
    if not path.exists():
        r=requests.get('https://mast.stsci.edu/api/v0.1/Download/file',params={'uri':x['dataURL']},timeout=(10,60));r.raise_for_status();path.write_bytes(r.content)
    out.append(dict(sector=sec,path=str(path),mast_uri=x['dataURL'],sha256=hashlib.sha256(path.read_bytes()).hexdigest(),bytes=path.stat().st_size))
(H/'alternative-receipts.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
