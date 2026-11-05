import json, math, numpy as np
from pathlib import Path
from astropy.io import fits
from astropy.wcs import WCS
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
B=Path(__file__).resolve().parent;tic='449012335';h=B/'helper-pixels'/tic;g=json.loads((B/'SOURCE-SNAPSHOT.json').read_text())[tic]['target']['gaia']; n=next(x for x in json.loads((B/'helper-pixels/final-neighbors.json').read_text()) if x['tic']==tic)
with fits.open(h/'tesscut.fits',memmap=False) as f:t=np.array(f[1].data['TIME'],float);F=np.array(f[1].data['FLUX'],float);q=np.array(f[1].data['QUALITY']);w=WCS(f[2].header)
ok=np.isfinite(t)&(q==0)&np.isfinite(F).all(axis=(1,2));t=t[ok];F=F[ok];F-=np.median(np.sort(F.reshape(len(F),-1),axis=1)[:,:48],axis=1)[:,None,None];core=(t>4084.8)&(t<4085.55);pre=(t>4083.4)&(t<4084.2);post=(t>4086.1)&(t<4086.8);O=.5*(np.median(F[pre],axis=0)+np.median(F[post],axis=0));D=O-np.median(F[core],axis=0);tx,ty=map(float,w.all_world2pix(float(g['ra']),float(g['dec']),0));yy,xx=np.indices(O.shape);mask=(abs(xx-tx)<=2)&(abs(yy-ty)<=2);v=np.clip(D,0,None)*mask;cx=float((v*xx).sum()/v.sum());cy=float((v*yy).sum()/v.sum());res={'tic':tic,'sector':100,'windows_btjd':{'core':[4084.8,4085.55],'pre':[4083.4,4084.2],'post':[4086.1,4086.8]},'samples':[int(sum(core)),int(sum(pre)),int(sum(post))],'centroid_offset_pixels':math.hypot(cx-tx,cy-ty),'aperture5_fractional_loss_ppt':float(1000*D[mask].sum()/O[mask].sum()),'note':'Positive-clipped centroid descriptive, not calibrated localization. Explicit local windows avoid later aperture drift.'};(h/'custom-local-difference.json').write_text(json.dumps(res,indent=2)+'\n');fig,axs=plt.subplots(1,2,figsize=(9,4));
for ax,img,title in zip(axs,[O,D],['out','out minus in']):
 ax.imshow(img,origin='lower');ax.plot(tx,ty,'r+',ms=12);ax.set_title(title)
 for x in n['capable_at_minimum_all_apertures']:
  # positions supplied from source table
  pass
axs[1].plot(cx,cy,'mo',mfc='none');fig.suptitle('TIC 449012335 s100 local windows');fig.tight_layout();fig.savefig(h/'custom-local-difference.png',dpi=130);print(res)
