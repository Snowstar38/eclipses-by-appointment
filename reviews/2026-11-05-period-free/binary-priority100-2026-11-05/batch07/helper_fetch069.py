import requests,zipfile,io,hashlib,json
from pathlib import Path
p=Path(__file__).parent/'159851783'
for sec in (25,26,52):
 r=requests.get('https://mast.stsci.edu/tesscut/api/v0.1/astrocut',params=dict(ra=269.20305283850354,dec=39.29748048697943,x=9,y=9,units='px',sector=sec),timeout=120);r.raise_for_status();z=zipfile.ZipFile(io.BytesIO(r.content));d=z.read(z.namelist()[0]);(p/f'helper-s{sec}-tesscut.fits').write_bytes(d);(p/f'helper-s{sec}-receipt.json').write_text(json.dumps(dict(url=r.url,status=r.status_code,zip_sha256=hashlib.sha256(r.content).hexdigest(),member=z.namelist()[0],fits_sha256=hashlib.sha256(d).hexdigest()),indent=2));print(sec,len(d),flush=True)
