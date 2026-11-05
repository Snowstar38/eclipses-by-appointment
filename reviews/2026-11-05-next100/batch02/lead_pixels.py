"""Hash-verified TESSCut difference maps at representative narrow losses."""
import csv, hashlib, io, json, zipfile
from pathlib import Path
import numpy as np
from astropy.io import fits
from astropy.wcs import WCS
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
B=Path(__file__).resolve().parent
rows={r['sample_id']:r for r in csv.DictReader((B/'queue.csv').open(encoding='utf-8',newline=''))}
events={'Q011':{29:[2089.59,2096.15,2109.27],69:[3184.64,3191.19,3204.32]},'Q015':{41:[2427.14,2435.83,2441.60],55:[2800.24,2806.03,2814.71],82:[3537.73,3540.67,3549.34]}}
for sid,by_sec in events.items():
    row=rows[sid]; out=B/row['tic']/'cutouts'
    receipts=json.loads((out/'receipts.json').read_text(encoding='utf-8')); allres=[]
    for rec in receipts:
        sec=rec['sector']; fp=Path(rec['path']); assert hashlib.sha256(fp.read_bytes()).hexdigest()==rec['sha256']
        with zipfile.ZipFile(fp) as z: raw=z.read(z.namelist()[0])
        with fits.open(io.BytesIO(raw),memmap=False) as h:
            a=h[1].data;t=np.asarray(a['TIME'],float);cube=np.asarray(a['FLUX'],float);q=np.asarray(a['QUALITY'],int);w=WCS(h[2].header)
        tx,ty=w.world_to_pixel_values(float(row['ra_deg']),float(row['dec_deg']))
        tx=float(np.asarray(tx).item());ty=float(np.asarray(ty).item())
        usable=(q==0)&np.isfinite(t)&np.all(np.isfinite(cube),axis=(1,2))
        fig,axs=plt.subplots(len(by_sec[sec]),2,figsize=(9,3.2*len(by_sec[sec])),squeeze=False)
        obj=dict(sector=sec,zip_sha256=rec['sha256'],target_xy=[float(tx),float(ty)],cube_shape=list(cube.shape),events=[])
        for j,center in enumerate(by_sec[sec]):
            core=usable&(np.abs(t-center)<.035)
            pre=usable&(t-center>-.45)&(t-center<-.15)
            post=usable&(t-center>.15)&(t-center<.45)
            if core.sum()<3 or pre.sum()<3 or post.sum()<3:
                obj['events'].append(dict(center_btjd=center,n_core=int(core.sum()),n_pre=int(pre.sum()),n_post=int(post.sum()),valid=False));continue
            before=np.median(cube[pre],axis=0);after=np.median(cube[post],axis=0)
            base=(before+after)/2; depth=base-np.median(cube[core],axis=0)
            peak=np.unravel_index(np.argmax(depth),depth.shape)
            yy,xx=np.indices(depth.shape);near=(xx-tx)**2+(yy-ty)**2<2.5**2
            pos=np.maximum(depth,0)*near
            cx=float(np.sum(xx*pos)/np.sum(pos));cy=float(np.sum(yy*pos)/np.sum(pos))
            xi,yi=int(round(tx)),int(round(ty)); target_d=float(depth[yi,xi]) if 0<=yi<depth.shape[0] and 0<=xi<depth.shape[1] else None
            obj['events'].append(dict(center_btjd=center,valid=True,n_core=int(core.sum()),n_pre=int(pre.sum()),n_post=int(post.sum()),peak_yx=list(map(int,peak)),peak_depth_e_per_s=float(depth[peak]),target_pixel_depth_e_per_s=target_d,local_positive_centroid_xy=[cx,cy],local_centroid_target_distance_px=float(np.hypot(cx-tx,cy-ty)),baseline_target_pixel_e_per_s=float(base[yi,xi]) if target_d is not None else None))
            ax=axs[j,0];ax.imshow(base,origin='lower');ax.set_title(f'S{sec} baseline {center:.3f}');ax.plot(tx,ty,'rx',ms=10)
            ax=axs[j,1];ax.imshow(depth,origin='lower',cmap='RdBu_r');ax.set_title(f'baseline - core, peak {peak[::-1]}');ax.plot(tx,ty,'rx',ms=10)
        fig.tight_layout();fig.savefig(out/f's{sec:03d}-lead-difference.png',dpi=130);plt.close(fig)
        allres.append(obj)
        print(sid,sec,'target',round(tx,2),round(ty,2),[(e.get('peak_yx'),round(e.get('local_centroid_target_distance_px',float('nan')),2)) for e in obj['events']],flush=True)
    (out/'lead-pixel-evidence.json').write_text(json.dumps(allres,indent=2)+'\n',encoding='utf-8')
