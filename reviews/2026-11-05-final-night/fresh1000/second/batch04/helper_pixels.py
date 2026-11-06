import json,hashlib,io,zipfile,requests,concurrent.futures
from pathlib import Path
import numpy as np
from astropy.io import fits
from astropy.wcs import WCS
B=Path(__file__).resolve().parent
def run(spec):
 tic,sec,c,dur=spec; D=B/tic; ctx=json.loads((D/'lead-context.json').read_text()); h=next(s['header'] for s in ctx['sectors'] if s['sector']==sec); ra,dec=h['RA_OBJ'],h['DEC_OBJ']; out=dict(tic=tic,sector=sec,center=c,duration=dur,ra=ra,dec=dec)
 try:
  raw=(D/'helper-tesscut.fits').read_bytes(); prior=json.loads((D/'helper-localization.json').read_text()); out.update(url=prior['url'],zip_sha256=prior['zip_sha256'],fits_sha256=hashlib.sha256(raw).hexdigest())
  with fits.open(io.BytesIO(raw),memmap=False) as f:
   t=np.array(f[1].data['TIME'],float);q=np.array(f[1].data['QUALITY'],int); cube=np.array(f[1].data['FLUX'],float);w=WCS(f[2].header);x,y=w.world_to_pixel_values(ra,dec)
  x,y=float(x),float(y); good=(q==0)&np.isfinite(t); core=good&(abs(t-c)<dur*.25);side=good&(abs(t-c)>dur*.75)&(abs(t-c)<dur*2); before=np.nanmedian(cube[side],axis=0); diff=before-np.nanmedian(cube[core],axis=0); yy,xx=np.indices(diff.shape);ap=(abs(xx-round(x))<=1)&(abs(yy-round(y))<=1);sky=(np.hypot(xx-x,yy-y)>3);bg=np.nanmedian(cube[:,sky],axis=1);flux=np.nansum(cube[:,ap]-bg[:,None],axis=1);base=np.nanmedian(flux[side]);pos=np.maximum(diff,0)*(np.hypot(xx-x,yy-y)<3);cent=[float(np.nansum(pos*xx)/np.nansum(pos)),float(np.nansum(pos*yy)/np.nansum(pos))]; peak=np.unravel_index(np.nanargmax(diff),diff.shape)
  out.update(status='measured',target_xy=[float(x),float(y)],core_n=int(core.sum()),side_n=int(side.sum()),difference=diff.tolist(),peak_xy=[int(peak[1]),int(peak[0])],centroid_xy=cent,centroid_offset=float(np.hypot(cent[0]-x,cent[1]-y)),aperture_loss=float(1-np.nanmedian(flux[core])/base))
 except Exception as e:out.update(status='failed',error=repr(e))
 (D/'helper-localization.json').write_text(json.dumps(out,indent=2));print(out,flush=True)
with concurrent.futures.ThreadPoolExecutor(max_workers=2) as ex:list(ex.map(run,[('469894984',83,3566.0527847072594,.287617),('248308520',55,2818.4607334418615,.23)]))

