import requests,zipfile,io,json,hashlib,concurrent.futures,csv
from pathlib import Path
from datetime import datetime,timezone
B=Path(__file__).resolve().parent;Q={r['tic']:r for r in csv.DictReader((B/'queue.csv').open())}
def run(item):
 tic,s=item;p=Q[tic];z={'tic':tic,'sector':s,'utc':datetime.now(timezone.utc).isoformat()}
 try:
  r=requests.get('https://mast.stsci.edu/tesscut/api/v0.1/astrocut',params={'ra':p['ra_deg'],'dec':p['dec_deg'],'x':11,'y':11,'units':'px','sector':s},timeout=150);r.raise_for_status();zz=zipfile.ZipFile(io.BytesIO(r.content));data=zz.read(zz.namelist()[0]);dest=B/tic/f'helper-cut-s{s}.fits';dest.write_bytes(data);z.update(url=r.url,status=r.status_code,sha256=hashlib.sha256(data).hexdigest(),path=str(dest))
 except Exception as e:z['error']=str(e)
 return z
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as ex:out=list(ex.map(run,[('185744410',61),('149316567',88),('378411251',64),('387124290',81)]))
(B/'helper-cut-receipts.json').write_text(json.dumps(out,indent=2));print(out)
