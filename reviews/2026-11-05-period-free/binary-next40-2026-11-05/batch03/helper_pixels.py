from pathlib import Path
import numpy as np,json,hashlib
from astropy.io import fits
from astropy.wcs import WCS
from astropy.timeseries import BoxLeastSquares
import matplotlib;matplotlib.use('Agg')
import matplotlib.pyplot as plt
p=Path('batch03/288649491/helper-tesscut-s034.fits')
with fits.open(p) as h:
 t=np.array(h[1].data['TIME']); F=np.array(h[1].data['FLUX']);q=np.array(h[1].data['QUALITY']);w=WCS(h[2].header)
g=np.isfinite(t)&(q==0)&np.isfinite(F).all(axis=(1,2));t=t[g];F=F[g]; bg=np.median(F[:,[0,0,-1,-1],[0,-1,0,-1]],axis=1); F=F-bg[:,None,None]
print('median positive',np.median(F[:,5,5]),'background',np.median(bg),'n',len(t)); tx,ty=w.all_world2pix(114.56091667734572,-16.39317626748244,0); nx,ny=w.all_world2pix(114.56257,-16.38967,0);print('pixels',tx,ty,nx,ny)
f=F[:,4:7,4:7].sum(axis=(1,2)); f/=np.median(f); bls=BoxLeastSquares(t,f).power(np.linspace(.538,.542,3000),[.04,.06,.08,.10,.12]);i=np.argmax(bls.power);P=float(bls.period[i]);epoch=float(bls.transit_time[i]);print('fit',P,epoch,bls.duration[i]);phase=((t-epoch+P/2)%P-P/2); inside=np.abs(phase)<.04;outside=(np.abs(phase)>.13)&(np.abs(phase)<.23); O=np.median(F[outside],axis=0); D=O-np.median(F[inside],axis=0);print('counts',inside.sum(),outside.sum());
# fit difference to shifted mean PRF templates: target image represents target-dominated PSF, interpolate
from scipy.ndimage import shift
from scipy.optimize import nnls
Y,X=np.indices(O.shape); mask=(X>=2)&(X<=8)&(Y>=2)&(Y<=8); templ=np.clip(O,0,None); templ[~mask]=0; templ=templ/templ.sum(); shifted=shift(templ,(ny-ty,nx-tx),order=3,mode='constant'); A=np.array([templ[mask],shifted[mask],np.ones(mask.sum())]).T; coef=np.linalg.lstsq(A,D[mask],rcond=None)[0]; print('coeff target,neighbor,bg',coef)
fig,ax=plt.subplots(1,3,figsize=(12,4));ax[0].imshow(O,origin='lower');ax[1].imshow(D,origin='lower');ax[2].plot(phase,f,'.',ms=1,alpha=.4);ax[2].set_xlabel('phase days');
for a in ax[:2]:a.plot(tx,ty,'r+',ms=12,label='target');a.plot(nx,ny,'cx',ms=12,label='VSX');a.legend();
fig.tight_layout();fig.savefig('batch03/288649491/helper-pixels.png',dpi=130)
out={'fits_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'period_local_days':P,'epoch_btjd':epoch,'target_xy':[float(tx),float(ty)],'vsx_xy':[float(nx),float(ny)],'n_in':int(inside.sum()),'n_out':int(outside.sum()),'background_median':float(np.median(bg)),'target_pixel_median_sky_subtracted':float(np.median(F[:,5,5])),'coefficients_target_neighbor_background':coef.tolist(),'caveat':'simple shifted empirical template, blended PSF and unmodeled neighbor; same photons, not independent observing occasion'}
Path('batch03/288649491/helper-pixels.json').write_text(json.dumps(out,indent=2))
