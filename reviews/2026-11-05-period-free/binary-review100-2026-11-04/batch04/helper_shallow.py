import csv,json,math,hashlib
from pathlib import Path
import numpy as np
from astropy.io import fits
from astropy.io.votable import parse_single_table
from astropy.coordinates import SkyCoord
from astropy import units as u
from astropy.wcs import WCS
import matplotlib;matplotlib.use('Agg')
import matplotlib.pyplot as plt
B=Path(__file__).resolve().parent;H=B/'helper-pixels';Q={r['tic']:r for r in csv.DictReader((B/'queue.csv').open())};out={}
for tic,mid,dur in [('372989764',3100.4,1.6)]:
 z=Q[tic];h=H/tic;T=parse_single_table(h/'gaia.raw').to_table(); C=SkyCoord(np.array(T['ra'],float)*u.deg,np.array(T['dec'],float)*u.deg);p=SkyCoord(float(z['ra_deg'])*u.deg,float(z['dec_deg'])*u.deg);sep=C.separation(p).arcsec
 with fits.open(h/'tesscut.fits',memmap=False) as f:t=np.asarray(f[1].data['TIME'],float);F=np.asarray(f[1].data['FLUX'],float);qual=np.asarray(f[1].data['QUALITY']);w=WCS(f[2].header)
 ok=np.isfinite(t)&(qual==0)&np.isfinite(F).all(axis=(1,2));t=t[ok];F=F[ok];bg=np.median(np.sort(F.reshape(len(F),-1),axis=1)[:,:48],axis=1);F-=bg[:,None,None];x=t-mid;core=abs(x)<.25*dur;pre=(x<-.65*dur)&(x>-1.4*dur);post=(x>.65*dur)&(x<1.4*dur);O=.5*(np.median(F[pre],axis=0)+np.median(F[post],axis=0));D=O-np.median(F[core],axis=0);tx,ty=map(float,w.all_world2pix(p.ra.deg,p.dec.deg,0));yy,xx=np.indices(O.shape);mask=(abs(xx-tx)<=2)&(abs(yy-ty)<=2);v=np.clip(D,0,None)*mask;cx=float((v*xx).sum()/v.sum());cy=float((v*yy).sum()/v.sum());depth=float(D[mask].sum()/O[mask].sum());ns=[]
 for i in np.where(sep<=60)[0]:
  a=T[i];sid=str(a['datalinkID']);
  if sid==z['gaia_dr3'] or np.ma.is_masked(a['phot_g_mean_mag']):continue
  ratio=10**(-.4*(float(a['phot_g_mean_mag'])-float(z['gaia_G'])));need=depth*(1+ratio)/ratio;nx,ny=map(float,w.all_world2pix(float(a['ra']),float(a['dec']),0));ns.append({'source_id':sid,'sep_arcsec':float(sep[i]),'G':float(a['phot_g_mean_mag']),'flux_ratio_G':ratio,'required_total_disappearance_fraction_approx':need,'pixel_xy':[nx,ny]})
 out[tic]={'sector':json.loads((h/'receipt.json').read_text())['sector'],'counts_core_pre_post':[int(sum(core)),int(sum(pre)),int(sum(post))],'ap5_depth_ppt':depth*1000,'target_xy':[tx,ty],'positive_difference_centroid_xy':[cx,cy],'offset_pixels':math.hypot(cx-tx,cy-ty),'gaia_neighbors':ns,'caveat':'Approximate Gaia G flux and full inclusion; aperture response, TESS bandpass, crowding, background and centroid bias limit attribution. Two reductions use same photons.'}
 fig,axs=plt.subplots(1,2,figsize=(10,4))
 for ax,img,title in zip(axs,[O,D],['out of event','out minus in']):
  im=ax.imshow(img,origin='lower');ax.plot(tx,ty,'r+',ms=15,mew=2,label='target');
  for n in ns:
   nx,ny=n['pixel_xy'];ax.plot(nx,ny,'wx');ax.annotate(n['source_id'][-5:],(nx,ny),color='white',fontsize=7)
  ax.set_title(title);fig.colorbar(im,ax=ax)
 axs[1].plot(cx,cy,'mo',mfc='none');fig.suptitle(tic);fig.tight_layout();fig.savefig(h/'helper-shallow-difference.png',dpi=130);plt.close(fig)
 print(tic,json.dumps(out[tic]),flush=True)
(B/'helper-shallow-attribution.json').write_text(json.dumps(out,indent=2)+'\n')



