from pathlib import Path
import json,urllib.request,urllib.parse,hashlib
from datetime import datetime,timezone
from concurrent.futures import ThreadPoolExecutor
p=Path('[local path omitted]');rs=json.loads((p/'service-controls.json').read_text())
def query(r):
 s=(p/r['file']).read_text();ls=[z for z in s.splitlines() if z and not z.startswith('#')];h=[z.strip() for z in ls[0].split('\t')];row=dict(zip(h,[z.strip() for z in ls[3].split('\t')]))
 params={'-source':r['table'],'-c':row['RAJ2000']+' '+row['DEJ2000'],'-c.rs':60 if r['table'] in ['B/vsx/vsx','II/366/catv2021'] else 5,'-out.max':100,'-out.all':'','-out.add':'_r'};url='http[local path omitted]'+urllib.parse.urlencode(params);o={'table':r['table'],'url':url,'utc':datetime.now(timezone.utc).isoformat(),'expected':row}
 try:
  raw=urllib.request.urlopen(url,timeout=20).read();s=raw.decode('latin1');assert 'VizieR' in s and '#ERROR' not in s and '<html' not in s.lower();ls=[z for z in s.splitlines() if z and not z.startswith('#')];h=[z.strip() for z in ls[0].split('\t')];assert '_r' in h;rows=[dict(zip(h,[z.strip() for z in line.split('\t')])) for line in ls[3:]];key='TIC' if 'TIC' in row else 'Name' if 'Name' in row else 'ASASSN-V';assert any(z[key].strip()==row[key].strip() for z in rows);name='cone-'+r['file'];(p/name).write_bytes(raw);o.update(status='success',rows=rows,file=name,sha256=hashlib.sha256(raw).hexdigest())
 except Exception as e:o.update(status='unavailable',error=repr(e))
 return o
out=list(ThreadPoolExecutor(6).map(query,[r for r in rs if 'file' in r]));(p/'cone-positive-controls.json').write_text(json.dumps(out,indent=2));print([(r['table'],r['status'],r.get('error')) for r in out])
