"""Current TESSCut sector availability for bounded ambiguous/single cases."""
import csv,json,requests
from pathlib import Path
B=Path(__file__).resolve().parent
q=list(csv.DictReader((B/'queue.csv').open(encoding='utf-8',newline='')))
out=[]
for row in q:
    if row['sample_id'] in ('T041','T042'):continue
    url='https://mast.stsci.edu/tesscut/api/v0.1/sector'
    try:
        response=requests.get(url,params=dict(ra=row['ra_deg'],dec=row['dec_deg'],radius=0,units='deg'),timeout=20)
        response.raise_for_status();payload=response.json()
        sectors=payload['results']
        out.append(dict(sample_id=row['sample_id'],tic=row['tic'],url=response.url,status_code=response.status_code,sectors=sectors))
        print(row['sample_id'],[p.get('sector') for p in sectors],flush=True)
    except Exception as ex:
        out.append(dict(sample_id=row['sample_id'],tic=row['tic'],url=url,error=repr(ex)))
        print(row['sample_id'],'UNKNOWN',repr(ex),flush=True)
(B/'lead-current-sectors.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
