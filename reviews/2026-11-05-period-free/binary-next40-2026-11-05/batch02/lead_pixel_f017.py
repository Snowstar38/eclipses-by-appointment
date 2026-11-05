"""Source attribution of F017 full eclipses in fresh TESSCut WCS cubes."""
import hashlib,io,json,requests,zipfile
from pathlib import Path
import numpy as np
from astropy.io import fits
from astropy.wcs import WCS
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
B=Path(__file__).resolve().parent;O=B/'28059397'/'cutouts';O.mkdir(parents=True,exist_ok=True)
catalogue=json.loads((B.parent/'shared-catalogues'/'gaia-neighbors.json').read_text())['targets']['F017']
rec=[]
for sec,center in [(56,2835.22350),(83,3561.05438)]:
    args=dict(ra=334.08762874,dec=26.51721982,x=11,y=11,sector=sec)
    r=requests.get('https://mast.stsci.edu/tesscut/api/v0.1/astrocut',params=args,timeout=90);r.raise_for_status()
    p=O/f's{sec:03d}.zip';p.write_bytes(r.content)
    with zipfile.ZipFile(io.BytesIO(r.content)) as z:raw=z.read(z.namelist()[0])
    with fits.open(io.BytesIO(raw),memmap=False) as h:
        a=h[1].data;t=np.asarray(a['TIME'],float);cube=np.asarray(a['FLUX'],float);q=np.asarray(a['QUALITY'],int);w=WCS(h[2].header)
    valid=(q==0)&np.isfinite(t)&np.all(np.isfinite(cube),axis=(1,2))
    core=valid&(abs(t-center)<.12);side=valid&(abs(t-center)>.4)&(abs(t-center)<1)
    base=np.nanmedian(cube[side],axis=0);dip=np.nanmedian(cube[core],axis=0);diff=base-dip
    coords=[]
    for s in catalogue:
        if float(s['separation_arcsec'])>80 or float(s['phot_g_mean_mag'])>16:continue
        x,y=w.world_to_pixel_values(float(s['ra']),float(s['dec']));coords.append(dict(source_id=s['source_id'],G=float(s['phot_g_mean_mag']),x=float(x),y=float(y),is_target=s['is_queue_gaia_source']))
    target=next(c for c in coords if c['is_target']); yy,xx=np.indices(diff.shape);wt=np.maximum(diff,0);near=(xx-target['x'])**2+(yy-target['y'])**2<3**2
    cx=float(np.sum(wt[near]*xx[near])/np.sum(wt[near]));cy=float(np.sum(wt[near]*yy[near])/np.sum(wt[near]));peak=np.unravel_index(np.argmax(diff),diff.shape)
    rec.append(dict(sector=sec,center_btjd=center,download_url=r.url,zip_sha256=hashlib.sha256(r.content).hexdigest(),zip_bytes=len(r.content),n_core=int(core.sum()),n_side=int(side.sum()),sources=coords,peak_yx=list(map(int,peak)),difference_centroid_xy=[cx,cy],centroid_target_distance_px=float(np.hypot(cx-target['x'],cy-target['y']))))
    fig,axs=plt.subplots(1,2,figsize=(9,4));axs[0].imshow(base,origin='lower');axs[1].imshow(diff,origin='lower',cmap='RdBu_r')
    for ax in axs:
        for s in coords:
            ax.plot(s['x'],s['y'],'rx' if s['is_target'] else 'co',ms=8)
            ax.text(s['x']+.1,s['y']+.1,f"G{s['G']:.1f}",color='white',fontsize=8)
    axs[0].set_title(f'S{sec} baseline');axs[1].set_title('baseline - eclipse core');fig.tight_layout();fig.savefig(O/f's{sec:03d}-difference.png',dpi=130);plt.close(fig)
    print(sec,peak,rec[-1]['centroid_target_distance_px'],flush=True)
(O/'pixel-evidence.json').write_text(json.dumps(rec,indent=2)+'\n',encoding='utf-8')
