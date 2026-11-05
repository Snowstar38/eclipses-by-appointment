import requests,zipfile,io,pathlib,hashlib,json
p=pathlib.Path('batch03/288649491/helper-tesscut-s034.fits')
r=requests.get('https://mast.stsci.edu/tesscut/api/v0.1/astrocut',params={'ra':114.56091667734572,'dec':-16.39317626748244,'y':11,'x':11,'units':'px','sector':34},timeout=120); print(r.status_code,len(r.content),r.url); r.raise_for_status(); z=zipfile.ZipFile(io.BytesIO(r.content)); p.write_bytes(z.read(z.namelist()[0])); print(hashlib.sha256(p.read_bytes()).hexdigest())
import requests,zipfile,io,pathlib,hashlib
p=pathlib.Path('batch03/324424395/helper-tesscut-s093.fits'); r=requests.get('https://mast.stsci.edu/tesscut/api/v0.1/astrocut',params={'ra':285.51475471576595,'dec':-73.66926980232525,'y':11,'x':11,'units':'px','sector':93},timeout=120);print(r.status_code,len(r.content));r.raise_for_status();z=zipfile.ZipFile(io.BytesIO(r.content));p.write_bytes(z.read(z.namelist()[0]));print(hashlib.sha256(p.read_bytes()).hexdigest())
