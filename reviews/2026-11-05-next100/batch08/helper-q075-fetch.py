import urllib.request,pathlib,hashlib,json
b=pathlib.Path(__file__).parent; url='https://mast.stsci.edu/tesscut/api/v0.1/astrocut?ra=187.4382754243&dec=-45.6950742162&y=11&x=11&units=px&sector=99'
try:
 data=urllib.request.urlopen(url,timeout=45).read();p=b/'72497715/helper-tesscut-s99.zip';p.write_bytes(data);r={'url':url,'sha256':hashlib.sha256(data).hexdigest(),'bytes':len(data)}
except Exception as e:r={'url':url,'error':str(e)}
(b/'72497715/helper-download.json').write_text(json.dumps(r,indent=2));print(r)
