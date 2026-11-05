"""Bounded, receipt-preserving VizieR cones for four gates and the sealed forty."""
import csv, hashlib, json, re, urllib.parse, urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
from pathlib import Path

H=Path(__file__).resolve().parent; Q=H.parent/'queue.csv'
rows=list(csv.DictReader(Q.open(encoding='utf-8-sig',newline='')))
assert len(rows)==40
qhash=hashlib.sha256(Q.read_bytes()).hexdigest()
tables={'vsx':('B/vsx/vsx',60),'asassn':('II/366/catv2021',60),'kostov3':('J/ApJS/279/50/table3',5),'kostov4':('J/ApJS/279/50/table4',5)}
rawdir=H/'vizier-raw';rawdir.mkdir(exist_ok=True)

def one(row,label,table,radius):
    params={'-source':table,'-c':f"{row['ra_deg']} {row['dec_deg']}",'-c.rs':radius,'-out.max':100,'-out.all':'','-out.add':'_r','-sort':'_r'}
    url='https://vizier.cfa.harvard.edu/viz-bin/asu-tsv?'+urllib.parse.urlencode(params)
    rec={'sample_id':row['sample_id'],'tic':row['tic'],'gaia_dr3':row['gaia_dr3'],'table':table,'radius_arcsec':radius,'url':url,'queue_sha256':qhash,'queried_utc':datetime.now(timezone.utc).isoformat(),'timeout_seconds':12}
    try:
        with urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':'Astra-next40-vizier-gate/1.0'}),timeout=12) as response:raw=response.read(300001)
        if len(raw)>300000:raise ValueError('oversize response')
        tx=raw.decode('utf-8-sig')
        if 'VizieR' not in tx or table not in tx or '#ERROR' in tx or '<html' in tx.lower():raise ValueError('invalid VizieR table response')
        lines=[x for x in tx.splitlines() if x and not x.startswith('#')]
        if lines:
            header=[x.strip() for x in lines[0].split('\t')]
            if '_r' not in header or len(lines)<3:raise ValueError('invalid data layout')
            found=[dict(zip(header,[v.strip() for v in x.split('\t')])) for x in lines[3:]]
            if len(found)>=100:raise ValueError('cone may be truncated')
        else:found=[]
        p=rawdir/(row['sample_id']+'-'+label+'.tsv');p.write_bytes(raw)
        rec.update(status='success',raw=str(p),sha256=hashlib.sha256(raw).hexdigest(),rows=len(found))
    except Exception as exc:rec.update(status='unavailable',error=repr(exc));found=[]
    exact=[]
    for x in found:
        vals=' '.join(str(v) for k,v in x.items() if k not in ('_r','Period','RAJ2000','DEJ2000'))
        if re.search(r'(?<!\d)'+row['tic']+r'(?!\d)',vals) or re.search(r'(?<!\d)'+row['gaia_dr3']+r'(?!\d)',vals):exact.append(x)
    return row['sample_id'],label,rec,found,exact

out={r['sample_id']:{} for r in rows};receipts={}
with ThreadPoolExecutor(max_workers=4) as pool:
    tasks=[pool.submit(one,r,label,table,radius) for r in rows for label,(table,radius) in tables.items()]
    for task in as_completed(tasks):
        sample,label,rec,found,exact=task.result()
        receipts[sample+'-'+label]=rec
        out[sample][label]={'status':rec['status'],'exact_rows':exact,'nearby_rows':found}
(H/'vizier-gate-receipts.json').write_text(json.dumps(receipts,indent=2)+'\n',encoding='utf-8')
(H/'vizier-gate-results.json').write_text(json.dumps({'queue_sha256':qhash,'tables':tables,'targets':out},indent=2)+'\n',encoding='utf-8')
print(json.dumps({'requests':len(receipts),'status':{k:sum(v['status']==k for v in receipts.values()) for k in ('success','unavailable')},'exact':[(s,k,len(v['exact_rows'])) for s,t in out.items() for k,v in t.items() if v['exact_rows']]}))
