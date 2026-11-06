import requests,zipfile,io,json,hashlib,concurrent.futures
from pathlib import Path
from datetime import datetime,timezone
B=Path(__file__).resolve().parent; pop=json.loads((B.parent/'fresh-band'/'population.json').read_text())['targets']
items=[('259614821',38),('371856921',23),('412521418',34),('86182628',49),('26486304',81),('356801225',81),('331643517',56),('343187602',24)]
def run(item):
 tic,s=item;p=pop[tic];z={'tic':tic,'sector':s,'utc':datetime.now(timezone.utc).isoformat()}
 try:
  r=requests.get('https://mast.stsci.edu/tesscut/api/v0.1/astrocut',params={'ra':p['ra'],'dec':p['dec'],'x':7,'y':7,'units':'px','sector':s},timeout=100);r.raise_for_status();data=zipfile.ZipFile(io.BytesIO(r.content)).read(zipfile.ZipFile(io.BytesIO(r.content)).namelist()[0]);out=B/tic/f'helper-cut-s{s}.fits';out.write_bytes(data);z.update(url=r.url,status=r.status_code,sha256=hashlib.sha256(data).hexdigest(),bytes=len(data))
 except Exception as e:z['error']=str(e)
 return z
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as ex: out=list(ex.map(run,items))
(B/'helper-cuts-receipts.json').write_text(json.dumps(out,indent=2));print(json.dumps(out,indent=2))
