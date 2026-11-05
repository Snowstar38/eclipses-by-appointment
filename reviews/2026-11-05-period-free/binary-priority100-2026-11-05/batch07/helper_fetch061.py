import requests,zipfile,io,hashlib,json
from pathlib import Path
p=Path(r'[local-path-redacted]')
r=requests.get('https://mast.stsci.edu/tesscut/api/v0.1/astrocut',params=dict(ra=352.5436348384747,dec=45.50009877742365,x=11,y=11,units='px',sector=84),timeout=120)
r.raise_for_status(); z=zipfile.ZipFile(io.BytesIO(r.content)); d=z.read(z.namelist()[0]); f=p/'helper-s84-tesscut.fits'; f.write_bytes(d)
(p/'helper-s84-receipt.json').write_text(json.dumps(dict(url=r.url,status=r.status_code,zip_sha256=hashlib.sha256(r.content).hexdigest(),member=z.namelist()[0],fits_sha256=hashlib.sha256(d).hexdigest()),indent=2))
print(len(d))
