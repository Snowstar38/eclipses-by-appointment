import requests,concurrent.futures,json
cases=[('Q082',213.0506965594,-59.8044561966,11),('Q083',10.4607302911,42.9937724794,57),('Q083',10.4607302911,42.9937724794,84),('Q090',288.2374831584,58.1078730882,41)]
def get(c):
 try:
  r=requests.get('https://mast.stsci.edu/tesscut/api/v0.1/astrocut',params=dict(ra=c[1],dec=c[2],x=11,y=11,sector=c[3]),timeout=60); p=f'helper-{c[0]}-s{c[3]}.zip';
  if r.ok:open(p,'wb').write(r.content)
  return dict(case=c,url=r.url,status=r.status_code,bytes=len(r.content),body=r.text[:200] if not r.ok else None)
 except Exception as e:return dict(case=c,error=repr(e))
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as e: out=list(e.map(get,cases))
open('helper-tesscut-access.json','w').write(json.dumps(out,indent=2));print(json.dumps(out,indent=2))
