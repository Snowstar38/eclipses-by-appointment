from pathlib import Path
import numpy as np,json,csv,hashlib
from astropy.io import fits
from astropy.wcs import WCS
B=Path(__file__).parent;rows=list(csv.DictReader((B/'queue.csv').open()));out=[]
for r in rows[2:6]:
 p=B/r['tic'];rec=json.loads(next(p.glob('helper-s*-receipt.json')).read_text());f=next(p.glob('helper-s*-tesscut.fits'));e=rec['event'];c=e['screen_btjd'];d=e['screen_duration_days']
 with fits.open(f,memmap=False) as h:
  a=h[1].data;t=np.asarray(a['TIME']);q=np.asarray(a['QUALITY']);flux=np.asarray(a['FLUX']);w=WCS(h[2].header);x,y=w.all_world2pix(float(r['ra_deg']),float(r['dec_deg']),0)
 good=(q==0)&np.isfinite(t);core=good&(abs(t-c)<min(d*.18,.07));side=good&(abs(t-c)>max(d*.8,.35))&(abs(t-c)<max(d*1.6,.8));diff=np.nanmedian(flux[side],axis=0)-np.nanmedian(flux[core],axis=0);yy,xx=np.indices(diff.shape);sel=(np.abs(xx-round(float(x)))<=2)&(np.abs(yy-round(float(y)))<=2)&np.isfinite(diff);z=diff[sel];xx=xx[sel];yy=yy[sel];tot=np.sum(z);cx=np.sum(xx*z)/tot;cy=np.sum(yy*z)/tot
 out.append(dict(sample_id=r['sample_id'],center=c,difference_flux_sum=float(tot),difference_flux_centroid_xy=[float(cx),float(cy)],target_xy=[float(x),float(y)],caution='5x5 signed difference moment; no PRF model or uncertainty; saturation and background gradients may bias; not unique attribution',source_sha256=hashlib.sha256(f.read_bytes()).hexdigest()))
 print(r['sample_id'],round(cx,3),round(cy,3),flush=True)
(B/'helper-moments.json').write_text(json.dumps(out,indent=2))
