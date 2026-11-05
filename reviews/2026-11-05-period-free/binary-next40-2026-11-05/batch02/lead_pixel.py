"""Inspect actual WCS difference flux around the F014 repeated eclipses."""
import hashlib, json, zipfile
from pathlib import Path
import numpy as np
from astropy.io import fits
from astropy.wcs import WCS
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

B=Path(__file__).resolve().parent;O=B/'236223193'/'cutouts'
receipts=json.loads((O/'receipts.json').read_text())
catalogue=json.loads((B.parent/'shared-catalogues'/'gaia-neighbors.json').read_text())['targets']['F014']
stars=[v for v in catalogue if float(v['phot_g_mean_mag'])<15 and float(v['separation_arcsec'])<80]
events={41:[2424.6169,2431.2596],55:[2812.2604,2818.8631],75:[3340.8387,3347.4436]}
outputs=[]
for r in receipts:
    sec=r['sector'];p=O/f's{sec:03d}.zip';assert hashlib.sha256(p.read_bytes()).hexdigest()==r['sha256']
    with zipfile.ZipFile(p) as z:
        raw=z.read(z.namelist()[0])
    import io
    with fits.open(io.BytesIO(raw),memmap=False) as h:
        a=h[1].data; t=np.asarray(a['TIME'],float);cube=np.asarray(a['FLUX'],float);q=np.asarray(a['QUALITY'],int);w=WCS(h[2].header)
    coords=[]
    for v in stars:
        x,y=w.world_to_pixel_values(float(v['ra']),float(v['dec']))
        coords.append(dict(source_id=v['source_id'],G=float(v['phot_g_mean_mag']),separation_arcsec=float(v['separation_arcsec']),x=float(x),y=float(y),is_target=v['is_queue_gaia_source']))
    fig,axs=plt.subplots(2,2,figsize=(10,9));rec=dict(sector=sec,zip_sha256=r['sha256'],sources=coords,events=[])
    for j,center in enumerate(events[sec]):
        valid=(q==0)&np.isfinite(t)&np.all(np.isfinite(cube),axis=(1,2))
        core=valid&(abs(t-center)<.045)
        side=valid&(abs(t-center)>.22)&(abs(t-center)<.55)
        pre=valid&(t-center>-.55)&(t-center<-.22)
        post=valid&(t-center>.22)&(t-center<.55)
        base=np.nanmedian(cube[side],axis=0);event=np.nanmedian(cube[core],axis=0);diff=base-event
        peak=np.unravel_index(np.nanargmax(diff),diff.shape)
        target=next(c for c in coords if c['is_target'])
        yy,xx=np.indices(diff.shape);weights=np.maximum(diff,0)
        near=(xx-target['x'])**2+(yy-target['y'])**2<2.6**2
        cx=float(np.sum(weights[near]*xx[near])/np.sum(weights[near]));cy=float(np.sum(weights[near]*yy[near])/np.sum(weights[near]))
        e=dict(center_btjd=center,n_core=int(core.sum()),n_side=int(side.sum()),n_pre=int(pre.sum()),n_post=int(post.sum()),peak_yx=list(map(int,peak)),peak_difference_e_per_s=float(diff[peak]),target_xy=[target['x'],target['y']],local_difference_centroid_xy=[cx,cy],local_centroid_target_distance_px=float(np.hypot(cx-target['x'],cy-target['y'])))
        for c in coords:
            x,y=c['x'],c['y'];xi=int(round(x));yi=int(round(y))
            if 0<=xi<11 and 0<=yi<11:c[f"pixel_{c['source_id']}"]=float(diff[yi,xi])
        rec['events'].append(e)
        ax=axs[j,0];ax.imshow(base,origin='lower');ax.set_title(f'S{sec} baseline at {center:.4f}')
        ax=axs[j,1];im=ax.imshow(diff,origin='lower',cmap='RdBu_r');ax.set_title(f'S{sec} baseline - core; peak {peak[::-1]}')
        for c in coords:
            if 0<=c['x']<11 and 0<=c['y']<11 and (c['is_target'] or c['G']<14.5):
                for aa in (axs[j,0],axs[j,1]):
                    aa.plot(c['x'],c['y'],'rx' if c['is_target'] else 'co',ms=8,mew=1)
                    aa.text(c['x']+.15,c['y']+.15,f"{c['G']:.1f}",color='white',fontsize=7)
    fig.tight_layout();fig.savefig(O/f's{sec:03d}-difference.png',dpi=130);plt.close(fig)
    outputs.append(rec);print(sec,[e['peak_yx'] for e in rec['events']],flush=True)
(O/'pixel-evidence.json').write_text(json.dumps(outputs,indent=2)+'\n',encoding='utf-8')
