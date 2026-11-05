import requests,hashlib,zipfile,io,json,csv
from pathlib import Path
B=Path(__file__).resolve().parent
out=[]
for tid,s in [('341688154',48),('219765764',79),('219765764',77)]:
 row=next(r for r in csv.DictReader((B/'queue.csv').open()) if r['tic']==tid)
 rec={'tic':tid,'sector':s}
 try:
  r=requests.get('https://mast.stsci.edu/tesscut/api/v0.1/astrocut',params={'ra':row['ra_deg'],'dec':row['dec_deg'],'y':11,'x':11,'units':'px','sector':s},timeout=120); rec.update(status=r.status_code,url=r.url,response_sha256=hashlib.sha256(r.content).hexdigest());r.raise_for_status();z=zipfile.ZipFile(io.BytesIO(r.content));data=z.read(z.namelist()[0]);p=B/tid/f'helper-tesscut-s{s}.fits';p.write_bytes(data);rec.update(path=str(p),sha256=hashlib.sha256(data).hexdigest())
 except Exception as e:rec['error']=repr(e)
 out.append(rec);print(rec,flush=True)
(B/'helper-fetch.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
