from pathlib import Path
import csv,json,requests,hashlib,zipfile,io
from concurrent.futures import ThreadPoolExecutor
from astropy.io import fits
B=Path(__file__).resolve().parent
Q={r['tic']:r for r in csv.DictReader((B/'queue.csv').open())}
jobs=[('423569223',101),('393487481',46),('393487481',72),('41859748',104),('41859748',105),('41859748',106),('41859748',107)]
def get(job):
 tic,s=job;r=Q[tic];p={'ra':r['ra_deg'],'dec':r['dec_deg'],'x':11,'y':11,'units':'px','sector':s};rec={'tic':tic,'sector':s,'params':p}
 try:
  resp=requests.get('https://mast.stsci.edu/tesscut/api/v0.1/astrocut',params=p,timeout=(15,90));rec.update(url=resp.url,http_status=resp.status_code,response_sha256=hashlib.sha256(resp.content).hexdigest());resp.raise_for_status()
  z=zipfile.ZipFile(io.BytesIO(resp.content));names=[n for n in z.namelist() if n.endswith('.fits')];assert len(names)==1
  data=z.read(names[0]);path=B/tic/f'helper-cutout-s{s:03d}.fits';path.write_bytes(data)
  with fits.open(path) as h: rec['samples']=len(h[1].data)
  rec.update(status='ok',path=str(path),sha256=hashlib.sha256(data).hexdigest(),member=names[0])
 except Exception as e:rec.update(status='unavailable',error=repr(e))
 print(tic,s,rec['status'],flush=True);return rec
with ThreadPoolExecutor(4) as pool:r=list(pool.map(get,jobs))
(B/'helper-cutout-receipts.json').write_text(json.dumps(r,indent=2)+'\n')
