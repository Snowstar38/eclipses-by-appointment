from pathlib import Path
import csv,json,requests,hashlib,zipfile,io
from concurrent.futures import ThreadPoolExecutor
from astropy.io import fits
W=Path(__file__).resolve().parent;O=W/'missing-coverage'
Q={r['tic']:r for r in csv.DictReader((W/'queue.csv').open(encoding='utf8'))}
jobs=[('231694897',105),('231694897',103),('231694897',1),('323818250',10),('323818250',65)]
def get(job):
 tic,sector=job;r=Q[tic];params={'ra':r['ra_deg'],'dec':r['dec_deg'],'x':11,'y':11,'units':'px','sector':sector};rec={'tic':tic,'sector':sector,'params':params}
 try:
  resp=requests.get('https://mast.stsci.edu/tesscut/api/v0.1/astrocut',params=params,timeout=(10,50));rec.update(url=resp.url,http_status=resp.status_code,response_sha256=hashlib.sha256(resp.content).hexdigest())
  (O/f'{tic}-s{sector:03d}.bin').write_bytes(resp.content);resp.raise_for_status()
  z=zipfile.ZipFile(io.BytesIO(resp.content));names=[n for n in z.namelist() if n.endswith('.fits')];assert len(names)==1
  data=z.read(names[0]);p=W/'batch02'/tic/f'missing-cutout-s{sector:03d}.fits';p.write_bytes(data)
  with fits.open(p) as h:
   assert int(h[0].header.get('SECTOR',sector))==sector
   rec['columns']=h[1].columns.names;rec['samples']=len(h[1].data)
  rec.update(status='ok',path=str(p),member=names[0],sha256=hashlib.sha256(data).hexdigest(),bytes=len(data),same_photon_alternative=True)
 except Exception as e:rec.update(status='unavailable',error=repr(e))
 (O/f'{tic}-s{sector:03d}-receipt.json').write_text(json.dumps(rec,indent=2)+'\n',encoding='utf8');print(tic,sector,rec['status'],flush=True);return rec
with ThreadPoolExecutor(2) as pool:results=list(pool.map(get,jobs))
(O/'cutout-receipts.json').write_text(json.dumps(results,indent=2)+'\n',encoding='utf8')
