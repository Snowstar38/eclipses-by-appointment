import json,hashlib,urllib.parse,urllib.request
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime,timezone
p=Path(__file__).parent;t=json.loads((p/'targets-selected.json').read_text());d=p/'eb-battery';d.mkdir(exist_ok=True)
tabs=['J/ApJS/258/16/tess-ebs','J/A+A/691/A242/obaf-eb1','J/ApJS/279/50/table3','J/ApJS/279/50/table4']
def query(z):
 tic,x,tb=z;params={'-source':tb,'-c':f"{x['ra']} {x['dec']}",'-c.rs':5,'-out.max':100,'-out.all':'','-out.add':'_r'};url='httplocal-source/omitted
 try:
  raw=urllib.request.urlopen(url,timeout=15).read(1000000);s=raw.decode('latin1');assert 'VizieR' in s and '#ERROR' not in s and '<html' not in s.lower();name=tic+'-'+tb.split('/')[-1]+'.tsv';(d/name).write_bytes(raw); lines=[z for z in s.splitlines() if z and not z.startswith('#')];rows=[]
  if lines:
   h=[z.strip() for z in lines[0].split('\t')];assert '_r' in h;rows=[dict(zip(h,[z.strip() for z in line.split('\t')])) for line in lines[3:]];assert len(rows)<100
  else: assert tb in s and ('No object found' in s or '#INFO' in s)
  r.update(status='success',rows=rows,sha256=hashlib.sha256(raw).hexdigest(),file=name)
 except Exception as e:r.update(status='unavailable',error=repr(e))
 return r
# Probe one per service table before issuing bounded batches.
first=next(iter(t.items())); probes=[query((first[0],first[1],tb)) for tb in tabs];results=probes[:]
for tb,probe in zip(tabs,probes):
 if probe['status']=='success':
  with ThreadPoolExecutor(max_workers=8) as pool:results+=list(pool.map(query,[(tic,x,tb) for tic,x in list(t.items())[1:]]))
(p/'eb-battery-receipts.json').write_text(json.dumps(results,indent=2));print('results',len(results),'success',sum(r['status']=='success' for r in results),'matches',[(r['tic'],r['table'],r['rows']) for r in results if r.get('rows')],'errors',[(r['tic'],r['table'],r.get('error')) for r in results if r['status']!='success'])
