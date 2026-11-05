from pathlib import Path
import numpy as np,json,csv,hashlib
from astropy.io import fits
from astropy.wcs import WCS
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
B=Path(__file__).parent; rows=list(csv.DictReader((B/'queue.csv').open())); neighbors=json.loads((B.parent/'shared-catalogues/gaia-neighbors.json').read_text())['targets'];out=[]
for r in [x for x in rows if x['sample_id']=='T088']:
 p=B/r['tic'];rec=json.loads((p/'helper-s77-receipt.json').read_text());f=(p/'helper-s77-tesscut.fits');e=rec['event'];center=e.get('fit_mid_btjd',e['screen_btjd']);dur=e.get('fit_duration_days',e['screen_duration_days']);
 with fits.open(f,memmap=False) as h:
  d=h[1].data;t=np.asarray(d['TIME']);q=np.asarray(d['QUALITY']);flux=np.asarray(d['FLUX']);w=WCS(h[2].header);x,y=w.all_world2pix(float(r['ra_deg']),float(r['dec_deg']),0)
 x,y=float(x),float(y);ix,iy=round(x),round(y);med=np.nanmedian(flux[q==0],axis=0);yy,xx=np.indices(med.shape);sky=(np.hypot(xx-x,yy-y)>3)&(med>0)&np.isfinite(med);bg=np.nanmedian(np.where(flux[:,sky]>0,flux[:,sky],np.nan),axis=1);ap=flux[:,iy-1:iy+2,ix-1:ix+2].sum(axis=(1,2))-9*bg;g=(q==0)&np.isfinite(t)&np.isfinite(ap);core=g&(abs(t-center)<min(dur*.18,.07));side=g&(abs(t-center)>max(dur*.8,.35))&(abs(t-center)<max(dur*1.6,.8));diff=np.nanmedian(flux[side],axis=0)-np.nanmedian(flux[core],axis=0); peak=np.unravel_index(np.nanargmax(diff),diff.shape); norm=np.nanmedian(ap[side]);depth=1-np.nanmedian(ap[core])/norm
 ns=[]
 for n in neighbors[r['sample_id']]:
  if n['is_queue_gaia_source'] or not n['phot_g_mean_mag']:continue
  nx,ny=w.all_world2pix(float(n['ra']),float(n['dec']),0);ratio=10**(-.4*(float(n['phot_g_mean_mag'])-float(r['gaia_G'])));ns.append(dict(source_id=n['source_id'],separation_arcsec=n['separation_arcsec'],gmag=float(n['phot_g_mean_mag']),flux_ratio_to_target=ratio,xy=[float(nx),float(ny)]))
 capable=[n for n in ns if n['flux_ratio_to_target']>=depth];capable.sort(key=lambda n:n['separation_arcsec'])
 fig,ax=plt.subplots(1,2,figsize=(10,4));ax[0].imshow(diff,origin='lower',cmap='magma');ax[0].scatter([x],[y],marker='+',color='cyan',s=120);ax[0].scatter([peak[1]],[peak[0]],marker='x',color='lime');ax[0].set_title('out - in; cyan target, green peak');ax[1].plot(t[g],ap[g]/norm,'.',ms=1);ax[1].axvline(center,color='r');ax[1].set_xlim(center-1,center+1);ax[1].set_title('independent sky-corrected 3x3');fig.suptitle(r['sample_id']);fig.tight_layout();fig.savefig(p/'helper-s77-difference.png',dpi=110);plt.close(fig)
 item=dict(sample_id=r['sample_id'],sector=e['sector'],center=center,core_count=int(core.sum()),baseline_count=int(side.sum()),target_xy=[float(x),float(y)],target_pixel_median=float(med[iy,ix]),zero_pixels=int((med==0).sum()),valid_sky_pixels=int(sky.sum()),background_median=float(np.nanmedian(bg[side])),aperture_baseline=float(norm),independent_aperture_depth_ppt=float(depth*1000),difference_peak_xy=[int(peak[1]),int(peak[0])],peak_to_target_pixels=float(np.hypot(peak[1]-x,peak[0]-y)),capable_gaia_neighbors=capable,cutout_sha256=hashlib.sha256(f.read_bytes()).hexdigest(),neighbors_sha256=hashlib.sha256((B.parent/'shared-catalogues/gaia-neighbors.json').read_bytes()).hexdigest());out.append(item);print(r['sample_id'],round(depth*1000,1),'xy',round(x,2),round(y,2),'peak',peak[::-1],'sky',int(sky.sum()),'capable',[(n['separation_arcsec'],round(n['flux_ratio_to_target'],2)) for n in capable],flush=True)
(B/'helper-s77-pixel-audit.json').write_text(json.dumps(out,indent=2,allow_nan=False))




