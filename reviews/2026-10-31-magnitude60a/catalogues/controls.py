import json,urllib.request,urllib.parse,hashlib,csv,io
from pathlib import Path
from datetime import datetime,timezone
from concurrent.futures import ThreadPoolExecutor
p=Path('[local path omitted]')
tabs=['B/vsx/vsx','II/366/catv2021','J/ApJS/258/16/tess-ebs','J/A+A/691/A242/obaf-eb1','J/ApJS/279/50/table3','J/ApJS/279/50/table4']
def v(tb):
 url='http[local path omitted]'+urllib.parse.urlencode({'-source':tb,'-out.max':1,'-out.all':''});r={'table':tb,'url':url,'utc':datetime.now(timezone.utc).isoformat()}
 try:
  raw=urllib.request.urlopen(url,timeout=25).read();s=raw.decode('latin1');assert '#ERROR' not in s and '<html' not in s.lower();lines=[x for x in s.splitlines() if x and not x.startswith('#')];assert len(lines)>=4;name='control-'+tb.split('/')[-1]+'.tsv';(p/name).write_bytes(raw);r.update(status='success',file=name,sha256=hashlib.sha256(raw).hexdigest(),rows=lines[3:])
 except Exception as e:r.update(status='unavailable',error=repr(e))
 return r
rs=list(ThreadPoolExecutor(6).map(v,tabs))
url='http[local path omitted]';q='SELECT TOP 1 source_id FROM gaiadr3.vari_eclipsing_binary';r={'table':'Gaia DR3 EB','url':url,'query':q,'utc':datetime.now(timezone.utc).isoformat()}
try:
 raw=urllib.request.urlopen(url,urllib.parse.urlencode({'REQUEST':'doQuery','LANG':'ADQL','FORMAT':'csv','QUERY':q}).encode(),timeout=25).read();rows=list(csv.DictReader(io.StringIO(raw.decode())));assert len(rows)==1 and rows[0]['source_id'];(p/'control-gaia-eb.csv').write_bytes(raw);r.update(status='success',rows=rows,sha256=hashlib.sha256(raw).hexdigest())
except Exception as e:r.update(status='unavailable',error=repr(e))
rs.append(r);(p/'service-controls.json').write_text(json.dumps(rs,indent=2));print([(r['table'],r['status']) for r in rs])
