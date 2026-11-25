"""Read local SPOC TPF and characterize temporal difference images. Usage: python inspect_stamp.py CONFIG.json OUTPUT_DIR."""
import sys,json,pathlib,hashlib
import numpy as np
from astropy.io import fits
from astropy.wcs import WCS
from astropy.time import Time
import matplotlib;matplotlib.use('Agg')
import matplotlib.pyplot as plt
p=pathlib.Path(sys.argv[1]);config=json.loads(p.read_text());out=pathlib.Path(sys.argv[2]);out.mkdir(parents=True,exist_ok=True)
with fits.open(config['tpf'],memmap=True) as h:
 d=h[1].data;t=d['TIME'];q=d['QUALITY'];corr=d['TIMECORR'];flux=d['FLUX'];bkg=d['FLUX_BKG'];mask=(h[2].data&2)!=0;w=WCS(h[2].header);ref=h[1].header.get('BJDREFI',2457000)+h[1].header.get('BJDREFF',0)
 good=(q==0)&np.isfinite(t);center=config['center_btjd'];off=abs(t-center);limits=config.get('baseline_offsets_d',[.15,.3]);baseline=good&(off>limits[0])&(off<limits[1]);quiet=np.nanmedian(flux[baseline]+bkg[baseline],axis=0);baseflux=np.nanmedian(flux[baseline],axis=0);basebkg=np.nanmedian(bkg[baseline],axis=0)
 if baseline.sum()<10: raise ValueError('Insufficient quality-zero baseline')
 frames=[];fig,axes=plt.subplots(2,5,figsize=(15,6));
 for ax1,ax2,dh in zip(axes[0],axes[1],[-1,-.5,0,.5,1]):
  ind=good&(abs((t-center)*24-dh)<.075); raw=(flux+bkg)[ind]; dif=np.nanmedian(raw,axis=0)-quiet
  if not ind.any() or not np.isfinite(dif).any():
   frames.append({'offset_h':dh,'status':'no valid samples'});continue
  yp,xp=np.unravel_index(np.nanargmax(dif),dif.shape);yn,xn=np.unravel_index(np.nanargmin(dif),dif.shape);ra,dec=w.pixel_to_world_values(xp,yp);jd=np.median(t[ind]-corr[ind])+ref;utc=Time(jd,format='jd',scale='tdb').utc.isot
  frames.append(dict(offset_h=dh,n=int(ind.sum()),utc=utc,ra_deg=float(ra),dec_deg=float(dec),peak_x=int(xp),peak_y=int(yp),peak_excess=float(dif[yp,xp]),loss_x=int(xn),loss_y=int(yn),ap_flux_delta=float(np.nansum(np.nanmedian(flux[ind],axis=0)[mask]-baseflux[mask])),ap_bkg_delta=float(np.nansum(np.nanmedian(bkg[ind],axis=0)[mask]-basebkg[mask]))))
  for ax,im,title in [(ax1,dif,'FLUX + BKG excess'),(ax2,np.nanmedian(flux[ind],axis=0)-baseflux,'FLUX difference')]:
   mx=np.nanmax(abs(im));ax.imshow(im,origin='lower',cmap='coolwarm',vmin=-mx,vmax=mx);ax.contour(mask.astype(float),levels=[.5],colors='yellow',linewidths=.6);ax.plot(xp,yp,'gx',ms=7);ax.set_title(f'{dh:+.1f}h {title}',fontsize=8)
 fig.suptitle(f"TIC {config['tic']} sector {config['sector']}: baseline-subtracted target stamp");fig.tight_layout();fig.savefig(out/'diagnostic.png',dpi=150)
 def native(a):
  if isinstance(a,np.generic):return a.item()
  raise TypeError
 evidence=dict(config=config,sha256=hashlib.sha256(pathlib.Path(config['tpf']).read_bytes()).hexdigest(),camera=h[0].header.get('CAMERA'),ccd=h[0].header.get('CCD'),baseline_n=int(baseline.sum()),aperture_pixels=int(mask.sum()),frames=frames,limitations='Peak sky positions are integer pixel coordinates in TPF WCS (~21 arcsec per pixel), spacecraft UTC, no centroid error/observer parallax. Raw FLUX+BKG restores estimated background, not independent calibrated FFI; quality mask and time-window medians apply.')
 (out/'evidence.json').write_text(json.dumps(evidence,indent=2,default=native));print(json.dumps(frames,indent=2))
