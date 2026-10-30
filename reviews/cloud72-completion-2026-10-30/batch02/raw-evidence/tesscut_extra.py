from pathlib import Path
import json,urllib.request,zipfile,io,hashlib,concurrent.futures
R=Path(__file__).parent;T=json.load(open(R.parent/'targets-selected.json'));old=json.load(open(R/'tesscut-downloads.json'));jobs=[('126363604',61),('126363604',88),('376082142',15),('376082142',57),('251357000',18),('251357000',85)]
def run(j):
 tic,sec=j;d=T[tic];url=f"https://mast.stsci.edu/tesscut/api/v0.1/astrocut?ra={d['ra']}&dec={d['dec']}&y=11&x=11&units=px&sector={sec}"
 try:
  b=urllib.request.urlopen(url,timeout=90).read(50000001);assert len(b)<=50000000;z=zipfile.ZipFile(io.BytesIO(b));(R/tic/f'tesscut_s{sec:03d}.zip').write_bytes(b);z.extractall(R/tic);return dict(tic=tic,sector=sec,url=url,sha256=hashlib.sha256(b).hexdigest(),members=z.namelist())
 except Exception as e:return dict(tic=tic,sector=sec,url=url,error=repr(e))
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as ex:new=list(ex.map(run,jobs))
json.dump(old+new,open(R/'tesscut-downloads.json','w'),indent=2);print(new)
