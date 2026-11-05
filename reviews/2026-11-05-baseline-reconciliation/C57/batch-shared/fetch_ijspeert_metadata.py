"""One primary author-deposit metadata request; no bulk time-series download."""
from pathlib import Path
import datetime,hashlib,json,requests
O=Path(__file__).resolve().parent/'catalogue-archives'
url='https://zenodo.org/api/records/13862856';rfile=O/'ijspeert-zenodo-metadata.receipt.json';assert not rfile.exists()
info=dict(url=url,utc=datetime.datetime.now(datetime.timezone.utc).isoformat())
try:
    r=requests.get(url,timeout=20);(O/'ijspeert-zenodo-metadata.json').write_bytes(r.content)
    info.update(http_status=r.status_code,bytes=len(r.content),sha256=hashlib.sha256(r.content).hexdigest());r.raise_for_status();data=r.json()
    info['status']='success'
    print(data.get('metadata',{}).get('title'))
    for f in data.get('files',[]):print(f['key'],f['size'],f.get('links'))
except Exception as e:info.update(status='unavailable',error=repr(e))
rfile.write_text(json.dumps(info,indent=2)+'\n',encoding='utf-8');print(info['status'])
