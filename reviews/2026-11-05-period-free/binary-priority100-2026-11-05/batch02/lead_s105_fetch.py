"""Fetch newly listed TESSCut S105 for T011 and T019 after helper audit."""
import csv,hashlib,io,json,zipfile
from pathlib import Path
import requests
B=Path(__file__).resolve().parent;Q={r['sample_id']:r for r in csv.DictReader((B/'queue.csv').open(newline='',encoding='utf-8'))};out=[]
for sid in ('T011','T019'):
    r=Q[sid];tic=r['tic'];entry={'sample_id':sid,'tic':tic,'sector':105}
    try:
        response=requests.get('https://mast.stsci.edu/tesscut/api/v0.1/astrocut',params={'ra':r['ra_deg'],'dec':r['dec_deg'],'y':11,'x':11,'units':'px','sector':105},timeout=120);entry['url']=response.url;entry['http_status']=response.status_code;response.raise_for_status();entry['zip_sha256']=hashlib.sha256(response.content).hexdigest();z=zipfile.ZipFile(io.BytesIO(response.content));data=z.read(z.namelist()[0]);path=B/f'lead-{tic}-s105.fits';path.write_bytes(data);entry['fits_path']=str(path);entry['fits_sha256']=hashlib.sha256(data).hexdigest()
    except Exception as ex:entry['error']=repr(ex)
    out.append(entry);print(entry,flush=True)
(B/'lead-s105-fetch.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
