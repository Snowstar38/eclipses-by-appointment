import json,hashlib
from pathlib import Path
import numpy as np
from astropy.io import fits
from astropy.wcs import WCS
B=Path(__file__).resolve().parent
jobs=[('295176393',39,270.34925752923124,-69.60515069877758,[2365.9714]),('341419787',7,120.15339783069679,-54.50900340546292,[1493.4364,1514.5080]),('341419787',61,120.15339783069679,-54.50900340546292,[2968.28])]
out=[]
for tic,s,ra,dec,events in jobs:
 p=B/f'helper-{tic}-s{s:03d}-cutout.fits'
 with fits.open(p) as h:
  a=h[1].data;t=np.array(a['TIME'],float);F=np.array(a['FLUX'],float);q=np.array(a['QUALITY']);w=WCS(h[2].header);x,y=w.all_world2pix(ra,dec,0);hdr=h[0].header.get('SECTOR')
 ok=np.isfinite(t)&np.all(np.isfinite(F.reshape(len(t),-1)),axis=1)&(q==0);t=t[ok];F=F[ok]; sky=np.median(np.sort(F.reshape(len(t),-1),axis=1)[:,:35],axis=1);F=F-sky[:,None,None]; zs=[];os=[]; ev=[]
 for c in events:
  a=np.abs(t-c)<.035; b=(np.abs(t-c)>.12)&(np.abs(t-c)<.3)
  o=np.median(F[b],axis=0); z=o-np.median(F[a],axis=0);os.append(o);zs.append(z);ev.append({'center':c,'in':int(a.sum()),'out':int(b.sum())})
 O=np.mean(os,axis=0);Z=np.mean(zs,axis=0);xx,yy=np.meshgrid(np.arange(11),np.arange(11)); ix=int(round(float(x)));iy=int(round(float(y)));mask=(abs(xx-ix)<=2)&(abs(yy-iy)<=2);v=np.maximum(Z,0)*mask;cx=(v*xx).sum()/v.sum();cy=(v*yy).sum()/v.sum();m3=(abs(xx-ix)<=1)&(abs(yy-iy)<=1)
 np.savez_compressed(B/f'helper-{tic}-s{s:03d}-pixels.npz',baseline=O,deficit=Z)
 out.append(dict(tic=tic,sector=s,sector_header=hdr,sha256=hashlib.sha256(p.read_bytes()).hexdigest(),target_xy=[float(x),float(y)],centroid_xy=[float(cx),float(cy)],centroid_offset_arcsec=float(np.hypot(cx-x,cy-y)*21),peak_xy=list(map(int,np.unravel_index(np.argmax(Z),Z.shape)[::-1])),depth_3x3=float(Z[m3].sum()/O[m3].sum()),baseline_3x3=float(O[m3].sum()),events=ev,sky_median=float(np.median(sky)),note='clipped centroid in 5x5 is biased, no uncertainty; same photons'))
(B/'helper-pixel-results.json').write_text(json.dumps(out,indent=2));print(json.dumps(out,indent=2))
