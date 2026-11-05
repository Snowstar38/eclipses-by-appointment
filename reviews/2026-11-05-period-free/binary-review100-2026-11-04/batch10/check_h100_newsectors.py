"""Fetch H100 current-footprint s59/s85 cutouts and check actual fold windows."""
import io,json,hashlib,zipfile
from pathlib import Path
import requests,numpy as np
from astropy.io import fits
from astropy.wcs import WCS
B=Path(__file__).resolve().parent/'390853987';fold=json.loads((B/'raw-fold.json').read_text())['fold']['P']
ra=44.27578316743679;dec=61.21550146740097;out=[]
for sec in (59,85):
 p=B/f'followup-tesscut-s{sec}.zip'
 if not p.exists():
  r=requests.get('https://mast.stsci.edu/tesscut/api/v0.1/astrocut',params={'ra':ra,'dec':dec,'x':9,'y':9,'units':'px','sector':sec},timeout=(15,90));r.raise_for_status();p.write_bytes(r.content)
 with zipfile.ZipFile(p) as z:
  with fits.open(io.BytesIO(z.read(next(n for n in z.namelist() if n.endswith('.fits'))))) as h:
   a=h[1].data;t=np.asarray(a['TIME'],float);q=np.asarray(a['QUALITY'],int);cube=np.asarray(a['FLUX'],float);x,y=WCS(h[2].header).world_to_pixel_values(ra,dec)
   g=np.isfinite(t)&(q==0);c=fold['t0']+round((np.nanmedian(t)-fold['t0'])/fold['P'])*fold['P'];off=t-c
   core=g&(abs(off)<fold['dur']/2);left=g&(off>=-.7)&(off<=-.3);right=g&(off>=.3)&(off<=.7);side=left|right
   f=np.nansum(cube[:,3:6,3:6],axis=(1,2));base=float(np.nanmedian(f[side])) if side.sum() else None
   rec={'sector':sec,'archive_path':str(p),'archive_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'wcs_target_x0':float(x),'wcs_target_y0':float(y),'time_start':float(np.nanmin(t[g])),'time_end':float(np.nanmax(t[g])),'predicted_btjd':float(c),'duration_days':fold['dur'],'n_core':int(core.sum()),'n_left':int(left.sum()),'n_right':int(right.sum()),'core_first':float(t[core].min()) if core.sum() else None,'core_last':float(t[core].max()) if core.sum() else None,'depth_ppt':float(1000*(1-np.nanmedian(f[core])/base)) if base and core.sum()>=3 else None,'median_3x3_aperture':float(np.nanmedian(f[g])),'median_central_pixel':float(np.nanmedian(cube[g,4,4]))}
   out.append(rec)
(B/'followup-newsectors.json').write_text(json.dumps(out,indent=2)+'\n')
for x in out:print(x,flush=True)
