import pathlib,json,csv,numpy as np
from astropy.io import fits
from astropy.wcs import WCS
from astropy.time import Time
from scipy.optimize import least_squares
import matplotlib;matplotlib.use('Agg')
import matplotlib.pyplot as plt
import argparse
parser = argparse.ArgumentParser(description="Fit the moving excess near the stamp edge peaks in the wider TESScut image.")
parser.add_argument("fits", type=pathlib.Path, help="Sector 108, 35 by 35 pixel cutout as retrieved by wide_track.py")
f = parser.parse_args().fits
out = pathlib.Path(__file__).resolve().parent
ev = json.loads((out/'evidence.json').read_text())
with fits.open(f,memmap=True) as h:
 d=h[1].data;t=d['TIME'];q=d['QUALITY'];cc=d['TIMECORR']; ref=h[1].header.get('BJDREFI',2457000)+h[1].header.get('BJDREFF',0);cube=d['FLUX'];w=WCS(h[2].header);c=4312.17265243838;good=(q==0)&np.isfinite(t);baseline=good&(abs(t-c)>.15)&(abs(t-c)<.28);base=np.nanmedian(cube[baseline],axis=0);print('baseline',baseline.sum());fig,axes=plt.subplots(1,5,figsize=(16,4));rows=[]
 for ax,fr in zip(axes,ev['frames']):
  ix=np.where(good)[0];i=ix[np.argmin(abs(t[ix]-(c+fr['offset_h']/24)))];diff=cube[i]-base;ex,ey=w.world_to_pixel_values(fr['ra_deg'],fr['dec_deg']);ex=float(ex);ey=float(ey);xc=int(round(ex));yc=int(round(ey));lo=max(0,xc-5);hi=min(35,xc+6);bot=max(0,yc-5);top=min(35,yc+6);arr=diff[bot:top,lo:hi];Y,X=np.indices(arr.shape);X=X+lo;Y=Y+bot;ij=np.unravel_index(np.nanargmax(arr),arr.shape);init=[max(float(np.nanmax(arr)),1),float(X[ij]),float(Y[ij]),1,0]
  def residual(v):
   A,x,y,s,b=v;return np.nan_to_num(A*np.exp(-((X-x)**2+(Y-y)**2)/(2*s*s))+b-arr,nan=0).ravel()
  r=least_squares(residual,init,bounds=([0,lo-1,bot-1,.3,-np.inf],[np.inf,hi,top,5,np.inf]));A,x,y,s,b=r.x;ra,dec=w.pixel_to_world_values(x,y);utc=Time(t[i]-cc[i]+ref,format='jd',scale='tdb').utc.isot;rows.append(dict(offset_h=fr['offset_h'],utc=utc,ra_deg=float(ra),dec_deg=float(dec),x=float(x),y=float(y),sigma_pixel=float(s),amplitude=float(A),quality=int(q[i]),ffi_file=str(d['FFI_FILE'][i])));ax.imshow(diff,origin='lower',cmap='viridis',vmin=np.nanpercentile(diff,20),vmax=np.nanpercentile(diff,99.5));ax.plot(x,y,'r+');ax.set_xlim(x-4,x+4);ax.set_ylim(y-4,y+4);ax.set_title(utc[11:19])
 fig.suptitle('S108 FFI: moving excess, Gaussian centroids');fig.tight_layout();fig.savefig(out/'wide-ffi.png',dpi=160)
with (out/'wide-positions.csv').open('w',newline='') as f:
 writer=csv.DictWriter(f,rows[0].keys());writer.writeheader();writer.writerows(rows)
print(rows)
