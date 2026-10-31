import csv, hashlib, io, json, urllib.parse, urllib.request
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from pathlib import Path
HERE=Path(__file__).resolve().parent
targets=json.loads((HERE/'targets-selected.json').read_text())
ids=sorted({str(v['gaia']['source_id']) for v in targets.values()})
url='http[local path omitted]'
def fetch(table):
    query=f'SELECT * FROM gaiadr3.{table} WHERE source_id IN ('+','.join(ids)+')'
    params=urllib.parse.urlencode({'REQUEST':'doQuery','LANG':'ADQL','FORMAT':'csv','QUERY':query}).encode()
    r={'url':url,'table':table,'query':query,'queried_at_utc':datetime.now(timezone.utc).isoformat()}
    try:
        with urllib.request.urlopen(urllib.request.Request(url,data=params),timeout=30) as response: raw=response.read(2000000)
        reader=csv.DictReader(io.StringIO(raw.decode())); assert 'source_id' in reader.fieldnames
        rows=list(reader); assert {x['source_id'] for x in rows}<=set(ids)
        name='gaia-'+table+'.csv'; (HERE/name).write_bytes(raw)
        r.update(status='success',file=name,rows=len(rows),sha256=hashlib.sha256(raw).hexdigest(),queried_sources=len(ids))
    except Exception as ex:r.update(status='unavailable',error=str(ex))
    return r
with ThreadPoolExecutor(max_workers=2) as pool: results=list(pool.map(fetch,['vari_summary','vari_eclipsing_binary']))
(HERE/'gaia-vari-receipts.json').write_text(json.dumps(results,indent=2),encoding='utf-8')
print(json.dumps([{k:v for k,v in r.items() if k!='query'} for r in results],indent=2))
