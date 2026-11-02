import json,hashlib,urllib.parse,urllib.request
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime,timezone
p=Path(__file__).parent; t=json.loads((p/'targets-selected.json').read_text()); d=p/'asassn';d.mkdir(exist_ok=True)
def query(it):
 tic,x=it; params={'-source':'II/366/catv2021','-c':f"{x['ra']} {x['dec']}",'-c.rs':60,'-out.max':100,'-out.all':'','-out.add':'_r','-sort':'_r'}; url='httplocal-source/omitted r={'tic':tic,'url':url,'table':'II/366/catv2021','queried_at_utc':datetime.now(timezone.utc).isoformat()}
 try:
  raw=urllib.request.urlopen(url,timeout=18).read(1000000); s=raw.decode('latin1'); assert 'VizieR' in s and '#ERROR' not in s and '<html' not in s.lower(); (d/(tic+'.tsv')).write_bytes(raw); lines=[z for z in s.splitlines() if z and not z.startswith('#')]; rows=[]
  if lines:
   h=[z.strip() for z in lines[0].split('\t')]; assert '_r' in h; rows=[dict(zip(h,[z.strip() for z in line.split('\t')])) for line in lines[3:]]; assert len(rows)<100
  else: assert 'II/366/catv2021' in s and ('No object found' in s or '#INFO' in s)
  r.update(status='success',rows=rows,sha256=hashlib.sha256(raw).hexdigest())
 except Exception as e:r.update(status='unavailable',error=repr(e))
 return r
with ThreadPoolExecutor(max_workers=8) as pool: results=list(pool.map(query,t.items()))
(p/'asassn-receipts.json').write_text(json.dumps(results,indent=2));print('success',sum(x['status']=='success' for x in results),'rows',sum(bool(x.get('rows')) for x in results),'failed',sum(x['status']!='success' for x in results))
