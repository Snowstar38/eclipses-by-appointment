import urllib.request,concurrent.futures,json,pathlib,hashlib
b=pathlib.Path('[local-path-redacted]'); jobs=[('270523058',293.3773175310484,44.01657359497792,14),('295351347',223.30317599308512,-61.30028070964274,11),('280051953',45.67036251522263,-73.54919359108234,13)]
def go(j):
 t,ra,dec,s=j; url=f'https://mast.stsci.edu/tesscut/api/v0.1/astrocut?ra={ra}&dec={dec}&y=11&x=11&units=px&sector={s}'
 try:
  data=urllib.request.urlopen(url,timeout=90).read(); p=b/t/f'helper-tesscut-s{s}.zip';p.write_bytes(data);return {'tic':t,'url':url,'sha256':hashlib.sha256(data).hexdigest(),'bytes':len(data)}
 except Exception as e:return {'tic':t,'url':url,'error':str(e)}
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as ex:r=list(ex.map(go,jobs))
(b/'helper-downloads.json').write_text(json.dumps(r,indent=2));print(r)
