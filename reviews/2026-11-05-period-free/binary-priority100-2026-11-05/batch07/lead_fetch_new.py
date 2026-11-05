"""Fetch only newly available TESSCut sectors for bounded review."""
import csv, hashlib, io, json, zipfile
from pathlib import Path
import requests

B=Path(__file__).resolve().parent
rows={r['sample_id']:r for r in csv.DictReader((B/'queue.csv').open())}
for sample, sector in [('T064',109),('T070',107),('T070',108)]:
    r=rows[sample]; out=B/r['tic'];out.mkdir(exist_ok=True)
    url='https://mast.stsci.edu/tesscut/api/v0.1/astrocut'
    response=requests.get(url,params=dict(ra=r['ra_deg'],dec=r['dec_deg'],x=7,y=7,units='px',sector=sector),timeout=120)
    raw=out/f'lead-s{sector}-tesscut.raw';raw.write_bytes(response.content)
    rec=dict(sample_id=sample,tic=r['tic'],sector=sector,url=response.url,status=response.status_code,raw_sha256=hashlib.sha256(response.content).hexdigest(),raw_bytes=len(response.content))
    if response.ok:
        z=zipfile.ZipFile(io.BytesIO(response.content));name=z.namelist()[0];dat=z.read(name)
        fp=out/f'lead-s{sector}-tesscut.fits';fp.write_bytes(dat)
        rec.update(member=name,fits_path=str(fp),fits_sha256=hashlib.sha256(dat).hexdigest(),fits_bytes=len(dat))
    (out/f'lead-s{sector}-receipt.json').write_text(json.dumps(rec,indent=2)+'\n')
    print(sample,sector,response.status_code,len(response.content),flush=True)
