import urllib.request,urllib.parse,pathlib,concurrent.futures,hashlib,json
b=pathlib.Path(__file__).parent
jobs=[('270523058',293.377317531,44.016573595),('295351347',223.303175993,-61.30028071),('280051953',45.670362515,-73.549193591)]
def go(j):
 tic,ra,dec=j;p=urllib.parse.urlencode({'-source':'I/355/gaiadr3','-c':f'{ra} {dec}','-c.rs':'150','-out':'Source,RA_ICRS,DE_ICRS,Gmag','-out.max':'unlimited'});url='https://vizier.cds.unistra.fr/viz-bin/asu-tsv?'+p
 try:
  data=urllib.request.urlopen(url,timeout=30).read();(b/tic/'helper-gaia-vizier.tsv').write_bytes(data);return {'tic':tic,'url':url,'sha256':hashlib.sha256(data).hexdigest(),'bytes':len(data)}
 except Exception as e:return {'tic':tic,'url':url,'error':str(e)}
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as ex:r=list(ex.map(go,jobs))
(b/'helper-vizier-receipts.json').write_text(json.dumps(r,indent=2));print(r)
