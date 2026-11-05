"""Independent pixel extraction and phase difference for the T057 short trial clock."""
import hashlib,json
from pathlib import Path
import numpy as np
from astropy.io import fits
from astropy.wcs import WCS
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
B=Path(__file__).resolve().parent
fp=next(B.glob('*0009*astrocut.fits'))
with fits.open(fp,memmap=False) as h:
 a=h[1].data;t=np.asarray(a['TIME'],float);q=np.asarray(a['QUALITY'],int);cube=np.asarray(a['FLUX'],float);w=WCS(h[2].header)
 xy=w.world_to_pixel_values(144.7027809786175,-49.51336098047716)
good=(q==0)&np.isfinite(t)&np.all(np.isfinite(cube),axis=(1,2))
t=t[good];cube=cube[good]
P=.3753022026165229;t0=1554.910;phase=((t-t0)/P+.5)%1-.5
ap={'1x1':cube[:,2,3], '3x3':cube[:,1:4,2:5].sum(axis=(1,2)), '5x5':cube.sum(axis=(1,2))}
fig,ax=plt.subplots(3,1,figsize=(10,9))
for a0,(name,flux) in zip(ax,ap.items()):
 y=flux/np.median(flux);a0.plot(phase,y,'.',ms=3);a0.set_title(name);a0.set_xlim(-.5,.5);a0.set_ylabel('flux / median')
fig.tight_layout();fig.savefig(B/'s09-pixel-fold.png',dpi=140);plt.close(fig)
inside=(abs(phase)<.08);outer=(abs(phase)>.25)&(abs(phase)<.45)
diff=np.median(cube[outer],axis=0)-np.median(cube[inside],axis=0)
fig,ax=plt.subplots(figsize=(6,5));im=ax.imshow(diff,origin='lower',cmap='coolwarm');ax.plot(xy[0],xy[1],'k+',ms=14);fig.colorbar(im,ax=ax,label='out minus in counts');fig.tight_layout();fig.savefig(B/'s09-pixel-difference.png',dpi=140);plt.close(fig)
out={'path':str(fp),'sha256':hashlib.sha256(fp.read_bytes()).hexdigest(),'n_good':int(sum(good)),'target_wcs_zero_based_xy':[float(v) for v in xy],'phase_trial_period_days':P,'phase_epoch_btjd':t0,'n_in':int(sum(inside)),'n_out':int(sum(outer)),'median_flux_grid':np.median(cube,axis=0).tolist(),'median_difference_grid':diff.tolist(),'central_target_pixel_out_minus_in':float(diff[2,3]),'aperture_relative_phase_loss_ppt':{name:float(1000*(1-np.median(v[inside])/np.median(v[outer]))) for name,v in ap.items()},'caution':'Same TESS photons as QLP; different extraction. Broad phase bins and local background not calibrated. Difference is not a source localization likelihood.'}
(B/'s09-pixels.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(out['aperture_relative_phase_loss_ppt'],out['central_target_pixel_out_minus_in'])
