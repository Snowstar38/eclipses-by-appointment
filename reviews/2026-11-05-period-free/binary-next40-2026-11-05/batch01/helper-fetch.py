import requests,zipfile,io,hashlib,json,csv,concurrent.futures
from pathlib import Path
B=Path(__file__).resolve().parent; H=B.parent.parent/'binary-exploration-2026-11-04'; Q=list(csv.DictReader((B/'queue.csv').open())); cases=[]
for r in Q:
 b=json.loads((H/'bulk-results'/f"{r['tic']}.json").read_text()); xs=[dict(x,sector=f['sector']) for f in b['files'] for x in f.get('windows',[]) if x['kind']=='dip' and x['flag']]; x=max(xs,key=lambda x:x['contrast']);cases.append((r,x))
def fetch(z):
 r,x=z;tic=r['tic'];o={'tic':tic,'sample_id':r['sample_id'],**x}
 try:
  v=requests.get('https://mast.stsci.edu/tesscut/api/v0.1/astrocut',params={'ra':r['ra_deg'],'dec':r['dec_deg'],'y':11,'x':11,'units':'px','sector':x['sector']},timeout=180);o.update(url=v.url,status=v.status_code,raw_sha256=hashlib.sha256(v.content).hexdigest());v.raise_for_status();a=zipfile.ZipFile(io.BytesIO(v.content));d=a.read(a.namelist()[0]);(B/f'helper-{tic}-tesscut.fits').write_bytes(d);o['fits_sha256']=hashlib.sha256(d).hexdigest()
 except Exception as e:o['error']=repr(e)
 return o
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as p: out=list(p.map(fetch,cases))
(B/'helper-fetch.json').write_text(json.dumps(out,indent=2));print([(x['sample_id'],x['sector'],x.get('status'),x.get('error')) for x in out])
