import requests,zipfile,io,json,hashlib,pathlib,concurrent.futures
B=pathlib.Path(r'[local-path-redacted]')
def go(a):
 tic,ra,dec,s=a; r=requests.get('https://mast.stsci.edu/tesscut/api/v0.1/astrocut',params=dict(ra=ra,dec=dec,x=11,y=11,units='px',sector=s),timeout=90); raw=B/f'helper-{tic}-tesscut.raw'; raw.write_bytes(r.content); out=dict(url=r.url,status=r.status_code,headers=dict(r.headers),raw_sha256=hashlib.sha256(r.content).hexdigest());
 if r.ok:
  z=zipfile.ZipFile(io.BytesIO(r.content)); name=z.namelist()[0]; dat=z.read(name); (B/f'helper-{tic}-tesscut.fits').write_bytes(dat); out.update(member=name,fits_sha256=hashlib.sha256(dat).hexdigest())
 (B/f'helper-{tic}-receipt.json').write_text(json.dumps(out,indent=2)); print(tic,r.status_code,len(r.content))
with concurrent.futures.ThreadPoolExecutor(max_workers=2) as ex: list(ex.map(go,[(362778566,271.4743001692025,-12.030042465995317,80),(309965535,138.07788256853726,76.50309237623361,73)]))
