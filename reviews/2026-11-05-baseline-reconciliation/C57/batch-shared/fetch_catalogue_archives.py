"""Bounded primary CDS archive route; preserves failures separately from cones."""
from pathlib import Path
import concurrent.futures,datetime,hashlib,json,requests
W=Path(__file__).resolve().parent;O=W/'catalogue-archives';O.mkdir(exist_ok=True)
items=[('ijspeert-ReadMe','https://cdsarc.cds.unistra.fr/ftp/J/A%2BA/691/A242/ReadMe'),('prsa-ReadMe','https://cdsarc.cds.unistra.fr/ftp/J/ApJS/258/16/ReadMe'),('prsa-data.gz','https://cdsarc.cds.unistra.fr/ftp/J/ApJS/258/16/tess-ebs.dat.gz')]
def run(pair):
    key,url=pair;receipt=O/(key+'.receipt.json');dest=O/key
    assert not receipt.exists(),'do not overwrite previous attempts'
    info=dict(url=url,utc=datetime.datetime.now(datetime.timezone.utc).isoformat())
    try:
        r=requests.get(url,timeout=15);dest.write_bytes(r.content)
        info.update(http_status=r.status_code,bytes=len(r.content),sha256=hashlib.sha256(r.content).hexdigest());r.raise_for_status()
        assert '<html' not in r.text[:100].lower(),'HTML instead of data'
        info['status']='retrieved_unvalidated'
    except Exception as e:info.update(status='unavailable',error=repr(e))
    receipt.write_text(json.dumps(info,indent=2)+'\n',encoding='utf-8')
    return key,info['status'],info.get('bytes')
with concurrent.futures.ThreadPoolExecutor(3) as ex:
    for result in ex.map(run,items):print(result,flush=True)
