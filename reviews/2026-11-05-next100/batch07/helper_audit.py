import json,hashlib,urllib.request,zipfile,io,concurrent.futures
from pathlib import Path
import numpy as np
from astropy.io import fits
B=Path(__file__).resolve().parent
jobs=[('295176393',270.34925752923124,-69.60515069877758,39),('341419787',120.15339783069679,-54.50900340546292,7)]
def fetch(j):
 tic,ra,dec,s=j; url=f'https://mast.stsci.edu/tesscut/api/v0.1/astrocut?ra={ra}&dec={dec}&y=11&x=11&units=px&sector={s}'
 try:
  data=urllib.request.urlopen(url,timeout=45).read(50000001);z=zipfile.ZipFile(io.BytesIO(data)); out=[]
  for name in z.namelist():
   if name.endswith('.fits'):
    p=B/f'helper-{tic}-s{s:03d}-cutout.fits';p.write_bytes(z.read(name));out.append({'file':str(p),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()})
  return {'tic':tic,'url':url,'files':out,'zip_sha256':hashlib.sha256(data).hexdigest()}
 except Exception as e:return {'tic':tic,'url':url,'error':repr(e)}
with concurrent.futures.ThreadPoolExecutor(max_workers=2) as ex: d=list(ex.map(fetch,jobs))
(B/'helper-downloads.json').write_text(json.dumps(d,indent=2))
out={}
for tic,t0,p in [('341419787',1493.4364264326475,21.071622669899853),('295176393',2365.971852753895,27.254540389441)]:
 c=json.loads((B/tic/'lead-context.json').read_text()); rows=[]
 for s in c['sectors']:
  fp=Path(s['source_path']);assert hashlib.sha256(fp.read_bytes()).hexdigest()==s['source_sha256']
  with fits.open(fp) as h:
   a=h[1].data;t=np.array(a['TIME'],float);f=np.array(a['SAP_FLUX'],float);q=np.array(a['QUALITY']);m=np.isfinite(t)&np.isfinite(f)&(f>0)&(q==0);t=t[m];f=f[m]
  for n in range(int(np.floor((t.min()-t0)/p)),int(np.ceil((t.max()-t0)/p))+1):
   center=t0+n*p
   if center<t.min()-.15 or center>t.max()+.15:continue
   core=(abs(t-center)<.06);base=(abs(t-center)>.15)&(abs(t-center)<.5);tc=t[core]
   rows.append(dict(sector=s['sector'],cycle=n,center=center,n_core=int(core.sum()),core_first=float(tc.min()) if len(tc) else None,core_last=float(tc.max()) if len(tc) else None,max_gap=float(np.diff(tc).max()) if len(tc)>1 else None,n_baseline=int(base.sum()),depth_ppt=float(1000*(1-np.median(f[core])/np.median(f[base]))) if core.sum() and base.sum()>5 else None,sha256=s['source_sha256']))
 out[tic]=rows
(B/'helper-measured-period-coverage.json').write_text(json.dumps(out,indent=2))
print(json.dumps(d,indent=2));print(json.dumps(out['341419787'],indent=2))
