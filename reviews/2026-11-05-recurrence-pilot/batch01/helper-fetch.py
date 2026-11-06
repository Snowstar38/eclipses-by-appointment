from pathlib import Path
import requests,zipfile,io,hashlib,json,concurrent.futures
B=Path(__file__).resolve().parent
jobs=[('147413927',163.21764583099278,-47.70130734349548,37),('147413927',163.21764583099278,-47.70130734349548,90),('265066551',347.36321314194146,68.42988151080459,17)]
def fetch(j):
 tic,ra,dec,sec=j; args=dict(ra=ra,dec=dec,x=11,y=11,units='px',sector=sec)
 try:
  r=requests.get('https://mast.stsci.edu/tesscut/api/v0.1/astrocut',params=args,timeout=100); r.raise_for_status(); z=zipfile.ZipFile(io.BytesIO(r.content)); raw=z.read(z.namelist()[0]);p=B/tic/f'helper-tesscut-s{sec:03}.fits';p.write_bytes(raw)
  return dict(tic=tic,sector=sec,url=r.url,status=r.status_code,zip_sha256=hashlib.sha256(r.content).hexdigest(),fits_sha256=hashlib.sha256(raw).hexdigest(),path=str(p))
 except Exception as e:return dict(tic=tic,sector=sec,error=str(e))
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as ex: out=list(ex.map(fetch,jobs))
(B/'helper-fetch.json').write_text(json.dumps(out,indent=2)+'\n');print(out)
