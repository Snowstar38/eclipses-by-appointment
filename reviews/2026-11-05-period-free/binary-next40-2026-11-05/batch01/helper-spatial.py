import json,csv,hashlib
from pathlib import Path
import numpy as np
from astropy.io import fits
from astropy.wcs import WCS
import matplotlib;matplotlib.use('Agg')
import matplotlib.pyplot as plt
B=Path(__file__).resolve().parent;Q={r['tic']:r for r in csv.DictReader((B/'queue.csv').open())};out=[]
for e in json.loads((B/'helper-fetch.json').read_text()):
 tic=e['tic']; row=Q[tic]; tm=e['time']; d=e['duration']; fp=B/f'helper-{tic}-tesscut.fits'; o={'tic':tic,'sample_id':row['sample_id'],'sector':e['sector'],'screen_btjd':tm,'duration':d}
 if not fp.exists():o['error']=e.get('error');out.append(o);continue
 with fits.open(fp,memmap=False) as h:
  t=np.asarray(h[1].data['TIME'],float);f=np.asarray(h[1].data['FLUX'],float);q=np.asarray(h[1].data['QUALITY'],int);w=WCS(h[2].header)
 good=np.isfinite(t)&(q==0)&np.isfinite(f).all(axis=(1,2));t=t[good];f=f[good];x=t-tm;core=abs(x)<d*.35;pre=(x<-.65*d)&(x>-1.3*d);post=(x>.65*d)&(x<1.3*d);o['counts']=[int(core.sum()),int(pre.sum()),int(post.sum())];o['fits_sha256']=hashlib.sha256(fp.read_bytes()).hexdigest()
 tx,ty=map(float,w.all_world2pix(float(row['ra_deg']),float(row['dec_deg']),0));o['target_pixel']=[tx,ty]; yy,xx=np.indices(f.shape[1:]); mask=(abs(xx-round(tx))<=1)&(abs(yy-round(ty))<=1); sky=((xx<2)|(xx>8)|(yy<2)|(yy>8)); med=np.median(f,axis=0);o['median_target_sum']=float(np.sum(med[mask]));o['median_sky_min']=float(np.min(med[sky]));o['zero_or_negative_sky_pixels']=int(np.sum(med[sky]<=0));o['valid_pixel_data']=bool(o['median_target_sum']>0 and o['zero_or_negative_sky_pixels']==0 and mask.sum()==9)
 if min(o['counts'])>=2 and o['valid_pixel_data']:
  bg=np.median(f[:,sky],axis=1);f=f-bg[:,None,None];base=.5*(np.median(f[pre],axis=0)+np.median(f[post],axis=0));dif=base-np.median(f[core],axis=0);local=(abs(xx-round(tx))<=2)&(abs(yy-round(ty))<=2);v=np.clip(dif,0,None)*local; s=v.sum();cx=float((v*xx).sum()/s) if s>0 else None;cy=float((v*yy).sum()/s) if s>0 else None;bs=float(base[mask].sum());ds=float(dif[mask].sum());o.update(diff_centroid=[cx,cy],base_ap3=bs,difference_ap3=ds,depth_ppt=1000*ds/bs if bs>0 else None)
  fig,ax=plt.subplots(1,2,figsize=(9,4));
  for a,img,title in zip(ax,[base,dif],['out of event','out minus in']):a.imshow(img,origin='lower');a.plot(tx,ty,'r+',ms=12);a.set_title(title)
  if cx is not None:ax[1].plot(cx,cy,'mo',mfc='none')
  fig.suptitle(f'{row["sample_id"]} TIC {tic} S{e["sector"]}, screening {tm:.4f}');fig.tight_layout();fig.savefig(B/f'helper-{tic}-difference.png',dpi=110);plt.close(fig)
 out.append(o);print(o,flush=True)
(B/'helper-spatial.json').write_text(json.dumps(out,indent=2,allow_nan=False))
