"""Independent bounded TESSCut receipts and current sector inventories."""
import csv, hashlib, json, zipfile, io
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
from pathlib import Path
import requests

B = Path(__file__).resolve().parent
rows = {r['tic']: r for r in csv.DictReader((B/'queue.csv').open(encoding='utf8',newline=''))}
jobs = [('3299934',62),('3299934',89),('311461544',101),('47675509',86),('447274265',93)]

def fetch(job):
    tic, sec = job; row=rows[tic]; out={'tic':tic,'sector':sec,'checked_utc':datetime.now(timezone.utc).isoformat()}
    try:
        r=requests.get('https://mast.stsci.edu/tesscut/api/v0.1/astrocut',params={'ra':row['ra_deg'],'dec':row['dec_deg'],'x':11,'y':11,'units':'px','sector':sec},timeout=100)
        out.update(url=r.url,status=r.status_code,zip_sha256=hashlib.sha256(r.content).hexdigest(),bytes=len(r.content))
        r.raise_for_status(); z=zipfile.ZipFile(io.BytesIO(r.content)); data=z.read(z.namelist()[0]);
        p=B/tic/f'helper-tesscut-s{sec}.fits';p.write_bytes(data);out.update(fits_path=str(p),fits_sha256=hashlib.sha256(data).hexdigest())
    except Exception as e:out['error']=str(e)
    return out

def inventory(tic):
    row=rows[tic];out={'tic':tic,'checked_utc':datetime.now(timezone.utc).isoformat()}
    try:
        r=requests.get('https://mast.stsci.edu/tesscut/api/v0.1/sector',params={'ra':row['ra_deg'],'dec':row['dec_deg']},timeout=35)
        out.update(url=r.url,status=r.status_code,response_sha256=hashlib.sha256(r.content).hexdigest())
        r.raise_for_status();body=r.json();out['response']=body;out['sectors']=sorted(int(v['sector']) for v in body['results'])
    except Exception as e:out['error']=str(e)
    return out

with ThreadPoolExecutor(max_workers=5) as ex:
    cuts=list(ex.map(fetch,jobs));inv=list(ex.map(inventory,['311461544','47675509','447274265']))
(B/'helper-fetch-receipts.json').write_text(json.dumps({'cutouts':cuts,'inventory':inv},indent=2)+'\n',encoding='utf8')
for x in cuts:print(x['tic'],x['sector'],x.get('bytes'),x.get('error'))
for x in inv:print('inventory',x['tic'],x.get('sectors'),x.get('error'))
