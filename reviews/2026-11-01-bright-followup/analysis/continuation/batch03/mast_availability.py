import datetime,json,requests
from pathlib import Path
B=Path(__file__).parent
tic='382581210'
req={'service':'Mast.Caom.Filtered','params':{'columns':'obs_id,sequence_number,project,obs_collection,target_name','filters':[{'paramName':'target_name','values':[tic]}]},'format':'json','pagesize':5000,'page':1}
r=requests.post('http[local path omitted]',data={'request':json.dumps(req)},timeout=30)
r.raise_for_status();body=r.json();assert body['status']=='COMPLETE'
qlp=sorted({int(x['sequence_number']) for x in body['data'] if x['obs_id'].startswith('hlsp_qlp_') and x['target_name']==tic})
out={'queried_at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'endpoint':'http[local path omitted]','request':req,'response':body,'qlp_sectors':qlp}
(B/'382581210-mast-availability.json').write_text(json.dumps(out,indent=2)+'\n')
print('QLP sectors',qlp,'rows',len(body['data']))
