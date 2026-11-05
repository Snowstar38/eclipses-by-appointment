import csv,json,requests,zipfile,io,hashlib,concurrent.futures
from pathlib import Path
B=Path(__file__).parent
rows=list(csv.DictReader((B/'queue.csv').open()))
def run(r):
 try:
  d=json.loads((B/r['tic']/'lead-numeric.json').read_text()); e=max(d['events'],key=lambda x:x.get('raw_core_median_deficit_ppt',0)); sec=e['sector']; p=B/r['tic'];
  resp=requests.get('https://mast.stsci.edu/tesscut/api/v0.1/astrocut',params=dict(ra=r['ra_deg'],dec=r['dec_deg'],x=9,y=9,units='px',sector=sec),timeout=150);resp.raise_for_status();z=zipfile.ZipFile(io.BytesIO(resp.content)); dat=z.read(z.namelist()[0]); f=p/f'helper-s{sec}-tesscut.fits';f.write_bytes(dat); (p/f'helper-s{sec}-receipt.json').write_text(json.dumps(dict(url=resp.url,status=resp.status_code,zip_sha256=hashlib.sha256(resp.content).hexdigest(),member=z.namelist()[0],fits_sha256=hashlib.sha256(dat).hexdigest(),event=e),indent=2)); return (r['sample_id'],sec,len(dat))
 except Exception as ex:return (r['sample_id'],str(ex))
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as ex:
 for o in ex.map(run,rows[2:]):print(o,flush=True)
