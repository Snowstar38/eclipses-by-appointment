import json,csv,hashlib,math
from pathlib import Path
import numpy as np
from astropy.io import fits
from astropy.wcs import WCS
import matplotlib;matplotlib.use('Agg')
import matplotlib.pyplot as plt
B=Path(__file__).resolve().parent; Q={r['tic']:r for r in csv.DictReader((B/'queue.csv').open())}; npath=B.parent/'shared-catalogues/gaia-neighbors.json'; N=json.loads(npath.read_text());out=[]
for e in json.loads((B/'helper-fetch.json').read_text()):
 tic=e['tic'];r=Q[tic];tm=e['mid'];p=B/f'helper-{tic}-s{e["sector"]}.fits'
 with fits.open(p,memmap=False) as h:t=np.asarray(h[1].data['TIME'],float);f=np.asarray(h[1].data['FLUX'],float);q=np.asarray(h[1].data['QUALITY'],int);w=WCS(h[2].header)
 good=np.isfinite(t)&(q==0)&np.isfinite(f).all(axis=(1,2));t=t[good];f=f[good];x=t-tm;core=abs(x)<.06;pre=(x<-1.8)&(x>-2.5);post=(x>1.8)&(x<2.5) if tic=='323458448' else (x>.25)&(x<.55);pre=pre if tic=='323458448' else (x<-.25)&(x>-.55)
 bg=np.median(np.sort(f.reshape(len(f),-1),axis=1)[:,:40],axis=1);f=f-bg[:,None,None];base=.5*(np.median(f[pre],axis=0)+np.median(f[post],axis=0));dif=base-np.median(f[core],axis=0);tx,ty=map(float,w.all_world2pix(float(r['ra_deg']),float(r['dec_deg']),0));yy,xx=np.indices(base.shape);mask=(abs(xx-round(tx))<=2)&(abs(yy-round(ty))<=2);v=np.clip(dif,0,None)*mask;cx=float((v*xx).sum()/v.sum());cy=float((v*yy).sum()/v.sum());depth=float(1000*dif[mask].sum()/base[mask].sum());ns=[]
 for n in N['targets'][r['sample_id']]:
  if n['is_queue_gaia_source'] or not n['phot_g_mean_mag']:continue
  ratio=10**(-.4*(float(n['phot_g_mean_mag'])-float(r['gaia_G'])));need=(depth/1000)*(1+ratio)/ratio
  if need<=1:
   nx,ny=map(float,w.all_world2pix(float(n['ra']),float(n['dec']),0));ns.append({'source_id':n['source_id'],'separation_arcsec':n['separation_arcsec'],'G':n['phot_g_mean_mag'],'required_fraction_ideal':need,'xy':[nx,ny],'distance_diff_pix':math.hypot(nx-cx,ny-cy)})
 o={'tic':tic,'sector':e['sector'],'counts':[int(core.sum()),int(pre.sum()),int(post.sum())],'target_xy':[tx,ty],'difference_centroid':[cx,cy],'offset_pix':math.hypot(cx-tx,cy-ty),'base_ap5':float(base[mask].sum()),'depth_ppt':depth,'capable':ns,'neighbor_sha256':hashlib.sha256(npath.read_bytes()).hexdigest()}
 bulk=json.loads((B.parent.parent/'binary-exploration-2026-11-04'/'bulk-results'/f'{tic}.json').read_text());receipt=next(z for z in bulk['files'] if z['sector']==e['sector']);p=Path(receipt['path']);hsh=hashlib.sha256(p.read_bytes()).hexdigest();assert hsh==receipt['sha256']
 with fits.open(p,memmap=False) as h:
  d=h[1].data;names=h[1].columns.names;t=np.asarray(d['TIME'],float);q=np.asarray(d['QUALITY'],int);x=t-tm;good=(q==0)&np.isfinite(t);c=(abs(x)<.06)&good;a=((x<-1.8)&(x>-2.5) if tic=='323458448' else (x<-.25)&(x>-.55))&good;b=((x>1.8)&(x<2.5) if tic=='323458448' else (x>.25)&(x<.55))&good;o['qlp_sha256']=hsh;o['qlp_depths_ppt']={}
  for name in ['SAP_FLUX','KSPSAP_FLUX_SML','KSPSAP_FLUX','KSPSAP_FLUX_LAG']:
   if name in names:
    z=np.asarray(d[name],float);v0=.5*(np.nanmedian(z[a])+np.nanmedian(z[b]));o['qlp_depths_ppt'][name]=float(1000*(1-np.nanmedian(z[c])/v0))
 fig,ax=plt.subplots(1,2,figsize=(9,4))
 for a,img,title in zip(ax,[base,dif],['baseline','out minus in']):a.imshow(img,origin='lower');a.plot(tx,ty,'r+',ms=12);a.set_title(title)
 ax[1].plot(cx,cy,'mo',mfc='none');fig.suptitle(f'TIC {tic} S{e["sector"]}');fig.tight_layout();fig.savefig(B/f'helper-{tic}-difference.png',dpi=130);plt.close(fig);out.append(o);print(o)
(B/'helper-spatial.json').write_text(json.dumps(out,indent=2))

