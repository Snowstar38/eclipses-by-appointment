"""Bounded 11x11 TESSCut fetches for three deciding positive events."""
import csv,json,requests,hashlib,zipfile,io
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
B=Path(__file__).resolve().parent;Q={r['tic']:r for r in csv.DictReader((B/'queue.csv').open())}
def fetch(task):
 tic,sector=task;q=Q[tic];dest=B/tic;rec={'tic':tic,'sector':sector,'service':'MAST TESSCut','size_pixels':[11,11]}
 try:
  r=requests.get('https://mast.stsci.edu/tesscut/api/v0.1/astrocut',params={'ra':q['ra_deg'],'dec':q['dec_deg'],'y':11,'x':11,'units':'px','sector':sector},timeout=100)
  (dest/'tesscut.raw').write_bytes(r.content);rec.update(url=r.url,http_status=r.status_code,response_sha256=hashlib.sha256(r.content).hexdigest());r.raise_for_status()
  z=zipfile.ZipFile(io.BytesIO(r.content));data=z.read(next(n for n in z.namelist() if n.lower().endswith('.fits')));(dest/'tesscut.fits').write_bytes(data);rec['fits_sha256']=hashlib.sha256(data).hexdigest()
 except Exception as e:rec['error']=repr(e)
 (dest/'tesscut-receipt.json').write_text(json.dumps(rec,indent=2)+'\n',encoding='utf8');return rec
with ThreadPoolExecutor(max_workers=2) as pool:
 for rec in pool.map(fetch,[('146516744',32),('433693445',17),('43868028',98)]):print(rec,flush=True)
