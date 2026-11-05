import numpy as np,json,zipfile,io,hashlib,csv
from astropy.io import fits
from astropy.wcs import WCS
from pathlib import Path
b=Path(__file__).parent
jobs=[('270523058',1692.1553728,.641,293.377317531,44.016573595,.05,.16),('295351347',1620.1610088,.692,223.303175993,-61.30028071,.05,.18),('280051953',1663.320493,None,45.670362515,-73.549193591,.35,1.2)]
out=[]
for tic,ep,period,ra,dec,core,base in jobs:
 p=next((b/tic).glob('helper-tesscut*.zip'));z=zipfile.ZipFile(p);h=fits.open(io.BytesIO(z.read(z.namelist()[0]))); a=h[1].data; t=np.array(a['TIME']); f=np.array(a['FLUX']);q=np.array(a['QUALITY']);w=WCS(h[2].header);x,y=w.all_world2pix(ra,dec,0)
 d=(t-ep+period/2)%period-period/2 if period else t-ep
 good=np.isfinite(t)&(q==0); inside=good&(np.abs(d)<core); outside=good&(np.abs(d)>base)&(np.abs(d)<(period/2 if period else 2.5));diff=np.nanmedian(f[outside],axis=0)-np.nanmedian(f[inside],axis=0)
 yy,xx=np.indices(diff.shape); bg=np.nanmedian(diff[(xx<2)|(xx>8)|(yy<2)|(yy>8)]);pos=np.maximum(diff-bg,0);pos[(xx<2)|(xx>8)|(yy<2)|(yy>8)]=0
 centroid=[float((pos*xx).sum()/pos.sum()),float((pos*yy).sum()/pos.sum())];peak=np.unravel_index(np.nanargmax(diff),diff.shape)
 o={'tic':tic,'target_xy':[float(x),float(y)],'centroid_positive_7x7':centroid,'peak_xy':[int(peak[1]),int(peak[0])],'inside':int(inside.sum()),'outside':int(outside.sum()),'diff_background':float(bg),'peak_diff':float(np.nanmax(diff)),'difference_image':diff.tolist(),'time_min':float(np.nanmin(t[good])),'time_max':float(np.nanmax(t[good])),'source_sha256':hashlib.sha256(p.read_bytes()).hexdigest()};out.append(o)
 np.savetxt(b/tic/'helper-difference.csv',diff,delimiter=',')
print(json.dumps(out,indent=2));(b/'helper-numeric.json').write_text(json.dumps(out,indent=2))
