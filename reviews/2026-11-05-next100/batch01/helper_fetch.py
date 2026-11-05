import csv,json,requests,hashlib,zipfile,io,concurrent.futures
from pathlib import Path
B=Path(__file__).parent; rows={r['tic']:r for r in csv.DictReader((B/'queue.csv').open())}; picks={'72747845':30,'1535458':32,'364268504':87,'117157551':104}
def fetch(item):
 tic,sector=item;r=rows[tic]; d={'tic':tic,'sector':sector}
 try:
  x=requests.get('https://mast.stsci.edu/tesscut/api/v0.1/astrocut',params={'ra':r['ra_deg'],'dec':r['dec_deg'],'y':11,'x':11,'units':'px','sector':sector},timeout=75);d.update(status=x.status_code,url=x.url,raw_sha256=hashlib.sha256(x.content).hexdigest());x.raise_for_status();z=zipfile.ZipFile(io.BytesIO(x.content)); data=z.read(z.namelist()[0]);p=B/('helper-cut-'+tic+'.fits');p.write_bytes(data);d['fits_sha256']=hashlib.sha256(data).hexdigest()
 except Exception as e:d['error']=repr(e)
 return d
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool: out=list(pool.map(fetch,picks.items()))
(B/'helper-cut-receipts.json').write_text(json.dumps(out,indent=2));print(out)
