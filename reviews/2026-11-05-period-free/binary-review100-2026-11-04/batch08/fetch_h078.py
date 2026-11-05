import csv,hashlib,io,json,zipfile
from pathlib import Path
import requests
B=Path(__file__).resolve().parent
r=next(x for x in csv.DictReader((B/'queue.csv').open()) if x['tic']=='295743311')
for sector in (87,108):
 rec={'tic':r['tic'],'sector':sector,'purpose':'source and current-sector check for insecure fold event'}
 try:
  response=requests.get('https://mast.stsci.edu/tesscut/api/v0.1/astrocut',params={'ra':r['ra_deg'],'dec':r['dec_deg'],'x':7,'y':7,'units':'px','sector':sector},timeout=90)
  raw=response.content;p=B/r['tic']/f's{sector}-tesscut.raw';p.write_bytes(raw)
  rec.update(url=response.url,http_status=response.status_code,raw_sha256=hashlib.sha256(raw).hexdigest())
  response.raise_for_status();z=zipfile.ZipFile(io.BytesIO(raw));data=z.read(z.namelist()[0]);p=B/r['tic']/f's{sector}-tesscut.fits';p.write_bytes(data);rec['fits_sha256']=hashlib.sha256(data).hexdigest()
 except Exception as e:rec['error']=repr(e)
 (B/r['tic']/f's{sector}-tesscut-receipt.json').write_text(json.dumps(rec,indent=2)+'\n')
 print(sector,rec.get('http_status'),rec.get('error'),flush=True)
