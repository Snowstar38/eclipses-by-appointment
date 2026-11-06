import csv,json,hashlib,io,zipfile,requests,concurrent.futures
from pathlib import Path
import numpy as np
from astropy.io import fits
from astropy.wcs import WCS
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
B=Path(__file__).resolve().parent
rows=list(csv.DictReader((B/'queue.csv').open()))
def run(row):
 tic=row['tic']; D=B/tic; context=json.loads((D/'lead-context.json').read_text()); times=json.loads((D/'lead-timing.json').read_text()); 
 if not times:return tic,'no_discrete_event',None,None
 ev=max(times,key=lambda x:x.get('depth_ppt',0)); sec=ev['sector']; h=next(s['header'] for s in context['sectors'] if s['sector']==sec); ra,dec=h['RA_OBJ'],h['DEC_OBJ']; c=ev['center_btjd']; dur=ev['duration_d']; url='https://mast.stsci.edu/tesscut/api/v0.1/astrocut'
 out={'tic':tic,'event':ev,'ra':ra,'dec':dec}
 try:
  r=requests.get(url,params=dict(ra=ra,dec=dec,x=7,y=7,units='px',sector=sec),timeout=180);r.raise_for_status(); z=zipfile.ZipFile(io.BytesIO(r.content)); raw=z.read(z.namelist()[0]); p=D/'helper-tesscut.fits';p.write_bytes(raw);out.update(request_url=r.url,zip_sha256=hashlib.sha256(r.content).hexdigest(),fits_sha256=hashlib.sha256(raw).hexdigest())
  with fits.open(io.BytesIO(raw),memmap=False) as f:
   t=np.array(f[1].data['TIME'],float);q=np.array(f[1].data['QUALITY'],int); cube=np.array(f[1].data['FLUX'],float);w=WCS(f[2].header);x,y=w.world_to_pixel_values(ra,dec)
  x,y=float(x),float(y); good=(q==0)&np.isfinite(t); core=good&(abs(t-c)<dur*.25);side=good&(abs(t-c)>dur*.75)&(abs(t-c)<dur*2);out.update(target_xy=[x,y],core_n=int(core.sum()),side_n=int(side.sum()))
  if core.sum()<2 or side.sum()<4: raise ValueError('insufficient usable core or side samples')
  before=np.nanmedian(cube[side],axis=0); diff=before-np.nanmedian(cube[core],axis=0); yy,xx=np.indices(diff.shape); ix,iy=round(x),round(y);ap=(abs(xx-ix)<=1)&(abs(yy-iy)<=1);sky=(np.hypot(xx-x,yy-y)>2.8); bg=np.nanmedian(cube[:,sky],axis=1); flux=np.nansum(cube[:,ap]-bg[:,None],axis=1);base=np.nanmedian(flux[side]); loss=1-np.nanmedian(flux[core])/base; peak=np.unravel_index(np.nanargmax(diff),diff.shape); pos=np.maximum(diff,0); near=np.hypot(xx-x,yy-y)<3; wt=pos*near; centroid=[float(np.nansum(wt*xx)/np.nansum(wt)),float(np.nansum(wt*yy)/np.nansum(wt))];out.update(aperture_loss=float(loss),diff_peak_xy=[int(peak[1]),int(peak[0])],positive_diff_centroid_xy=centroid,centroid_offset_pixels=float(np.hypot(centroid[0]-x,centroid[1]-y)))
  fig,ax=plt.subplots(1,3,figsize=(13,4));ax[0].imshow(before,origin='lower');ax[1].imshow(diff,origin='lower',cmap='coolwarm');
  for a in ax[:2]:a.plot(x,y,'wx',ms=10,mew=2);a.plot(*centroid,'g+',ms=10,mew=2)
  ax[0].set_title('out of eclipse; white target');ax[1].set_title('out minus in; green centroid');g=good&(abs(t-c)<max(2*dur,.5));ax[2].plot(t[g]-c,flux[g]/base,'.');ax[2].axvspan(-dur*.25,dur*.25,alpha=.2,color='r');ax[2].set_title(f'3x3 aperture loss {loss:.3f}');ax[2].set_xlabel('BTJD minus event center');fig.suptitle(f"{row['sample_id']} TIC {tic} sector {sec}");fig.tight_layout();fig.savefig(D/'helper-localization.png',dpi=130);plt.close(fig);out['status']='measured'
 except Exception as e:out.update(status='failed',error=repr(e))
 (D/'helper-localization.json').write_text(json.dumps(out,indent=2));return tic,out.get('status'),out.get('centroid_offset_pixels'),out.get('error')
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as ex:
 for a in ex.map(run,rows):print(a,flush=True)



