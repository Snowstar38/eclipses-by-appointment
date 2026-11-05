import requests,csv,json,zipfile,io,hashlib
from pathlib import Path
B=Path(__file__).resolve().parent;q=list(csv.DictReader((B/'queue.csv').open()));out=[]
for row in [q[7],q[9]]:
 try:
  r=requests.get('https://mast.stsci.edu/tesscut/api/v0.1/astrocut',params={'ra':row['ra_deg'],'dec':row['dec_deg'],'x':11,'y':11,'units':'px','sector':109},timeout=120);r.raise_for_status();z=zipfile.ZipFile(io.BytesIO(r.content));data=z.read(z.namelist()[0]);(B/f'helper-{row["tic"]}-s109.fits').write_bytes(data);out.append({'tic':row['tic'],'url':r.url,'status':r.status_code,'zip_sha256':hashlib.sha256(r.content).hexdigest(),'fits_sha256':hashlib.sha256(data).hexdigest()})
 except Exception as e:out.append({'tic':row['tic'],'error':repr(e)})
(B/'helper-s109-fetch.json').write_text(json.dumps(out,indent=2));print(out)
