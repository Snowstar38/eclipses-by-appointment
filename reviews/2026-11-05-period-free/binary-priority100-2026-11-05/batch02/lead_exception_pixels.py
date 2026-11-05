"""Lead-owned alternate raw pixel apertures at four ambiguous screened windows."""
import csv,hashlib,json,math
from pathlib import Path
import numpy as np
from astropy.io import fits
from astropy.wcs import WCS
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
B=Path(__file__).resolve().parent;Q={r['sample_id']:r for r in csv.DictReader((B/'queue.csv').open(newline='',encoding='utf-8'))}
SPEC={'T011':(96,3921.746,(.05,.20),(-2.5,-1.5),(1,2)), 'T016':(19,1840.639,(-.07,.07),(-.55,-.3),(.2,.38)), 'T018':(104,4179.448,(-.09,.09),(-.5,-.25),(.35,.6)), 'T019':(103,4165.008,(-.25,0),(-1.5,-.8),(1.6,2.2))}
receipts={(x['sample_id'],x['sector']):x for x in json.loads((B/'lead-exception-fetch.json').read_text())};out=[]
for sid,(sector,tm,co,pr,po) in SPEC.items():
    r=Q[sid];tic=r['tic'];p=B/f'lead-{tic}-s{sector}.fits';receipt=receipts[(sid,sector)];assert hashlib.sha256(p.read_bytes()).hexdigest()==receipt['fits_sha256']
    with fits.open(p,memmap=False) as h:
        d=h[1].data;t=np.asarray(d['TIME'],float);f=np.asarray(d['FLUX'],float);q=np.asarray(d['QUALITY'],int);w=WCS(h[2].header)
    good=np.isfinite(t)&np.isfinite(f).all(axis=(1,2))&(q==0);t=t[good];f=f[good];x=t-tm
    bg=np.median(np.sort(f.reshape(len(f),-1),axis=1)[:,:40],axis=1);f=f-bg[:,None,None]
    core=(x>=co[0])&(x<=co[1]);pre=(x>=pr[0])&(x<=pr[1]);post=(x>=po[0])&(x<=po[1]);
    tx,ty=map(float,w.all_world2pix(float(r['ra_deg']),float(r['dec_deg']),0));yy,xx=np.indices(f.shape[1:]);mask=(abs(xx-round(tx))<=2)&(abs(yy-round(ty))<=2)
    ap=f[:,mask].sum(axis=1);baseline=np.median(np.r_[ap[pre],ap[post]]) if pre.any() and post.any() else np.nan;depth=float(1000*(1-np.median(ap[core])/baseline)) if core.any() and np.isfinite(baseline) else None
    rec={'sample_id':sid,'tic':tic,'sector':sector,'time_btjd':tm,'fits_sha256':receipt['fits_sha256'],'target_xy':[tx,ty],'counts':{'core':int(sum(core)),'pre':int(sum(pre)),'post':int(sum(post))},'windows_days':{'core':co,'pre':pr,'post':po},'target_5x5_depth_ppt':depth}
    if core.any() and pre.any() and post.any():
        base=.5*(np.median(f[pre],axis=0)+np.median(f[post],axis=0));dif=base-np.median(f[core],axis=0);v=np.clip(dif,0,None)*mask;tot=v.sum()
        if tot>0:
            cx=float((v*xx).sum()/tot);cy=float((v*yy).sum()/tot);rec['difference_centroid_xy']=[cx,cy];rec['target_offset_pix']=float(math.hypot(cx-tx,cy-ty))
        fig,axs=plt.subplots(1,2,figsize=(9,4))
        axs[0].imshow(base,origin='lower');axs[0].plot(tx,ty,'r+',ms=12);axs[0].set_title('baseline')
        axs[1].imshow(dif,origin='lower');axs[1].plot(tx,ty,'r+',ms=12);axs[1].set_title('baseline minus core')
        if tot>0:axs[1].plot(cx,cy,'mo',mfc='none')
        fig.tight_layout();fig.savefig(B/f'lead-{tic}-s{sector}-difference.png',dpi=140);plt.close(fig)
    fig,ax=plt.subplots(figsize=(9,4));m=abs(x)<3;ax.plot(x[m],ap[m]/baseline,'.',ms=2);ax.axvspan(*co,color='orange',alpha=.2);ax.set(xlabel='days from screened time',ylabel='target 5x5 raw / baseline',title=f'{sid} S{sector}: {depth:.1f} ppt, counts {sum(core)}/{sum(pre)}/{sum(post)}');fig.tight_layout();fig.savefig(B/f'lead-{tic}-s{sector}-pixel-curve.png',dpi=140);plt.close(fig)
    out.append(rec);print(rec,flush=True)
(B/'lead-exception-pixels.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
