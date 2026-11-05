import csv,json
from pathlib import Path
import numpy as np
from astropy.io import fits
from astropy.wcs import WCS
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
B=Path(__file__).parent;rows={r['tic']:r for r in csv.DictReader((B/'queue.csv').open())};windows={'72747845':[(2119.9,2120.0),(2120.08,2120.22),(2120.3,2120.45)],'1535458':[(2193.05,2193.25),(2193.55,2193.8),(2193.98,2194.15)],'364268504':[(3679.55,3679.65),(3679.75,3679.86),(3679.95,3680.05)],'117157551':[(4196.0,4196.6),(4197.4,4197.9),(4198.25,4198.6)]};out=[]
for tic,win in windows.items():
 with fits.open(B/('helper-cut-'+tic+'.fits')) as h:
  a=h[1].data;t=np.array(a['TIME']);f=np.array(a['FLUX']);q=np.array(a['QUALITY']);w=WCS(h[2].header);xy=w.all_world2pix(float(rows[tic]['ra_deg']),float(rows[tic]['dec_deg']),0);good=(q==0)&np.isfinite(t)&np.isfinite(f).all(axis=(1,2));t=t[good];f=f[good]; masks=[(t>=l)&(t<=r) for l,r in win]; ims=[np.median(f[m],axis=0) for m in masks]; diff=(ims[0]+ims[2])/2-ims[1]; y,x=np.indices(diff.shape);pos=np.maximum(diff,0); xx=float(np.sum(x*pos)/pos.sum()); yy=float(np.sum(y*pos)/pos.sum()); tx,ty=map(float,xy); kx=int(round(tx));ky=int(round(ty));target=float(np.median(ims[0][ky-1:ky+2,kx-1:kx+2])); bg=float(np.median(np.sort(ims[0].ravel())[:30]));
  fig,axs=plt.subplots(1,2,figsize=(9,4));axs[0].imshow(ims[0],origin='lower');axs[1].imshow(diff,origin='lower',cmap='RdBu_r');
  for ax in axs:ax.plot(tx,ty,'gx',ms=9);ax.set_title('baseline' if ax==axs[0] else 'baseline minus event');
  fig.suptitle(tic+' '+' '.join(map(str,win)));fig.tight_layout();fig.savefig(B/('helper-diff-'+tic+'.png'));plt.close(fig)
  out.append({'tic':tic,'windows':win,'counts':[int(m.sum()) for m in masks],'wcs_target_xy':[tx,ty],'positive_diff_centroid':[xx,yy],'median_target_pixel':target,'background_median':bg,'target_minus_background':target-bg,'warning':'positive difference centroid is heuristic; background/instrumental variability can dominate; inspect map'})
(B/'helper-diff.json').write_text(json.dumps(out,indent=2));print(out)
