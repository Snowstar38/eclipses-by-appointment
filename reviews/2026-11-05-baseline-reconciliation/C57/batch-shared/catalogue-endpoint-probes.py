"""Three bounded alternative primary-endpoint checks, retaining all failures."""
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
import datetime,hashlib,json,requests
O=Path(__file__).resolve().parent/'catalogue-endpoint-probes';O.mkdir(exist_ok=True)
jobs=[('ijspeert-readme','https://cdsarc.cds.unistra.fr/ftp/J/A+A/691/A242/ReadMe'),('harvard-control-id','https://vizier.cfa.harvard.edu/viz-bin/asu-tsv?-source=J/ApJS/279/50/table4&TIC=10507&-out.all&-out.max=100'),('cds-control-id','https://vizier.cds.unistra.fr/viz-bin/asu-tsv?-source=J/ApJS/279/50/table4&TIC=10507&-out.all&-out.max=100')]
def run(job):
 name,url=job;rec=dict(url=url,utc=datetime.datetime.now(datetime.timezone.utc).isoformat())
 try:
  r=requests.get(url,timeout=(8,20));(O/(name+'.response')).write_bytes(r.content)
  rec.update(status_code=r.status_code,bytes=len(r.content),sha256=hashlib.sha256(r.content).hexdigest(),retrieved_url=r.url);r.raise_for_status();rec['status']='http_success_not_yet_parsed'
 except Exception as ex:rec.update(status='unavailable',error=repr(ex))
 (O/(name+'.json')).write_text(json.dumps(rec,indent=2)+'\n',encoding='utf-8');return name,rec['status'],rec.get('bytes')
with ThreadPoolExecutor(3) as pool:
 for r in pool.map(run,jobs):print(r,flush=True)
