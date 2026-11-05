import csv,json,requests,hashlib,zipfile,io
from pathlib import Path
B=Path(__file__).resolve().parent
Q={r['tic']:r for r in csv.DictReader((B/'queue.csv').open())}
for tic,sector in [('392924671',23)]:
 q=Q[tic];dest=B/tic;rec={'sector':sector}
 try:
  r=requests.get('https://mast.stsci.edu/tesscut/api/v0.1/astrocut',params={'ra':q['ra_deg'],'dec':q['dec_deg'],'y':11,'x':11,'units':'px','sector':sector},timeout=90)
  (dest/'tesscut.raw').write_bytes(r.content)
  rec.update(url=r.url,http_status=r.status_code,response_sha256=hashlib.sha256(r.content).hexdigest())
  r.raise_for_status()
  z=zipfile.ZipFile(io.BytesIO(r.content));data=z.read(z.namelist()[0]);(dest/'tesscut.fits').write_bytes(data)
  rec['fits_sha256']=hashlib.sha256(data).hexdigest()
 except Exception as e:rec['error']=repr(e)
 (dest/'tesscut-receipt.json').write_text(json.dumps(rec,indent=2)+'\n')
 print(tic,rec,flush=True)
