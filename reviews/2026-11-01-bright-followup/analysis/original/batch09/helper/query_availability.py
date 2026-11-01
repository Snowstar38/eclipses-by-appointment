"""Live MAST timeseries availability check for the sparse-repeat exception."""
import json,requests
from pathlib import Path
B=Path(__file__).parent;tic='57047535'
req={'service':'Mast.Caom.Filtered','format':'json','pagesize':2000,'page':1,
     'params':{'columns':'obs_collection,provenance_name,sequence_number,t_min,t_max,t_obs_release,obs_id,dataproduct_type,target_name,dataURL',
               'filters':[{'paramName':'target_name','values':[tic]},{'paramName':'dataproduct_type','values':['timeseries']}]}}
try:
 r=requests.post('http[local path omitted]',data={'request':json.dumps(req)},timeout=30)
 r.raise_for_status();out={'request':req,'response':r.json()}
except Exception as exc:out={'request':req,'error':str(exc)}
(B/'57047535-availability.json').write_text(json.dumps(out,indent=2)+'\n')
if 'response' in out:
 data=out['response'].get('data',[])
 print('QLP sectors',sorted({int(x['sequence_number']) for x in data if x.get('provenance_name')=='QLP' and x.get('sequence_number') is not None}))
else:print(out['error'])


