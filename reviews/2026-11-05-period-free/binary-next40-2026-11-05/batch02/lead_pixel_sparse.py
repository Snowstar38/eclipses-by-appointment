"""WCS difference checks for sparse real-looking F013 and F016 dips."""
import hashlib,io,json,requests,zipfile
from pathlib import Path
import numpy as np
from astropy.io import fits
from astropy.wcs import WCS
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
B=Path(__file__).resolve().parent
neigh=json.loads((B.parent/'shared-catalogues'/'gaia-neighbors.json').read_text())['targets']
cases=[('F013','458457983',209.63455829,13.12096412,[(23,1950.8494,.035),(50,2685.5131,.03)]),('F016','161826828',241.05756763,59.37569537,[(23,1943.5216,.3),(85,3611.2398,.2),(85,3624.2871,.2)])]
for sid,tic,ra,dec,events in cases:
    o=B/tic/'cutouts';o.mkdir(parents=True,exist_ok=True);out=[]
    for sec in sorted(set(x[0] for x in events)):
        params=dict(ra=ra,dec=dec,x=11,y=11,sector=sec);p=o/f's{sec:03d}.zip'
        if p.exists():
            zipped=p.read_bytes();url=requests.Request('GET','https://mast.stsci.edu/tesscut/api/v0.1/astrocut',params=params).prepare().url
        else:
            r=requests.get('https://mast.stsci.edu/tesscut/api/v0.1/astrocut',params=params,timeout=90);r.raise_for_status();p.write_bytes(r.content);zipped=r.content;url=r.url
        with zipfile.ZipFile(io.BytesIO(zipped)) as z:raw=z.read(z.namelist()[0])
        with fits.open(io.BytesIO(raw),memmap=False) as h:
            a=h[1].data;t=np.asarray(a['TIME'],float);cube=np.asarray(a['FLUX'],float);q=np.asarray(a['QUALITY'],int);w=WCS(h[2].header)
        coords=[]
        for s in neigh[sid]:
            if float(s['separation_arcsec'])>100 or float(s['phot_g_mean_mag'])>16:continue
            x,y=w.world_to_pixel_values(float(s['ra']),float(s['dec']));coords.append(dict(source_id=s['source_id'],G=float(s['phot_g_mean_mag']),x=float(x),y=float(y),is_target=s['is_queue_gaia_source']))
        for _,center,half in [x for x in events if x[0]==sec]:
            ok=(q==0)&np.isfinite(t)&np.all(np.isfinite(cube),axis=(1,2));core=ok&(abs(t-center)<half);side=ok&(abs(t-center)>max(.22,half*1.7))&(abs(t-center)<max(.65,half*3))
            if core.sum()<1 or side.sum()<3:
                out.append(dict(sector=sec,center_btjd=center,status='insufficient TESSCut core or side coverage',n_core=int(core.sum()),n_side=int(side.sum()),zip_sha256=hashlib.sha256(zipped).hexdigest(),zip_bytes=len(zipped),download_url=url))
                continue
            base=np.nanmedian(cube[side],axis=0);diff=base-np.nanmedian(cube[core],axis=0);target=next(c for c in coords if c['is_target']);peak=np.unravel_index(np.argmax(diff),diff.shape)
            yy,xx=np.indices(diff.shape);wt=np.maximum(diff,0);near=(xx-target['x'])**2+(yy-target['y'])**2<3**2
            if np.sum(wt[near])>0:
                cx=float(np.sum(wt[near]*xx[near])/np.sum(wt[near]));cy=float(np.sum(wt[near]*yy[near])/np.sum(wt[near]));dist=float(np.hypot(cx-target['x'],cy-target['y']))
            else:cx=cy=dist=None
            out.append(dict(sector=sec,center_btjd=center,core_half_width_days=half,n_core=int(core.sum()),n_side=int(side.sum()),zip_sha256=hashlib.sha256(zipped).hexdigest(),zip_bytes=len(zipped),download_url=url,sources=coords,peak_yx=list(map(int,peak)),centroid_xy=[cx,cy],centroid_target_distance_px=dist,status='no positive local target difference' if dist is None else 'difference measured'))
            fig,axs=plt.subplots(1,2,figsize=(9,4));axs[0].imshow(base,origin='lower');axs[1].imshow(diff,origin='lower',cmap='RdBu_r')
            for ax in axs:
                for s in coords:
                    if 0<=s['x']<11 and 0<=s['y']<11:
                        ax.plot(s['x'],s['y'],'rx' if s['is_target'] else 'co',ms=7)
                        if s['is_target'] or s['G']<14:ax.text(s['x']+.1,s['y']+.1,f"G{s['G']:.1f}",color='white',fontsize=7)
            axs[0].set_title(f'S{sec} baseline');axs[1].set_title(f'baseline - dip {center:.3f}');fig.tight_layout();fig.savefig(o/f's{sec:03d}-{center:.3f}-difference.png',dpi=125);plt.close(fig)
        print(sid,sec,flush=True)
    (o/'pixel-evidence.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
