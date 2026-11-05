import json,csv,requests,hashlib,zipfile,io,concurrent.futures
from pathlib import Path
B=Path(__file__).resolve().parent
Q=list(csv.DictReader((B/'queue.csv').open()))[:4]
def work(row):
 tic=row['tic']; src=json.loads((B.parent/'source-packets'/tic/'sources.json').read_text()); bulk=json.loads((B.parent.parent/'binary-exploration-2026-11-04'/'bulk-results'/f'{tic}.json').read_text());
 events=[(w['contrast'],f['sector'],w['time'],w['duration']) for f in bulk['files'] for w in f.get('windows',[]) if w.get('flag') and w['kind']=='dip']; e=max(events)
 o={'tic':tic,'sector':e[1],'screen_time':e[2],'screen_duration':e[3]}
 try:
  r=requests.get('https://mast.stsci.edu/tesscut/api/v0.1/astrocut',params={'ra':row['ra_deg'],'dec':row['dec_deg'],'y':11,'x':11,'units':'px','sector':e[1]},timeout=120); o.update(url=r.url,status=r.status_code,raw_sha256=hashlib.sha256(r.content).hexdigest());r.raise_for_status();z=zipfile.ZipFile(io.BytesIO(r.content));data=z.read(z.namelist()[0]);f=B/f'helper-{tic}-tesscut.fits';f.write_bytes(data);o['fits_sha256']=hashlib.sha256(data).hexdigest()
 except Exception as ex:o['error']=repr(ex)
 return o
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as p: out=list(p.map(work,Q))
(B/'helper-fetch.json').write_text(json.dumps(out,indent=2));print(json.dumps(out,indent=2))
