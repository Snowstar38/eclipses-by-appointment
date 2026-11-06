import json,numpy as np
from pathlib import Path
from astropy.io import fits
from astropy.wcs import WCS
import matplotlib;matplotlib.use('Agg')
import matplotlib.pyplot as plt
b=Path(__file__).resolve().parent;d=b/'48099288';c=4313.440381225984;dur=.13524
ctx=json.loads((d/'lead-context.json').read_text()); h=ctx['sectors'][0]['header'];ra,dec=h['RA_OBJ'],h['DEC_OBJ']
with fits.open(d/'extra-s108.fits') as f:
 t=np.array(f[1].data['TIME']);q=np.array(f[1].data['QUALITY']);cube=np.array(f[1].data['FLUX']);w=WCS(f[2].header);x,y=w.world_to_pixel_values(ra,dec);x=float(x);y=float(y)
g=(q==0)&np.isfinite(t)&(abs(t-c)<.5); core=g&(abs(t-c)<dur*.25);side=g&(abs(t-c)>dur*.75)&(abs(t-c)<.4)
# remove each pixel's local linear trend before differencing
z=t-c; slopes=np.zeros(cube.shape[1:]);inter=slopes.copy();diff=slopes.copy()
for iy in range(cube.shape[1]):
 for ix in range(cube.shape[2]):
  v=cube[:,iy,ix];ok=side&np.isfinite(v); p=np.polyfit(z[ok],v[ok],1);slopes[iy,ix],inter[iy,ix]=p;diff[iy,ix]=np.nanmedian((p[0]*z+p[1]-v)[core])
yy,xx=np.indices(diff.shape);wt=np.maximum(diff,0);cent=[float((wt*xx).sum()/wt.sum()),float((wt*yy).sum()/wt.sum())];peak=np.unravel_index(np.nanargmax(diff),diff.shape)
ap=(abs(xx-round(x))<=1)&(abs(yy-round(y))<=1); flux=np.nansum(cube[:,ap],axis=1); p=np.polyfit(z[side],flux[side],1); norm=flux/(p[0]*z+p[1]);loss=1-np.nanmedian(norm[core]);neighbors=json.loads((d/'lead-neighbors.json').read_text())['neighbors']; mapped=[]
for n in neighbors:
 nx,ny=w.world_to_pixel_values(float(n['ra']),float(n['dec'])); dist=float(np.hypot(nx-x,ny-y))
 if dist<3: mapped.append(dict(source_id=n['source_id'],mag=n['phot_g_mean_mag'],xy=[float(nx),float(ny)],target_distance=dist,relative_G_flux=n['relative_G_flux']))
out=dict(target_xy=[float(x),float(y)],centroid=cent,offset=float(np.hypot(cent[0]-x,cent[1]-y)),peak_xy=[int(peak[1]),int(peak[0])],core_n=int(core.sum()),side_n=int(side.sum()),detrended_3x3_loss=float(loss),neighbors=sorted(mapped,key=lambda a:a['target_distance']))
(d/'audit-s108-spatial.json').write_text(json.dumps(out,indent=2));fig,ax=plt.subplots(1,2,figsize=(10,4));ax[0].imshow(diff,origin='lower',cmap='coolwarm');ax[0].plot(x,y,'wx',ms=10);ax[0].plot(*cent,'g+',ms=10);ax[1].plot(z[g],norm[g],'.');ax[1].axvspan(-dur*.25,dur*.25,alpha=.2,color='r');fig.tight_layout();fig.savefig(d/'audit-s108-spatial.png');print(json.dumps(out,indent=2))

