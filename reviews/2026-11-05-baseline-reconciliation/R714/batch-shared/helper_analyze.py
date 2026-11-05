import json,math,hashlib
from pathlib import Path
import numpy as np
from astropy.io import fits
from astropy.io.votable import parse_single_table
from astropy.coordinates import SkyCoord
from astropy import units as u
from astropy.wcs import WCS
import matplotlib;matplotlib.use('Agg')
import matplotlib.pyplot as plt
B=Path(__file__).resolve().parent;H=B/'helper-pixels';D=json.loads((B/'SOURCE-SNAPSHOT.json').read_text(encoding='utf8'));tab=parse_single_table(H/'gaia-all.raw').to_table(); print('Gaia rows',len(tab));out=[]
coords=SkyCoord(ra=np.array(tab['ra'],float)*u.deg,dec=np.array(tab['dec'],float)*u.deg)
for tic,s in D.items():
 g=s['target']['gaia'];m=json.loads((B/tic/'measurements.json').read_text(encoding='utf8')); gt=float(g['phot_g_mean_mag']);depth=m['depth_ppt']/1000; pos=SkyCoord(float(g['ra'])*u.deg,float(g['dec'])*u.deg);sep=coords.separation(pos).arcsec;neigh=[]
 for i in np.where(sep<=60)[0]:
  x=tab[i];sid=str(x['datalinkID']);
  if sid==str(g['source_id']) or np.ma.is_masked(x['phot_g_mean_mag']): continue
  G=float(x['phot_g_mean_mag']);ratio=10**(-.4*(G-gt));need=depth*(1+ratio)/ratio
  if need<=1:neigh.append(dict(source_id=sid,sep_arcsec=float(sep[i]),G=G,flux_ratio_G=ratio,intrinsic_eclipse_fraction=need,ra=float(x['ra']),dec=float(x['dec'])))
 selected=json.loads((H/tic/'receipt.json').read_text())['event']; ev=next(x for x in m['events'] if x['sector']==selected['sector'] and x['cycle']==selected['cycle']);fp=next(x['path'] for x in m['source_receipts'] if x['sector']==ev['sector'])
 with fits.open(fp,memmap=False) as hd:
  t=np.asarray(hd[1].data['TIME'],float);q=np.asarray(hd[1].data['QUALITY'],int); cols={k:np.asarray(hd[1].data[k],float) for k in ['KSPSAP_FLUX_SML','KSPSAP_FLUX','KSPSAP_FLUX_LAG'] if k in hd[1].columns.names}
 x=t-ev['mid_btjd'];dur=ev['duration_days']; core=(abs(x)<.3*dur)&(q==0);pre=(x<-.75*dur)&(x>-1.75*dur)&(q==0);post=(x>.75*dur)&(x<1.75*dur)&(q==0);aps={}
 for k,f in cols.items():
  a=f[core&np.isfinite(f)];b=f[pre&np.isfinite(f)];c=f[post&np.isfinite(f)];base=.5*(np.median(b)+np.median(c)) if min(len(b),len(c))>=2 else np.nan;aps[k]=float(1000*(1-np.median(a)/base)) if len(a)>=2 and base>0 else None
 o=dict(tic=tic,gaia_id=g['source_id'],test_depth_ppt=1000*depth,gaia_sources_within_60arcsec=int(sum(sep<=60)),capable_neighbors=neigh,qlp_alternative_aperture_ppt=aps,sector=ev['sector'],core_pre_post=[int(sum(core)),int(sum(pre)),int(sum(post))],qlp_source_sha256=hashlib.sha256(Path(fp).read_bytes()).hexdigest())
 h=H/tic
 if (h/'tesscut.fits').exists():
  with fits.open(h/'tesscut.fits',memmap=False) as hd:t=np.array(hd[1].data['TIME'],float);F=np.array(hd[1].data['FLUX'],float);q=np.array(hd[1].data['QUALITY'],int);w=WCS(hd[2].header)
  good=np.isfinite(t)&(q==0)&np.isfinite(F).all(axis=(1,2));t=t[good];F=F[good];x=t-ev['mid_btjd'];mi=abs(x)<.3*dur;pre=(x<-.75*dur)&(x>-1.75*dur);post=(x>.75*dur)&(x<1.75*dur)
  if min(sum(mi),sum(pre),sum(post))>=2:
   bg=np.median(np.sort(F.reshape(len(F),-1),axis=1)[:,:48],axis=1);F=F-bg[:,None,None];O=.5*(np.median(F[pre],axis=0)+np.median(F[post],axis=0));dif=O-np.median(F[mi],axis=0);tx,ty=map(float,w.all_world2pix(float(g['ra']),float(g['dec']),0));yy,xx=np.indices(O.shape);mask=(abs(xx-tx)<=2)&(abs(yy-ty)<=2);v=np.clip(dif,0,None)*mask;cx=float((v*xx).sum()/v.sum());cy=float((v*yy).sum()/v.sum());o['cutout']={'ap5_depth_ppt':float(1000*dif[mask].sum()/O[mask].sum()),'centroid_offset_pixels':math.hypot(cx-tx,cy-ty),'core_pre_post':[int(sum(mi)),int(sum(pre)),int(sum(post))]}
   fig,axs=plt.subplots(1,2,figsize=(9,4));
   for ax,img,title in zip(axs,[O,dif],['out','out minus in']):
    ax.imshow(img,origin='lower');ax.plot(tx,ty,'r+',ms=12);ax.set_title(title)
    for n in neigh:
     px,py=map(float,w.all_world2pix(n['ra'],n['dec'],0));ax.plot(px,py,'wx');ax.annotate(n['source_id'][-5:],(px,py),color='white',fontsize=6)
   axs[1].plot(cx,cy,'mo',mfc='none');fig.suptitle(f'TIC {tic} s{ev["sector"]}');fig.tight_layout();fig.savefig(h/'difference.png',dpi=130);plt.close(fig)
  else:o['cutout']={'error':'insufficient symmetric samples','counts':[int(sum(mi)),int(sum(pre)),int(sum(post))]}
 out.append(o);print(tic,'neighbors',len(neigh),'ap',aps,'cutout',o.get('cutout'))
(H/'results.json').write_text(json.dumps(out,indent=2,allow_nan=False)+'\n',encoding='utf8')


