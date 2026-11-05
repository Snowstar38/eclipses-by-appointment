"""Bounded TESSCut extraction at four insecure single-event flags."""
import csv,hashlib,io,json,zipfile
from pathlib import Path
import requests
import numpy as np
from astropy.io import fits
from astropy.wcs import WCS
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
B=Path(__file__).resolve().parent
Q={r['sample_id']:r for r in csv.DictReader((B/'queue.csv').open(encoding='utf-8',newline=''))}
cases=[('T044',6,1484.82915866,.24,.9),('T045',67,3147.36205335,.16,.6),('T048',26,2011.75778664,.06,.3),('T050',27,2047.30107791,.5,2.5)]
for sid,sector,center,half,sideouter in cases:
    row=Q[sid];tic=row['tic'];out=B/tic
    url='https://mast.stsci.edu/tesscut/api/v0.1/astrocut'
    try:
        r=requests.get(url,params=dict(ra=row['ra_deg'],dec=row['dec_deg'],x=11,y=11,units='px',sector=sector),timeout=120);r.raise_for_status()
        z=zipfile.ZipFile(io.BytesIO(r.content));payload=z.read(z.namelist()[0]);p=out/f'lead-s{sector:03d}-tesscut.fits';p.write_bytes(payload)
        receipt=dict(url=r.url,status_code=r.status_code,zip_sha256=hashlib.sha256(r.content).hexdigest(),member=z.namelist()[0],fits_sha256=hashlib.sha256(payload).hexdigest())
        (out/'lead-cutout-receipt.json').write_text(json.dumps(receipt,indent=2)+'\n')
        with fits.open(p,memmap=False) as hd:
            a=hd[1].data;t=np.asarray(a['TIME'],float);f=np.asarray(a['FLUX'],float);q=np.asarray(a['QUALITY'],int);w=WCS(hd[2].header)
        x,y=map(float,w.all_world2pix(float(row['ra_deg']),float(row['dec_deg']),0));yy,xx=np.indices(f.shape[1:]);mask=(abs(xx-round(x))<=1)&(abs(yy-round(y))<=1)
        valid=np.isfinite(t)&(q==0);core=valid&(abs(t-center)<half);side=valid&(abs(t-center)>half*1.8)&(abs(t-center)<sideouter)
        lc=np.nansum(f[:,mask],axis=1);median=float(np.nanmedian(lc[side]));depth=float(1000*(1-np.nanmedian(lc[core])/median)) if core.sum()>0 and side.sum()>0 else None
        diff=np.nanmedian(f[side],axis=0)-np.nanmedian(f[core],axis=0) if core.sum()>0 and side.sum()>0 else np.full(f.shape[1:],np.nan)
        peak=np.unravel_index(np.nanargmax(diff),diff.shape) if np.isfinite(diff).any() else None
        rec=dict(sample_id=sid,tic=tic,sector=sector,center_seed_btjd=center,core_half_width_days=half,side_outer_days=sideouter,target_pixel=[x,y],rounded_mask_center=[round(x),round(y)],mask_pixel_count=int(mask.sum()),core_n=int(core.sum()),side_n=int(side.sum()),target_aperture_side_median_electrons_per_second=median,target_aperture_loss_ppt=depth,difference_peak_yx=list(map(int,peak)) if peak else None,difference_peak_value=float(diff[peak]) if peak else None,source_fits_sha256=receipt['fits_sha256'],note='Same TESS photons, independently extracted cutout aperture. Seed is not a fitted eclipse center; event morphology and sensitive coverage decide interpretation.')
        (out/'lead-cutout.json').write_text(json.dumps(rec,indent=2)+'\n')
        fig,axs=plt.subplots(1,3,figsize=(14,4));axs[0].imshow(np.nanmedian(f[side],axis=0),origin='lower');axs[0].plot(x,y,'rx');axs[0].set_title('raw baseline');im=axs[1].imshow(diff,origin='lower',cmap='coolwarm');axs[1].plot(x,y,'kx');axs[1].set_title('side minus core');fig.colorbar(im,ax=axs[1]);sel=valid&(abs(t-center)<sideouter);axs[2].plot(t[sel]-center,lc[sel]/median,'.',ms=2);axs[2].set_title('target-centered 3x3 raw');axs[2].set_xlabel('days from screen seed');fig.tight_layout();fig.savefig(out/'lead-cutout.png',dpi=120);plt.close(fig)
        print(sid,rec['core_n'],rec['side_n'],round(depth,2) if depth is not None else None,round(median,1),flush=True)
    except Exception as ex:
        (out/'lead-cutout-error.json').write_text(json.dumps(dict(sample_id=sid,sector=sector,error=repr(ex)),indent=2)+'\n')
        print(sid,'UNKNOWN',repr(ex),flush=True)
