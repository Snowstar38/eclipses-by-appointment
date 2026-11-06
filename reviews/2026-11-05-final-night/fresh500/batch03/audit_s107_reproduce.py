"""Reproduce E027 cutouts and S107 fit. Default reads saved FITS; --download refetches."""
import sys,io,zipfile,hashlib,json,requests,numpy as np
from pathlib import Path
from astropy.io import fits
from scipy.optimize import curve_fit
P=Path(__file__).resolve().parent/'12878982'; out={}
for sec in [3,107]:
 path=P/f'audit-s{sec:03}.fits'
 if '--download' in sys.argv:
  r=requests.get('https://mast.stsci.edu/tesscut/api/v0.1/astrocut',params={'ra':4.41960302691,'dec':-13.8949570917,'x':5,'y':5,'units':'px','sector':sec},timeout=180);r.raise_for_status();z=zipfile.ZipFile(io.BytesIO(r.content));path.write_bytes(z.read(z.namelist()[0]));print('resolved URL',r.url)
 with fits.open(path) as h:
  a=h[1].data;t=np.array(a['TIME']);q=np.array(a['QUALITY']);cube=np.array(a['FLUX'])
 out[str(sec)]={'fits_sha256':hashlib.sha256(path.read_bytes()).hexdigest(),'time_range':[float(np.nanmin(t)),float(np.nanmax(t))],'pixel_median_range':[float(np.nanmin(np.nanmedian(cube,axis=0))),float(np.nanmax(np.nanmedian(cube,axis=0)))]}
 if sec==107:
  edge=np.ones((5,5),bool);edge[1:4,1:4]=False;flux=np.nansum(cube[:,1:4,1:4],axis=(1,2))-9*np.nanmedian(cube[:,edge],axis=1);g=np.isfinite(t)&np.isfinite(flux)&(q==0)&(abs(t-4271.55)<1);base=np.nanmedian(flux[g&(abs(t-4271.55)>.5)]);tt=t[g]-4271.55;ff=flux[g]/base
  def trap(x,b,s,d,c,w,ing):return b+s*x-d*np.clip((w/2-np.abs(x-c))/(w*ing),0,1)
  v,cov=curve_fit(trap,tt,ff,p0=[1,0,.035,0,.3,.3],bounds=([.8,-.2,0,-.2,.05,.05],[1.2,.2,.8,.2,.9,.49]),maxfev=30000);out[str(sec)].update(center_btjd=float(4271.55+v[3]),formal_error_d=float(np.sqrt(cov[3,3])),depth_ppt=float(v[2]*1000),duration_d=float(v[4]))
print(json.dumps(out,indent=2))
