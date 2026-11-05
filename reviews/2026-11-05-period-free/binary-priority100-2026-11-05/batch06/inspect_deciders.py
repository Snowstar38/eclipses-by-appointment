"""Actual target pixel coverage for the three deciding ambiguous raw windows."""
import hashlib,json
from pathlib import Path
import numpy as np
from astropy.io import fits
from astropy.wcs import WCS
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
B=Path(__file__).resolve().parent
cases=[('417309915',359.8873146380807,56.88765626700866,24,1969.36),('51255152',128.50628283033708,-8.13219430194474,99,4068.53),('405542204',256.82000732240635,40.053531927939915,25,2006.41)]
for tic,ra,dec,sec,c in cases:
 o=B/tic;fp=next(o.glob('*astrocut.fits'))
 with fits.open(fp,memmap=False) as h:
  a=h[1].data;t=np.asarray(a['TIME'],float);q=np.asarray(a['QUALITY'],int);cube=np.asarray(a['FLUX'],float);xy=WCS(h[2].header).world_to_pixel_values(ra,dec)
 xi=int(round(float(xy[0])));yi=int(round(float(xy[1])))
 good=(q==0)&np.isfinite(t)&np.isfinite(cube[:,yi,xi]);t=t[good];cube=cube[good]
 target=cube[:,yi,xi];ap3=cube[:,max(0,yi-1):yi+2,max(0,xi-1):xi+2].sum(axis=(1,2));ap5=cube.sum(axis=(1,2))
 fig,axs=plt.subplots(3,1,figsize=(11,8))
 for ax,name,v in zip(axs,('target pixel','3x3','5x5'),(target,ap3,ap5)):
  ax.plot(t,v/np.nanmedian(v),'.',ms=2);ax.axvline(c,color='red');ax.set_title(name);ax.set_xlim(c-8,c+8)
 fig.tight_layout();fig.savefig(o/'deciding-pixels.png',dpi=140);plt.close(fig)
 vals={'path':str(fp),'sha256':hashlib.sha256(fp.read_bytes()).hexdigest(),'target_wcs_zero_based_xy':[float(v) for v in xy],'n_quality0':int(sum(good)),'median_target_pixel_flux':float(np.nanmedian(target)),'median_pixel_grid':np.nanmedian(cube,axis=0).tolist(),'note':'Raw TESSCut pixels, same photons as QLP; target-centered 1x1,3x3,5x5, no local background correction. Plot is morphology check, not calibrated photometry.'}
 (o/'deciding-pixels.json').write_text(json.dumps(vals,indent=2)+'\n',encoding='utf-8')
 print(tic,vals['target_wcs_zero_based_xy'],vals['median_target_pixel_flux'])
