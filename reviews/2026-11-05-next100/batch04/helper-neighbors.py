"""Fetch bounded Gaia DR3 neighbor cones for Q031 and Q036, retaining raw receipts."""
import csv
import hashlib
import io
import json
import math
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

B = Path(__file__).resolve().parent
rows = [r for r in csv.DictReader((B/'queue.csv').open(newline='',encoding='utf8')) if r['sample_id'] in ('Q031','Q036')]
def sep(a,b,c,d):
    a,b,c,d=map(math.radians,(a,b,c,d))
    z=math.sin((b-d)/2)**2+math.cos(b)*math.cos(d)*math.sin((a-c)/2)**2
    return 7200*math.degrees(math.asin(min(1,math.sqrt(z))))
clauses=[f"1=CONTAINS(POINT('ICRS',ra,dec),CIRCLE('ICRS',{r['ra_deg']},{r['dec_deg']},{120/3600}))" for r in rows]
query='SELECT source_id,ra,dec,phot_g_mean_mag FROM gaiadr3.gaia_source WHERE '+' OR '.join('('+c+')' for c in clauses)
url='https://gaia.ari.uni-heidelberg.de/tap/sync'
body=urllib.parse.urlencode({'REQUEST':'doQuery','LANG':'ADQL','FORMAT':'csv','QUERY':query}).encode()
receipt={'queried_utc':datetime.now(timezone.utc).isoformat(),'url':url,'request_sha256':hashlib.sha256(body).hexdigest(), 'queue_sha256':hashlib.sha256((B/'queue.csv').read_bytes()).hexdigest(),'radius_arcsec':120}
try:
    req=urllib.request.Request(url,data=body,headers={'User-Agent':'Astra-next100-batch04-helper/1.0'})
    with urllib.request.urlopen(req,timeout=50) as response: raw=response.read(5000001)
    assert len(raw)<=5000000
    data=list(csv.DictReader(io.StringIO(raw.decode('utf-8-sig'))))
    assert data and 'source_id' in data[0]
    (B/'helper-neighbors-raw.csv').write_bytes(raw)
    receipt.update(status='success',raw_sha256=hashlib.sha256(raw).hexdigest(),rows=len(data))
except Exception as exc:
    data=[];receipt.update(status='unavailable',error=repr(exc))
out={}
for r in rows:
    rr=[]
    for x in data:
        s=sep(float(x['ra']),float(x['dec']),float(r['ra_deg']),float(r['dec_deg']))
        if s<=120:
            rr.append({**x,'separation_arcsec':s,'is_target':x['source_id']==r['gaia_dr3'],
                       'flux_ratio_to_target_G':10**(-.4*(float(x['phot_g_mean_mag'])-float(r['gaia_G'])))})
    out[r['sample_id']]=sorted(rr,key=lambda x:x['separation_arcsec'])
(B/'helper-neighbors.json').write_text(json.dumps({'receipt':receipt,'targets':out},indent=2)+'\n',encoding='utf8')
print(receipt)
for k,v in out.items(): print(k,[(x['source_id'],round(x['separation_arcsec'],1),round(float(x['phot_g_mean_mag']),2),round(x['flux_ratio_to_target_G'],3)) for x in v[:12]])
