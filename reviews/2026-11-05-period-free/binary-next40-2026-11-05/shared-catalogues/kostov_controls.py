"""Queue-bound fresh positive controls for the two Kostov VizieR tables."""
import hashlib,json,urllib.parse,urllib.request
from datetime import datetime,timezone
from pathlib import Path
H=Path(__file__).resolve().parent
qhash=hashlib.sha256((H.parent/'queue.csv').read_bytes()).hexdigest()
controls={'kostov3':('J/ApJS/279/50/table3','219.00555469 -27.56944137','8636'),
          'kostov4':('J/ApJS/279/50/table4','219.04301800 -24.33205152',None)}
out={}
for label,(table,coords,expected) in controls.items():
    url='https://vizier.idia.ac.za/viz-bin/asu-tsv?'+urllib.parse.urlencode({'-source':table,'-c':coords,'-c.rs':5,'-out.max':100,'-out.all':'','-out.add':'_r'})
    rec={'url':url,'table':table,'queue_sha256':qhash,'queried_utc':datetime.now(timezone.utc).isoformat(),'timeout_seconds':20}
    try:
        with urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':'Astra-next40-positive-control/1.0'}),timeout=20) as r:raw=r.read(100001)
        tx=raw.decode('utf-8-sig'); lines=[x for x in tx.splitlines() if x and not x.startswith('#')]
        if len(raw)>100000 or table not in tx or '#ERROR' in tx or len(lines)<4 or '_r' not in lines[0] or (expected and expected not in lines[-1]):raise ValueError('positive control failed')
        p=H/(label+'-positive-control.tsv');p.write_bytes(raw)
        rec.update(status='success',raw=str(p),sha256=hashlib.sha256(raw).hexdigest(),data_rows=len(lines)-3)
    except Exception as e:rec.update(status='unavailable',error=repr(e))
    out[label]=rec
(H/'kostov-controls.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print({k:(v['status'],v.get('data_rows')) for k,v in out.items()})
