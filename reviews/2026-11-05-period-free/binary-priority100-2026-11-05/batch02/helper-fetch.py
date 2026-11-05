import csv,json,requests,zipfile,io,hashlib,concurrent.futures
from pathlib import Path
B=Path(__file__).resolve().parent;Q={r['tic']:r for r in csv.DictReader((B/'queue.csv').open())}
def work(z):
 tic,sec,tm=z;r=Q[tic];o={'tic':tic,'sector':sec,'mid':tm}
 try:
  a=requests.get('https://mast.stsci.edu/tesscut/api/v0.1/astrocut',params={'ra':r['ra_deg'],'dec':r['dec_deg'],'y':11,'x':11,'units':'px','sector':sec},timeout=120);a.raise_for_status();o['url']=a.url;o['zip_sha256']=hashlib.sha256(a.content).hexdigest();v=zipfile.ZipFile(io.BytesIO(a.content));data=v.read(v.namelist()[0]);(B/f'helper-{tic}-s{sec}.fits').write_bytes(data);o['sha256']=hashlib.sha256(data).hexdigest()
 except Exception as e:o['error']=repr(e)
 return o
with concurrent.futures.ThreadPoolExecutor(max_workers=2) as p: out=list(p.map(work,[('323458448',37,2326.12609),('313142904',19,1832.66591)]))
(B/'helper-fetch.json').write_text(json.dumps(out,indent=2));print(out)
