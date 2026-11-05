import csv,hashlib,json
from pathlib import Path
import requests
B=Path(__file__).resolve().parent
Q={q['sample_id']:q for q in csv.DictReader((B/'queue.csv').open(newline='',encoding='utf-8'))}
out={}
for sid in ('H039','H031','H040'):
 q=Q[sid];tic=q['tic']
 try:
  r=requests.get('https://mast.stsci.edu/tesscut/api/v0.1/sector',params={'ra':q['ra_deg'],'dec':q['dec_deg']},timeout=25)
  raw=r.content;(B/tic/'sector-availability.raw').write_bytes(raw)
  rec={'url':r.url,'http_status':r.status_code,'response_sha256':hashlib.sha256(raw).hexdigest()}
  if r.ok:
   rec['response']=r.json();rec['available_sectors']=sorted({int(x['sector']) for x in rec['response'].get('results',[]) if 'sector' in x})
  else:rec['error']=r.text[:500]
 except Exception as exc:rec={'error':repr(exc),'status':'UNKNOWN'}
 out[tic]=rec
 print(sid,tic,rec.get('available_sectors'),rec.get('error'),flush=True)
(B/'sector-availability.json').write_text(json.dumps(out,indent=2)+'\n')
