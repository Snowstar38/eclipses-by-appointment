from pathlib import Path
import requests,json,hashlib,datetime,sys
D=Path(__file__).parent
tic=sys.argv[1];req={'service':'Mast.Caom.Filtered','params':{'columns':'obs_id,sequence_number,project,obs_collection,target_name','filters':[{'paramName':'target_name','values':[tic]}]},'format':'json','pagesize':5000,'page':1};out=dict(tic=tic,queried_at_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),endpoint='httplocal-source/omitted
try:
 r=requests.post(out['endpoint'],data={'request':json.dumps(req)},timeout=30);r.raise_for_status();body=r.json();assert body['status']=='COMPLETE';assert len(body['data'])<5000;out.update(status='success',response=body,qlp_sectors=sorted({int(x['sequence_number']) for x in body['data'] if x['obs_id'].startswith('hlsp_qlp_') and x['target_name']==tic}))
except Exception as e:out.update(status='unknown',error=repr(e))
p=D/(tic+'-mast-availability.json');p.write_text(json.dumps(out,indent=2)+'\n');print(out.get('qlp_sectors',out),hashlib.sha256(p.read_bytes()).hexdigest())
