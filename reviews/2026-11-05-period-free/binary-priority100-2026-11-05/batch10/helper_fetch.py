import csv,json,requests,zipfile,io,hashlib,concurrent.futures
from pathlib import Path
B=Path(__file__).parent
rows=list(csv.DictReader((B/'queue.csv').open()))
sectors={'T092':81,'T093':37,'T094':43,'T095':22,'T097':35,'T100':34}
def run(r):
 try:
  d=json.loads((B/r['tic']/'lead-numeric.json').read_text()); ev=[e for e in d['events'] if e['sector']==sectors.get(r['sample_id'],0)] or d['events']; e=max(ev,key=lambda e:e.get('fit_depth_ppt',0)); sec=e['sector'];p=B/r['tic']
  resp=requests.get('https://mast.stsci.edu/tesscut/api/v0.1/astrocut',params=dict(ra=r['ra_deg'],dec=r['dec_deg'],x=9,y=9,units='px',sector=sec),timeout=150);resp.raise_for_status();z=zipfile.ZipFile(io.BytesIO(resp.content));dat=z.read(z.namelist()[0]);(p/f'helper-s{sec}-tesscut.fits').write_bytes(dat);(p/f'helper-s{sec}-receipt.json').write_text(json.dumps(dict(url=resp.url,status=resp.status_code,zip_sha256=hashlib.sha256(resp.content).hexdigest(),member=z.namelist()[0],fits_sha256=hashlib.sha256(dat).hexdigest(),event=e),indent=2));return r['sample_id'],sec,len(dat)
 except Exception as ex:return r['sample_id'],str(ex)
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as ex:
 for o in ex.map(run,rows):print(o,flush=True)
