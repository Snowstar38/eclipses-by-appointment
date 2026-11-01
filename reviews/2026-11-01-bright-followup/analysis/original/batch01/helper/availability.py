import json,csv,requests,concurrent.futures
from pathlib import Path
B=Path('[local path omitted]'); ids=[r['tic'] for r in csv.DictReader(open(B/'queue.csv'))]
def query(t):
 req={'service':'Mast.Caom.Filtered','format':'json','pagesize':2000,'page':1,'params':{'columns':'obs_collection,provenance_name,sequence_number,t_min,t_max,t_obs_release,obs_id,dataproduct_type,target_name,dataURL','filters':[{'paramName':'target_name','values':[t]},{'paramName':'dataproduct_type','values':['timeseries']}]}}
 try:
  r=requests.post('http[local path omitted]',data={'request':json.dumps(req)},timeout=25);r.raise_for_status(); return t,{'request':req,'response':r.json()}
 except Exception as e:return t,{'request':req,'error':str(e)}
with concurrent.futures.ThreadPoolExecutor(max_workers=10) as pool: out=dict(pool.map(query,ids))
json.dump(out,open(B/'helper'/'availability.json','w'),indent=2)
for t,d in out.items(): print(t,d.get('error',[(x.get('provenance_name'),x.get('sequence_number')) for x in d.get('response',{}).get('data',[]) if x.get('provenance_name')=='QLP']))
