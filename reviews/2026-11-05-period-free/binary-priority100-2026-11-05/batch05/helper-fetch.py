import requests,hashlib,json,zipfile,io,pathlib
B=pathlib.Path(__file__).parent
r=requests.get('https://mast.stsci.edu/tesscut/api/v0.1/astrocut',params=dict(ra=258.80305873874653,dec=-68.89193314417133,x=11,y=11,units='px',sector=66),timeout=120)
o=dict(url=r.url,status=r.status_code,raw_sha256=hashlib.sha256(r.content).hexdigest());r.raise_for_status();z=zipfile.ZipFile(io.BytesIO(r.content));d=z.read(z.namelist()[0]);p=B/'helper-255912894-s66.fits';p.write_bytes(d);o.update(member=z.namelist()[0],fits_sha256=hashlib.sha256(d).hexdigest());(B/'helper-fetch-receipt.json').write_text(json.dumps(o,indent=2));print(o)
