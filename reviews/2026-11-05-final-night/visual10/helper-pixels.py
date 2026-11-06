from pathlib import Path
import json,csv,hashlib
import numpy as np
from astropy.io import fits
from astropy.wcs import WCS
import matplotlib;matplotlib.use('Agg')
import matplotlib.pyplot as plt
B=Path(__file__).resolve().parent;Q={r['tic']:r for r in csv.DictReader((B/'queue.csv').open())};cl=json.loads((B/'lead-clocks.json').read_text());out={}
for tic,sec,centers,core,lo,hi in [('185744410',61,cl['185744410']['event_times_btjd'][1:-1],.035,.12,.25),('149316567',88,[3691.8916,3694.7573,3698.9634,3701.8546,3706.0629,3708.9148,3713.1277,3716.0212],.035,.12,.28),('378411251',64,cl['378411251']['event_times_btjd'][:6],.035,.12,.28),('387124290',81,[x for x in cl['387124290']['event_times_btjd'] if abs(x-3513.2033)>.1 and x<3532.5],.04,.14,.25)]:
 p=B/tic/f'helper-cut-s{sec}.fits';h=fits.open(p);d=h[1].data;t=np.array(d['TIME']);f=np.array(d['FLUX']);q=np.array(d['QUALITY']);xy=WCS(h[2].header).all_world2pix([[float(Q[tic]['ra_deg']),float(Q[tic]['dec_deg'])]],0)[0];h.close();ok=(q==0)&np.isfinite(t);diffs=[];bases=[];used=[]
 for c in centers:
  a=ok&(abs(t-c)<core);b=ok&(abs(t-c)>lo)&(abs(t-c)<hi)
  if sum(a)>=3 and sum(b)>=6:
   ba=np.nanmedian(f[b],axis=0);di=ba-np.nanmedian(f[a],axis=0);diffs.append(di);bases.append(ba);used.append(c)
 diff=np.nanmedian(diffs,axis=0);base=np.nanmedian(bases,axis=0);peak=np.unravel_index(np.nanargmax(diff),diff.shape)[::-1];yy,xx=np.indices(diff.shape);mask=(xx-peak[0])**2+(yy-peak[1])**2<2.5**2;weight=np.maximum(diff,0)*mask;cent=[float(np.sum(xx*weight)/np.sum(weight)),float(np.sum(yy*weight)/np.sum(weight))];aper=(xx-xy[0])**2+(yy-xy[1])**2<1.6**2;loss=float(np.sum(diff[aper]));bl=float(np.sum(base[aper]));rec=dict(target_xy=xy.tolist(),peak_xy=list(map(int,peak)),centroid_xy=cent,offset_px=float(np.hypot(cent[0]-xy[0],cent[1]-xy[1])),approx_arcsec=float(21*np.hypot(cent[0]-xy[0],cent[1]-xy[1])),mean_target_aperture_blended_fraction=loss/bl,aperture_loss_e_per_s=loss,base_aperture_e_per_s=bl,centers=used,sha256=hashlib.sha256(p.read_bytes()).hexdigest(),baseline='each local symmetric sidebands, median event differences; no background subtraction; centroid clipped positive within 2.5px peak, diagnostic only');out[tic]=rec
 fig,ax=plt.subplots(1,2,figsize=(9,4));
 for a,z,name in zip(ax,[base,diff],['baseline','median eclipse deficit']):
  im=a.imshow(z,origin='lower');fig.colorbar(im,ax=a);a.plot(*xy,'rx',ms=12,mew=2);a.plot(*cent,'c+',ms=12,mew=2);a.set_title(name);a.grid(alpha=.3)
 fig.suptitle(f'{tic} S{sec}: red target, cyan deficit centroid');fig.tight_layout();fig.savefig(B/tic/'helper-pixels.png',dpi=150);plt.close(fig)
 print(tic,rec,flush=True)
(B/'helper-pixels.json').write_text(json.dumps(out,indent=2))
