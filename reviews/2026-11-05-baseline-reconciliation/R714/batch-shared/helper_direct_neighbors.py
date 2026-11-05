import json,math
from pathlib import Path
import numpy as np
from astropy.io import fits
from astropy.io.votable import parse_single_table
from astropy.wcs import WCS
import matplotlib;matplotlib.use('Agg')
import matplotlib.pyplot as plt
B=Path(__file__).resolve().parent;S=json.loads((B/'SOURCE-SNAPSHOT.json').read_text());N={x['tic']:x for x in json.loads((B/'helper-pixels/final-neighbors.json').read_text())};T=parse_single_table(B/'helper-pixels/gaia-all.raw').to_table();out={}
for tic in ['117930511','436013770']:
 g=S[tic]['target']['gaia'];h=B/'helper-pixels'/tic;e=json.loads((h/'receipt.json').read_text())['event'];
 with fits.open(h/'tesscut.fits',memmap=False) as f:t=np.array(f[1].data['TIME'],float);F=np.array(f[1].data['FLUX'],float);q=np.array(f[1].data['QUALITY']);w=WCS(f[2].header)
 ok=np.isfinite(t)&(q==0)&np.isfinite(F).all(axis=(1,2));t=t[ok];F=F[ok];F-=np.median(np.sort(F.reshape(len(F),-1),axis=1)[:,:48],axis=1)[:,None,None];x=t-e['mid_btjd'];d=e['duration_days'];core=abs(x)<.3*d;pre=(x<-.75*d)&(x>-1.75*d);post=(x>.75*d)&(x<1.75*d);O=.5*(np.median(F[pre],axis=0)+np.median(F[post],axis=0));D=O-np.median(F[core],axis=0);tx,ty=map(float,w.all_world2pix(float(g['ra']),float(g['dec']),0));n=N[tic]['capable_at_minimum_all_apertures'][0];z=next(z for z in T if str(z['datalinkID'])==n['source_id']);nx,ny=map(float,w.all_world2pix(float(z['ra']),float(z['dec']),0));pixel=lambda xx,yy:float(D[round(yy),round(xx)]);out[tic]={'target_pixel_xy':[tx,ty],'neighbor_pixel_xy':[nx,ny],'neighbor_source_id':n['source_id'],'difference_at_nearest_target_pixel':pixel(tx,ty),'difference_at_nearest_neighbor_pixel':pixel(nx,ny),'note':'Pixel values are blended and neither independent source photometry nor a PRF likelihood.'};fig,ax=plt.subplots(figsize=(6,5));im=ax.imshow(D,origin='lower');ax.plot(tx,ty,'r+',ms=15,mew=2,label='target');ax.plot(nx,ny,'wx',ms=10,mew=2,label='capable Gaia neighbor');ax.legend(loc='upper left');fig.colorbar(im,ax=ax,label='out minus in (flux)');ax.set_title('TIC '+tic+' actual difference');fig.tight_layout();fig.savefig(h/'final-neighbor-difference.png',dpi=160);plt.close(fig)
(B/'helper-pixels/final-neighbor-direct-check.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
