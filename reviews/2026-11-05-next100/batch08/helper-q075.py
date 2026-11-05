import numpy as np,io,zipfile,json
from pathlib import Path
from astropy.io import fits
from astropy.wcs import WCS
b=Path(__file__).parent;p=b/'72497715/helper-tesscut-s99.zip';z=zipfile.ZipFile(p);h=fits.open(io.BytesIO(z.read(z.namelist()[0]))); a=h[1].data;t=np.array(a['TIME']);f=np.array(a['FLUX']);q=np.array(a['QUALITY']);w=WCS(h[2].header);x,y=w.all_world2pix(187.4382754243,-45.6950742162,0); yy,xx=np.indices((11,11));out=[]
for ep in [4053.25,4068.06]:
 d=np.abs(t-ep);good=np.isfinite(t)&(q==0);inside=good&(d<.15);outside=good&(d>.5)&(d<1.2);diff=np.nanmedian(f[outside],axis=0)-np.nanmedian(f[inside],axis=0);bg=np.nanmedian(diff[(xx<2)|(xx>8)|(yy<2)|(yy>8)]);pos=np.maximum(diff-bg,0);pos[(xx<2)|(xx>8)|(yy<2)|(yy>8)]=0;cen=[float((pos*xx).sum()/pos.sum()),float((pos*yy).sum()/pos.sum())];peak=np.unravel_index(np.nanargmax(diff),diff.shape);out.append({'center':ep,'target_xy':[float(x),float(y)],'centroid':cen,'peak_xy':[int(peak[1]),int(peak[0])],'inside':int(inside.sum()),'outside':int(outside.sum()),'peak_diff':float(np.nanmax(diff)),'background':float(bg)});np.savetxt(b/'72497715'/f'helper-diff-{ep}.csv',diff,delimiter=',')
(b/'72497715/helper-numeric.json').write_text(json.dumps(out,indent=2));print(out)
