import requests,hashlib,io,zipfile,json
from pathlib import Path
B=Path(__file__).parent
r=requests.get('https://mast.stsci.edu/tesscut/api/v0.1/astrocut',params={'ra':76.02231052016369,'dec':-31.955054951066305,'x':11,'y':11,'units':'px','sector':98},timeout=90);o={'status':r.status_code,'url':r.url,'zip_sha256':hashlib.sha256(r.content).hexdigest()};r.raise_for_status(); z=zipfile.ZipFile(io.BytesIO(r.content));data=z.read(z.namelist()[0]);(B/'helper-cut-1535458-s98.fits').write_bytes(data);o['fits_sha256']=hashlib.sha256(data).hexdigest();(B/'helper-cut-1535458-s98-receipt.json').write_text(json.dumps(o,indent=2));print(o)
