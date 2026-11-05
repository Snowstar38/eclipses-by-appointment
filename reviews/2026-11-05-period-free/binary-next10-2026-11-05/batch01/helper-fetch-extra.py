import requests, zipfile,io,hashlib,json,csv,concurrent.futures
from pathlib import Path
B=Path(__file__).resolve().parent; Q={x['tic']:x for x in csv.DictReader((B/'queue.csv').open())}; cases=[('370126865',18,1797.827),('62374377',67,3131.71),('82550215',79,3454.352)]
def fetch(z):
 tic,s,t=z;r=Q[tic];o={'tic':tic,'sector':s,'screen_time':t}
 try:
  v=requests.get('https://mast.stsci.edu/tesscut/api/v0.1/astrocut',params={'ra':r['ra_deg'],'dec':r['dec_deg'],'y':11,'x':11,'units':'px','sector':s},timeout=120);o.update(url=v.url,status=v.status_code,raw_sha256=hashlib.sha256(v.content).hexdigest());v.raise_for_status();a=zipfile.ZipFile(io.BytesIO(v.content)); d=a.read(a.namelist()[0]);(B/f'helper-{tic}-s{s}-tesscut.fits').write_bytes(d);o['fits_sha256']=hashlib.sha256(d).hexdigest()
 except Exception as e:o['error']=repr(e)
 return o
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as p: out=list(p.map(fetch,cases))
(B/'helper-fetch-extra.json').write_text(json.dumps(out,indent=2));print(out)

