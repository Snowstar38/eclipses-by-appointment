import requests,zipfile,io,pathlib,hashlib
p=pathlib.Path('batch04/51321183/helper-tesscut-s061.fits')
r=requests.get('https://mast.stsci.edu/tesscut/api/v0.1/astrocut',params={'ra':128.7041155236352,'dec':-6.074294318670607,'y':11,'x':11,'units':'px','sector':61},timeout=120);print(r.status_code,len(r.content));r.raise_for_status();z=zipfile.ZipFile(io.BytesIO(r.content));p.write_bytes(z.read(z.namelist()[0]));print(hashlib.sha256(p.read_bytes()).hexdigest())
