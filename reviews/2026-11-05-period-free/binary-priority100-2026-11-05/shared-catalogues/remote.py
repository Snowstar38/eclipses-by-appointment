"""Single bounded Gaia/SIMBAD bulk attempts; no negative inference on outage."""
import csv, hashlib, io, json, urllib.parse, urllib.request
from datetime import datetime, timezone
from pathlib import Path
HERE=Path(__file__).resolve().parent
Q=list(csv.DictReader((HERE.parent/'queue.csv').open(encoding='utf-8-sig')))
ids={x['gaia_dr3'] for x in Q}
jobs=[]
for label,table in [('gaia_eb','vari_eclipsing_binary'),('gaia_summary','vari_summary'),('gaia_nss','nss_two_body_orbit')]:
    query='SELECT * FROM gaiadr3.'+table+' WHERE source_id IN ('+','.join(sorted(ids))+')'
    jobs.append((label,'https://gaia.ari.uni-heidelberg.de/tap/sync',query,'source_id'))
query="SELECT ident.id,basic.main_id,basic.otype,basic.ra,basic.dec FROM ident JOIN basic ON ident.oidref=basic.oid WHERE ident.id IN ("+','.join("'Gaia DR3 "+x+"'" for x in sorted(ids))+')'
jobs.append(('simbad','https://simbad.cfa.harvard.edu/simbad/sim-tap/sync',query,'id'))
out={}
for label,url,query,key in jobs:
    body=urllib.parse.urlencode({'REQUEST':'doQuery','LANG':'ADQL','FORMAT':'csv','QUERY':query}).encode()
    rec={'catalogue':label,'url':url,'body_sha256':hashlib.sha256(body).hexdigest(),'timeout_seconds':8,'queried_utc':datetime.now(timezone.utc).isoformat(),'queue_sha256':hashlib.sha256((HERE.parent/'queue.csv').read_bytes()).hexdigest()}
    try:
        req=urllib.request.Request(url,data=body,headers={'User-Agent':'Astra-catalogue-review100/1.0'})
        with urllib.request.urlopen(req,timeout=8) as response: raw=response.read(2000001)
        if len(raw)>2000000: raise ValueError('response too long')
        txt=raw.decode('utf-8-sig');data=list(csv.DictReader(io.StringIO(txt)))
        if key not in (data[0].keys() if data else txt.splitlines()[0].split(',')): raise ValueError('unexpected CSV layout')
        allowed=ids if label!='simbad' else {'Gaia DR3 '+x for x in ids}
        if not all(x[key] in allowed for x in data): raise ValueError('unexpected identity')
        p=HERE/(label+'.csv');p.write_bytes(raw)
        rec.update(status='success',raw=str(p),sha256=hashlib.sha256(raw).hexdigest(),bytes=len(raw),rows=len(data))
    except Exception as exc: rec.update(status='unavailable',error=repr(exc))
    out[label]=rec
(HERE/'bulk-remote-receipts.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:(v['status'],v.get('rows')) for k,v in out.items()}))
