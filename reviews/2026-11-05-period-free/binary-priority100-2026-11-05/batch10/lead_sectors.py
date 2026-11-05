"""Current public Tesscut sector availability for fixed batch10 coordinates."""
import csv,json,requests,hashlib
from pathlib import Path
B=Path(__file__).resolve().parent;out=[]
for r in csv.DictReader((B/'queue.csv').open()):
 url='https://mast.stsci.edu/tesscut/api/v0.1/sector'
 resp=requests.get(url,params={'ra':r['ra_deg'],'dec':r['dec_deg']},timeout=30);resp.raise_for_status();data=resp.json()
 out.append(dict(sample_id=r['sample_id'],tic=r['tic'],request_url=resp.url,response_sha256=hashlib.sha256(resp.content).hexdigest(),sectors=[int(x['sector']) for x in data['results']],response=data))
 print(r['sample_id'],out[-1]['sectors'],flush=True)
(B/'lead-sector-availability.json').write_text(json.dumps(out,indent=2)+'\n')
