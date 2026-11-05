"""Record current official TESSCut sector coverage for the batch coordinates."""
import csv, hashlib, json
from pathlib import Path
import requests
B=Path(__file__).resolve().parent
rows=list(csv.DictReader((B/'queue.csv').open(newline='',encoding='utf-8')))
out=[]
for r in rows:
 try:
  res=requests.get('https://mast.stsci.edu/tesscut/api/v0.1/sector',params={'ra':r['ra_deg'],'dec':r['dec_deg']},timeout=30)
  payload=res.json(); secs=[int(x['sector']) for x in payload['results']]
  out.append({'sample_id':r['sample_id'],'tic':r['tic'],'request_url':res.url,'http_status':res.status_code,'response_sha256':hashlib.sha256(res.content).hexdigest(),'sectors':secs,'newer_than_cached':[s for s in secs if s>max(int(p.name.split('_s')[-1][:3]) for p in Path('[local-path-redacted]').glob(r['tic']+'_s*.fits'))]})
 except Exception as e:out.append({'sample_id':r['sample_id'],'tic':r['tic'],'error':str(e)})
(B/'current-sector-availability.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
for x in out:print(x['sample_id'],x.get('newer_than_cached'),x.get('error'))
