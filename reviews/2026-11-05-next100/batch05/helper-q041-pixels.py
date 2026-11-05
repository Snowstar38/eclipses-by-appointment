"""Fresh TESSCut WCS difference images for selected Q041-Q050 events."""
import csv
import hashlib
import io
import json
import zipfile
from pathlib import Path

import numpy as np
import requests
from astropy.io import fits
from astropy.wcs import WCS
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

B=Path(__file__).resolve().parent
Q={r['sample_id']:r for r in csv.DictReader((B/'queue.csv').open(newline='',encoding='utf8'))}
N=json.loads((B/'lead-neighbors.json').read_text())['targets']
EVENTS=[('Q041',67,3146.525,.18),('Q041',101,4119.237,.18)]
out=[]
for sid,sector,center,half in EVENTS:
    row=Q[sid]
    args=dict(ra=float(row['ra_deg']),dec=float(row['dec_deg']),x=11,y=11,sector=sector)
    response=requests.get('https://mast.stsci.edu/tesscut/api/v0.1/astrocut',params=args,timeout=120)
    response.raise_for_status()
    zipped=response.content
    (B/f'helper-{sid}-s{sector:03d}.zip').write_bytes(zipped)
    with zipfile.ZipFile(io.BytesIO(zipped)) as z: raw=z.read(z.namelist()[0])
    with fits.open(io.BytesIO(raw),memmap=False) as h:
        a=h[1].data;t=np.asarray(a['TIME'],float);F=np.asarray(a['FLUX'],float);q=np.asarray(a['QUALITY'],int);w=WCS(h[2].header)
    valid=(q==0)&np.isfinite(t)&np.all(np.isfinite(F),axis=(1,2))
    core=valid&(np.abs(t-center)<half)
    side=valid&(np.abs(t-center)>.6)&(np.abs(t-center)<1.3)
    if core.sum()<2 or side.sum()<8:
        out.append(dict(sample_id=sid,sector=sector,status='insufficient_core_or_side',n_core=int(core.sum()),n_side=int(side.sum()),zip_sha256=hashlib.sha256(zipped).hexdigest()))
        continue
    base=np.median(F[side],axis=0);dip=np.median(F[core],axis=0);diff=base-dip
    yy,xx=np.indices(base.shape)
    sources=[]
    for s in N[sid]:
        if s['separation_arcsec']>80: continue
        x,y=w.world_to_pixel_values(float(s['ra']),float(s['dec']))
        sources.append(dict(source_id=s['source_id'],G=float(s['phot_g_mean_mag']),x=float(x),y=float(y),distance_arcsec=s['separation_arcsec'],is_target=s['is_target'],G_flux_ratio=s['flux_ratio_to_target_G']))
    target=next(s for s in sources if s['is_target'])
    tx,ty=target['x'],target['y']
    sky_mask=((xx<2)|(xx>8))&((yy<2)|(yy>8))
    bg=np.median(F[:,sky_mask],axis=1)
    target_pixel=F[:,round(ty),round(tx)]-bg
    local=((xx-tx)**2+(yy-ty)**2)<2.5**2
    wt=np.maximum(diff,0)*local
    cx=float((wt*xx).sum()/wt.sum()) if wt.sum()>0 else None
    cy=float((wt*yy).sum()/wt.sum()) if wt.sum()>0 else None
    peak=np.unravel_index(np.argmax(diff),diff.shape)
    ap3=(np.abs(xx-round(tx))<=1)&(np.abs(yy-round(ty))<=1)
    raw_loss=1000*diff[ap3].sum()/(base[ap3].sum()-np.median(bg[side])*ap3.sum())
    r=dict(sample_id=sid,sector=sector,center_btjd=center,half_width_days=half,status='measured',
           request_url=response.url,zip_sha256=hashlib.sha256(zipped).hexdigest(),zip_bytes=len(zipped),
           n_core=int(core.sum()),n_side=int(side.sum()),core_first_btjd=float(t[core].min()),core_last_btjd=float(t[core].max()),
           side_first_btjd=float(t[side].min()),side_last_btjd=float(t[side].max()),
           sky_median=float(np.median(bg[valid])),target_pixel_sky_subtracted_median=float(np.median(target_pixel[valid])),
           target_pixel_sky_subtracted_min=float(np.min(target_pixel[valid])),
           target_ap3_loss_ppt=float(raw_loss),sources=sources,peak_yx=list(map(int,peak)),
           diff_centroid_xy=[cx,cy],diff_centroid_target_distance_px=float(np.hypot(cx-tx,cy-ty)) if cx is not None else None)
    out.append(r)
    fig,axs=plt.subplots(1,2,figsize=(9,4))
    for ax,data,title in zip(axs,[base-np.median(bg[side]),diff],['baseline sky subtracted','baseline minus core']):
        im=ax.imshow(data,origin='lower',cmap='RdBu_r');fig.colorbar(im,ax=ax,shrink=.7);ax.set_title(title)
        for s in sources:
            if s['G']>17:continue
            ax.plot(s['x'],s['y'],'r+' if s['is_target'] else 'cx',ms=8)
            ax.text(s['x']+.1,s['y']+.1,f"{s['G']:.1f}",fontsize=7,color='white')
    fig.suptitle(f'{sid} S{sector} BTJD {center:.3f}');fig.tight_layout()
    fig.savefig(B/f'helper-{sid}-s{sector:03d}-difference.png',dpi=130);plt.close(fig)
    print(sid,sector,'n',r['n_core'],r['n_side'],'target',round(tx,2),round(ty,2),'centroid',r['diff_centroid_xy'],'ap3',round(raw_loss,2),flush=True)
(B/'helper-q041-pixels.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf8')

