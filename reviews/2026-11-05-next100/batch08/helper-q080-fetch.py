import urllib.request,pathlib,hashlib,json,concurrent.futures
b=pathlib.Path(__file__).parent; tic='99243741';ra=107.93578118490746;dec=-22.44168599835311
def go(sec):
 url=f'https://mast.stsci.edu/tesscut/api/v0.1/astrocut?ra={ra}&dec={dec}&y=11&x=11&units=px&sector={sec}'
 try:
  d=urllib.request.urlopen(url,timeout=50).read();p=b/tic/f'helper-tesscut-s{sec}.zip';p.write_bytes(d);return {'sector':sec,'url':url,'sha256':hashlib.sha256(d).hexdigest(),'bytes':len(d)}
 except Exception as e:return {'sector':sec,'url':url,'error':str(e)}
with concurrent.futures.ThreadPoolExecutor(max_workers=2) as ex:r=list(ex.map(go,[7,34]))
(b/tic/'helper-download.json').write_text(json.dumps(r,indent=2));print(r)
