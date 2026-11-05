import datetime,json,requests
from pathlib import Path
H=Path(__file__).parent
req={'service':'Mast.Caom.Filtered','params':{'columns':'obs_id,sequence_number,project,obs_collection,target_name,provenance_name,dataURL','filters':[{'paramName':'target_name','values':['412639100']}]},'format':'json','pagesize':5000,'page':1}
r=requests.post('https://mast.stsci.edu/api/v0/invoke',data={'request':json.dumps(req)},timeout=30)
r.raise_for_status(); body=r.json()
out=dict(queried_at_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),request=req,response=body)
(H/'mast-availability.json').write_text(json.dumps(out,indent=2)+'\n')
print('status',body.get('status'),'rows',len(body.get('data',[])))
for x in body.get('data',[]):print(x)
