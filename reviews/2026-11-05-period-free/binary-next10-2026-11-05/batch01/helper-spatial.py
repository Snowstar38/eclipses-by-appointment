import json,csv,hashlib
from pathlib import Path
import numpy as np
from astropy.io import fits
from astropy.wcs import WCS
import matplotlib;matplotlib.use('Agg')
import matplotlib.pyplot as plt
B=Path(__file__).resolve().parent
Q={r['tic']:r for r in csv.DictReader((B/'queue.csv').open())}; out=[]
for e in json.loads((B/'helper-fetch.json').read_text()):
 tic=e['tic']; row=Q[tic]; tm=e['screen_time'];fp=B/f'helper-{tic}-tesscut.fits'
 with fits.open(fp,memmap=False) as h:
  t=np.asarray(h[1].data['TIME'],float);f=np.asarray(h[1].data['FLUX'],float);q=np.asarray(h[1].data['QUALITY'],int);w=WCS(h[2].header)
 good=np.isfinite(t)&(q==0)&np.isfinite(f).all(axis=(1,2));t=t[good];f=f[good]; x=t-tm
 core=abs(x)<.07;pre=(x<-.25)&(x>-.55);post=(x>.25)&(x<.55)
 o={'tic':tic,'sector':e['sector'],'screen_btjd':tm,'counts':[int(core.sum()),int(pre.sum()),int(post.sum())],'fits_sha256':hashlib.sha256(fp.read_bytes()).hexdigest()}
 if min(o['counts'])>=2:
  bg=np.median(np.sort(f.reshape(len(f),-1),axis=1)[:,:40],axis=1);f=f-bg[:,None,None];base=.5*(np.median(f[pre],axis=0)+np.median(f[post],axis=0));dif=base-np.median(f[core],axis=0);tx,ty=map(float,w.all_world2pix(float(row['ra_deg']),float(row['dec_deg']),0));yy,xx=np.indices(base.shape);cx0=int(round(tx));cy0=int(round(ty));mask=(abs(xx-cx0)<=2)&(abs(yy-cy0)<=2); v=np.clip(dif,0,None)*mask;cx=float((v*xx).sum()/v.sum());cy=float((v*yy).sum()/v.sum());o.update(target_pixel=[tx,ty],diff_centroid=[cx,cy],offset_pix=float(np.hypot(cx-tx,cy-ty)),base_ap5=float(base[mask].sum()),difference_ap5=float(dif[mask].sum()),depth_ppt=float(1000*dif[mask].sum()/base[mask].sum()))
  fig,ax=plt.subplots(1,2,figsize=(9,4));
  for a,img,title in zip(ax,[base,dif],['out of event','out minus in']):
   a.imshow(img,origin='lower');a.plot(tx,ty,'r+',ms=12);a.set_title(title)
  ax[1].plot(cx,cy,'mo',mfc='none');fig.suptitle(f'TIC {tic} S{e["sector"]}');fig.tight_layout();fig.savefig(B/f'helper-{tic}-difference.png',dpi=130);plt.close(fig)
 # compare QLP raw and alternative columns, same samples
 s=json.loads((B.parent/'source-packets'/tic/'sources.json').read_text());bulk=json.loads((B.parent.parent/'binary-exploration-2026-11-04'/'bulk-results'/f'{tic}.json').read_text()); receipt=next(z for z in bulk['files'] if z['sector']==e['sector']); p=Path(receipt['path']);actual=hashlib.sha256(p.read_bytes()).hexdigest();assert actual==receipt['sha256']
 with fits.open(p,memmap=False) as h:
  d=h[1].data; names=h[1].columns.names;t=np.asarray(d['TIME'],float);q=np.asarray(d['QUALITY'],int);x=t-tm;good=(q==0)&np.isfinite(t);core=(abs(x)<.07)&good;pre=(x<-.25)&(x>-.55)&good;post=(x>.25)&(x<.55)&good;o['qlp_sha256']=actual;o['qlp_counts']=[int(core.sum()),int(pre.sum()),int(post.sum())];o['qlp_depths_ppt']={}
  for name in ['SAP_FLUX','KSPSAP_FLUX_SML','KSPSAP_FLUX','KSPSAP_FLUX_LAG']:
   if name not in names:continue
   a=np.asarray(d[name],float); a1=a[core&np.isfinite(a)];a2=a[pre&np.isfinite(a)];a3=a[post&np.isfinite(a)];base=.5*(np.median(a2)+np.median(a3)) if min(len(a2),len(a3))>=2 else np.nan;o['qlp_depths_ppt'][name]=float(1000*(1-np.median(a1)/base)) if len(a1)>=2 and np.isfinite(base) and base>0 else None
 out.append(o);print(o,flush=True)
(B/'helper-spatial.json').write_text(json.dumps(out,indent=2,allow_nan=False))

