import requests,csv,json
from pathlib import Path
B=Path(__file__).resolve().parent
q=list(csv.DictReader((B/'queue.csv').open()))
out=[]
for row in [q[5],q[6],q[7]]:
 try:
  r=requests.get('https://mast.stsci.edu/tesscut/api/v0.1/sector',params={'ra':row['ra_deg'],'dec':row['dec_deg'],'radius':0,'units':'deg'},timeout=30);out.append({'tic':row['tic'],'url':r.url,'status':r.status_code,'response':r.json()})
 except Exception as e:out.append({'tic':row['tic'],'error':repr(e)})
(B/'helper-current-sectors.json').write_text(json.dumps(out,indent=2));print(json.dumps(out,indent=2))

