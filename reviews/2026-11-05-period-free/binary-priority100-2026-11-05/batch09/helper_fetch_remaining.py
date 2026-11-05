import csv,json,requests,zipfile,io,hashlib,concurrent.futures
from pathlib import Path
B=Path(__file__).parent
rows=[r for r in csv.DictReader((B/'queue.csv').open()) if r['sample_id'] in ['T081','T082','T087','T088','T089','T090']]
def run(r):
 try:
  d=json.loads((B.parent.parent/'binary-exploration-2026-11-04/bulk-results'/f"{r['tic']}.json").read_text()); pairs=[(w,f) for f in d['files'] for w in f.get('windows',[]) if w['kind']=='dip']; w,f=max(pairs,key=lambda p:p[0]['contrast']); sec=f['sector'];p=B/r['tic'];p.mkdir(exist_ok=True)
  resp=requests.get('https://mast.stsci.edu/tesscut/api/v0.1/astrocut',params=dict(ra=r['ra_deg'],dec=r['dec_deg'],x=9,y=9,units='px',sector=sec),timeout=150);resp.raise_for_status();z=zipfile.ZipFile(io.BytesIO(resp.content));dat=z.read(z.namelist()[0]);file=p/f'helper-s{sec}-tesscut.fits';file.write_bytes(dat); e=dict(sector=sec,screen_btjd=w['time'],screen_duration_days=w['duration']);(p/f'helper-s{sec}-receipt.json').write_text(json.dumps(dict(url=resp.url,status=resp.status_code,zip_sha256=hashlib.sha256(resp.content).hexdigest(),member=z.namelist()[0],fits_sha256=hashlib.sha256(dat).hexdigest(),event=e),indent=2));return r['sample_id'],sec,len(dat)
 except Exception as ex:return r['sample_id'],str(ex)
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as ex:
 for o in ex.map(run,rows):print(o,flush=True)

