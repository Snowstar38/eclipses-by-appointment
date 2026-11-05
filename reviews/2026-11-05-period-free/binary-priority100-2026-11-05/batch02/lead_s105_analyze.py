"""Lead-owned raw-pixel inspection of newly available S105, after helper audit."""
import csv,hashlib,json
from pathlib import Path
import numpy as np
from astropy.io import fits
from astropy.wcs import WCS
from scipy.ndimage import median_filter
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
B=Path(__file__).resolve().parent;Q={r['sample_id']:r for r in csv.DictReader((B/'queue.csv').open(newline='',encoding='utf-8'))};out=[]
for sid in ('T011','T019'):
    r=Q[sid];tic=r['tic'];p=B/f'lead-{tic}-s105.fits';receipt=next(x for x in json.loads((B/'lead-s105-fetch.json').read_text()) if x['tic']==tic);assert hashlib.sha256(p.read_bytes()).hexdigest()==receipt['fits_sha256']
    with fits.open(p,memmap=False) as h:
        d=h[1].data;t=np.asarray(d['TIME'],float);f=np.asarray(d['FLUX'],float);q=np.asarray(d['QUALITY'],int);w=WCS(h[2].header)
    tx,ty=map(float,w.all_world2pix(float(r['ra_deg']),float(r['dec_deg']),0));yy,xx=np.indices(f.shape[1:]);mask=(abs(xx-round(tx))<=2)&(abs(yy-round(ty))<=2)
    good=np.isfinite(t)&np.isfinite(f).all(axis=(1,2))&(q==0);t=t[good];f=f[good]
    bg=np.median(np.sort(f.reshape(len(f),-1),axis=1)[:,:40],axis=1);ap=(f-bg[:,None,None])[:,mask].sum(axis=1)
    dt=np.median(np.diff(t));trend=median_filter(ap,size=int(8/dt)//2*2+1,mode='nearest');y=ap/np.median(ap);res=ap/trend-1
    fig,axs=plt.subplots(2,1,figsize=(12,6))
    axs[0].plot(t,y,'.',ms=1);axs[0].set(xlabel='BTJD',ylabel='5x5 raw pixel flux / sector median',title=f'{sid} TIC {tic} S105; target WCS ({tx:.2f},{ty:.2f}); {len(t)} q0 cadences')
    axs[1].plot(t,res,'.',ms=1);axs[1].set(xlabel='BTJD',ylabel='flux / 8 d median - 1')
    if sid=='T019':
        pred=4165.008+float(r['gaia_period_days']);axs[0].axvspan(pred-.5,pred+.5,color='orange',alpha=.2);axs[1].axvspan(pred-.5,pred+.5,color='orange',alpha=.2)
    fig.tight_layout();fig.savefig(B/f'lead-{tic}-s105.png',dpi=140);plt.close(fig)
    rec={'sample_id':sid,'tic':tic,'fits_sha256':receipt['fits_sha256'],'sector':105,'target_xy':[tx,ty],'n_quality0':len(t),'first_btjd':float(t.min()),'last_btjd':float(t.max()),'cadence_days':float(dt),'max_gap_days':float(np.max(np.diff(t))),'min_residual':float(res.min()),'max_residual':float(res.max())}
    if sid=='T019':
        pred=4165.008+float(r['gaia_period_days']);x=t-pred;core=(abs(x)<.4);post=(x>1.2)&(x<2.0);pre=(x<-.8)&(x>-.4)
        rec.update(predicted_btjd=pred,core_n=int(sum(core)),core_first_offset=float(x[core].min()) if core.any() else None,core_last_offset=float(x[core].max()) if core.any() else None,core_max_gap=float(np.max(np.diff(t[core]))) if sum(core)>1 else None,pre_n=int(sum(pre)),post_n=int(sum(post)),core_to_post_deficit_ppt=float(1000*(1-np.median(ap[core])/np.median(ap[post]))) if core.any() and post.any() else None)
        fig,ax=plt.subplots(figsize=(9,4));m=(abs(x)<3);ax.plot(x[m],ap[m]/np.median(ap[post]),'.',ms=2);ax.axvspan(-.4,.4,color='orange',alpha=.2);ax.set(xlabel='days from conditional Gaia repeat',ylabel='target 5x5 raw / post median',title=f'T019 S105 conditional repeat {pred:.3f}');fig.tight_layout();fig.savefig(B/'lead-220343379-s105-window.png',dpi=150);plt.close(fig)
    out.append(rec);print(rec,flush=True)
(B/'lead-s105-analysis.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
