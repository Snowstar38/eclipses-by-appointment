"""Bounded Gaia DR3 120-arcsec neighbor lookup for the sealed queue."""
import csv, hashlib, io, json, math, urllib.parse, urllib.request
from datetime import datetime, timezone
from pathlib import Path

H=Path(__file__).resolve().parent
Q=H.parent/'queue.csv'
rows=list(csv.DictReader(Q.open(encoding='utf-8-sig',newline='')))
assert len(rows)==100
qhash=hashlib.sha256(Q.read_bytes()).hexdigest()
RADIUS_DEG=120/3600

def angle(a,b,c,d):
    a,b,c,d=map(math.radians,(a,b,c,d))
    h=math.sin((b-d)/2)**2+math.cos(b)*math.cos(d)*math.sin((a-c)/2)**2
    return math.degrees(2*math.asin(min(1,math.sqrt(h))))*3600

for batch,part in (('first4',rows[:4]),('remaining96',rows[4:])):
    recpath=H/f'gaia-neighbors-{batch}.receipt.json'
    rawpath=H/f'gaia-neighbors-{batch}.csv'
    clauses=[f"1=CONTAINS(POINT('ICRS',ra,dec),CIRCLE('ICRS',{r['ra_deg']},{r['dec_deg']},{RADIUS_DEG}))" for r in part]
    query='SELECT source_id,ra,dec,phot_g_mean_mag FROM gaiadr3.gaia_source WHERE '+' OR '.join('('+c+')' for c in clauses)
    body=urllib.parse.urlencode({'REQUEST':'doQuery','LANG':'ADQL','FORMAT':'csv','QUERY':query}).encode()
    rec={'queue_sha256':qhash,'sample_ids':[r['sample_id'] for r in part], 'radius_arcsec':120,'url':'https://gaia.ari.uni-heidelberg.de/tap/sync','body_sha256':hashlib.sha256(body).hexdigest(),'timeout_seconds':30,'queried_utc':datetime.now(timezone.utc).isoformat()}
    try:
        req=urllib.request.Request(rec['url'],data=body,headers={'User-Agent':'Astra-priority100-neighbor-audit/1.0'})
        with urllib.request.urlopen(req,timeout=30) as response: raw=response.read(5000001)
        assert len(raw)<=5000000
        data=list(csv.DictReader(io.StringIO(raw.decode('utf-8-sig'))))
        assert 'source_id' in raw.decode('utf-8-sig').splitlines()[0]
        assert all(any(angle(float(x['ra']),float(x['dec']),float(r['ra_deg']),float(r['dec_deg']))<=120.001 for r in part) for x in data)
        rawpath.write_bytes(raw)
        rec.update(status='success',raw=str(rawpath),raw_sha256=hashlib.sha256(raw).hexdigest(),rows=len(data),bytes=len(raw))
    except Exception as exc:
        rec.update(status='unavailable',error=repr(exc));data=[]
    recpath.write_text(json.dumps(rec,indent=2)+'\n',encoding='utf-8')
    print(batch,rec['status'],len(data),flush=True)

by={r['sample_id']:[] for r in rows}
receipts=[]
for batch,part in (('first4',rows[:4]),('remaining96',rows[4:])):
    rec=json.loads((H/f'gaia-neighbors-{batch}.receipt.json').read_text())
    receipts.append(rec)
    if rec['status']!='success': continue
    for x in csv.DictReader(Path(rec['raw']).open(encoding='utf-8-sig',newline='')):
        for r in part:
            dist=angle(float(x['ra']),float(x['dec']),float(r['ra_deg']),float(r['dec_deg']))
            if dist<=120:
                by[r['sample_id']].append({**x,'separation_arcsec':round(dist,5),'is_queue_gaia_source':x['source_id']==r['gaia_dr3']})
for v in by.values():v.sort(key=lambda x:x['separation_arcsec'])
(H/'gaia-neighbors.json').write_text(json.dumps({'scope':'Gaia DR3 gaia_source, 120 arcsec from each queue coordinate; includes the target where returned','queue_sha256':qhash,'receipts':[str(H/f'gaia-neighbors-{b}.receipt.json') for b in ('first4','remaining96')],'targets':by},indent=2)+'\n',encoding='utf-8')
