import json,math,hashlib
from pathlib import Path
import numpy as np
from astropy.io import fits
from astropy.io.votable import parse_single_table
from astropy.wcs import WCS
import matplotlib;matplotlib.use('Agg')
import matplotlib.pyplot as plt
B=Path(__file__).resolve().parent;H=B/'helper-pixels';D=json.loads((B/'SOURCE-SNAPSHOT.json').read_text(encoding='utf8'));result=[]
for tic,s in D.items():
 h=H/tic;r=json.loads((h/'receipt.json').read_text(encoding='utf8'));g=s['target']['gaia']; ra=float(g['ra']);dec=float(g['dec']);gt=float(g['phot_g_mean_mag']);e=r.get('event');o={'tic':tic,'gaia_source_id':g['source_id']}
 try:
  tab=parse_single_table(h/'gaia.xml').to_table();dep=e['depth_ppt']/1000;ns=[]
  for x in tab:
   sid=str(x['datalinkID']);
   if sid==str(g['source_id']) or np.ma.is_masked(x['phot_g_mean_mag']):continue
   G=float(x['phot_g_mean_mag']);sep=math.hypot((float(x['ra'])-ra)*math.cos(math.radians(dec)),float(x['dec'])-dec)*3600;fr=10**(-.4*(G-gt));need=dep*(1+fr)/fr
   if need<=1:ns.append({'id':sid,'G':G,'sep_arcsec':sep,'required_fraction':need,'ra':float(x['ra']),'dec':float(x['dec'])})
  o['capable_neighbors']=ns;o['gaia_sha256']=hashlib.sha256((h/'gaia.xml').read_bytes()).hexdigest()
 except Exception as ex:o['gaia_error']=repr(ex);ns=[]
 try:
  with fits.open(h/'tesscut.fits',memmap=False) as hd:
   t=np.array(hd[1].data['TIME'],float);F=np.array(hd[1].data['FLUX'],float);q=np.array(hd[1].data['QUALITY'],int);w=WCS(hd[2].header)
  good=np.isfinite(t)&(q==0)&np.isfinite(F).all(axis=(1,2));t=t[good];F=F[good];x=t-e['mid_btjd'];dur=e['duration_days'];mi=abs(x)<.3*dur;pre=(x<-.75*dur)&(x>-1.75*dur);post=(x>.75*dur)&(x<1.75*dur)
  if min(sum(mi),sum(pre),sum(post))<2:raise ValueError('inadequate core or symmetric shoulders')
  bg=np.median(np.sort(F.reshape(len(F),-1),axis=1)[:,:int(F.shape[1]*F.shape[2]*.4)],axis=1);F=F-bg[:,None,None];O=.5*(np.median(F[pre],axis=0)+np.median(F[post],axis=0));dif=O-np.median(F[mi],axis=0);tx,ty=map(float,w.all_world2pix(ra,dec,0));yy,xx=np.indices(O.shape);mask=(abs(xx-tx)<=2)&(abs(yy-ty)<=2);v=np.clip(dif,0,None)*mask;cx=float((v*xx).sum()/v.sum());cy=float((v*yy).sum()/v.sum());den=O[mask].sum();ap=float(dif[mask].sum()/den);o.update(sector=e['sector'],event_btjd=e['mid_btjd'],target_px=[tx,ty],centroid_px=[cx,cy],offset_px=math.hypot(cx-tx,cy-ty),ap5_depth_ppt=ap*1000,n_in=int(sum(mi)),n_pre=int(sum(pre)),n_post=int(sum(post)),tesscut_sha256=r['tesscut_sha256'])
  fig,axs=plt.subplots(1,2,figsize=(9,4));
  for ax,img,title in zip(axs,[O,dif],['out','out minus in']):
   ax.imshow(img,origin='lower');ax.plot(tx,ty,'r+',ms=12);ax.set_title(title)
   for n in ns:
    px,py=map(float,w.all_world2pix(n['ra'],n['dec'],0));n['pixel']=[px,py];ax.plot(px,py,'wx');ax.annotate(n['id'][-5:],(px,py),color='white',fontsize=6)
  axs[1].plot(cx,cy,'mo',mfc='none');fig.suptitle(f'TIC {tic} sector {e["sector"]}');fig.tight_layout();fig.savefig(h/'difference.png',dpi=130);plt.close(fig)
 except Exception as ex:o['pixel_error']=repr(ex)
 result.append(o);print(tic,'neighbors',len(ns),'pixel',o.get('offset_px'),o.get('ap5_depth_ppt'),o.get('pixel_error'))
(H/'results.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf8')

