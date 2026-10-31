import json,csv,io,urllib.request,urllib.parse,hashlib
from pathlib import Path
from datetime import datetime,timezone
p=Path(__file__).parent;t=json.loads((p/'targets-selected.json').read_text()); ids=[x['gaia']['source_id'] for x in t.values()]; url='http[local path omitted]'
q='SELECT * FROM gaiadr3.nss_two_body_orbit WHERE source_id IN ('+','.join(ids)+')';r={'query':q,'url':url,'utc':datetime.now(timezone.utc).isoformat()}
try:
 raw=urllib.request.urlopen(url,urllib.parse.urlencode({'REQUEST':'doQuery','LANG':'ADQL','FORMAT':'csv','QUERY':q}).encode(),timeout=40).read(); rows=list(csv.DictReader(io.StringIO(raw.decode())));assert 'source_id' in rows[0] and set(x['source_id'] for x in rows)<=set(ids); (p/'gaia-nss-full.csv').write_bytes(raw);r.update(status='success',rows=len(rows),sha256=hashlib.sha256(raw).hexdigest())
except Exception as e:r.update(status='unavailable',error=repr(e))
(p/'gaia-nss-receipt.json').write_text(json.dumps(r,indent=2));print(r['status'],r.get('rows'),r.get('error'))
