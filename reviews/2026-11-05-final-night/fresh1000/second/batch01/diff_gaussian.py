import json,numpy as np
from pathlib import Path
from astropy.io import fits
from astropy.wcs import WCS
from scipy.optimize import least_squares
b=Path(__file__).resolve().parent
for tic in ['240615841','258216510','241100642','272726082','280692653']:
 d=b/tic;l=json.loads((d/'helper-localization.json').read_text());e=l['event'];c=e['center_btjd'];dur=e['duration_d']
 with fits.open(d/'helper-tesscut.fits') as h:
  a=h[1].data;t=np.array(a['TIME']);cube=np.array(a['FLUX']);q=np.array(a['QUALITY']);w=WCS(h[2].header)
 g=(q==0);core=g&(abs(t-c)<dur*.25);side=g&(abs(t-c)>dur*.75)&(abs(t-c)<dur*2);z=np.nanmedian(cube[side],axis=0)-np.nanmedian(cube[core],axis=0);yy,xx=np.indices(z.shape)
 def fun(v):
  amp,x,y,s,bg=v;return (amp*np.exp(-((xx-x)**2+(yy-y)**2)/(2*s*s))+bg-z).ravel()
 iy,ix=np.unravel_index(np.argmax(z),z.shape);f=least_squares(fun,[z.max(),ix,iy,1,0],bounds=([0,0,0,.3,-np.inf],[np.inf,10,10,3,np.inf]));v=f.x;sky=w.pixel_to_world_values(v[1],v[2]);o={'gaussian_xy':v[1:3].tolist(),'sigma_pixels':v[3],'sky_radec':[float(x) for x in sky],'target_offset_pixels':float(np.linalg.norm(v[1:3]-l['target_xy'])),'fit_rms':float(np.std(fun(v)))};(d/'lead-diff-gaussian.json').write_text(json.dumps(o,indent=2));print(tic,o)
