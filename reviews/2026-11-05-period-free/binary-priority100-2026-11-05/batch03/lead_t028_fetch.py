"""Fetch bounded new/omitted sectors for T028 current coverage."""
import requests,hashlib,zipfile,io,json,csv
from pathlib import Path
B=Path(__file__).resolve().parent;row=next(r for r in csv.DictReader((B/'queue.csv').open()) if r['sample_id']=='T028');out=[]
for sector in (7,108):
    rec=dict(tic=row['tic'],sector=sector)
    try:
        r=requests.get('https://mast.stsci.edu/tesscut/api/v0.1/astrocut',params={'ra':row['ra_deg'],'dec':row['dec_deg'],'y':11,'x':11,'units':'px','sector':sector},timeout=180)
        rec.update(url=r.url,status=r.status_code,response_sha256=hashlib.sha256(r.content).hexdigest());r.raise_for_status();z=zipfile.ZipFile(io.BytesIO(r.content));data=z.read(z.namelist()[0]);p=B/row['tic']/f'lead-tesscut-s{sector}.fits';p.write_bytes(data);rec.update(fits_path=str(p),fits_sha256=hashlib.sha256(data).hexdigest(),bytes=len(data))
    except Exception as ex:rec['error']=repr(ex)
    out.append(rec);print(rec,flush=True)
(B/'lead-t028-fetch.json').write_text(json.dumps(out,indent=2)+'\n')
