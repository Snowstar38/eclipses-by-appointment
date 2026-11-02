"""Exact-identifier SIMBAD cache; no cone or bibliography completeness claim."""
import csv, hashlib, io, json, urllib.parse, urllib.request
from datetime import datetime, timezone
from pathlib import Path
HERE=Path(__file__).resolve().parent
targets=json.loads((HERE/'targets-selected.json').read_text())
identifiers=sorted({'Gaia DR3 '+str(v['gaia']['source_id']) for v in targets.values()})
query='SELECT ident.id,basic.main_id,basic.otype,basic.ra,basic.dec FROM ident JOIN basic ON ident.oidref=basic.oid WHERE ident.id IN ('+','.join("'"+x+"'" for x in identifiers)+')'
url='httplocal-source/omitted
r={'url':url,'query':query,'queried_at_utc':datetime.now(timezone.utc).isoformat(),'queried_identifiers':len(identifiers)}
try:
    params=urllib.parse.urlencode({'REQUEST':'doQuery','LANG':'ADQL','FORMAT':'csv','QUERY':query}).encode()
    with urllib.request.urlopen(url,params,timeout=25) as response: raw=response.read(1000000)
    reader=csv.DictReader(io.StringIO(raw.decode()));assert 'main_id' in reader.fieldnames
    rows=list(reader);(HERE/'simbad-targets.csv').write_bytes(raw)
    r.update(status='success',rows=len(rows),sha256=hashlib.sha256(raw).hexdigest())
except Exception as ex:r.update(status='unavailable',error=str(ex))
(HERE/'simbad-targets-receipt.json').write_text(json.dumps(r,indent=2),encoding='utf-8')
print(json.dumps({k:v for k,v in r.items() if k!='query'},indent=2))
