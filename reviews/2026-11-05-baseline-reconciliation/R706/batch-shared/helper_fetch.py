import json,requests,hashlib,zipfile,io,concurrent.futures
from pathlib import Path
B=Path(__file__).resolve().parent;D=json.loads((B/'SOURCE-SNAPSHOT.json').read_text(encoding='utf8'));H=B/'helper-pixels'
def fetch(tic):
 h=H/tic;h.mkdir(exist_ok=True);m=json.loads((B/tic/'measurements.json').read_text(encoding='utf8'));e=max([x for x in m['events'] if x.get('timing_usable')],key=lambda x:x['depth_ppt']/x['oot_scatter_ppt']);g=D[tic]['target']['gaia'];receipt={'event':e}
 try:
  r=requests.get('https://mast.stsci.edu/tesscut/api/v0.1/astrocut',params={'ra':g['ra'],'dec':g['dec'],'y':11,'x':11,'units':'px','sector':e['sector']},timeout=120);(h/'tesscut.raw').write_bytes(r.content);receipt.update(url=r.url,status=r.status_code,headers=dict(r.headers),raw_sha256=hashlib.sha256(r.content).hexdigest());r.raise_for_status();z=zipfile.ZipFile(io.BytesIO(r.content));name=z.namelist()[0];data=z.read(name);(h/'tesscut.fits').write_bytes(data);receipt.update(member=name,fits_sha256=hashlib.sha256(data).hexdigest())
 except Exception as ex:receipt['error']=repr(ex)
 (h/'receipt.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf8');return tic,receipt.get('status'),receipt.get('error')
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as pool:
 for x in pool.map(fetch,[k for k in D if k not in ['121277143','174303697']]):print(x,flush=True)
