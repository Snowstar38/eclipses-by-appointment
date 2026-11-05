import requests,json,datetime
ra,dec=10.460730291128636,42.99377247942513
url='https://mast.stsci.edu/tesscut/api/v0.1/sector'; r=requests.get(url,params={'ra':ra,'dec':dec,'radius':0,'units':'deg'},timeout=30);x={'url':r.url,'status':r.status_code,'queried_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'response':r.json() if r.ok else r.text[:500]};open('helper-q083-availability.json','w').write(json.dumps(x,indent=2));print(json.dumps(x,indent=2))
