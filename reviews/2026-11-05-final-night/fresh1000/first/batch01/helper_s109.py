import requests,io,zipfile,json,hashlib
from pathlib import Path
import numpy as np
from astropy.io import fits
from astropy.wcs import WCS
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
D=Path(__file__).resolve().parent/'34308477';o=json.loads((D/'helper-localization.json').read_text());ra,dec=o['ra'],o['dec'];r=requests.get('https://mast.stsci.edu/tesscut/api/v0.1/astrocut',params=dict(ra=ra,dec=dec,x=11,y=11,units='px',sector=109),timeout=180);r.raise_for_status();z=zipfile.ZipFile(io.BytesIO(r.content));raw=z.read(z.namelist()[0]);(D/'helper-s109-tesscut.fits').write_bytes(raw)
with fits.open(io.BytesIO(raw)) as f:
 t=np.array(f[1].data['TIME'],float);q=np.array(f[1].data['QUALITY'],int);cube=np.array(f[1].data['FLUX'],float);w=WCS(f[2].header);x,y=w.world_to_pixel_values(ra,dec)
yy,xx=np.indices(cube.shape[1:]);ap=(abs(xx-round(float(x)))<=1)&(abs(yy-round(float(y)))<=1);sky=np.hypot(xx-x,yy-y)>4;bg=np.nanmedian(cube[:,sky],axis=1);f=np.nansum(cube[:,ap]-bg[:,None],axis=1);good=(q==0)&np.isfinite(t)&np.isfinite(f)&(f>0); t=t[good];f=f[good]; f=f/np.median(f); a,b=1442.6972366799441,2182.4488695378413;results=[]
for n in range(1,61):
 P=(b-a)/n; k0=int(np.floor((min(t)-a)/P));k1=int(np.ceil((max(t)-a)/P));checks=[]
 for k in range(k0,k1+1):
  c=a+k*P;core=abs(t-c)<.1;left=(t>c-.5)&(t<c-.2);right=(t>c+.2)&(t<c+.5)
  if min(core.sum(),left.sum(),right.sum())>=5:
   depth=1-np.median(f[core])/((np.median(f[left])+np.median(f[right]))/2);checks.append(dict(center=float(c),n_core=int(core.sum()),n_left=int(left.sum()),n_right=int(right.sum()),depth=float(depth)))
 results.append(dict(n=n,period=float(P),checks=checks))
fig,ax=plt.subplots(figsize=(12,3));ax.plot(t,f,'.',ms=1); ax.set(xlabel='BTJD',ylabel='target 3x3 normalized flux',title='Z003 sector 109 independent extraction');fig.tight_layout();fig.savefig(D/'helper-s109.png',dpi=140)
out=dict(request_url=r.url,zip_sha256=hashlib.sha256(r.content).hexdigest(),fits_sha256=hashlib.sha256(raw).hexdigest(),target_xy=[float(x),float(y)],valid_n=len(t),time_range=[float(min(t)),float(max(t))],candidate_aliases=results);(D/'helper-s109.json').write_text(json.dumps(out,indent=2));print('n15',results[14]);print('range',out['time_range'])
