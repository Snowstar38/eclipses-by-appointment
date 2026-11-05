import csv,json,hashlib,urllib.parse,urllib.request
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from datetime import datetime,timezone
H=Path(__file__).resolve().parent;qhash=hashlib.sha256((H.parent/'queue.csv').read_bytes()).hexdigest(); old=list(csv.DictReader(Path('[local-path-redacted]').open(encoding='utf8')))
coords=lambda id:next(r['ra_deg']+' '+r['dec_deg'] for r in old if r['sample_id']==id)
items={'vsx':('B/vsx/vsx',coords('F008'),60),'asassn':('II/366/catv2021',coords('F006'),60),'kostov3':('J/ApJS/279/50/table3','219.00555469 -27.56944137',5),'kostov4':('J/ApJS/279/50/table4','219.04301800 -24.33205152',5)}
def probe(item):
 label,(table,c,rad)=item;url='https://vizier.cfa.harvard.edu/viz-bin/asu-tsv?'+urllib.parse.urlencode({'-source':table,'-c':c,'-c.rs':rad,'-out.max':100,'-out.all':'','-out.add':'_r'}); rec={'url':url,'table':table,'queue_sha256':qhash,'time_utc':datetime.now(timezone.utc).isoformat(),'timeout_seconds':10}
 try:
  with urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':'Astra-next100-audit/1.0'}),timeout=10) as r:raw=r.read(300001)
  tx=raw.decode('utf8-sig');lines=[x for x in tx.splitlines() if x and not x.startswith('#')];assert len(raw)<=300000 and table in tx and '#ERROR' not in tx and len(lines)>=4 and '_r' in lines[0]
  p=H/(label+'-positive-control.tsv');p.write_bytes(raw);rec.update(status='success',sha256=hashlib.sha256(raw).hexdigest(),raw=str(p),rows=len(lines)-3)
 except Exception as e:rec.update(status='unavailable',error=repr(e))
 return label,rec
with ThreadPoolExecutor(max_workers=4) as pool:out=dict(pool.map(probe,items.items()))
(H/'gate-controls.json').write_text(json.dumps(out,indent=2)+'\n');print({k:v['status'] for k,v in out.items()})
