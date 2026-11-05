import requests,zipfile,io,hashlib,json,concurrent.futures
from pathlib import Path
B=Path(__file__).resolve().parent;H=B/'helper-pixels'/'95623701';g=json.loads((B/'SOURCE-SNAPSHOT.json').read_text(encoding='utf8'))['95623701']['target']['gaia']
def run(sec):
 try:
  r=requests.get('https://mast.stsci.edu/tesscut/api/v0.1/astrocut',params={'ra':g['ra'],'dec':g['dec'],'y':11,'x':11,'units':'px','sector':sec},timeout=120);r.raise_for_status();z=zipfile.ZipFile(io.BytesIO(r.content));p=H/f's{sec}.fits';p.write_bytes(z.read(z.namelist()[0]));return {'sector':sec,'url':r.url,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()}
 except Exception as e:return {'sector':sec,'error':repr(e)}
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as ex: out=list(ex.map(run,[12,39,65]));print(out);(H/'extra-receipts.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf8')
