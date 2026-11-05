import csv,json,requests,hashlib,zipfile,io
from pathlib import Path
B=Path(__file__).resolve().parent;z=next(r for r in csv.DictReader((B/'queue.csv').open()) if r['tic']=='299187993');h=B/'helper-pixels'/'299187993-s100';h.mkdir(exist_ok=True);s={'sector':100}
try:
 r=requests.get('https://mast.stsci.edu/tesscut/api/v0.1/astrocut',params={'ra':z['ra_deg'],'dec':z['dec_deg'],'y':11,'x':11,'units':'px','sector':100},timeout=45);(h/'tesscut.raw').write_bytes(r.content);s.update(url=r.url,status=r.status_code,raw_sha256=hashlib.sha256(r.content).hexdigest());r.raise_for_status();z=zipfile.ZipFile(io.BytesIO(r.content));data=z.read(z.namelist()[0]);(h/'tesscut.fits').write_bytes(data);s['fits_sha256']=hashlib.sha256(data).hexdigest()
except Exception as e:s['error']=repr(e)
(h/'receipt.json').write_text(json.dumps(s,indent=2));print(s)
