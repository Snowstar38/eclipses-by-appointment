"""Fetch deciding alternate raw-pixel cutouts for ambiguous batch02 singles."""
import csv,hashlib,io,json,zipfile
from pathlib import Path
import requests
B=Path(__file__).resolve().parent;Q={r['sample_id']:r for r in csv.DictReader((B/'queue.csv').open(newline='',encoding='utf-8'))};out=[]
for sid,sector in [('T011',96),('T016',19),('T018',104),('T019',103)]:
    r=Q[sid];tic=r['tic'];entry={'sample_id':sid,'tic':tic,'sector':sector}
    try:
        response=requests.get('https://mast.stsci.edu/tesscut/api/v0.1/astrocut',params={'ra':r['ra_deg'],'dec':r['dec_deg'],'y':11,'x':11,'units':'px','sector':sector},timeout=120);entry['url']=response.url;entry['http_status']=response.status_code;response.raise_for_status();entry['zip_sha256']=hashlib.sha256(response.content).hexdigest();z=zipfile.ZipFile(io.BytesIO(response.content));data=z.read(z.namelist()[0]);path=B/f'lead-{tic}-s{sector}.fits';path.write_bytes(data);entry['fits_path']=str(path);entry['fits_sha256']=hashlib.sha256(data).hexdigest()
    except Exception as ex:entry['error']=repr(ex)
    out.append(entry);print(entry,flush=True)
(B/'lead-exception-fetch.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
